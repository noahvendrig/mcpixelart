import pandas as pd
import cv2
import math
from PIL import Image
import numpy as np
import os
# pandas stuff


DATA_CSV = pd.read_csv('data.csv')
# print(DATA_CSV)
blocks_rgb = DATA_CSV["RGB"]
# d= d.split()
# blocks_rgb2 = tuple(map(int,blocks_rgb.split(',')))


# print(blocks_rgb)

def Find_Euclidian_Distance(pxColour, blockColour):
    distance = math.sqrt((pxColour[0] - blockColour[0])**2 + (pxColour[1] - blockColour[1])**2 + (pxColour[2] - blockColour[2])**2)
    return distance

def Find_Colour_Match(pxColour, DATA_CSV=DATA_CSV):
    closest_distance = 473
    closest_colour = None
    for colour in blocks_rgb:
        blockColour = tuple(map(int,colour.split(',')))
        colour_distance = Find_Euclidian_Distance(pxColour, blockColour)

        if colour_distance < closest_distance:
            closest_colour, closest_distance = colour, colour_distance

    # print(closest_colour)
    indexMatch = DATA_CSV[DATA_CSV['RGB']==closest_colour].index
    # colourMatch = DATA_CSV['file_name'][indexMatch]

    return indexMatch

# pxColour = (42,35,42)
# cd = Find_Colour_Match(pxColour)
# print(cd)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
boxLength = 4
boxSize = boxLength* boxLength

# Open Paddington and make sure he is RGB - not palette
IMG_NAME = '4.jpg'
im = Image.open(f"input/{IMG_NAME}").convert('RGB')
width, height = im.size

if width > 1000 or height > 1000:
    w2 = int(width/8)
    h2 = int(height/8)
    im = im.resize((w2,h2))
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

wScale = 2

for x in range(0, width-(boxLength), boxLength):
    
    for y in range(0, height-(wScale*boxLength), boxLength):
        origin = (x,y)
        boxPoints.append(origin)

print(boxPoints[-4:])

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
            # print(pt, "d:",px,py)
            colours.append(im.getpixel((px,py)))
            # print(px,py)
    for rgb in colours:
        ave_r += rgb[0]
        ave_g += rgb[1]
        ave_b += rgb[2]
    avgRGB = int(ave_r/boxSize),int(ave_g/boxSize),int(ave_b/boxSize) # find the average rgb OF THE 4*4 box

    
    indexMatch = list(Find_Colour_Match(avgRGB))[0] # find the block that matches the colours of the avg pixel rgb. convert it to a string for ease of use later
    nameMatch = DATA_CSV['file_name'][indexMatch] # useless but good to see the names in development
    matchImgPath = DATA_CSV['img_location'][indexMatch] # get the path of the img - we need this bit
    # print(nameMatch)
    # print(f"{matchImgPath = }")

    currBlockImg = Image.open(matchImgPath).convert('RGB')
    currColour = None

    for px in range(x-1,x+3): # Change the colour to the average
        for py in range(y-1, y+3):
            currColour = currBlockImg.getpixel((px-x,py-y))
            new.putpixel((px,py), currColour) 


                

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
new = new.resize((width*10,height*10))

dir = os.listdir("./output")

if len(dir) == 0:
    num = 1
else:
    prevName = str(max(dir))
    num = int(list(prevName)[-5])+1
new = new.save(f"./output/{IMG_NAME}")


# new.save('output/1.png')
#         new.putpixel((x, y), (255, 255, 255))
        # r,g,b = im.getpixel((x,y))
        # colours.append((r,g,b))




