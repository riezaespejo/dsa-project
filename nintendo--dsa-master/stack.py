
import os

gw = False

def cls():
    os.system('cls')

def check_ver():
    for row in range(6):
        xCounter = 0
        for col in range(5):
            if (grid[col][row] == "X"):
                xCounter += 1
        if xCounter == 4:
            xw()
    for row in range(6):
        oCounter = 0
        for col in range(5):
            if (grid[col][row] == "O"):
                oCounter += 1
        if oCounter == 4:
            ow()

def check_hor():
    for col in range(5):
        xCounter = 0
        for row in range(6):
            if (grid[col][row] == "X"):
                xCounter += 1
            if xCounter == 4:
                xw()
    for col in range(5):
        oCounter = 0
        for row in range(6):
            if (grid[col][row] == "O"):
                oCounter += 1
            if oCounter == 4:
                xw()

def check_all():
    check_ver()
    check_hor()

def p():
    cls()
    check_all()
    for x in range(5):
        print(*grid[x], sep=" | ")
    for x in range(2):
        print(*info[x], sep=" | ")

def em():
    for x in range(3):
        print("")

def ow():
    cls()
    em()
    print("O, Wins!".center(16))
    em()
    gw = True

def xw():
    cls()
    em()
    print("X, Wins!".center(16))
    em()
    gw = True

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
info = [['==+===+===+===+===+=='],
        ['1', '2', '3', '4', '5', '6']]

while True:
    if gw == True:
        break
    else:
        p()
        row = int(input("X, column: "))
        row -= 1
        if 0 > row or row > 6:
            continue
        else:
            for x in range(4, -1, -1):
                if grid[x][row] == '.':
                    grid[x][row] = 'X'
                    break
        p()
        row = int(input("O, column: "))
        row -= 1
        if 0 > row or row > 6:
            continue
        else:
            for x in range(4, -1, -1):
                if grid[x][row] == '.':
                    grid[x][row] = 'O'
                    break


