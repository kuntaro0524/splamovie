import cv2,sys

input_video_path = sys.argv[1]

cap = cv2.VideoCapture(input_video_path)

while(cap.isOpened()):
    ret, frame = cap.read()
    print(frame, ret)
    if ret:
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
    else:
        break

cap.release()
cv2.destroyAllWindows()
