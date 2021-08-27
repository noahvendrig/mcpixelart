
# # f = open("list.txt", "r")
# # lines = f.readlines()
# # res=[]

# # for line in lines: 
# #     line = line.split()
# #     line_content = []
# #     for word in line:
# #         if not any(letter for letter in word if letter.islower()): # append the word to the list if it doesn't have any capital letters
# #             line_content.append(word)
# #     res.append(line_content)

# # # print(res)
# # with open('output.txt', 'w') as f:
# #     f.write("%s\n" % res)

# # d="wool_colored_yellow"
# # n = d.split("_")
# # n = n[2]+"_"+n[0]
# # print(n)
# x= 255
# def myround(x, base=16):
#     return base * round(float(x) / base)

# print(myround(x))

from PIL import Image
im = Image.open('img/birch_trapdoor.png').convert('RGB')
w,h = im.size
for x in range(w):
    for y in range(h):
        r,g,b = im.getpixel((x,y))

im.show()

# for px in range(x+1,x+4):
#             for py in range(y+1, y+4):
#                 new.putpixel((px,py), (255,0,255))