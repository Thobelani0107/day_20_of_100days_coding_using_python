from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.update_board()

    def update_board(self):
        self.write(f"Score board :{self.score}", False, "center", ("Arial",8,"normal"))

    def Wall_collition(self):
        self.goto(0,0)
        self.write("Game Over!!", False, "center", ("Arial", 8, "normal"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_board()



