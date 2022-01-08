import cv2,sys

temp = cv2.imread("./template_killed.png", 0)

def match(img , temp):
 result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
 min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
 return (max_val)

video = cv2.VideoCapture(sys.argv[1])
prefix = sys.argv[1].replace(".mp4","")
frame_count = int(video.get(7)) 
frame_rate = int(video.get(5))

deadTime = 0 
kill_records = [] 
n=2 

print(frame_rate)
print(frame_count)

for i in range(int((frame_count / frame_rate)/n)): 
    video.set(1 ,frame_rate * n * i);
    _, frame = video.read() 
    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    height,width = framegray.shape
    checkVal = match(framegray,temp); 
    # print(i,checkVal)

    if checkVal > 0.8 and deadTime < (i-1) *n - 10 :
        deadTime = (i-1) * (n)
        print ("Killed : "+str(deadTime))
        kill_records.append(deadTime);

print(kill_records)

before_sec = 10
after_sec = 5

kill_index = 1

if len(kill_records)>0 :
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    newVideo = cv2.VideoWriter('%s_kill.mp4' % prefix, fourcc, frame_rate, (width, height))

    for i in kill_records:
        comment = "Kill index = %5d" % kill_index
        sFrame = i * frame_rate - frame_rate * before_sec
        eFrame = i * frame_rate + frame_rate * after_sec
        video.set(1 ,sFrame)
        for no in range(sFrame,eFrame):
            _, frame = video.read()
            cv2.putText(frame,
            	text=comment,
            	org=(0, 300),
            	fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            	fontScale=1.0,
            	color=(255, 255, 255),
            	thickness=5,
            	lineType=cv2.LINE_4)

            newVideo.write(frame)
        kill_index+=1
