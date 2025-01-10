import turtle
t = turtle.Turtle()

def beginGame():
    # reset turtle before each game play
  t.reset()
  t.shape("turtle")
  t.pensize(5)
  t.hideturtle()

  t.penup()
  t.goto(0, 250)
  t.pendown()
  t.forward(105)
  t.right(90)
  t.forward(400)
  t.left(90)
  t.penup()
  t.goto(-115, -150)
  t.pendown()
  t.forward(275)

def drawHangman(missedLetters):
  if len(missedLetters) == 1:
      # head 
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.circle(30)
  elif len(missedLetters) == 2:
      # body
    t.right(90)
    t.forward(100)
  elif len(missedLetters) == 3:
      # lArm
    t.penup()
    t.goto(0, 70)
    t.pendown()
    t.right(115)
    t.forward(45)
  elif len(missedLetters) == 4:
      # rArm
    t.penup()
    t.goto(0, 70)
    t.pendown()
    t.right(130)
    t.forward(45)
  elif len(missedLetters) == 5:
      # lLeg
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(150)
    t.forward(75)
  elif len(missedLetters) == 6:
      # rLeg
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(68)
    t.forward(75)
  elif len(missedLetters) == 7:
      # noose
    t.penup()
    t.goto(0, 250)
    t.pendown()
    t.right(33)
    t.forward(90)
      # game over
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.pencolor("red")
    t.write("Game Over", font=("Palace Script MT", 45, "bold"), align="center")
