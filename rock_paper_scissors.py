# rock-paper-scissors
import random

# 定義石頭、剪刀、布的選項
options = ["石頭", "剪刀", "布"]

print("歡迎來到石頭、剪刀、布遊戲！")
print("請選擇你的選項：")
print("1. 石頭")
print("2. 剪刀")
print("3. 布")

while True:
    # 讀取玩家的選擇
    player_choice = int(input("你的選擇(1, 2, 3)：")) - 1

    # 產生電腦的選擇
    computer_choice = random.randint(0, 2)

    print("你選擇了", options[player_choice])
    print("電腦選擇了", options[computer_choice])

    # 判斷選擇結果
    if player_choice == computer_choice:
        print("平手！")
    elif (player_choice == 0 and computer_choice == 1) or \
            (player_choice == 1 and computer_choice == 2) or \
            (player_choice == 2 and computer_choice == 0):
        print("你贏了！")
    else:
        print("你輸了！")

    play_again = input("要再玩一次嗎？(y/n)")
    if play_again.lower() != "y":
        break
