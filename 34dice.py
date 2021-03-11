from graphics import *


def main():
    win = GraphWin('dice',500,300)
    win.setCoords(0,0,10,6)
    win.setBackground('blue')

    square = Rectangle(Point(1,1),Point(4,4))
    square.setFill('red')
    square.draw(win)

    s = square.clone()
    s.move(4,0)
    s.draw(win)

    def circ(x,y):
        center = Point(x,y)
        circ = Circle(center,.3)
        circ.setFill('white')
        circ.draw(win)
        return circ

    #dicethree

    circ(3.5,1.5)
    
    x = circ(2.5,2.5).clone()
    x.draw(win)

    y = circ(1.5,3.5).clone()
    y.draw(win)

    #dicefour

    a = circ(5.5,1.5).clone()
    a.draw(win)

    b = circ(5.5,3.5).clone()
    b.draw(win)

    c = circ(7.5,3.5).clone()
    c.draw(win)

    d = circ(7.5,1.5).clone()
    d.draw(win)

main()
