import time
import turtle
from turtle import Screen
from snake import Snake
from Food import Food
from Score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def restart():
    screen.running = True
    screen.clear()
    snake = Snake()
    food = Food()
    score_board = ScoreBoard()
    score_board.update_score_board()




screen.running = True
program_running = True
while program_running:
    snake = Snake()
    food = Food()
    score_board = ScoreBoard()
    score_board.update_score_board()

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")

    while screen.running:
        screen.update()
        time.sleep(.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score_board.increase_score()

        # wall collison
        if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
            score_board.Game_Over()
            #score_board.again()
            again = input("Do you want to play again? ")
            if again == 'r':
                screen.clear()
                break
            else:
                print('Bye!')
                running = False
                program_running = False
                break

        # tail collison
        for segment in snake.segments:
            if segment == snake.head or segment == snake.segments[1:3]:
                pass
            elif snake.head.distance(segment) < 10:
                print(segment)
                print(snake.segments)
                score_board.Game_Over()
                #score_board.again()
                again = input("Do you want to play again? ")
                if again == 'r':
                    screen.clear()
                    break
                else:
                    print('Bye!')
                    running = False
                    program_running = False
                    break




    screen.onclick(restart)

screen.exitonclick()
