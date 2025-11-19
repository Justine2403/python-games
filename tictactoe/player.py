import math 
import random
# Create a game where human can play against computer or human and computer can play against computer 
# Seperate player and game into 2 classes

class Player:
    def __init__(self, letter):
        # Initialize letter: either X or O players
        self.letter = letter 
    
    # We want players to get their next move
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves()) # choose a random available spot 
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None 
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # check if input is a valid number 
            try:
                val = int(square) # return error if input is not a number
                if val not in game.available_moves(): # if input is not in the available moves
                    raise ValueError
                valid_square = True # if it pass then valid move 
            except ValueError:
                print('Invalid square. Try again')
        return val