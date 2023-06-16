# Breakout
import turtle

# 初始化遊戲視窗
window = turtle.Screen()
window.title("打磚塊")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# 球拍
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# 球
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# 移動球拍
def move_paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)

def move_paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)

# 鍵盤綁定
window.listen()
window.onkeypress(move_paddle_left, "Left")
window.onkeypress(move_paddle_right, "Right")

# 遊戲主迴圈
while True:
    window.update()

    # 移動球
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # 碰撞邊界
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    elif ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # 碰撞球拍
    if (ball.dy < 0) and (ball.ycor() < -240) and (ball.ycor() > -250) and \
            (paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60):
        ball.sety(-240)
        ball.dy *= -1

    # 碰撞磚塊（根據遊戲需求進行實現）

    # 碰撞底部邊界（遊戲結束）

