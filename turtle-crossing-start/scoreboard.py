from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "Center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(x=-250, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"LEVEL={self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

