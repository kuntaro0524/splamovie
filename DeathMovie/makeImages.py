import cv2,sys

video = cv2.VideoCapture(sys.argv[1])
frame_count = int(video.get(7)) 
frame_rate = int(video.get(5))

deadTime = 0 
dead = [] 
# frame analysis interval
interval_time = 5

print(frame_rate)
print(frame_count)

for i in range(int((frame_count / frame_rate)/interval_time)): 
    video.set(1 ,frame_rate * interval_time * i);
    _, frame = video.read() 
    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imwrite("frame_%03d.png"%i,frame)
