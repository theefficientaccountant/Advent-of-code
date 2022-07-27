#Advent of Code Day 3 Part 1

def main():

    length = 0
    one = 0
    zero = 0
    gamma = ''
    epsilon = ''
    
    #read in txt file
    #note - inputexample.txt is example from problem
    with open('inputexample.txt', 'r') as my_file:
        content_list = my_file.readlines()
    
    length = len(content_list[1])

    for l in range(len(content_list)):
        content_list[l] = content_list[l].strip()

    #loop through bit and check each item in list
    for h in range(length):

        #loop through list and check the h position
        for i in range(len(content_list)):
            if content_list[i][h] == '0':
                zero += 1
            else:
                one += 1
        
        if zero > one:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        else:
            gamma = gamma + '1'
            epsilon = epsilon + '0'

    print(gamma)
    print(epsilon)

main()