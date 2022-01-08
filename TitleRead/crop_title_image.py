import cv2,sys
import pyocr
from PIL import Image


#画像をグレースケールで読み込む
filename = sys.argv[1]
prefix = filename.replace(".png","")
img = cv2.imread(sys.argv[1], 0)

# Crop area
x_min = 530
x_max = 740
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

cv2.imwrite("%s_crop.png"%prefix, img_th)
