from graphics import *
import random

win = GraphWin("dicegraph",700,500)
win.setCoords(-2,-20,16,200)
win.setBackground('white')


L = [0,0,0,0,0,0,0,0,0,0,0]

#random loop
for i in range(1000):
    X = random.randint(1,6)
    Y = random.randint(1,6)
    diceroll = X+Y
    for i in range(2,13):
        if diceroll == i:
            L[i-2] += 1

#x axis line
Line(Point(0,0),Point(14,0)).draw(win)

#labels
Text(Point(-1.5,110),"Freq").draw(win)
Text(Point(6,-15),"Sum of 2 Dice").draw(win)


#y axis labels
c = 0

for i in range(10):
    Text(Point(-.5,c),str(c)).draw(win)
    c += 20

#x axis labels
a = 2
b = 1.5

for i in range(11):
    Text(Point(a,-5),str(a)).draw(win)
    bar = Rectangle(Point(b,0),Point(b+1,L[i]))
    bar.setFill('pink')
    bar.draw(win)
    b += 1
    a += 1


print(L)
