# Tic Tac Toe
# 初始化空白的井字遊戲棋盤
board = [[" " for _ in range(3)] for _ in range(3)]

# 顯示井字遊戲棋盤
def display_board():
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {' '.join(board[i])}")

# 檢查是否有玩家獲勝
def check_win(player):
    for i in range(3):
        # 檢查行
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # 檢查列
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # 檢查對角線
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

print("歡迎來到井字遊戲！")

current_player = "X"
while True:
    display_board()

    # 讀取玩家的下棋位置
    row = int(input("請輸入要下棋的列數(0-2)："))
    col = int(input("請輸入要下棋的行數(0-2)："))

    # 檢查下棋位置是否合法
    if board[row][col] != " ":
        print("該位置已經有棋子了，請重新輸入。")
        continue

    # 下棋
    board[row][col] = current_player

    # 檢查是否有玩家獲勝
    if check_win(current_player):
        display_board()
        print("恭喜玩家", current_player, "獲勝！")
        break

    # 檢查是否平局
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        display_board()
        print("平局！")
        break

    # 切換玩家
    current_player = "O" if current_player == "X" else "X"
