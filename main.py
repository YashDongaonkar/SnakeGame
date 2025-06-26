from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import props

game_is_on = True

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

s = Screen()
s.tracer(0)
s.listen()

s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

s.setup(width = props.SCREENXMAX*2 , height = props.SCREENYMAX*2)
s.bgcolor("black")
s.title("Snake Game")

while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    scoreBoard.show()

    # check collision

    if snake.collided():
        scoreBoard.gameOver()
        snake.reset()

    for seg in snake.segs[1:]:
        if snake.head.distance(seg)<props.TURTLEWIDTH/4:
            scoreBoard.gameOver()
            snake.reset()

    if snake.eat(food):
        food.randomise()
        snake.update(food)
        scoreBoard.increment()        

s.exitonclick()