#Advent of Code Day 2 Part 1

def main():
    horizontal_position = 0
    depth = 0
    
    #read in txt file
    #note - inputtest.txt is example from problem
    with open('input.txt', 'r') as my_file:
        content_list = my_file.readlines()
    
    #Split the lines and convert the second item to integer
    for i in range(len(content_list)):
        content_list[i] = content_list[i].split()
        content_list[i][1] = int(content_list[i][1])

        
    #Update the position
    for i in range(len(content_list)):
        if content_list[i][0] == 'forward':
            horizontal_position += content_list[i][1]
        elif content_list[i][0] == 'down':
            depth += content_list[i][1]
        elif content_list[i][0] == 'up':
            depth -= content_list[i][1]


    print(horizontal_position)
    print(depth)
    
main()


