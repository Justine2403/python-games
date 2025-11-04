import random
def rock_paper_scissors():
    """Try a fun game of rock paper scissors with the computer. 
    User need to enter the full move name to make it work"""
    
    list_move = ["rock", "paper", "scissors"]
    rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    # the first player to have 3 points wins
    bot_point = 0
    user_point = 0

    while bot_point != 3 and user_point !=3:
        bot_move = random.choice(list_move)
        print("Rock, paper or scissors ?")
        user_move = input()
        if user_move in list_move:
            if user_move == bot_move:
                print(f"Equals ! Bot used {bot_move}")
            elif rules[user_move]==bot_move:
                print(f"You won this round, bot used {bot_move}")
                user_point+=1
            else:
                print(f"Bot won this round, bot used {bot_move}")
                bot_point+=1
            print(f"Your points: {user_point}\nBot's points: {bot_point}")
        
        else:
            print("Not an autorised move ! Try again between rock, paper or scissors...")
        
    if bot_point == 3:
        print("You lost !")
    else:
        print("You won !")

rock_paper_scissors()