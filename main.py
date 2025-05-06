import turtle
screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("tan")
t = turtle.Turtle()
t2 = turtle.Turtle()
#intro screen
t.penup()
t.goto(0, 100)
t.pendown()
t.write("Hi my name is Alexa", font=("arial", 30, "italic"), align="center")

t2.penup()
t2.goto(200, -365)
t2.pendown()
t2.write("Press enter to continue", font=("arial", 15, "italic"), align="center")
t2.hideturtle()

t.penup()
t.goto(-150, -50)
t.pendown()
screen.addshape("clickingfinger.gif")
t.shape("clickingfinger.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(150, -50)
t.pendown()
screen.addshape("enterbutton.gif")
t.shape("enterbutton.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0, 0)
t.pendown()

t.penup()
t.goto(0, -200)
t.pendown()
t.write("To move to the next page press enter", font=("arial", 25, "italic"), align="center")

#circle
t.penup()
t.goto(0,-310)
t.pendown()
t.setheading(0)
t.fillcolor("pink")
t.begin_fill()
t.circle(30)
t.end_fill()
t.hideturtle()

round = input("Press Enter to Continue: ")
t.clear()

screen.bgcolor("tan")



#Favorite Foods Screen
screen.bgcolor("light yellow")

t.penup()
t.goto(0, 175)
t.pendown()
t.write("My favorite foods are: ", font=("arial", 30, "italic"), align="center")

t.penup()
t.goto(-150, -30)
t.pendown()
screen.addshape("pasta.gif")
t.shape("pasta.gif")
t.stamp()
t.shape("classic")


t.penup()
t.goto(150, -30)
t.pendown()
screen.addshape("chipotle.gif")
t.shape("chipotle.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0, 0)
t.pendown()

t.penup()
t.goto(0, -225)
t.pendown()
t.write("Penne pasta with chicken, mac and cheese, and a Chipotle bowl", font=("arial", 16, "italic"), align="center")

#Square
t.penup()
t.goto(-50,-250
       )
t.pendown()
t.fillcolor("purple")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()
t.penup()

t.hideturtle()

round = input("Press Enter to Continue: ")
t.clear()

#Hobbies Screen
screen.bgcolor("light blue")

t.penup()
t.goto(0, 175)
t.pendown()
t.write("My favorite Hobbies are: ", font=("arial", 30, "italic"), align="center")

t.penup()
t.goto(-125, -30)
t.pendown()
screen.addshape("bake.gif")
t.shape("bake.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(125, -30)
t.pendown()
screen.addshape("sleep.gif")
t.shape("sleep.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0, 0)
t.pendown()

t.penup()
t.goto(0, -250)
t.pendown()
t.write("Running track, organizing, baking, and sleeping", font=("arial", 20, "italic"), align="center")

#Triangle
t.penup()
t.goto(0,-275)
t.pendown()
t.fillcolor("peachpuff1")
t.begin_fill()
t.goto(50,-325)
t.goto(-50,-325)
t.goto(0,-275)
t.end_fill()

round = input("Press Enter to Continue: ")
t.clear()

#favorite Movie Screen
screen.bgcolor("pink")

t.penup()
t.goto(0, 200)
t.pendown()
t.write("My favorite movies are: ", font=("arial", 30, "italic"), align="center")

t.penup()
t.goto(-150, -25)
t.pendown()
screen.addshape("waves.gif")
t.shape("waves.gif")
t.stamp()
t.shape("classic")


t.penup()
t.goto(150, -25)
t.pendown()
screen.addshape("interstellar.gif")
t.shape("interstellar.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0, 0)
t.pendown()

t.penup()
t.goto(0, -265)
t.pendown()
t.write("Waves and Interstellar", font=("arial", 30, "italic"), align="center")

#Flower
t.speed(0)
t.penup()
t.goto(0,-325)
t.pendown()
t.pencolor("DeepPink2")
t.fillcolor("DeepPink2")

t.begin_fill()
t.circle(25)
t.setheading(270)
t.circle(25)
t.setheading(90)
t.circle(25)
t.setheading(180)
t.circle(25)
t.end_fill()

t.penup()
t.goto(0,-338)
t.pendown()
t.setheading(0)
t.fillcolor("LightGoldenrod1")
t.begin_fill()
t.circle(15)
t.end_fill()

round = input("Press Enter to Continue: ")
t.clear()



#favorite Sport Screen
screen.bgcolor("MediumPurple1")

t.pencolor("black")
t.penup()
t.goto(0, 175)
t.pendown()
t.write("My favorite sport is: ", font=("arial", 30, "italic"), align="center")

t.penup()
t.goto(-150, -25)
t.pendown()
screen.addshape("running.gif")
t.shape("running.gif")
t.stamp()
t.shape("classic")


t.penup()
t.goto(150, -25)
t.pendown()
screen.addshape("track.gif")
t.shape("track.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0, 0)
t.pendown()

t.penup()
t.goto(0, -225)
t.pendown()
t.write("Track and Field", font=("arial", 30, "italic"), align="center")

#rectangle
t.penup()
t.goto(-70,-275)
t.pendown()
t.fillcolor("cyan1")
t.begin_fill()
t.forward(150)
t.right(90)
t.forward(50)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()
t.penup()

round = input("Press Enter to Continue: ")
t.clear()

screen.bgcolor("RoyalBlue1")

t.pencolor("black")
t.penup()
t.goto(-5, -20)
t.pendown()
t.write("The End", font=("arial", 50, "italic"), align="center")

t2.clear()































turtle.done()