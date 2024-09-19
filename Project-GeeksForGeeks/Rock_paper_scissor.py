import random 
 user_wins = 0
 computer_wins = 0
 options  = ["Rock", "paper", "scissors", "test"]
 option[0]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:)
    if user_input == "q":
       break
       quit(0)
    if user_input in ["rock", "paper", "scissors"}:
       continue
    random_number = random.randint(0,2)
    #rock = 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("computer_picked", computer_pick + ".")
    
    if user_input ==  ("rock" and computer_pick == "scissors")
       print("You won!")
       users_wins += 1
    elif user_input == ("paper" and computer_pick == "rock")
        print("You won!")
    elif user_input == ("scissors" and computer_pick == "paper")
        print("You won"!)
    else:
        print("You lost!")
        computer_wins += 1
 print("You won", users_wins, "times.")
 print("The computer won", computer_wins, "times.")
 print("Goodbye!")
    
    

    

    