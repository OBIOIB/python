import random
import turtle
ts=['blue','red','yellow','brown','green',]
def setup():
    global ts
    screen=turtle.Screen()
    screen.setup(1280,480)
    screen.bgpic('pavement.gif')
    startline=-620
    for i in range(len(ts)):
        t=turtle.Turtle()
        t.shape('turtle')
        t.color(ts[i])
        t.penup()
        t.setpos(startline,(len(ts)//2)*-40+40*i)
        t.pendown()
        ts[i]=t
def race():
    global ts
    finishline=540

    while True:
        for current_t in ts:
            move=random.randint(0,20)
            current_t.forward(move)

            x=current_t.xcor()

            if x >= finishline:
                winner_color=current_t.color()
                current_t.write('Win!'+winner_color[0],font=('Arial',16,'bold'))
                return

setup()
race()
turtle.mainloop()
