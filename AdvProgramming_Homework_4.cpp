//Eric Saldana 09/22/2023 "Advanced Robotic Programming - Assignment 4"

#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
//I don't like using the scope resolution operator  so:
using namespace std;
using namespace cv;

int main()
{
    // Number of features to match
    const int MIN_MATCH_COUNT = 9;

    // Open the video capture (0 for webcam or provide a video file path)
    VideoCapture cap("video.mp4");

    // Check if the video capture is successful
    if (!cap.isOpened())
    {
        cout << "Error: Video not found or cannot be opened." << endl;
        return -1;
    }

    // Create a SIFT object
    Ptr < SIFT > sift = SIFT::create();

    // List of images to search for
    vector < pair < string, string >> query_images = {
                                                        {"chisel.png", "Chisel"},
                                                        {"RPi_Pico.png", "Pico"},
                                                        {"plug.png", "Plug"}
                                                    };

    while (true)
    {
        // Capture frame-by-frame
        Mat frame;
        cap.read(frame);

        // Check if the video has ended
        if (frame.empty())
        {
            break;
        }

        for (const auto &query_info : query_images)
        {
            const string &query_filename = query_info.first;
            const string &query_name = query_info.second;

            // Load the query image
            Mat img_query = imread(query_filename);

            // Find keypoints and descriptors in the frame and query image
            vector<KeyPoint> kp1, kp2;
            Mat des1, des2;
            sift->detectAndCompute(img_query, Mat(), kp1, des1);
            sift->detectAndCompute(frame, Mat(), kp2, des2);

            // Algorithm Selection
            int FLANN_INDEX_KDTREE = 1;
            // Get index parameters as a dictionary
            flann::IndexParams *index_params = new flann::KDTreeIndexParams();
            // Use Flann-based matcher
            FlannBasedMatcher flann(index_params);
            // Get KNN matches for K value of 2
            vector < vector<DMatch>> knn_matches;
            flann.knnMatch(des1, des2, knn_matches, 2);

            // Store all the good matches
            vector<DMatch> good_matches;
            for (size_t i = 0; i < knn_matches.size(); ++i)
            {
                if (knn_matches[i][0].distance < 0.75 * knn_matches[i][1].distance)
                {
                    good_matches.push_back(knn_matches[i][0]);
                }
            }

            if (good_matches.size() > MIN_MATCH_COUNT)
            {
                // Draw lines and set color
                vector<Point2f> src_pts, dst_pts;
                for (const DMatch &match : good_matches)
                {
                    src_pts.push_back(kp1[match.queryIdx].pt);
                    dst_pts.push_back(kp2[match.trainIdx].pt);
                }
                Mat H = findHomography(src_pts, dst_pts, RANSAC, 5.0);
                vector<Point2f> obj_corners(4);
                obj_corners[0] = Point2f(0, 0);
                obj_corners[1] = Point2f(img_query.cols, 0);
                obj_corners[2] = Point2f(img_query.cols, img_query.rows);
                obj_corners[3] = Point2f(0, img_query.rows);
                vector<Point2f> scene_corners(4);
                perspectiveTransform(obj_corners, scene_corners, H);

                // Convert scene_corners points to CV_32S format
                vector<Point> scene_corners_int(scene_corners.size());
                for (size_t i = 0; i < scene_corners.size(); ++i)
                {
                    scene_corners_int[i] = scene_corners[i];
                }

                // Draw the polygon
                polylines(frame, scene_corners_int, true, Scalar(0, 0, 255), 3, LINE_AA);

                // Show frames
                imshow("Matching Image", frame);
            }
            
        }

        // Exit when 'q' is pressed
        if (waitKey(1) == 'q')
        {
            break;
        }

    }

    // Release the video capture and close all OpenCV windows
    cap.release();
    destroyAllWindows();

    return 0;
}
