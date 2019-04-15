import rule_function as r_f  

cont = True
while cont:
   
    print("make a move! (r/p/s)")
    your_choice=input()  
    r_f.rule(your_choice) #rule function is in another .py file 
    print("Enter sc to see the score! Press enter to skip!")
    score=input()
    if score == 'sc':
        print("human: ", str(len(r_f.p_w)))  
        print("computer: ", str(len(r_f.c_w)))

    print("Do you want to play again?(y/n)")
    p_a=input()#p_a:play_again
    if p_a == 'n':
        print("Thanks, bye!")
        break
    elif p_a == 'y':
        continue
    else:   # if player enter something else
        print("Please print y or n. Try one more time!")