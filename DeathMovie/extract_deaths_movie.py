import cv2,sys

temp = cv2.imread("./template_new.png", 0)

def match(img , temp):
 result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
 min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
 return (max_val)

video = cv2.VideoCapture(sys.argv[1])
frame_count = int(video.get(7)) 
frame_rate = int(video.get(5))

deadTime = 0 
dead = [] 
n=2 

prefix = sys.argv[1].replace(".mp4","")

for i in range(int((frame_count / frame_rate)/n)): 
    video.set(1 ,frame_rate * n * i);
    _, frame = video.read() 
    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    #cv2.imwrite("unko%d.png"%i,frame)
    height,width=framegray.shape
    checkVal = match(framegray,temp); 

    if checkVal > 0.8 and deadTime < (i-1) *n - 10 :
        deadTime = (i-1) * (n)
        print ("deadTime : "+str(deadTime))
        dead.append(deadTime);

print(dead)

before_sec = 10
after_sec = 5

if len(dead)>0 :
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    newVideo = cv2.VideoWriter('%s_deaths.mp4'%prefix, fourcc, frame_rate, (width, height))
    for i in dead:
        sFrame = i * frame_rate - frame_rate * before_sec; #n秒前
        eFrame = i * frame_rate + frame_rate * after_sec;
        video.set(1 ,sFrame);
        for no in range(sFrame,eFrame):
            _, frame = video.read()
            newVideo.write(frame)
