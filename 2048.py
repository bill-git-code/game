# 2048
import random

# 初始化2048棋盤
board = [[0] * 4 for _ in range(4)]

# 隨機生成一個新的數字
def generate_new_number():
    new_number = 2 if random.random() < 0.9 else 4
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = new_number

# 顯示2048棋盤
def display_board():
    for row in board:
        print('\t'.join(map(str, row)))
        print()

# 向左移動
def move_left():
    for i in range(4):
        for j in range(3):
            # 將相同數字合併
            if board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                board[i][j + 1] = 0

    # 向左移動數字
    for i in range(4):
        row = [cell for cell in board[i] if cell != 0]
        board[i] = row + [0] * (4 - len(row))

# 遊戲初始化
def game_init():
    # 生成兩個初始數字
    generate_new_number()
    generate_new_number()

print("歡迎來到2048遊戲！")
print("請使用方向鍵控制遊戲。")

game_init()
display_board()

while True:
    move = input("請輸入移動方向（上：w，下：s，左：a，右：d）：").lower()

    if move == 'w':
        move_left()
    elif move == 's':
        # 其他方向的移動可以根據遊戲需求進行實現
        pass
    elif move == 'a':
        # 其他方向的移動可以根據遊戲需求進行實現
        pass
    elif move == 'd':
        # 其他方向的移動可以根據遊戲需求進行實現
        pass
    else:
        print("無效的輸入，請重新輸入。")
        continue

    generate_new_number()
    display_board()

    # 檢查遊戲是否結束（例如，達到2048或沒有可移動的位置）
    # 根據遊戲需求進行檢查和相應處理
