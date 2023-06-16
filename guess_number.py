import random

# 產生一個1到100之間的隨機數
secret_number = random.randint(1, 100)
attempts = 0

print("歡迎來猜數字遊戲！")
print("請猜一個1到100之間的數字。")

while True:
    # 讀取玩家猜測的數字
    guess = int(input("你的猜測："))
    attempts += 1

    # 檢查玩家猜測的數字與答案之間的關係
    if guess == secret_number:
        print("恭喜你，猜對了！")
        break
    elif guess < secret_number:
        print("太小了，再來。")
    else:
        print("太大了，再來。")

print("你總共猜了", attempts, "次。")
