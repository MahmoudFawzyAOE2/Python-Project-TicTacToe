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
    
    pass

class Game ():
    
    pass

P1 = Player()
P1.set_name()
P1.set_symbol()
P1.print_player()

