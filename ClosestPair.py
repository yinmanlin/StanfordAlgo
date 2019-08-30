import MergeSort
import MergeSort2D
import math

def pointDistance(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def ClosestPair(points):
    '''
    points are list of points, i.e. list of list
    should input at least two points
    no duplicate x and y coordinates
    '''
    # first define two base cases
    if len(points) == 3:
        distance1 = pointDistance(points[0], points[1])
        distance2 = pointDistance(points[1], points[2])
        distance3 = pointDistance(points[0], points[2])
        if distance1 < min(distance2, distance3):
            return ([points[0], points[1]], distance1)
        elif distance2 < min(distance1, distance3):
            return ([points[1], points[2]], distance2)
        else:
            return ([points[0], points[2]], distance3)
    elif len(points) == 2:
        distance = pointDistance(points[0], points[1])
        return (points, distance)
    # start recursive calls
    else:
        split = int(len(points) / 2)
        Px = MergeSort.MergeSort([x[0] for x in points])
        xMidPoint = Px[split - 1]
        # sort points by y coordinates
        Py = MergeSort2D.MergeSort2D(points, 1)

        points1, dis1 = ClosestPair(points[:split])
        points2, dis2 = ClosestPair(points[split:])
        if dis1 < dis2:
            minDistance = dis1
            point1, point2 = points1
        else:
            minDistance = dis1
            point1, point2 = points2
        # filter out points whose x coordinates are in the range [xMidPoint - minDistance, xMidPoint + minDistance]
        Sy = [point for point in Py if point[0] >= xMidPoint - minDistance and point[0] <= xMidPoint + minDistance]
        iterLength = len(Sy)
        bestDistance = minDistance
        for i in range(iterLength - 6):
            for j in range(1, 8): # 1,2,3,4,5,6,7
                compDistance = pointDistance(Sy[i], Sy[i + j])
                if compDistance < minDistance:
                    bestDistance = compDistance
                    point1 = Sy[i]
                    point2 = Sy[i + j]
        return ([point1, point2], bestDistance)








