import pandas as pd
import cv2

from PIL import Image
import numpy as np

DATA_CSV = pd.read_csv('data.csv')

# img = cv2.imread('./input/1.png')
# img_width= img.shape[1]
# img_height= img.shape[0]
# img= cv2.resize(img, (img_width*16, img_height*16))
# print(img_width, img_height)
# img[0:15, 0:15] = (0,0,0)
# # img[0:50, 0:50] = "img/birch_trapdoor.png"
    
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

boxLength = 4
boxSize = boxLength* boxLength

# Open Paddington and make sure he is RGB - not palette
im = Image.open('input/2.jpg').convert('RGB')
width, height = im.size
colours = []

def adjustSize(dimension, base=boxSize):
    return base * round(float(dimension) / base)
# width = adjustSize(width) * 16
# height =adjustSize(height) * 16

im.resize((width,height))

new = Image.new(mode="RGB", size=(width, height))

print(width,height)   

boxPoints = []

for x in range(0, width, boxLength):
    
    for y in range(0, height, boxLength):
        origin = (x,y)
        boxPoints.append(origin)
        # print(colours)
        colours = []
        ave_r = 0
        ave_g = 0
        ave_b = 0
        newColour = int(ave_r/boxSize),int(ave_g/boxSize),int(ave_b/boxSize)
        # print(newColour)
        
        for px in range(x,x+3):
            for py in range(y, y+3):
                colours.append(im.getpixel((px,py)))
                # print(px,py)
                for rgb in colours:
                    ave_r += rgb[0]
                    ave_g += rgb[1]
                    ave_b += rgb[2]
                im.putpixel((px,py), (newColour))


                
print(boxPoints)         

   
# new.show()
im.show()
# new.save('output/1.png')
#         new.putpixel((x, y), (255, 255, 255))
        # r,g,b = im.getpixel((x,y))
        # colours.append((r,g,b))




