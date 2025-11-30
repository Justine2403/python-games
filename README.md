# Python Games 
Collection of simple games written in Python for practice and reference.
## Available Games
## Guess the number 
A number is randomly generated between 1 and 9. The user must guess it.
Key methods / libraries used:
- `random.randint()`
- `is.digit()` (boolean) to verify that user has entered a valid number

## Rock, paper, scissors 
The user plays rock-paper-scissors against the computer.
Key techniques:
- `random.choice(list)` where list contains the possible moves (rock, paper, scissors)
- dictionnary that define the key-value of winning pairs (rock-scissors, paper-rock, scissors-paper)

## Hangman Game
The user has to guess a word chosen either by another user or randomly by the program.
The game displays correct letters in the proper positions and limits the number of attempts.

Key functions / logic used:
- `random.choice(list)`: selects a random word when playing against the program
- Validation of user-provided words
- Tracking:
  - letters already used
  -   correct letters revealed in the word
  -   remaining lives
- List manipulation to update the displayed word (['__', '_', ...])
- Input validation (`isalpha()`, length checks)

## Chrono Game
A timing-based game: the program generates a random number of seconds; the user must stop a timer when that time is reached.
Key methods:
- `time.time()` to start and stop the time
- for countdown before the game start:
  - `divmod(t, 60)` to convert second into minute, second if needed
  - `print(timer, '\r')` where '\r' allows to print in the same line
 
## Tic-Tac-Toe
Play Tic Tac Toe with the computer, if you have 3 same symboles on a vertical, horizontal or diagonal line, you win !
A simple terminal-based Tic-Tac-Toe game where a human player (X) plays against a computer (O). The game uses OOP (Object-Oriented Programming) and is defined into two main parts:
Player classes:
- `HumanPlayer` asks the user for input
- `RandomComputerPlayer` picks a random available move

TicTacToe class:
- Manages the board, checks available moves, applies moves, prints the board, and detects wins across rows, columns, and diagonals

The play function runs the game loop, alternates turns between X and O, prints the board after each move, and stops when someone wins or the game ends in a tie.

## Snake Game

