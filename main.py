# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:45:29 2024

@author: HP
"""

class Player():
    
    #initialization
    def __init__ (self, name = "Anonymous", symbol = "&"):
        self._name = name
        self._symbol = symbol
    
    # methods
    def set_name(self):
        while True:
            name = input ("Enter your Name: ")
            if name.isalpha():
                self._name = name
                break
            print("invalid Name!")
        
    def set_symbol(self):
        while True:
            symbol = input ("Enter your Symbol: ")
            if symbol.isalpha() and len(symbol)==1:
                self._symbol = symbol
                break
            print("invalid Symbol!")
            
    def print_player(self):
        print(f"Name: {self._name}")
        print(f"Symbol: {self._symbol}")

class Board ():
    
    def __init__ (self, board = [1,2,3,4,5,6,7,8,9]):
        self._board = board
        
    def display_board(self):
        display = """
         {} | {} | {}
        -----------
         {} | {} | {}
        -----------
         {} | {} | {}      
        """
        print(display.format(*self._board))
        
    def insert_symbol(self, symbol, position):
        index = position - 1
        
        # validate the location before adding the symbol
        if self._board[index].isnum() :
            self._board[index] = symbol
            return True
        else: 
            print("invalid location!, pls try again")
            return False
        
    def clear_board(self):
        self._board = [1,2,3,4,5,6,7,8,9]

class Menu ():
    
    def display_start_menu(self):
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
        print("Game Over")
        print("1- Start Game")
        print("2- Quit Game")
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1" or choice == "2":
                return choice
            else:
                print("Invalid Input!")
        
class Game ():
    
    def __init__ (self):
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
            
            
            
            self.check_win()
     
    def check_win(self):
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
            if 
        
    def quit_game(self):
        print("Good Bye :) ")
        
TTT = Game()        
TTT.start_game()  
        
        
        
        
        

