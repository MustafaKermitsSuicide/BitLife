import turtle


LINES = []

fn = open("Data_Turtle.txt", "r+")

for x in fn:
    LINES.append(str(x))
    
fn.close()
fullname = LINES[0]
lifetime = LINES[1]


turtle.screensize(500, 500)
t = turtle.Turtle()
t.pencolor("Grey")
t.pensize(5)
t.shape("circle")


t.goto(-200, -300)

t.speed(100)
t.fillcolor("Grey")

t.begin_fill()

t.left(75)
t.forward(600)
t.right(75)
t.forward(200)
t.right(75)
t.forward(600)
t.right(105)
t.forward(300)

t.end_fill()


t.pensize(1)
t.up()
t.goto(60, 60)


t.pencolor("White")
style =("Cursive", 30, "bold")
t.write("R.I.P", font = style, align = "center")
t.hideturtle()



t.goto(60, -30)
t.write(str(fullname), font = style, align = "center")

t.goto(60, -120)
t.write(str(lifetime), font = style, align = "center")

