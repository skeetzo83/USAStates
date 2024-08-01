from turtle import Turtle

class Alona:
    def __init__(self):
        self.alona = Turtle()
        self.alona.penup()
        self.alona.hideturtle()

    def correct(self,state, x, y):
        self.alona.goto(x, y)
        self.alona.write(state, font=("Arial", 10, "bold"), align="center")