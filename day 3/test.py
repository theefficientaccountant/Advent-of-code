def main():
    list = []
    delete_list = []
     
    list = ['3', '1', '0', '4']
    delete_list = [0, 0, 3]
    
    #remove duplicates in delete_list
    print(delete_list)

    delete_list = dict.fromkeys(delete_list)
    print(delete_list)

    delete_list = delete_list.keys()
    print(delete_list)
    print(type(delete_list))




    #delete items off list based on delete_list (which has positions)
    delete_list.reverse()

    for i in range(len(delete_list)):
        list.pop(i)
    
    print(list)


#main()



def main2():
  my_list = [3, 4, 53, 88, 345] 
  print(my_list)

  my_list.reverse()
  print(my_list)
   


#main2()


def main3():
    watermelon = ['3','4','5']
    new_watermelon = list(watermelon)
    another_new_watermelon = list(watermelon)

    another_new_watermelon.pop(2)
    
    print(watermelon)
    print(new_watermelon)
    print(another_new_watermelon)




main3()
