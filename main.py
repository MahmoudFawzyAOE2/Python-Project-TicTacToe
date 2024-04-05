# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:45:29 2024

@author: Mahmoud Fawzy
"""

class Player():
    """
    This class represents a single player in the game.
    """
    
    #Initialization
    def __init__ (self, name = "Anonymous", symbol = "&"):
        """
        Initializes a Player object.

        Args:
          name: The player's name (int).
          symbol: The player's symbol (int).
        """
        self._name = name
        self._symbol = symbol
    
    # Methods
    def set_name(self):
        """
        Sets the name of the player object
        """
        while True:
            name = input ("Enter your Name: ")
            if name.isalpha():
                self._name = name
                break
            print("invalid Name!")
        
    def set_symbol(self):
        """
        Sets the symbol of the player object
        """
        while True:
            symbol = input ("Enter your Symbol: ")
            if symbol.isalpha() and len(symbol)==1:
                self._symbol = symbol
                break
            print("invalid Symbol!")
            
    def print_player(self):
        """
        Prints the name & symbol of the player
        """
        print(f"Name: {self._name}")
        print(f"Symbol: {self._symbol}")


class Board ():
    """
    This class represents the game board.
    """
    
    def __init__ (self, board = [1,2,3,4,5,6,7,8,9]):
        """
        Initializes a Board object.

        Args:
          board: The game's board (3*3) (List of length 9).
        """
        self._board = board
        
    def display_board(self):
        """
        Displays the board as a 3*3 array.
        """
        display = """
         {} | {} | {}
        -----------
         {} | {} | {}
        -----------
         {} | {} | {}      
        """
        print(display.format(*self._board))
        
    def insert_symbol(self, symbol, position):
        """
        inserting a game symbol to the board
        """
        # validate the inputted position from the user 
        if position.isnumeric():
            position = int(position)
            index = position - 1   
        else:
            print("invalid position!, pls try again")
            return False
        
        # validate the actual position before adding the symbol
        if isinstance(self._board[index], int) :
            self._board[index] = symbol
            return True
        else: 
            print("the position is already full!, pls try again")
            return False
        
    def clear_board(self):
        """
        Resets the board to the initial state
        """
        self._board = [1,2,3,4,5,6,7,8,9]


class Menu ():
    """
    This class represents the menues displayed during the game.
    """
    
    def display_start_menu(self):
        """
        Displays the initial menu of the game
        """
        print("Welcome to TicTacToe Game")
        print("1- Start Game")
        print("2- Quit Game")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1" or choice == "2":
                return choice
            else:
                print("Invalid Input!")
    
    def display_end_menu(self):
        """
        Displays the final menu of the game
        """
        print("Game Over")
        print("1- Restart Game")
        print("2- Quit Game")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1" or choice == "2":
                return choice
            else:
                print("Invalid Input!")

class Game ():
    """
    This class represents the main game logic.
    """
    def __init__ (self):
        """
        The Game's main block.

        Args:
          board: The game's board (3*3) (board object).
          menu: The displayed menues (3*3) (menu object).
          players: The game's board (3*3) (List of 2 player objects).
          current_player_index: holds the index of the player who is currently playing (int, 1 or 0).
        """
        self._board = Board()
        self._menu = Menu()
        self._players = [Player(), Player()]
        self._current_player_index = 0
        
    def start_game(self):
        choice = self._menu.display_start_menu()
        if choice == "1":
            self.set_players()
            self.play_game()
        else:
            self.quit_game()
  
    def set_players(self):
        
        # these lists are made to save the entered names and symbols
        # so we can use them to prevent duplicated data 
        names_list =[]
        symbols_list =[]
        for player in self._players:
            print()
            print("---data for player no #{} ---".format(self._players.index(player)+1))
            
            while True:
                player.set_name()
                
                # check if name is already used
                if player._name not in names_list:
                    names_list.append(player._name)
                    break
                else:
                    print("this name is already used")
            
            while True:
                player.set_symbol()
                
                # check if symbol is already used
                if player._symbol not in symbols_list:
                    symbols_list.append(player._symbol)
                    break
                else:
                    print("this symbol is already used")
                    
    def play_game(self):
        
        while True:
            self._current_player_index = (self._current_player_index + 1 ) % 2
            self.play_turn(self._current_player_index)
            
            condition = self.check_win_condition() or self.check_draw_condition()
            if condition :
                self._board.display_board()
                break
        self.get_winner(condition)
        choice = self._menu.display_end_menu()
        if choice == "1":
            self.reset_game()          
                
    def play_turn(self, player_index):
        
        player = self._players[player_index]
        
        self._board.display_board()
        
        print(f"{player._name}, Insert your symbol {player._symbol} in a cetain position")
        
        while True:
            position = input("Enter the number of the position: ")
            insertion = self._board.insert_symbol(player._symbol, position)
            if insertion : 
                print("nice move! ")
                break
        
    def check_draw_condition(self):
        board_list = "".join(map(str, self._board._board))
        print(board_list)
        if board_list.isalpha():
            return 10
        return False
        
    def check_win_condition(self):
        win_conditions = [
         [1,2,3],
         [4,5,6],
         [7,8,9],
         [1,4,7],
         [2,5,8],
         [3,6,9],
         [1,5,9],
         [3,5,7]]
        
        for condition in win_conditions:
            positions = [place-1 for place in condition]
            if self._board._board[positions[0]] == self._board._board[positions[1]] == self._board._board[positions[2]]:
                return condition[0]
        return False
    
    def get_winner(self, cell):
        if cell != 10 : #someone has won
            symbol = self._board._board[cell-1]
            if symbol == self._players[0]._symbol: # the winning symbol belongs to P1
                print(f"{self._players[0]._name} is the winner, Congrats!")
            else: 
                print(f"{self._players[1]._name} is the winner, Congrats!")

        else: # draw
            print(f"It's a draw between {self._players[0]._name} and {self._players[1]._name}")
    
    def reset_game(self):
        print("Resetting Game...")
        self._board.clear_board()
        self.play_game()
    def quit_game(self):
        print("Good Bye :) ")
        
TTT = Game()        
TTT.start_game()  
        