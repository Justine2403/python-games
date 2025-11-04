import random 
def guess_number():
    """This code is a little guessing game where the user have to try to guess a number between 1 and 9"""
    n = random.randint(1,9)
    print("Please choose a number between 1 and 9: ")
    
    
    # While number is not correct, ask user to enter new number 
    # Verify if the input is a number
    while True:
        m = input()
        if m.isdigit():
            m_int = int(m)
            # Verify if the number is between 1 and 9
            if m_int>=10 or m_int==0:
                print("This number is not between 1 and 9, please retry: ")

            else:
                if m_int<n:
                    print("This number is - that the guess number ! Try again: ")
                elif m_int>n:
                    print("This number is + that the guess number ! Try again: ")
                else:
                    print("You found the number !")
                    break
        else:   
            print("This is not a number, please retry: ")
        
        
guess_number()

