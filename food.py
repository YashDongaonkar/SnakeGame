from turtle import Turtle
import random
import props

COLORS = ["blue","green","red"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        # self.shapesize(stretch_len=0.5,stretch_wid=0.5)   
        self.speed("fastest")
        self.randomise()

    def randomise(self):
        self.color(random.choice(COLORS))
        self.goto(random.randint(-props.SCREENXMAX+40,props.SCREENYMAX-40),
                  random.randint(-props.SCREENXMAX+40,props.SCREENYMAX-40))