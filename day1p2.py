#Advent of Code Day 1 part 2

def main():
    #read in txt file to content_list variable:
    with open('input.txt', 'r') as my_file:
        content_list = [int(x) for x in my_file.readlines()]

    #define variable
    count = 0
    
    #go through list & count if measurement increases:
    for i in range(len(content_list)-3):
            a = content_list[i] + content_list[i+1] + content_list[i+2]
            b = content_list[i+1] + content_list[i+2] + content_list[i+3]
            if a < b:
                count += 1

    print(count)

main()
