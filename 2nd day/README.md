# 재귀함수를 이용한 지뢰 탐색

## 첫 번 째 시도

게임 화면을 표시하기 위하여 screen 배열을 추가하고, 입력된 표의 실제 정보를 mines에서 복사해서 표시한다.

``` python
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

# 실제 보이는 화면
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

make_mines(MINE_COUNT)
count_mines()

# 좌표 입력시 화면에 보이게 한다
while True:
    show_screen()
    x = int(input('x: '))
    y = int(input('y: '))
    screen[y][x] = mines[y][x]

```

## 두 번 째 시도

재귀호출을 이용해 지뢰가 없는 영역을 선택하면 연결된 모든 지뢰가 없는 영역을 표시한다.

``` python
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

# 사방으로 0을 탐색하는 함수
def check_mine(x,y):
    # x좌표가 범위에서 벗어나왔을 시 리턴
    if x not in range(MINE_WIDTH): return    

    # y좌표가 범위에서 벗어나왔을 시 리턴
    if y not in range(MINE_HEIGHT): return

    # 이미 처리(복사)된 곳이면 리턴
    if screen[y][x] != '*': return

    screen[y][x] = mines[y][x]

    # 0이 아니면 재귀호출 중단 (탈출조건)
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
    
    # 지뢰를 밟았을 시 게임종료
    if mines[y][x] == 9:
        print("Game over!")
        break

    check_mine(x, y)
```