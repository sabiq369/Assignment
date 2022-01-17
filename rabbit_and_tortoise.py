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
        for i in system_generated_number_to_list:
            for j in user_input_to_list:
                if i == j:
                    print("You got tortoise")
                break
            for j in user_input_to_list:
                if i==j:
                    print("you got rabbit")
                break
                
    
 

    
        
        
        

                    
     

    
        
