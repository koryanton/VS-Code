import numpy as np
import cv2 as cv

# Number of features to match
MIN_MATCH_COUNT = 10

# Open the video capture (0 for webcam or provide a video file path)
cap = cv.VideoCapture('video.mp4')  # Replace 'your_video.mp4' with your video file path
img_query = cv.imread('chisel.png') # query image
# Check if the video capture is successful
if not cap.isOpened():
    print('Error: Video not found or cannot be opened.')
    exit()

# Create a SIFT object
sift = cv.SIFT_create()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the video has ended
    if not ret:
        break

    # Find keypoints and descriptors in the frame
    kp1, des1 = sift.detectAndCompute(img_query, None)
    kp2, des2 = sift.detectAndCompute(frame, None)

    # Algorithm Selection
    FLANN_INDEX_KDTREE = 1
    # Get index parameters as a dictionary
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=7)
    # Get search parameters
    search_params = dict(checks=50)
    # Use Flann-based matcher
    flann = cv.FlannBasedMatcher(index_params, search_params)
    # Get KNN matches for K value of 2
    matches = flann.knnMatch(des1, des2, k=2)

    # Store all the good matches as per Lowe's ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    if len(good) > MIN_MATCH_COUNT:
        # Get source and destination points and reshape arrays
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        # Find homography on source/destination points
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

        # Matched mask to list
        matchesMask = mask.ravel().tolist()
        # Get height, width, and depth of the frame
        h, w, d = img_query.shape

        # Reshape points array to match height and width
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)

        dst = cv.perspectiveTransform(pts, M)
        # Draw lines and set color
        img_polylines = cv.polylines(frame, [np.int32(dst)], True, (0, 0, 255), 3, cv.LINE_AA)

        # Show polylines
        cv.imshow("Matching Image", img_polylines)

    # Display the video frame with matched features
    # cv.imshow("Video Frame", frame)

    # Exit when 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
