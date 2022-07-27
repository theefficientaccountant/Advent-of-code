
yellow = 0

with open('inputexample.txt', 'r') as my_file:
    content_list = my_file.readlines()

length = len(content_list[1])

for l in range(len(content_list)):
    content_list[l] = content_list[l].strip()
    print(range(length))



# #loop through bit and check each item in list
# for h in range(length):

#     #loop through list and check the h position
#     for i in range(len(content_list)):



print(yellow)