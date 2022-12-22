import numpy as np

def creat_board():
    X = int(input("Please specify the length of the page by entering an integer:"))
    Y = int(input("Please Specify the width of the page by entering an integer:"))
    B_count = int(input("Determine the number of bombs: "))

    
    Bomb_list = []
    
    
    for i in range(0,B_count):
        b = []
        # bomb number
        print("Bomb coordinates no " + str(i+1))
        # Horizontal coordinates
        b.append(input("Y : "))
        # Vertical coordinates
        b.append(input("X : "))
        # append to the general list
        Bomb_list.append(b)
    
    
    for i in range(0,10):
        for i in range(0,10):
            print("    ")
        print()
    print("Game Created ")

    
     # Matrix created
    matrix = []
    for i in range(0,Y):
        mat_x = []
        for j in range(0,X):
            mat_x.append("0")
        matrix.append(mat_x)
        
        
    # Game Board
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()

    print()
    print()
    print()
    
    
    # bombs are gonna located in places
    counter = 0
    for i in range(0, len(Bomb_list)):
        matrix[int(Bomb_list[i][0])-1][int(Bomb_list[i][1])-1] = "B"


    
    game_score = matrix
   # Board game with Bombs
    for row in game_score:
        for val in row:
            print(val, end=" ")
        print()
 
    print()
    print()
    print()
    clean()
    
