import pandas as pd
import cv2

from PIL import Image
import numpy as np

# pandas stuff
DATA_CSV = pd.read_csv('data.csv')
print(DATA_CSV)





boxLength = 4
boxSize = boxLength* boxLength



# Open Paddington and make sure he is RGB - not palette
im = Image.open('input/2.jpg').convert('RGB')
width, height = im.size
colours = []

def adjustSize(dimension, base=boxSize):
    return base * round(float(dimension) / base)
width = (adjustSize(width)) #* 16
height = (adjustSize(height)) #* 16

im.resize((width,height))

new = Image.new("RGB", (width, height),(255, 255, 255))

print(f'{width = }, {height}')

boxPoints = []

for x in range(0, width-boxLength, boxLength):
    
    for y in range(0, height-(2*boxLength), boxLength):
        origin = (x,y)
        boxPoints.append(origin)

   
for pt in boxPoints:
    # print(pt)
    x,y = pt
    # print("-"*50)
    # print(pt)
    colours = []
    ave_r = 0
    ave_g = 0
    ave_b = 0
    for px in range(x-1,x+3):
        for py in range(y-1, y+3):
            colours.append(im.getpixel((px,py)))
            # print(px,py)
    for rgb in colours:
        ave_r += rgb[0]
        ave_g += rgb[1]
        ave_b += rgb[2]
    avgRGB = int(ave_r/boxSize),int(ave_g/boxSize),int(ave_b/boxSize) # find the average rgb OF THE 4*4 box

    for px in range(x-1,x+3): # Change the colour to the average
        for py in range(y-1, y+3):
            new.putpixel((px,py), avgRGB) 


                

    # im.putpixel((pt[0],pt[1]), (90,120,50))
    # for x in range(pt[0], pt[0]+boxLength):
    #     for y in range(pt[1], pt[1]+boxLength):
    #         colours.append(im.getpixel((x,y)))
    

# for rgb in colours:
#     ave_r += rgb[0]
#     ave_g += rgb[1]
#     ave_b += rgb[2]

# avgRGB = int(ave_r/boxSize),int(ave_g/boxSize),int(ave_b/boxSize)
# # print(avgRGB)
# for x in range(pt[0], pt[0]+boxLength):
#     for y in range(pt[1], pt[1]+boxLength):
#         im.putpixel((x,y), avgRGB)

   
# new.show()
new.show()
# new.save('output/1.png')
#         new.putpixel((x, y), (255, 255, 255))
        # r,g,b = im.getpixel((x,y))
        # colours.append((r,g,b))




