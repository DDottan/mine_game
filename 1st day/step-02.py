# 주위에 지뢰가 몇 개 있는 지 확인하기 #1

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

def show_mines():
    for y in range(MINE_HEIGHT):
        for x in range(MINE_WIDTH):
            print(mines[y][x], end="")
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

make_mines(MINE_COUNT)
count_mines()
show_mines()