#Advent of Code Day 3 Part 1

def main():

    count_ones = 0
    count_zeros = 0
    digit_to_use = ''
    oxygen_gen_rate_int = 0
    oxy_pop_list = []
    co_scrub_rate_int = 0
    co_scrub_pop_list = []

    #PREP DATA
    #read in txt file
    #note - started with inputexample.txt - example from problem
    with open('input.txt', 'r') as my_file:
        content_list = my_file.readlines()

    #convert to a list of strings
    #set up the oxygen_gen_rate variable - start with the whole list
    for l in range(len(content_list)):
        content_list[l] = content_list[l].strip()
    
    oxygen_gen_rate = list(content_list)
    co_scrub_rate = list(content_list)
    
    #EVAL DATA FOR OXYGEN GEN RATE
    #loop through each bit place for entire list
    for h in range(len(oxygen_gen_rate[0])):
       
       #loop through each number in the list and count how many zeros/ones in the h position 
       for j in range(len(oxygen_gen_rate)):
           #count how often each bit occurs
           if oxygen_gen_rate[j][h] == '0':
               count_zeros +=1
           else:
               count_ones += 1

       #define the most common bit for that place
       if count_zeros <= count_ones:
           digit_to_use = '1'
       else:
           digit_to_use = '0'
       
       #loop through list again and populate the pop_list based on items that don't match
       for j in range(len(oxygen_gen_rate)):
        if oxygen_gen_rate[j][h] != digit_to_use:
            oxy_pop_list.append(j)
       
       #reverse the list so we can loop through it to delete items in the other list
       oxy_pop_list.reverse()
                     
       #loop through the pop_list and delete corresponding items in the oxygen_gen_rate list
       for k in range(len(oxy_pop_list)):
        oxygen_gen_rate.pop(oxy_pop_list[k])
   
       #reset the count of 0's and 1's and the pop_list
       oxy_pop_list = []
       count_ones = 0
       count_zeros = 0

       #stop when there's only one number left in the list
       if len(oxygen_gen_rate) == 1:
        break

    oxygen_gen_rate_int = int(oxygen_gen_rate[0], 2)
    print(f'The oxygen generator rate is {oxygen_gen_rate[0]} or {oxygen_gen_rate_int}.')

    #EVAL DATA FOR CO Scrub rate
    #loop through each bit place for entire list
    for m in range(len(co_scrub_rate[0])):
       #loop through each number in the list and count how many zeros/ones in the h position 
       for i in range(len(co_scrub_rate)):
           #count how often each bit occurs
           if co_scrub_rate[i][m] == '0':
               count_zeros +=1
           else:
               count_ones += 1

       #define the most common bit for that place
       
       if count_zeros > count_ones:
           digit_to_use = '1'
       else:
           digit_to_use = '0'
             
       #loop through list again and populate the pop_list based on items that don't match
       for i in range(len(co_scrub_rate)):
        if co_scrub_rate[i][m] != digit_to_use:
            co_scrub_pop_list.append(i)
       
       #reverse the list so we can loop through it to delete items in the other list
       co_scrub_pop_list.reverse()
                     
       #loop through the pop_list and delete corresponding items in the oxygen_gen_rate list
       for n in range(len(co_scrub_pop_list)):
        co_scrub_rate.pop(co_scrub_pop_list[n])
   
       #reset the count of 0's and 1's and the pop_list
       co_scrub_pop_list = []
       count_ones = 0
       count_zeros = 0

       #stop when there's only one number left in the list
       if len(co_scrub_rate) == 1:
        break

    co_scrub_rate_int = int(co_scrub_rate[0], 2)
    print(f'The co2 scrubber rate is {co_scrub_rate[0]} or {co_scrub_rate_int}.')
    print(f'The life support rating is {oxygen_gen_rate_int * co_scrub_rate_int}.')

main()