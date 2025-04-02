import cv2 as cv
import os


#makes copies of all the frames in the video inside of a folder called frames
def extract_frames(video_path):
    count = 0
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        print("video capture did not open correctly")
    success, image = cap.read()

    if not os.path.exists("./frames"):
        os.mkdir("./frames")
    
    print(success)

    while success:
        success, image = cap.read()

        if not success:
            break

        cv.imwrite('./frames/' + str(count) + '.jpg', image)
    
        if cv.waitKey(10) == 27:
            break
        count +=1