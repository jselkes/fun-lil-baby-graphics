#HW15

from graphics import *

def main():
    win = GraphWin('squareclick',500,500)
    win.setCoords(0,0,10,10)
    win.setBackground('blue')

    square = Rectangle(Point(2,2),Point(8,8))
    square.setFill('green')
    square.draw(win)

    def circ(x,y):
        center = Point(x,y)
        circ = Circle(center,.3)
        circ.setFill('white')
        #circ.draw(win)
        return circ

    T = Text(Point(5,1),"Click anywhere inside the square")
    T.setSize(15)
    T.setTextColor('white')
    T.draw(win)

    G = win.getMouse()

    while True:
        X = G.getX()
        Y = G.getY()
        circle = circ(X,Y)
        #circle.undraw()

        if 2 <= X <= 8 and 2 <= Y <= 8:
            circle.draw(win)
            G = win.getMouse()
            circle.undraw()
        else:
            break
        
    win.close()        
            

main()
