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
    elif len(points) == 4:
        distance1 = pointDistance(points[0], points[1])
        distance2 = pointDistance(points[0], points[2])
        distance3 = pointDistance(points[0], points[3])
        distance4 = pointDistance(points[1], points[2])
        distance5 = pointDistance(points[1], points[3])
        distance6 = pointDistance(points[2], points[3])
        if distance1 < min(distance2, distance3, distance4, distance5, distance6):
            return ([points[0], points[1]], distance1)
        elif distance2 < min(distance1, distance3, distance4, distance5, distance6):
            return ([points[0], points[2]], distance2)
        elif distance3 < min(distance1, distance2, distance4, distance5, distance6):
            return ([points[0], points[3]], distance3)
        elif distance4 < min(distance1, distance2, distance3, distance5, distance6):
            return ([points[1], points[2]], distance4)
        elif distance5 < min(distance1, distance2, distance3, distance4, distance6):
            return ([points[1], points[3]], distance5)
        else:
            return ([points[2], points[3]], distance6)
    # start recursive calls
    else:
        split = int(len(points) / 2)
        points1, dis1 = ClosestPair(points[:split])
        points2, dis2 = ClosestPair(points[split:])
        if dis1 < dis2:
            minDistance = dis1
            point1, point2 = points1
        else:
            minDistance = dis2
            point1, point2 = points2

        # split situation
        Px = MergeSort.MergeSort([x[0] for x in points])
        xMidPoint = Px[split - 1]
        # sort points by y coordinates
        Py = MergeSort2D.MergeSort2D(points, 1)

        # filter out points whose x coordinates are in the range [xMidPoint - minDistance, xMidPoint + minDistance]
        # note here length of Sy might be less than 8
        Sy = [point for point in Py if point[0] >= xMidPoint - minDistance and point[0] <= xMidPoint + minDistance]
        iterLength = len(Sy)
        bestDistance = minDistance
        if iterLength > 8: #9
            for i in range(iterLength - 8): # 0,1,
                for j in range(1, 8): # 1,2,3,4,5,6,7
                    compDistance = pointDistance(Sy[i], Sy[i + j])
                    if compDistance < minDistance:
                        bestDistance = compDistance
                        point1 = Sy[i]
                        point2 = Sy[i + j]
                        return ([point1, point2], bestDistance)
        else:
            pointSplit, distanceSplit = ClosestPair(Sy)
            if distanceSplit < bestDistance:
                point1, point2 = pointSplit
            return ([point1, point2], bestDistance)



print(ClosestPair([[1,2],[5,4],[0,0],[2,2],[3,3],[5,8],[6,0],[8,9],[1,4],[0,0]]))





