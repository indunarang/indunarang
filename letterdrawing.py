import io,sys,string
import numpy as np
import turtle
from turtle import *
sc=turtle.Screen()
alphabet=sc.textinput("Letter Drawing", "Enter a letter to draw : ")
alphabet = alphabet.upper()
print ("You entered:", alphabet)
len=len(alphabet)

def draw_givenLetter(input_letter):
    pendown()
    if input_letter == "A":
        left(65)  # Turn left to draw the first diagonal line
        forward(100)  # Draw the first diagonal line
        right(130)
        forward(100)
        backward(50)
        right(115)
        forward(40)
        pendown()
    elif input_letter == "B":
        left(90)
        forward(100)  # Draw the vertical line
        right(90)
        circle(-25, 180)  # Draw the top half of the "B"
        left(180)
        circle(-25, 180)  # Draw the bottom half of the "B"
        pendown()
    elif input_letter == "C":
        left(180)
        circle(50, 180) 
        pendown()
    elif input_letter == "D":
        right(90)  # Turn right to draw the vertical line
        forward(100)  # Draw the vertical line
        left(90)
        circle(50, 180) 
        pendown()
    elif input_letter == "E":
        forward(50)  # Draw HL,VL,HL 
        backward(50)  # E excluding middle line
        right(90)  
        forward(100) 
        left(90)  
        forward(50)  
        backward(50)
        left(90) # position in middle of vertical line
        forward(50)
        right(90) # draw middle line of letter E
        forward(50)
        backward(50)  
        pendown()
    elif input_letter == "F":
        forward(50)  # Draw the top horizontal line
        backward(50)  # Move back to the starting position 
        right(90)  # Turn right to draw the vertical line
        forward(100)  # Draw the vertical line
        backward(50)  # Move back to the starting position 
        left(90)  # Turn left to draw the middle horizontal line
        forward(30)  # Draw the middle horizontal line 
        pendown()
    elif input_letter == "G":
        left(180)
        circle(60, 180)
        left(90)
        forward(50)
        left(90)
        forward(30)
        pendown()
    elif input_letter == "H":
        forward(100)
        left(180)
        forward(50)
        right(90)
        forward(30)
        left(90)
        forward(50)
        backward(100)
        pendown()
    elif input_letter == "I":
        left(180)
        forward(20)
        backward(40)
        forward(20)
        left(90)
        forward(100)
        right(90)
        forward(20)
        backward(40)
    elif input_letter == "J":
        left(180)
        forward(20)
        backward(40)
        forward(20)
        left(90)
        forward(100)
        circle(-30, 180) 
        pendown()
    elif input_letter == "K":
        left(90)
        forward(100)
        backward(50)
        right(45)
        forward(60)
        backward(60)
        right(90)
        forward(60)
        pendown()
    elif input_letter == "L":
        left(90)
        forward(100)
        backward(100)
        right(90)
        forward(40)
        backward(40)
        pendown()
    elif input_letter == "M":
        right(90)
        forward(100)
        backward(100)
        left(50)
        forward(60)
        right(90)
        backward(60)
        left(40)
        forward(100)
        pendown()
    elif input_letter == "N":
        right(90)
        forward(100)
        backward(100)
        left(30)
        forward(110)
        left(150)
        forward(100)
        pendown()
    elif input_letter == "O":
        circle(50,360)
        pendown()
    elif input_letter == "P":
        right(90)
        forward(100)
        backward(100)
        left(90)
        circle(-30, 180) 
        pendown()
    elif input_letter == "Q":
        circle(50,360,35)
        forward(60)
        pendown()
    elif input_letter == "R":
        right(90)
        forward(100)
        backward(100)
        left(90)
        circle(-30, 180) 
        left(150)
        forward(75)
        pendown()
    elif input_letter == "S":
        left(180)
        forward(30)
        circle(30,200,240)
        circle(-30,220,240)
        forward(30)
        pendown()
    elif input_letter == "T":
        left(90)
        forward(100)
        right(90)
        forward(30)
        backward(60)
        forward(30)
        pendown()
    elif input_letter == "U":
        right(90)
        forward(100)
        left(35)
        circle(40,110, 110)
        left(35)
        forward(100)
        pendown()
    elif input_letter == "V":
        right(70)
        forward(100)
        left(140)
        forward(100)
        pendown()
    elif input_letter == "W":
        right(90)
        forward(100)
        left(150)
        forward(50)
        right(120)
        forward(50)
        left(150)
        forward(100)
    elif input_letter == "X":
        right(55)
        forward(100)
        pendown()
        backward(50)
        right(65)
        forward(50)
        backward(100)
        pendown()
    elif input_letter == "Y":
        right(55)
        forward(50)
        left(110)
        forward(50)
        backward(50)
        right(180)
        forward(50)
        pendown()
    elif input_letter == "Z":
        forward(50)
        right(120)
        forward(100)
        left(120)
        forward(50)
        pendown()
print (xcor())

if len>1 :
    for l in range(len):
        alphas=alphabet[l]
        if l==0:
            setheading(0)
            home()
            goto(-0,0)
        else:
            penup()
            setheading(0)
            home()
            goto(70,0)
        draw_givenLetter(alphas)
elif len==1: 
    setheading(0)
    goto(-0, 0)
    draw_givenLetter(alphabet)
else:
    reset()