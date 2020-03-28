import random

MINE_WIDTH  = 8
MINE_HEIGHT = 8
MINE_COUNT = 6

mines = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

screen = [
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*"]
]

def show_mines():
    for y in range(MINE_HEIGHT):
        for x in range(MINE_WIDTH):
            print(mines[y][x], end="")
        print("")

def show_screen():
    for y in range(MINE_HEIGHT):
        for x in range(MINE_WIDTH):
            print(screen[y][x], end="")
        print("")

def make_mines(size):
    count = 0
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if mines[y][x] != 9:
            mines[y][x]= 9
            count = count + 1
            if count >= size:
                break

def count_mines():
    for y in range(MINE_HEIGHT):
        for x in range(MINE_WIDTH):
            if mines[y][x] == 9:
                for i in range(-1,2):
                    for j in range(-1,2):
                        if (0 <= y+i) and y+i <= 7:
                            if (0 <= x+j) and x+j <= 7:
                                if mines[y+i][x+j] != 9:
                                    mines[y+i][x+j] = mines[y+i][x+j] + 1

def check_mine(x,y):
    if x not in range(MINE_WIDTH): return    
    if y not in range(MINE_HEIGHT): return
    if screen[y][x] != '*': return

    screen[y][x] = mines[y][x]

    if mines[y][x] != 0: return

    check_mine(x, y+1)
    check_mine(x, y-1)
    check_mine(x+1, y)
    check_mine(x-1, y)

make_mines(MINE_COUNT)
count_mines()

while True:
    show_screen()

    x = int(input('x: '))
    y = int(input('y: '))

    if mines[y][x] == 9:
        print("Game over!")
        break

    check_mine(x, y)