import random
list_word = ["word", "essay", "panda", "chair", "bear"]

def get_valid_word_list(list_word):
    """Check if the word in the list is valid"""
    word = random.choice(list_word)
    return word

def valid_word(word):
    """Check if the word input is valid"""
    while not word.isalpha(): 
        print("Not a valid word, please retry:")
        word = input()
    return word


def code_hangman(word):
    life = 7
    used_letter = []
    current_word = []

    # convert string into a list with each letter to have its position in the word
    letter_word = list(word)
    current_word = ["_"] * len(word)
            
    while life>0:

        print("Guess a letter: ")
        letter_choice = input()
        # verify if the input is a valid letter
        while len(letter_choice)>1 or not letter_choice.isalpha():
            print("This is not a letter, please choose a letter: ")
            letter_choice = input()

        # to show the progression of the player
        # we need to memorize the letter found and to show them at the right position

        # player used an already used letter
        if letter_choice in used_letter:
            print("Letter already used, choose another letter: ")
            continue

        # player found a letter
        elif letter_choice in letter_word:
            used_letter.append(letter_choice)
            for i in range(len(letter_word)):
                if letter_choice == letter_word[i]:
                    current_word[i]= letter_choice
            
            print("You found a letter !")
            print(f"You have {life} left and you use this letter: {used_letter}")
            print(f"Current word: {''.join(current_word)}")
            
        # player did not find the right letter
        else:
            used_letter.append(letter_choice)
            life-=1
            print(f"Your letter, {letter_choice}, is not in the word\n")
            print(f"You have {life} left and you use this letter: {used_letter}")
            print(f"Current word: {''.join(current_word)}")
        
        if ''.join(current_word) == word:
            print(f"You found the word, the word was {''.join(current_word)}")
            break

        elif life == 0:
            print("You have lost all your lifes...")
            print(f"The word was {word}")
            break


def hangman():
    """
    This program allows user to play hangman game, where user need to guess the
    word chosen by another user or the program (randomly) by entering one letter each time.
    User has a limited amount of try before the hangman is drawn. 
    """

    
    print("Do you want to play with the bot (1) or with another user (2)?")

    # user can choose between playing with the program or playing with another user
    choice = input()

    while choice not in ["1", "2"]:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input()

    if choice=="1":
        word = get_valid_word_list(list_word)
        code_hangman(word)
   
    if choice=="2":
        print("Please enter a word to make them guess: ")
        word_user = input()
        word_valid = valid_word(word_user)
        print("\n"*10)
        code_hangman(word_valid)        

hangman()

