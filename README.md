# Python games 
Little games to get to know better Python language.

# List of games:
## Guess the number 
Program generate randomly a number between 1 and 9, user need to find the number.
Methods used:
- random.randint()
- is.digit() (boolean) 

## Rock, paper, scissors 
User plays rock, paper, scissors with the program. 
Method used:
- random.choice(list) where list contains the possible moves (rock, paper, scissors)
- dictionnary that define the key-value of winning pairs (rock-scissors, paper-rock, scissors-paper)

## Hangman game
User plays hangman where they need to find the right word chosen by either another user or generated randomely by the program. User enter a specific letter, if letter is in the word, the program let you know where it is in the word. User has a limited number of attempts before losing.
