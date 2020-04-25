import util
import time
import matplotlib.pyplot as plt


# use BFS the get all reachable neighbor of a point
def getDensityReachablePt(pt, neighborhood):
    reachablePts = list()
    # BFS for reachable points
    isVisited = dict()
    for key in neighborhood.keys():
        isVisited[key] = False
    isVisited[pt] = True
    queue = list()
    queue.append(pt)
    while len(queue) != 0:
        point = queue.pop(0)
        reachablePts.append(point)
        for p in neighborhood[point]:
            if not isVisited[p]:
                isVisited[p] = True
                queue.append(p)
    return reachablePts


def DBscan(corePts, neighborhood):
    clusters = list()
    unProcessedPts = set(corePts)
    while len(unProcessedPts) != 0:
        # print(unProcessedPts)
        pt = unProcessedPts.pop()
        densityReachablePt = getDensityReachablePt(pt, neighborhood)
        clusters.append(densityReachablePt)
        unProcessedPts -= set(densityReachablePt)
    print(clusters)
    return clusters


# find all core pt and noise pt
# also find neighborhood of each pt
def classifyPts(eps, minPts):
    corePts = set()
    noisePts = set()
    neighborhood = dict()
    for i in range(size):
        temp = list()
        for j in range(size):
            distant = util.euclideanDistance(xCoord[i], yCoord[i], xCoord[j], yCoord[j])
            if distant <= eps:
                temp.append(j)
        neighborhood[i] = temp

    for pt, neighbors in neighborhood.items():
        if len(neighbors) >= minPts:
            corePts.add(pt)
    for pt, neighbors in neighborhood.items():
        if pt not in corePts:
            isBorderPt = False
            for neighbor in neighbors:
                if neighbor in corePts:
                    isBorderPt = True
                    break
            if not isBorderPt:
                noisePts.add(pt)
    return corePts, noisePts, neighborhood


def plotCluster(clusters, noisePts, eps, minPts):
    for cluster in clusters:
        x = list()
        y = list()
        for point in cluster:
            x.append(xCoord[point])
            y.append(yCoord[point])
        plt.scatter(x, y, s=1)
    x = list()
    y = list()
    for point in noisePts:
        x.append(xCoord[point])
        y.append(yCoord[point])
    plt.scatter(x, y, s=2, color="black")

    plt.title("eps= "+str(eps)+" minPts= "+str(minPts)+" DBScan")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig("eps= "+str(eps)+" minPts= "+str(minPts)+" DBScan.png")
    # plt.show()


xCoord, yCoord, size = util.readDataPoint("a3dataset.txt")

for eps, minPts in [[5, 5], [5, 6], [5, 7]]:
    start = time.time()
    corePts, noisePts, neighborhood = classifyPts(eps, minPts)
    clusters = DBscan(corePts, neighborhood)
    print("time taken = " + str(time.time() - start) + "s")
    plotCluster(clusters, noisePts, eps, minPts)
