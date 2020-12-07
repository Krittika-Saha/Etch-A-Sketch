from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()

def fd():
  timmy.fd(10)

def left():
  timmy.left(10)

def right():
  timmy.right(10)

def bk():
  timmy.backward(10)

screen.listen()
screen.onkey(fun=fd, key='w')
screen.onkey(fun=bk, key='s')
screen.onkey(fun=right, key='d')
screen.onkey(fun=left, key='a')
screen.onkey(fun=timmy.reset, key='c')
screen.exitonclick()