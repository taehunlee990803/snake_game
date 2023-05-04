from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake game")

location_list = [-40, -20, 0]

segments = []

snake = Snake()
food = Food()
score = scoreboard()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:

    screen.update()
    snake.move()
    time.sleep(0.1)

    # detect collision with  food
    if snake.segments[0].distance(food) < 15:
        food.random_move()
        snake.extend()
        score.detect_food()

    # detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        score.game_over()
        game_is_on = False


    #detect collision with tail
    for segment in segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
