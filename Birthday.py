'''
import os
import time

#Initialise settings
start=5
message=">  Happy Birthday peetabas!      <"

#Start the countdown
for counter in range(start,0,-1):
    print(counter)
    time.sleep(1)
    os.system('clear')  

#Display the message  
print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
print("<                           >")
print(message)
print("<                           >")
print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
'''
'''
import turtle
import random

# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("pink")

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(100)

def line(x1, y1, x2, y2, color, pensize):
  tommy.penup()
  tommy.goto(x1, y1)
  tommy.color(color)
  tommy.pensize(pensize)
  tommy.pendown()
  tommy.goto(x2, y2)
  tommy.penup()
  
snow_colors = ["white", "blue", "silver", "light yellow", "light blue",  "purple", "grey", "magenta", 'green', 'orange', 'gold', 'red', 'red']

line(-190, -180, 190, -180, random.choice(snow_colors), 6)
line(-160, -150, 160, -150, random.choice(snow_colors), 6)
line(-130, -120, 130, -120, random.choice(snow_colors), 6)

# draw cake
tommy.goto(-70,-110)
tommy.begin_fill()
tommy.pendown()
tommy.color("yellow")
tommy.goto(50,-110)
tommy.left(90)
tommy.forward(60)
tommy.left(90)
tommy.forward(125)
tommy.left(90)
tommy.forward(60)
tommy.penup()
tommy.end_fill()

#draw candles

def candle(x, color):
  tommy.goto(x, -40)
  tommy.color(color)
  tommy.pendown()
  tommy.pensize(3)
  tommy.goto(x, -20)
  tommy.penup()

candle(-60, random.choice(snow_colors))
candle(-40, random.choice(snow_colors))
candle(-20, random.choice(snow_colors))
candle(0, random.choice(snow_colors))
candle(20, random.choice(snow_colors))
candle(40, random.choice(snow_colors))

# print message
tommy.goto(-200, 30)
tommy.color("dark blue")
tommy.pendown()
tommy.write("Happy Birthday!", None, None, "45pt bold")




# send the turtle to the corner
tommy.penup()
tommy.goto(-250, 250)
'''



