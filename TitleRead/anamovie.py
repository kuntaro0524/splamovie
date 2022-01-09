import cv2,sys

temp = cv2.imread("./gachi.png", 0)

def match(img , temp):
 result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
 min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
 return (max_val)

video = cv2.VideoCapture(sys.argv[1])
frame_count = int(video.get(7)) 
frame_rate = int(video.get(5))

print(frame_count, frame_rate)

deadTime = 0 
dead = [] 
n=5 

for i in range(int((frame_count / frame_rate)/n)): 
    video.set(1 ,frame_rate * n * i);
    _, frame = video.read() 
    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    checkVal = match(framegray,temp); 
    print(i,checkVal)

    if checkVal > 0.8 and deadTime < (i-1) *n - 10 :
        deadTime = (i-1) * (n)
        print ("TitlePage : "+str(deadTime))
        dead.append(deadTime);
