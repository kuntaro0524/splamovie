import cv2,sys
import pyocr
from PIL import Image


#画像をグレースケールで読み込む
img = cv2.imread(sys.argv[1], 0)

# Crop area
x_min = 547
x_max = 753
y_min = 174
y_max = 343

# Cropする
im_cropped = img[y_min: y_max, x_min:x_max]

# Threshold
th = 140
img_th = cv2.threshold(
    im_cropped
    , th
    , 255
    , cv2.THRESH_BINARY
)[1]

#im_bit = cv2.bitwise_not(img_th)
#cv2.imwrite("result.png", im_bit)
cv2.imwrite("result.png", img_th)

# OCRする
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
res = tool.image_to_string(Image.open("result.png") ,lang="jpn",builder=builder)

print(res.replace(' ',''))
