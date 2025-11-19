from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:    
    def __init__(self):
        self.board = [' ' for _ in range(9)] # Define 3x3 board
        self.current_winner = None # track if their a current winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # 012 345 678 indices for the board 
        # for the first one 0:3 gives me the elements starting at index 0 up to (but not including) index 3
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_number_board():
        '''Tells us what number correspond to what box (ex for 0 | 1 | 2 )'''
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range (3) ]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        '''Available move after player or computer move'''
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ('x', 'x', 'o') --> [(0,'x'), (1,'x'), (2,'o')] it enumerate the index and the value of the list
        #     if spot == ' ':
        #         moves.append(i) # return the index of the empty spot
        
        # return moves 

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ') # count the number of empty squares
        # or len(self.available_moves)
    
    def make_move(self, square, letter):
        # if valid move then make the move (assign square to letter) and return true else false
        if [self.board == ' ']: # if square empty
            self.board[square] = letter # letter goes into this square
            if self.winner(square, letter):
                self.current_winner = letter 
            return True
        return False
    
    def winner(self, square, letter):
        '''winner if 3 in a row anywhere'''
        # wheck the row, we check the index, if all is filled with same letter then win (0,1,2; 3,4,5; 6,7,8)
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column (0,3,6; 1,4,7; 2,5,8)
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonal (0,4,8; 2,4,6)
        # diag if only index is an even number (0,2,4,6,8) only moves to win in diagonal
        if square % 2 == 0:
            diag_left = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diag_left]):
                return True
            diag_right = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diag_right]):
                return True
        
        return False        

    
def play(game, x_player, o_player, print_game = True): # print_game print the baord each time, set to false if computer play against each other
    # return the winner (the letter) else we return None which is a tie
    if print_game:
        game.print_number_board()

    letter = 'X' # starting move 
    # iterates while board has empty square, we don't need to worry abot the winner, it will break the loop if there's one
    while game.empty_squares():
        # get the move from the appropriate player

        if letter == 'O':   
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Function to make a move

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board() # print a new board with the move 
                print('')
                game.print_number_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins !')
                return letter 

        time.sleep(0.8)
        # after we make our move, we need to alternate the letter to next player
        letter = 'O' if letter == 'X' else 'X' 
        # short for:
        # if letter == 'X': 
        #   letter == 'O'
        # else:
        #   letter == 'X'

        # but what if we won ? if we win a game we should win on the current move 
    if print_game:
        print('It\'s a tie !')

    

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)