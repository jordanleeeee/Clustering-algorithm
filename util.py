import math


def decomposeLine(line):
    if line[-1] == "\n":
        line = line[:-1]            # remove \n in the char sequence
    return line.split(",")


# def readDataPoint2(path):
#     points = list()
#     database = open(path, 'r')
#     line = database.readline()
#     while line != "":
#         record = decomposeLine(line)
#         points.append(record)
#         line = database.readline()
#     return points


def readDataPoint(path):
    xCoord = list()
    yCoord = list()
    database = open(path, 'r')
    line = database.readline()
    while line != "":
        record = decomposeLine(line)
        xCoord.append(float(record[0]))
        yCoord.append(float(record[1]))
        line = database.readline()
    return xCoord, yCoord, len(xCoord)


def euclideanDistanceSquare(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def euclideanDistance(x1, y1, x2, y2):
    return math.sqrt(euclideanDistanceSquare(x1, y1, x2, y2))
