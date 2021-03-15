#currency converter

from graphics import *

win = GraphWin("Currency Converter", 600, 600)
win.setCoords(0,0,10,10)
win.setBackground('lavender')

#entry box
entry=Entry(Point(5,7),10)
entry.setSize(18)
entry.setTextColor('white')
entry.draw(win)

#convert button
box = Rectangle(Point(4,5),Point(6,3))
box.setFill('white')
box.draw(win)

#convert button text
boxt = Text(Point(5,4),"convert")
boxt.setSize(14)
boxt.setTextColor('black')
boxt.draw(win)

#exit button
leave = Rectangle(Point(8.5,1),Point(10,0))
leave.setFill('white')
leave.draw(win)

#exit button text
leavet = Text(Point(9.25,.5), "exit")
leavet.setSize(12)
leavet.setTextColor('black')
leavet.draw(win)

result = None

while True:
    G = win.getMouse()
    X = G.getX()
    Y = G.getY()
    if 4 <= X <= 6 and 3 <= Y <= 5:
        x = float(entry.getText())
        #conversion 
        convert = x*0.836856
        #undraw()
        if result != None:
            result.undraw()
        #printresult
        result = Text(Point(5,2),"${:.2f} converts to {:.2f} Euros".format(x,convert))
        result.setSize(18)
        result.setTextColor('black')
        result.draw(win)
        

    elif 8.5 <= X <= 10 and 0 <= Y <= 1:
        win.close()
        
