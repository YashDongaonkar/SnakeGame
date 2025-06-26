from turtle import Turtle
import props

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("highScore.txt","r") as f:
            self.highScore = int(f.read())

        self.setup()
        self.show()

    def setup(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto((0,props.SCREENYMAX-30))

    def show(self):
        self.clear()
        self.write(f"Score: {self.score}\t\tHighscore : {self.highScore}",False,
                   "center", font=('Arial', 20, 'normal'))

    def gameOver(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highScore.txt","w") as f:
                f.write(str(self.highScore))
        self.score = 0    
        self.show()

    def increment(self):
        self.score+=1