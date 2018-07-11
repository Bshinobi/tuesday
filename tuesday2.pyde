xCoord = 50
yCoord= 50
xSpeed = 3
ySpeed= 3
ellipseSize= 10

def setup():
    size(400, 400)
    background(0)
    
    
def draw():
    background (0)
    global xCoord, yCoord, xSpeed, ySpeed, ellipseSize 
    topBoundary = ellipseSize / 2 
    bottomBoundary = 400 - ellipseSize / 2
    
    leftBoundary = ellipseSize / 2
    rightBoundary = 800 - ellipseSize / 2
    
    yCoord += ySpeed
    
    

    if yCoord >= bottomBoundary or yCoord <= topBoundary:
      ySpeed = -ySpeed

    fill(255, 255, 0)
    ellipse(yCoord, yCoord, ellipseSize, ellipseSize)
