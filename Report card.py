"""
import turtle
use:
text and num input
turtle movement
turtlecolor
color fill
circle

"""
#import turtle
import re
import random
from turtle import*
colormode(255)
setup(900,750)

vo = textinput("Name","ELInnya")
v = vo.upper()
w = textinput("CLass","Enter Class")
x1 = int(numinput("MArk","Enter CRE mark",0,minval = 0, maxval = 100))
y = int(numinput("MArk","Enter Physics mark",0,minval = 0, maxval = 100))
z = int(numinput("MArk","Enter Chemistry mark",0,minval = 0, maxval = 100))
a = int(numinput("MArk","Enter Philosophy mark",0,minval = 0, maxval = 100))
b = int(numinput("MArk","Enter Computer mark",0,minval = 0, maxval = 100))

#draw the outline
up()
speed("fastest")
pencolor("blue")
pensize(3)
setheading(180)
fd(300)
seth(90)
fd(350)
seth(0)
pd()

fillcolor((51,255,255))
begin_fill()
for x in range (2):
    fd(700)
    rt(90)
    fd(600)
    rt(90)
end_fill()
resizemode("noresize")

#typing the information using text input

up()
seth(270)
fd(150)
seth(0)
fd(350)
pencolor("red")
write("CODE HIGH SCHOOL\nP.O.Box 424 , Kampala\nSTUDENT REPORT CARD\nEnd of Term 3 - 2021",move = None,align = "center",font = ("Jokerman",18,"normal"))
pencolor("blue")
fd(-350)
pd()
fd(700)
up()
fd(-700)
seth(270)
fd(40)
seth(0)
fd(20)

pencolor("black")
write(("Student Name : "+v), move = None,align = "left",font = ("Rockwell Extra Bold ",15,"normal"))
fd(500)

write(("Class : "+w), move = None,align = "left",font = ("Rockwell",15,"normal"))


#1. determine the grade of mark
#2. add a comment
comments = ["\tGReat Work","\tVery Good","\tGood","\tGood Try","\tFair","\tWork Harder"]
grades = ["D1\t","D2\t","C3\t","C4\t","C5\t","C6\t","P7\t","P8\t","F9\t"]
r1 = 90
r2 = 80
r3 = 70
r4 = 60
r5 = 50
r6 = 40
r7 = 30
r8 = 20

ax = []

def big(ma):
    if ma >= r1:
        write((grades[0]+comments[0]), move = None,align = "left",font = ("Rockwell",15,"normal"))
        ax.append(1)
    elif r2 <= ma < r1:
        ax.append(2)
        write((grades[1]+comments[1]), move = None,align = "left",font = ("Rockwell",15,"normal"))
    elif r3 <= ma < r2:
        ax.append(3)
        write((grades[2]+comments[2]), move = None,align = "left",font = ("Rockwell",15,"normal"))
    elif r4 <= ma < r3:
        ax.append(4)
        write((grades[3]+comments[3]), move = None,align = "left",font = ("Rockwell",15,"normal"))
    elif r5 <= ma < r4:
        ax.append(5)
        write((grades[4]+comments[3]), move = None,align = "left",font = ("Rockwell",15,"normal"))
    elif r6 <= ma < r5:
        ax.append(6)
        write((grades[5]+comments[3]), move = None,align = "left",font = ("Rockwell",15,"normal"))
    elif  r7 <= ma < r6:
        ax.append(7)
        write((grades[6]+comments[4]), move = None,align = "left",font = ("Rockwell",15,"normal"))
    elif r8 <=  ma < r7:
        ax.append(8)
        write((grades[7]+comments[4]), move = None,align = "left",font = ("Rockwell",15,"normal"))
    elif ma < r8:
        ax.append(9)
        write((grades[8]+comments[5]), move = None,align = "left",font = ("Rockwell",15,"normal"))
    else:
        write("Ungraded", move = None,align = "left",font = ("Rockwell",15,"normal"))
        

fd(-520)
seth(270)
fd(10)
seth(0)
fd(15)
pd()
cv = 140
for i in range(2):
    fd(cv)
    rt(90)
    fd(260)
    rt(90)
    
vc = 270
for i in range(2):
    fd(vc)
    rt(90)
    fd(260)
    rt(90)
    
vc2 = 340
for i in range(2):
    fd(vc2)
    rt(90)
    fd(260)
    rt(90)
    
vc3 = 660
for i in range(2):
    fd(vc3)
    rt(90)
    fd(260)
    rt(90)

up()
fd(-15)
seth(270)
fd(50)
seth(0)
fd(20)

pencolor("black")
write(("CRE\t\t"+str(x1)),move = None,align = "left",font = ("Rockwell",16,"normal"))
fd(300)
big(x1)

fd(-320)
seth(270)

fd(25)
seth(0)
fd(15)
pd()
fd(660)
fd(-660)
up()
fd(-15)
seth(270)
fd(25)

seth(0)
fd(20)
write(("Physics\t\t"+str(y)),move = None,align = "left",font = ("Rockwell",16,"normal"))
fd(300)
big(y)

fd(-320)
seth(270)

fd(25)
seth(0)
fd(15)
pd()
fd(660)
fd(-660)
up()
fd(-15)
seth(270)
fd(25)

seth(0)
fd(20)
write(("Chemistry\t"+str(z)),move = None,align = "left",font = ("Rockwell",16,"normal"))
fd(300)
big(z)

fd(-320)
seth(270)
fd(25)
seth(0)
fd(15)
pd()
fd(660)
fd(-660)
up()
fd(-15)
seth(270)
fd(25)

seth(0)
fd(20)
write(("Philosophy\t"+str(a)),move = None,align = "left",font = ("Rockwell",16,"normal"))
fd(300)
big(a)

fd(-320)
seth(270)

fd(25)
seth(0)
fd(15)
pd()
fd(660)
fd(-660)
up()
fd(-15)
seth(270)
fd(25)

seth(0)
fd(20)
write(("Computer\t"+str(b)),move = None,align = "left",font = ("Rockwell",16,"normal"))
fd(300)
big(b)

agg = ax[0] + ax[1] + ax[2] + ax[3] + ax[4]
aggr = str(agg)

e = x + y + z +a  + b 
e2 = e //6
e3 = e2 
ave = str(e3)

fd(-320)
seth(270)
fd(50)
seth(0)
fd(50)
write(("Aggregates  :"+aggr+"\t\t\t"+"Average (out of 100) : "+ave),move = None,align = "left",font = ("Rockwell",16,"normal"))

fd(-100)
seth(270)
fd(100)
seth(0)
fd(150)
pencolor("purple")
write("A BOOK HOLDS A HOUSE OF GOLD",move = None,align = "left",font = ("Segoe Script",20,"normal"))




































































































































































































