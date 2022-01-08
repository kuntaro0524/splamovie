import cv2,sys, pyocr
import numpy as np
from PIL import Image

#Display
def display_result_image(cap, color_image, skeleton):
    colorimg = color_image.copy()

    # カラー画像に細線化を合成
    colorimg = colorimg // 2 + 127
    colorimg[skeleton == 255] = 0

    cv2.imshow(cap + '_skeleton', skeleton)
    cv2.imshow(cap + '_color image', colorimg)
    cv2.waitKey(0)

# OpenCVのイメージを返却する
def convImage(infile):
	# Crop area
	x_min = 547
	x_max = 753
	y_min = 174
	y_max = 343
	
	# Cropする
	im_cropped = infile[y_min: y_max, x_min:x_max]
	return(im_cropped)

# 細線化
def main():
    # 入力画像の取得
    # colorimg = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
    colorimg = cv2.imread(sys.argv[1],0)
    cropImg = convImage(colorimg)
    cv2.imwrite("tttt.png", cropImg)

    # グレースケール変換 gray = cv2.cvtColor(colorimg, cv2.COLOR_BGR2GRAY)
    _, gray = cv2.threshold(cropImg, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # 二値画像反転
    #image = cv2.bitwise_not(gray)

    # 細線化(スケルトン化) THINNING_ZHANGSUEN
    skeleton1   =   cv2.ximgproc.thinning(cropImg, thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)
    cv2.imwrite("skelton.png", skeleton1)
    # display_result_image('ZHANGSUEN', colorimg, skeleton1)

    # OCRする
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    tool = tools[0]
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    res = tool.image_to_string(Image.open("skelton.png") ,lang="jpn",builder=builder)

    print(res.replace(' ',''))

    # 細線化(スケルトン化) THINNING_GUOHALL 
    # skeleton2   =   cv2.ximgproc.thinning(image, thinningType=cv2.ximgproc.THINNING_GUOHALL)
    # display_result_image('GUOHALL', colorimg, skeleton2)



if __name__ == '__main__':
    main()
