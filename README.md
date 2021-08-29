# Samson


## Description
This is a simple program that takes a source image, and returns the image in it's Minecraft Pixel Art form (a collection of blocks from the game Minecraft by Mojang). It uses Euclidian Distance to compare RGB values of the source image to the minecraft block images, then finds the closest match.

## Examples of Processed Images
![main](https://user-images.githubusercontent.com/69784959/131254544-fc6bc4ab-abcd-4bd8-a1c7-2018d2a41aa8.jpg)

![gameplay](https://user-images.githubusercontent.com/69784959/131254545-08535696-91d2-4df5-a51e-42711539f99e.jpg)
![](https://user-images.githubusercontent.com/69784959/131254547-aa0f7880-b6b6-499a-a1c6-7982d51ed5c5.jpg)
![](https://user-images.githubusercontent.com/69784959/131254548-dadd11b0-f80e-44e6-8694-34f58f4f969b.jpeg)
![](https://user-images.githubusercontent.com/69784959/131254645-1938617c-2692-4255-8dde-5ff66ff14eab.png)

## Requirements and Installation

Python Version >= [3.8.10](https://www.python.org/downloads/release/python-3810/)\
Pandas Version >= 1.3.2
Pillow Version >= 8.3.1
TQDM Version >= 4.62.2

#### Creating a new Anaconda enviroment
``` bash
conda create --name colour-blocks python=3.8.1
```
#### Activating the Anaconda Environment
###### Windows: 
```
conda activate colour-blocks
``` 
###### Linux / macOS: 
```
conda source activate colour-blocks
```

#### Package Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules.
Run the following command into the terminal or Anaconda prompt:
``` bash
pip install package==version
```

## Usage
Enter the following into the terminal or Anaconda prompt to run the script:
###### Windows
``` bash
python colour-blocks.py
```
###### Linux / macOs
``` bash
python3 colour-blocks.py
```
##### Optional Arguments
``` bash
usage: colour_blocks.py [-h] [-img [img]] [-width [width]] [-s] [-height [height]] [--version]
optional arguments:
  -h, --help        show this help message and exit
  -img [img]        Specify the path for the image to be turned into pixel art
  -width [width]    Specify the new width for the pixel art image. By default it will be 2000 and the height will be adjusted to keep aspect ratio
  -s                Specify whether the pixel art image will be displayed
  -height [height]  Specify the new height for the pixel art image (only if you want specific height). If you use this in conjuction with -width then this arg will be ignored.
  --version         show program's version number and exit
```

## Author
[Noah Vendrig](github.com/noahvendrig)


## License
[MIT License](https://prodicus.mit-license.org/)
Copyright (c) 2021 Noah Vendrig

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
