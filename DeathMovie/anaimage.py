import cv2,sys

temp = cv2.imread("./template.png")
tempgray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY) 

def match(img , temp):
 result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
 min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
 return (max_val)

frame = cv2.imread(sys.argv[1]) 
framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
checkVal = match(framegray,tempgray)

print(checkVal)

    # if checkVal > 0.8 and deadTime < (i-1) *n - 10 :
    #     deadTime = (i-1) * (n)
    #     print ("deadTime : "+str(deadTime))
    #     dead.append(deadTime);
