#include "opencv.hpp"


using namespace cv;

int main()
{
    // Number of features to match
    const int MIN_MATCH_COUNT = 9;

    // Open the video capture (0 for webcam or provide a video file path)
    VideoCapture cap("video.mp4"); // Replace "video.mp4" with your video file path

    // Check if the video capture is successful
    if (!cap.isOpened())
    {
        std::cout << "Error: Video not found or cannot be opened." << std::endl;
        return -1;
    }

    // Create a SIFT object
    Ptr<SIFT> sift = SIFT::create();

    // List of query images and their names
    std::vector<std::pair<std::string, std::string>> query_images = {
        {"chisel.png", "Chisel"}, // Replace with your query image filenames and names
        {"RPi_Pico.png", "Pico"},
        {"plug.png", "Plug"}};

    while (true)
    {
        // Capture frame-by-frame
        Mat frame;
        bool ret = cap.read(frame);

        // Check if the video has ended
        if (!ret)
            break;

        for (const auto &query_pair : query_images)
        {
            const std::string &query_filename = query_pair.first;
            const std::string &query_name = query_pair.second;

            // Load the query image
            Mat img_query = imread(query_filename);

            // Find keypoints and descriptors in the frame and query image
            std::vector<KeyPoint> kp1, kp2;
            Mat des1, des2;
            sift->detectAndCompute(img_query, noArray(), kp1, des1);
            sift->detectAndCompute(frame, noArray(), kp2, des2);

            // Algorithm Selection
            const int FLANN_INDEX_KDTREE = 1;
            // Get index parameters as a dictionary
            std::map<int, int> index_params = {{cv::flann::KDTreeIndexParams::algorithm, FLANN_INDEX_KDTREE},
                                               {cv::flann::KDTreeIndexParams::trees, 7}};
            // Get search parameters
            std::map<int, int> search_params = {{cv::flann::SearchParams::checks, 60}};
            // Use Flann-based matcher
            FlannBasedMatcher flann(index_params, search_params);
            // Get KNN matches for K value of 2
            std::vector<std::vector<DMatch>> matches;
            flann.knnMatch(des1, des2, matches, 2);

            // Store all the good matches
            std::vector<DMatch> good;
            for (size_t i = 0; i < matches.size(); i++)
            {
                if (matches[i][0].distance < 0.75 * matches[i][1].distance)
                    good.push_back(matches[i][0]);
            }

            if (good.size() > MIN_MATCH_COUNT)
            {
                // Get source and destination points and reshape arrays
                std::vector<Point2f> src_pts, dst_pts;
                for (const DMatch &match : good)
                {
                    src_pts.push_back(kp1[match.queryIdx].pt);
                    dst_pts.push_back(kp2[match.trainIdx].pt);
                }
                Mat M = findHomography(src_pts, dst_pts, RANSAC, 5.0);

                // Matched mask list
                std::vector<uchar> matchesMask(good.size(), 1);

                // Get height, width, and depth of the frame
                int h = img_query.rows;
                int w = img_query.cols;

                // Reshape points array to match height and width
                std::vector<Point2f> pts = {{0, 0}, {0, h - 1}, {w - 1, h - 1}, {w - 1, 0}};
                std::vector<Point2f> dst;
                perspectiveTransform(pts, dst, M);

                // Draw lines and set color
                std::vector<Point> dst_int;
                for (const Point2f &p : dst)
                    dst_int.push_back(Point(static_cast<int>(p.x), static_cast<int>(p.y)));
                polylines(frame, dst_int, true, Scalar(255, 200, 0), 3, LINE_AA);

                // Display the object name
                putText(frame, query_name, Point(50, 50), FONT_HERSHEY_SIMPLEX, 1, Scalar(0, 255, 0), 2);
            }
        }

        // Show frames
        imshow("Matching Image", frame);

        // Exit when 'q' is pressed
        if (waitKey(1) & 0xFF == 'q')
            break;
    }

    // Release the video capture
    cap.release();
    destroyAllWindows();

    return 0;
}