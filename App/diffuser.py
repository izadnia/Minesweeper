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
    
    
