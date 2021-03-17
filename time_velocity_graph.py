from graphics import *

tfile=open("t.txt", "r")
vfile=open("v.txt","r")

win = GraphWin("tvdata",500,600)
win.setCoords(-3.0,-3.0,30.0,40.0)
win.setBackground('white')

#vertical line
Line(Point(1,-1),Point(1,40)).draw(win)

#horizontal line
Line(Point(0,0),Point(30,0)).draw(win)

#create the y-axis labels
Text(Point(-1,0),"0m/s").draw(win)
Text(Point(-1,10),"10m/s").draw(win)
Text(Point(-1,20),"20m/s").draw(win)
Text(Point(-1,22),"Velocity").draw(win)
Text(Point(-1,30),"30m/s").draw(win)

#create the x-axis labels
Text(Point(1,-1),"0s").draw(win)
Text(Point(5,-1),"5s").draw(win)
Text(Point(10,-1),"10s").draw(win)
Text(Point(15,-1),"15s").draw(win)
Text(Point(20,-1),"20s").draw(win)
Text(Point(25,-1),"25s").draw(win)


#create a list for t and then iterate through t.txt, splitting the values into the list
x = []

for tnum in tfile:
    x += tnum.split()


#we will read the first line of v.txt and then strip it, and then split it and put it in a list
line = vfile.readline()
line = line.strip()
y = line.split(",")


#iterate through lists, and create points
for i in range(len(x)):
    Point(float(x[i]),float(y[i])).draw(win)


tfile.close()
vfile.close()
