# rasberry pico with pimoroni display pack
# https://shop.pimoroni.com/products/pico-display-pack
# micropython

import picodisplay as display
import utime
import math

# Initialise display with a bytearray display buffer
buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)
display.set_backlight(0.5)


class Turtle:
    """A simple example class"""
    x = 67
    y = 120
    heading = 0
    
    def __init__(self):
        self.x = 67
        self.y = 120
        self.heading = 0
        
    def clear(self):
        display.set_pen(0, 0, 0)
        display.clear()
        display.update()

    def setPen(self, color):
        print (color)
        display.set_pen(0,255,0)
        
    def forward(self, distance):
        oldx = self.x
        oldy = self.y
        self.x = self.x+int(math.sin(self.heading*2*math.pi/360)*distance)
        self.y = self.y+int(math.cos(self.heading*2*math.pi/360)*distance)
        self.line(oldy, oldx, self.y, self.x)
        display.update()

    def turn(self, degrees):
        self.heading += degrees
        
    def line(self, x0, y0, x1, y1):
        """Draw a line from (x0, y0) to (x1, y1).
        Input coordinates should be integers.
        """
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2*dy - dx
        y = 0

        for x in range(dx + 1):
            self.pixel(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy

    def pixel(self, x, y):
        if (x >= 0) and (x <= display.get_width()):
            if (y >= 0) and (y <= display.get_height()):
                display.pixel(x,y)

turtle = Turtle()
turtle.clear()
print (display.get_width()," x ",display.get_height())
turtle.setPen("green")
turtle.forward(20)
display.update()
turtle.turn(30)
turtle.forward(20)
display.update()
for i in range(36):
    turtle.turn(i)
    turtle.forward(i)
    utime.sleep(0.1)

