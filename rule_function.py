import random

computer_source = ['r','p','s']  
    
p_w = []  # p_w: player_win
c_w = []  # c_w: computer_win


def  rule(y_c):
    c_c = random.choice(computer_source)  # c_c:computer_choice
    if y_c == 'r': # y_c:your_choice
        computer_source.append('p')  # to make computer more intelligent
        if c_c == 'r':
            print("You chose ", y_c, " and the computer chose ", c_c, ". It is a draw!")
        elif c_c == 'p':
            print("You chose ", y_c, " and the computer chose ", c_c, ". You lose!")
            c_w.append(1)
        elif c_c == 's':
            print("You chose ", y_c, " and the computer chose ", c_c, ". You win!")
            p_w.append(1)
    elif y_c == 'p':
        computer_source.append('s')
        if c_c == 'r':
            print("You chose ", y_c, " and the computer chose ", c_c, ". You win!")
            p_w.append(1)
        elif c_c == 'p':
            print("You chose ", y_c, " and the computer chose ", c_c, ". It is a draw!")
        elif c_c == 's':
            print("You chose ", y_c, " and the computer chose ", c_c, ". You lose!")
            c_w.append(1)
    elif y_c == 's':
        computer_source.append('r')
        if c_c == 'r':
            print("You chose ", y_c, " and the computer chose ", c_c, ". You lose!")
            c_w.append(1)
        if c_c == 'p':
            print("You chose ", y_c, " and the computer chose ", c_c, ". You win!")
            p_w.append(1)
        if c_c == 's':
            print("You chose ", y_c, " and the computer chose ", c_c, ". It is a draw!")
    else:  # if player input something else
        print("Please enter r, p or s")