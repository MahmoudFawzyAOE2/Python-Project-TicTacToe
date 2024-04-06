# Python-Project-TicTacToe

This is a Project of making a 2-player TicTacToe game using python and OOP principles

## Main Idea

this is the game principle
https://www.youtube.com/watch?v=3qzcAMShotQ&ab_channel=wikiHow

this is the refrence of making this project by Eng: Islam Codezilla
https://www.youtube.com/watch?v=GCYYkOSKj80&list=PLuXY3ddo_8nzCVqXcTFqwcM5R0gZiMRiW&index=1&t=1130s&ab_channel=Codezilla

## Main Code Tasks
- the game starts by displaying a welcome message
- each of the players enter their names and symbols respectively
- the game starts by displaying an empty board & displaying the main game m
- each of the 2 players take turn to play (place his symbol in empty places on the board)
- the game ends when a winning condition occures


## Main Classes
Note: c more details about the classes, items, and methods are provided in code docstrings
### 1- class "Player"
This class construct both players objects

Items:
- name
  - string: only letters
- symbol
  - string: only a single letter

Methods:
- set_name()
- set_symbol()
- print_player()

-------------
### 2- class "Board"
This class constructs, displays & modifies the game's main board

Items:
- board
  - a list of lists [3*3] that contains 

Methods:

- display_board()
- insert_symbol()
- clear_board()

-------------
### 3- class "Menu"
This class displays the opening, each-turn menu & end-game menu

Methods:
- display_open()
- display_end()

-------------
### 4- class "Game"
This is the main constructor of the game and includes its main logic and functionalties, with the assocciation of other classes 

Items:
- player
  - Player(): 
- board
  - Board(): 
- menu
  - Menu(): 
- player_index
  - intger: only 0 or 1

Methods:
- start_game()
- set_players()
- play_game()
- play_turn()
- check_draw_condition()
- check_win_condition()
- get_winner()
- reset_game()
- quit_game()

-------------
## Sample Run
 


