input = [[1, 1, 2], [2, 2, 0.5], [-1, -3, 2], [5, 2, 1]]


class Circle():
    """ Represents a cirlce """

    def __init__(self, x, y, r):
        """ Initialize """
        self.x = x
        self.y = y
        self.r = r

    def getLeft(self):
        """ Return x coordinate of leftmost edge of circle """
        return self.x - self.r

    def getRight(self):
        """ Return x coordinate of rightmost edge of circle """
        return self.x + self.r

    def getTop(self):
        """ Return y coordinate of topmost edge of circle """
        return self.y + self.r

    def getBottom(self):
        """ Return y coordinate of bottommost edge of circle """
        return self.y - self.r


def findLeftmost(circleObjs):
    """ Iterate through list of circle objects  """
    """ and return leftmost coordinate """
    leftmost = 9999
    for circle in circleObjs:
        if circle.x - circle.r < leftmost:
            leftmost = circle.x - circle.r
    return leftmost


def findTopmost(circleObjs):
    """ Iterate through list of circle objects  """
    """ and return leftmost coordinate """
    topmost = -9999
    for circle in circleObjs:
        if circle.y + circle.r > topmost:
            topmost = circle.y + circle.r
    return topmost


def findRightmost(circleObjs):
    """ Iterate through list of circle objects  """
    """ and return leftmost coordinate """
    rightmost = -9999
    for circle in circleObjs:
        if circle.x + circle.r > rightmost:
            rightmost = circle.x + circle.r
    return rightmost


def findBottommost(circleObjs):
    """ Iterate through list of circle objects  """
    """ and return leftmost coordinate """
    bottommost = 9999
    for circle in circleObjs:
        if circle.y - circle.r < bottommost:
            bottommost = circle.y - circle.r
    return bottommost


def makeCircleList(coordList):
    """ Iterate through list of circle coordinates and make circle object """
    circleList = []
    for value in coordList:
        newCircle = Circle(value[0], value[1], value[2])
        circleList.append(newCircle)
    return circleList


def makeCorners(cornerList):
    corners = [[cornerList[0, 3], cornerList[0, 1],
                cornerList[2, 1], cornerList[2, 3]]
    return corners

circleList = makeCircleList(input)
cornerList = [findLeftmost(circleList), findTopmost(circleList),
              findRightmost(circleList), findBottommost(circleList)]
