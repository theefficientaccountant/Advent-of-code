#Advent of Code Day 3 Part 1

def main():

    count_ones = 0
    count_zeros = 0
    gamma_bit_val = ''
    epsilon_bit_val = ''
    gamma_rate = ''
    epsilon_rate = ''
    gamma_rate_int = 0
    epsilon_rate_int = 0
    power_consumption = 0
    
    #read in txt file
    #note - inputexample.txt is example from problem
    with open('input.txt', 'r') as my_file:
        content_list = my_file.readlines()

    #convert to a list of strings
    for l in range(len(content_list)):
        content_list[l] = content_list[l].strip()

    
    #loop through bit places and add to gamma and epsilon values
    for h in range(len(content_list[0])):

       #loop through each number in the list and count how many zeros/ones in the first position 
       for j in range(len(content_list)):
           if content_list[j][h] == '0':
               count_zeros +=1
           else:
               count_ones += 1
       
       if count_zeros > count_ones:
           gamma_bit_val = '0'
           epsilon_bit_val = '1'
       else:
           gamma_bit_val = '1'
           epsilon_bit_val = '0'
       
       gamma_rate += gamma_bit_val
       epsilon_rate += epsilon_bit_val

       count_ones = 0
       count_zeros = 0
       gamma_bit_val = ''
       epsilon_bit_val = ''

      
    gamma_rate_int = int(gamma_rate, 2)
    epsilon_rate_int = int(epsilon_rate, 2)
    power_consumption = gamma_rate_int * epsilon_rate_int

    print(f'The Gamma rate is {gamma_rate} or {gamma_rate_int}.')
    print(f'The Epsilon rate is {epsilon_rate} or {epsilon_rate_int}.')
    print(f'The power consumption is {power_consumption}.')

main()