import io,sys,string
import turtle 
from turtle import *

# Global Settings
screen = turtle.Screen()
screen.title("Turtle Graphics Example")

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.speed(2)  # Set the speed of the turtle
my_turtle.pensize(4)
my_turtle.pencolor("brown")
my_turtle.fillcolor("brown")
my_turtle.pen(outline="red")
my_turtle.color("#0B0B01")

alphabet=screen.textinput("Letter Drawing", "Enter a letter to draw : ")
alphabet = alphabet.upper()
print ("You entered:", alphabet)
len=len(alphabet)

def draw_givenLetter(input_letter):
    my_turtle.pencolor("brown")
    if input_letter == "A":
        my_turtle.left(65)  # Turn left to draw the first diagonal line
        my_turtle.forward(100)  # Draw the first diagonal line
        my_turtle.right(130)
        my_turtle.forward(100)
        my_turtle.backward(50)
        my_turtle.right(115)
        my_turtle.forward(40)
        my_turtle.pendown()
    elif input_letter == "B":
        my_turtle.left(90)
        my_turtle.forward(100)  # Draw the vertical line
        my_turtle.right(90)
        my_turtle.circle(-25, 180)  # Draw the top half of the "B"
        my_turtle.left(180)
        my_turtle.circle(-25, 180)  # Draw the bottom half of the "B"
        my_turtle.pendown()
    elif input_letter == "C":
        my_turtle.left(180)
        my_turtle.circle(50, 180) 
        my_turtle.pendown()
    elif input_letter == "D":
        my_turtle.right(90)  # Turn right to draw the vertical line
        my_turtle.forward(100)  # Draw the vertical line
        my_turtle.left(90)
        my_turtle.circle(50, 180) 
        my_turtle.pendown()
    elif input_letter == "E":
        my_turtle.forward(50)  # Draw HL,VL,HL 
        my_turtle.backward(50)  # E excluding middle line
        my_turtle.right(90)  
        my_turtle.forward(100) 
        my_turtle.left(90)  
        my_turtle.forward(50)  
        my_turtle.backward(50)
        my_turtle.left(90) # position in middle of vertical line
        my_turtle.forward(50)
        my_turtle.right(90) # draw middle line of letter E
        my_turtle.forward(50)
        my_turtle.backward(50)  
        my_turtle.pendown()
    elif input_letter == "F":
        my_turtle.forward(50)  # Draw the top horizontal line
        my_turtle.backward(50)  # Move back to the starting position 
        my_turtle.right(90)  # Turn right to draw the vertical line
        my_turtle.forward(100)  # Draw the vertical line
        my_turtle.backward(50)  # Move back to the starting position 
        my_turtle.left(90)  # Turn left to draw the middle horizontal line
        my_turtle.forward(30)  # Draw the middle horizontal line 
        my_turtle.pendown()
    elif input_letter == "G":
        my_turtle.left(180)
        my_turtle.circle(60, 180)
        my_turtle.left(90)
        my_turtle.forward(50)
        my_turtle.left(90)
        my_turtle.forward(30)
        my_turtle.pendown()
    elif input_letter == "H":
        # my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(180)
        my_turtle.forward(50)
        
        my_turtle.right(90)
        my_turtle.forward(30)
        my_turtle.left(90)
        my_turtle.forward(50)
        my_turtle.backward(100)
        my_turtle.pendown()
    elif input_letter == "I":
        my_turtle.left(180)
        my_turtle.forward(20)
        my_turtle.backward(40)
        my_turtle.forward(20)
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(20)
        my_turtle.backward(40)
    elif input_letter == "J":
        my_turtle.left(180)
        my_turtle.forward(20)
        my_turtle.backward(40)
        my_turtle.forward(20)

        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.circle(-30, 180) 
        my_turtle.pendown()

    elif input_letter == "K":
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.backward(50)
        my_turtle.right(45)
        my_turtle.forward(60)
        my_turtle.backward(60)

        my_turtle.right(90)
        my_turtle.forward(60)
        my_turtle.pendown()
    elif input_letter == "L":
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.backward(100)
        my_turtle.right(90)
        my_turtle.forward(40)
        my_turtle.backward(40)
        my_turtle.pendown()
    
    elif input_letter == "M":
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.backward(100)
        
        my_turtle.left(50)
        my_turtle.forward(60)

        my_turtle.right(90)
        my_turtle.backward(60)
        
        my_turtle.left(40)
        my_turtle.forward(100)
        my_turtle.pendown()
    elif input_letter == "N":
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.backward(100)
        
        my_turtle.left(30)
        my_turtle.forward(110)

        my_turtle.left(150)
        my_turtle.forward(100)
        my_turtle.pendown()
    elif input_letter == "O":
        my_turtle.circle(50,360)
        my_turtle.pendown()
    elif input_letter == "P":
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.backward(100)
        
        my_turtle.left(90)
        my_turtle.circle(-30, 180) 
        my_turtle.pendown()
    elif input_letter == "Q":
        my_turtle.circle(50,360,35)
        my_turtle.forward(60)
        my_turtle.pendown()
    elif input_letter == "R":
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.backward(100)
        
        my_turtle.left(90)
        my_turtle.circle(-30, 180) 
        my_turtle.left(150)
        my_turtle.forward(75)
        my_turtle.pendown()
    elif input_letter == "S":
        my_turtle.left(180)
        my_turtle.forward(30)

        my_turtle.circle(30,200,240)
        my_turtle.circle(-30,220,240)
        my_turtle.forward(30)
        my_turtle.pendown()
    elif input_letter == "T":
        my_turtle.left(90)
        my_turtle.forward(100)

        my_turtle.right(90)
        my_turtle.forward(30)
        my_turtle.backward(60)
        my_turtle.forward(30)
        my_turtle.pendown()
    elif input_letter == "U":
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(35)
        my_turtle.circle(40,110, 110)
        my_turtle.left(35)
        my_turtle.forward(100)
        my_turtle.pendown()
    elif input_letter == "V":
        my_turtle.right(70)
        my_turtle.forward(100)
        my_turtle.left(140)
        my_turtle.forward(100)
        my_turtle.pendown()
    elif input_letter == "W":
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.left(150)
        my_turtle.forward(50)
        my_turtle.right(120)
        my_turtle.forward(50)
        my_turtle.left(150)
        my_turtle.forward(100)
    elif input_letter == "X":
        my_turtle.right(55)
        my_turtle.forward(100)
        my_turtle.pendown()
        my_turtle.backward(50)
        my_turtle.right(65)
        my_turtle.forward(50)
        my_turtle.backward(100)
        my_turtle.pendown()
    elif input_letter == "Y":
        my_turtle.right(55)
        my_turtle.forward(50)
        my_turtle.left(110)
        my_turtle.forward(50)
        my_turtle.backward(50)
        my_turtle.right(180)
        my_turtle.forward(50)
        my_turtle.pendown()
    elif input_letter == "Z":
        my_turtle.forward(50)
        my_turtle.right(120)
        my_turtle.forward(100)
        my_turtle.left(120)
        my_turtle.forward(50)
        my_turtle.pendown()

if len>1 :
    for l in range(len):
        alphas=alphabet[l]
        if l==0:
            my_turtle.setheading(0)
            my_turtle.home()
        else:
            last_angle=my_turtle.heading()
            last_x=round(my_turtle.xcor(),0)
            last_y=round(my_turtle.ycor(),0)

            my_turtle.setheading(0)
            my_turtle.goto((last_x+20), (last_y+20))
        draw_givenLetter(alphas)
        print()
        print(last_angle,"Last Turtle Angle")
        print(last_x,"last X coordinate")
        print(last_y,"last Y coordinate")
elif len==1: 
    my_turtle.setheading(0)
    my_turtle.goto(-0, 0)
    draw_givenLetter(alphabet)

my_turtle.reset()   
