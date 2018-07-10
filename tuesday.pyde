xCoord = 50
yCoord= 50
xSpeed = 3
ySpeed= 3
ellipseSize= 40

def setup():
    size(400, 400)
    background(0)
    
    
def draw():
    background (0)
    global xCoord, yCoord, xSpeed, ySpeed, ellipseSize 
    leftBoundary = ellipseSize / 2
    rightBoundary = 400 - ellipseSize / 2
    topBoundary = ellipseSize / 2 
    bottomBoundary = 400 - ellipseSize / 2
    xCoord += xSpeed
    yCoord += ySpeed
    
    if xCoord >= rightBoundary or xCoord <= leftBoundary:
     xSpeed= -xSpeed
     if yCoord >= bottomBoundary or yCoord <= topBoundary:
      ySpeed = -ySpeed

    fill(255, 255, 0)
    ellipse(xCoord, yCoord, ellipseSize, ellipseSize)
