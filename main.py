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
            print("invalid Name!")
            
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
        self._board[index] = symbol
        
        


class Menu ():
    
    def display_main_menu(self):
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
    
    pass

b = Board()
b.display_board()

b.insert_symbol("X", 5)
b.display_board()
