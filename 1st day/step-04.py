# 주위에 지뢰가 몇 개 있는 지 확인하기 #3

import random

MINE_WIDTH  = 8
MINE_HEIGHT = 8
MINE_COUNT = 6

mines = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def get_mine(x, y):
    return mines[y+1][x+1]

def set_mine(x,y,value) :
    mines[y+1][x+1] = value

def inc_mine(x,y):
    if mines[y+1][x+1] != 9:
        mines[y+1][x+1] = mines[y+1][x+1] + 1

def show_mines():
    for y in range(MINE_HEIGHT):
        for x in range(MINE_WIDTH):
            print(get_mine(x, y), " ", end="")
        print("")

def make_mines(size):
    count = 0
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if get_mine(x, y) != 9:
            set_mine(x, y, 9)
            count = count + 1
            if count >= size:
                break

def count_mines():
    for y in range(MINE_HEIGHT):
        for x in range(MINE_WIDTH):
            if get_mine(x, y) == 9:
                inc_mine(x+1, y+0)
                inc_mine(x-1, y+0)
                inc_mine(x+0, y+1)
                inc_mine(x-0, y-1)
                inc_mine(x+1, y+1)
                inc_mine(x-1, y+1)
                inc_mine(x+1, y-1)
                inc_mine(x-1, y-1)

make_mines(MINE_COUNT)
count_mines()
show_mines()