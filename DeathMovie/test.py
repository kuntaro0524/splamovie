import cv2

#画像をグレースケールで読み込む
img = cv2.imread("splatoonimage.png", 0)
temp = cv2.imread("template.png", 0)

result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
w, h = temp.shape[::-1]
bottom_right = (top_left[0] + w, top_left[1] + h)

result = cv2.imread("splatoonimage.png")
cv2.rectangle(result,top_left, bottom_right, (255, 0, 0), 2)
cv2.imwrite("result.png", result)
