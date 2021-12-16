#Advent of Code Day 1

def main():
    #read in txt file to content_list variable:
    with open('input.txt', 'r') as my_file:
        content_list = [int(x) for x in my_file.readlines()]

    #define variable
    count = 0
    
    #go through list & count if measurement increases:
    for i in range(len(content_list)-1):
            if content_list[i] < content_list[i+1]:
                count += 1

    print(count)

main()
