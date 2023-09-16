from cmu_graphics import *

app.background = 'black'

Rect(30, 375, 340, 25, fill='grey')
Oval(200, 375, 340, 50, fill='darkGrey')

display = Group(
    Circle(200, 200, 150, fill='orange'),
    Star(200, 200, 150, 500, fill='red'),
    Circle(200, 200, 100),
    Star(200, 200, 95, 5, fill=gradient('red', 'orange')),
    Oval(200, 375, 300, 20, fill='dimGrey')
    )
display.widthChange = -8

def onStep():
    display.width += display.widthChange
    if display.width > 300:
        display.widthChange = -8
    elif display.width < 10:
        display.widthChange = 8


cmu_graphics.run()

