
# f = open("list.txt", "r")
# lines = f.readlines()
# res=[]

# for line in lines: 
#     line = line.split()
#     line_content = []
#     for word in line:
#         if not any(letter for letter in word if letter.islower()): # append the word to the list if it doesn't have any capital letters
#             line_content.append(word)
#     res.append(line_content)

# # print(res)
# with open('output.txt', 'w') as f:
#     f.write("%s\n" % res)

# d="wool_colored_yellow"
# n = d.split("_")
# n = n[2]+"_"+n[0]
# print(n)