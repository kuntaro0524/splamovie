import cv2, sys

frame = cv2.imread(sys.argv[1],0)
comment = "UNKO"
cv2.putText(frame,
            text=comment,
            org=(100, 300),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.0,
            color=(255, 255, 255),
            thickness=5,
            lineType=cv2.LINE_4)
cv2.imwrite("saved.png",frame)
