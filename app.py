from turle import Turtle, Screen
import random
import time

spaceD =15
def moveLeft():
    x=space.xcor()- spaceD
    if x<-220:
        x=220
    space.setx(x)



def moveRight():
    x=space.xcor()+spaceD
    if x>220:
        x=220
    space.setx(x)

def shoot():
    x=space.xcor()
    x=space.ycore()
    shoot.setposition(x,y+30)
    rock.showtTutle()


screen = Screen()
screen.setup(width=600,height=600)
screen.bg('black')
screen.title('Space Troopers')
screen.tracer(0)


score = 0


scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color('green')
scoreboard.penup()
score.setposition(-200,-205)
scoreboard.write('Score: %s' %score)
scoreboard.hideturtle()

space = Turtle()
space.shape('triangle')
space.color('green')
space.right(45)
space.goto('0, -280')
space.speed('fast')
space.pendown
space.setheading


rock = Turtle()
rock.color('mustard')
rock.shape('T')
rock.penup()
rock.setheading(90)
rock.shapesize(.6,.6)
rock.hideTurtle()


alien = Turtle()
alien.shape('spade')
alien.penup()
space.color('green')
alien.left(45)
alien.speed('fastest')


screen.listen()
screen.onkey(moveLeft.go_left,'left')
screen.onkey(moveRight.go_right,'right')
screen.onkey(shoot, 'space')


alien_spd=6
rock_spd = 8
    while true:
        alien.forward(alien_spd)
        if alien.xcor()>220 or alien.xcor() <-220:
            alien.right(180)
            alien.forward(alien_spd)
        rock.forward(rock_spd)

        if abs(rock.xcor()-alien.xcor())<115 and abs(rock.yxcor() -alien.ycor()) <15:
            scoreboard=scoreboard+1
            scoreboard.clear()
            score.write('score: %s' %score)
            rock.hideturtle()
            alien.hideturtle()
            time.sleep(3)

            alien.showturle()
            x=random.randint(-220,220)
            alien.setposition(x, 220)

            space




























# TODO: aliens
# TODO: big name Space
# TODO: score

























screen.exutonclick()
