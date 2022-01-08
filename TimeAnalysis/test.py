import cv2
import pyocr

#画像をグレースケールで読み込む
img = cv2.imread(sys.argv[1], 0)

# Crop area
x_min = 610
x_max = 677
y_min = 39
y_max = 66

# Cropする
im_cropped = img[x_min:x_max, y_min:y_max, :]
cv2.imwrite("result.png", result)

# OCRする
tools = pyocr.get_available_tools()

tool = tooles[0]
res = tool.image_to_string(im_cropped, lang="eng")
print(res)