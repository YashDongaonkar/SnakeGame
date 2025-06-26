from turtle import Turtle
import props

STARTING_POSITION = (0,0)
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segs = []
        self.createSnake()
        self.head = self.segs[0]

    def createSegment(self,position):
        t = Turtle(shape = "square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segs.append(t)

    def createSnake(self):
        self.createSegment(STARTING_POSITION)

    def move(self):
        for i in range(len(self.segs)-1,0,-1):
            self.segs[i].goto(self.segs[i-1].pos())

        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segs:
            seg.goto((1000,1000))
        self.segs.clear()
        self.createSnake()
        self.head = self.segs[0]

    def update(self, food):
        self.createSegment(self.segs[-1].pos())

    def collided(self):
        if -props.SCREENXMAX-10<=self.head.pos()[0]<=props.SCREENXMAX-10 and -props.SCREENYMAX-10<=self.head.pos()[1]<=props.SCREENYMAX-10 :
            return False
        else:
            return True
        
    def eat(self, food):
        return self.head.distance(food)<props.TURTLEWIDTH/2

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
