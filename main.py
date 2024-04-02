# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:45:29 2024

@author: HP
"""

class Player():
    
    def __init__ (self, name = "Anonymous", symbol = "&"):
        self._name = name
        self._symbol = symbol
        
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
    
    pass

class Menu ():
    
    def display_main_menu(self):
        print("Welcome to TicTacToe Game")
        print("1- Start Game")
        print("2- Quit Game")
        choice = input("Enter your choice (1 or 2): ")
        return choice
    
    def display_end_menu(self):
        print("Game Over")
        print("1- Start Game")
        print("2- Quit Game")
        choice = input("Enter your choice (1 or 2): ")
        return choice
        


class Game ():
    
    pass


