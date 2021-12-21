#Advent of Code Day 2 Part 2

def main():
    horizontal_position = 0
    depth = 0
    aim = 0

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
            depth += (aim * content_list[i][1])
        elif content_list[i][0] == 'down':
            aim += content_list[i][1]
        elif content_list[i][0] == 'up':
            aim -= content_list[i][1]


    print(f'Horizontal position is {horizontal_position}, depth is {depth}, the solution is {horizontal_position * depth}.')
    
main()


