system_generated_number = 1234

i = 1  
while i != 0:
    user_input = int(input("Guess the four digit number : "))
    user_input_to_list = [int(a) for a in str(user_input)]
    system_generated_number_to_list = [int(a) for a in str(system_generated_number)]
    if user_input == system_generated_number:
        print("You win")
        break
    
    elif system_generated_number != user_input:
        for i in range(0,len(user_input_to_list)):  
            if user_input_to_list[i] in system_generated_number_to_list:
                if user_input_to_list[i] == system_generated_number_to_list[i]:
                    print("you got rabbit")
                  

                else:
                    print("you got tortoise")
                    
    user_input_iterating = input("do you want to continue : y for yes, n for no : ")
    if user_input_iterating == "y":
        continue
    else:
        break
