__author__ = 'Noah Vendrig'
__license__ = 'MIT'  # copy of the license available @ https://prodicus.mit-license.org/
__version__ = '1.1'
__email__ = 'noahvendrig@gmail.com'
__github__ = "github.com/noahvendrig"  # @noahvendrig
__date__ = '09/09/2021'
__description__ = 'Turns any image into its minecraft pixel art'
__pyver__ = '3.8.10'
__info__ = "info available at: https://github.com/noahvendrig/colour-blocks/blob/main/README.md"

print("\n")
print('Author: ' + __author__)
print('License: ' + __license__)
print('Version: ' + __version__)
print('Email: ' + __email__)
print('Github: ' + __github__)
print('Date: ' + __date__)
print('Description: ' + __description__)
print(__info__)
print("Python " + __pyver__)
print('# ' + '=' * 78)


import pandas as pd
import math
from PIL import Image
import os
from tqdm import tqdm
import sys
import argparse
import random
import string

showPixelArt = False

newWidth = 2000
parser = argparse.ArgumentParser(
    description="Creating Minecraft Pixel Art from a source Image")

parser.add_argument('-img', metavar="img", default="1.png", nargs="?", type=str,
                    help="Specify the path for the image to be turned into pixel art")
parser.add_argument('-width', metavar="width", nargs="?", type=int,
                    help="Specify the new width for the pixel art image. By default it will be 2000 and the height will be adjusted to keep aspect ratio")
parser.add_argument('-s', action='store_true',
                    help="Specify whether the pixel art image will be displayed")
parser.add_argument('-v', action='store_true',
                    help="Specify if you would like to process a video instead of an image.")
parser.add_argument('-height', metavar="height", nargs="?", type=str,
                    help="Specify the new height for the pixel art image (only if you want specific height). If you use this in conjuction with -width then this arg will be ignored.")
parser.add_argument('--version', action='version', version='%(prog)s 1.2')
results = parser.parse_args()

# print('img     = {!r}'.format(results.img))
print('s       = {!r}'.format(results.s))
# print('width   = {!r}'.format(results.width))
# print('height  = {!r}'.format(results.height))

showPixelArt = results.s

if results.img != None:
    img_path = str(results.img)

if "/" not in img_path or "\\" not in img_path:
    img_path = "input/" + img_path

print(f"{img_path }")

DATA_CSV = pd.read_csv('data.csv')
# print(DATA_CSV)
blocks_rgb = DATA_CSV["RGB"]
# print(blocks_rgb)


def Find_Euclidian_Distance(pxColour, blockColour):
    distance = math.sqrt((pxColour[0] - blockColour[0])**2 + (
        pxColour[1] - blockColour[1])**2 + (pxColour[2] - blockColour[2])**2)
    return distance


def Find_Colour_Match(pxColour, DATA_CSV=DATA_CSV):
    closest_distance = 473
    closest_colour = None
    for colour in blocks_rgb:
        blockColour = tuple(map(int, colour.split(',')))
        colour_distance = Find_Euclidian_Distance(pxColour, blockColour)

        if colour_distance < closest_distance:
            closest_colour, closest_distance = colour, colour_distance
    # print(closest_colour)
    indexMatch = DATA_CSV[DATA_CSV['RGB'] == closest_colour].index

    return indexMatch


boxLength = 16
boxSize = boxLength * boxLength

im = Image.open(img_path).convert('RGB')
width, height = im.size

scaleFactor = None

if results.width != None:
    newWidth = results.width
    scaleFactor = newWidth/width
elif results.height != None:
    newHeight = int(results.height)
    scaleFactor = newHeight/height
else:
    scaleFactor = newWidth/width

width = int(width*scaleFactor)
height = int(height*scaleFactor)
im.resize((width, height))

colours = []


def adjustSize(dimension, base=boxLength):
    return base * round(float(dimension) / base)


width = (adjustSize(width))  # * 16
height = (adjustSize(height))  # * 16

im = im.resize((width, height))

new = Image.new("RGB", (width, height), (255, 255, 255))

# print(f'{width = }, {height = }')

boxPoints = []

print(f"{width = }, {height = }")
print(f"{img_path}")


for x in range(0, width, boxLength):

    for y in range(0, height, boxLength):
        origin = (x, y)
        boxPoints.append(origin)

for pt in tqdm(boxPoints, desc="Generating Image", unit=" Blocks"):
    # print(pt)
    x, y = pt
    colours = []
    ave_r = 0
    ave_g = 0
    ave_b = 0
    for px in range(x, x+boxLength):
        for py in range(y, y+boxLength):

            # print(pt, "w,h:",px,py, width, height)
            colours.append(im.getpixel((px, py)))

    for rgb in colours:
        ave_r += rgb[0]
        ave_g += rgb[1]
        ave_b += rgb[2]
    avgRGB = int(ave_r/boxSize), int(ave_g/boxSize), int(ave_b /
                                                         boxSize)  # find the average rgb OF THE 4*4 box

    # find the block that matches the colours of the avg pixel rgb. convert it to a string for ease of use later
    indexMatch = list(Find_Colour_Match(avgRGB))[0]
    # useless but good to see the names in development
    nameMatch = DATA_CSV['file_name'][indexMatch]
    # get the path of the img - we need this bit
    matchImgPath = DATA_CSV['img_location'][indexMatch]
    # print(nameMatch)
    # print(f"{matchImgPath = }")

    currBlockImg = Image.open(matchImgPath).convert('RGB')
    currColour = None

    for px in range(x, x+boxLength):  # Change the colour to the average
        for py in range(y, y+boxLength):
            currColour = currBlockImg.getpixel((px-x, py-y))
            new.putpixel((px, py), currColour)

dir = os.listdir("./output")

resName = ''.join(random.choice(string.ascii_uppercase + string.digits)
                  for _ in range(10))

savedPath = f"./output/{resName}.png"
new = new.save(savedPath)

print(f"Pixel Art Saved At {savedPath}")

if showPixelArt:
    new.show()
