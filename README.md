# Python games 
Little games to get to know better Python language.

## Guess the number 
Program generate randomly a number between 1 and 9, user need to find the number.
Methods used:
- `random.randint()`
- `is.digit()` (boolean) to verify that user has entered a valid number

## Rock, paper, scissors 
User plays rock, paper, scissors with the program. 
Method used:
- `random.choice(list)` where list contains the possible moves (rock, paper, scissors)
- dictionnary that define the key-value of winning pairs (rock-scissors, paper-rock, scissors-paper)

## Hangman game
User plays hangman game where they need to find the right word chosen by either another user or generated randomly by the program. User enter a specific letter, if letter is in the word, the program let you know where it is in the word. User has a limited number of attempts before losing.

## Chrono game
Program generate a random number, user need to stop when time reaches the corresponding number in second
Method used:
- `time.time()` to start and stop the time
- for countdown before the game start:
  - `divmod(t, 60)` to convert second into minute, second if needed
  - `print(timer, '\r')` where '\r' allows to print in the same line
 
## Tic Tac Toe
Play Tic Tac Toe with the computer, if you have 3 same symboles on a vertical, horizontal or diagonal line, you win !
A simple terminal-based Tic-Tac-Toe game where a human player (X) plays against a computer (O). The game uses OOP (Object-Oriented Programming) and is defined into two main parts:

This programs uses OOP (Object-Oriented Programming)

Player classes:
- HumanPlayer asks the user for input
- RandomComputerPlayer picks a random available move

TicTacToe class:
- Manages the board, checks available moves, applies moves, prints the board, and detects wins across rows, columns, and diagonals

The play function runs the game loop, alternates turns between X and O, prints the board after each move, and stops when someone wins or the game ends in a tie.
