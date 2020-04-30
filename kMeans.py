import numpy
import time
import util
import random
import copy
import matplotlib.pyplot as plt


def getClusters(means, k):
    while True:
        tempMean = copy.deepcopy(means)
        cluster = list()
        for i in range(k):
            cluster.append(list())
        for i in range(size):
            closestD = float('inf')
            suitableCusterId = -1
            for j in range(k):
                distant = util.euclideanDistance(xCoord[i], yCoord[i], means[j][0], means[j][1])
                if distant < closestD:
                    closestD = distant
                    suitableCusterId = j
            cluster[suitableCusterId].append(i)
        for i in range(k):
            means[i][0] = 0
            means[i][1] = 0
            for j in cluster[i]:
                means[i][0] += xCoord[j]
                means[i][1] += yCoord[j]
            clusterSize = len(cluster[i])
            means[i][0] /= clusterSize
            means[i][1] /= clusterSize
        if means == tempMean:
            return cluster


def getInitialMeans(k):
    randPt = random.randint(0, size - 1)
    meanPts = list()
    meanPts.append(randPt)
    for i in range(k - 1):
        probability = list()
        for j in range(size):
            minD = float('inf')
            for m in meanPts:
                d = util.euclideanDistanceSquare(xCoord[j], yCoord[j], xCoord[m], yCoord[m])
                if d < minD:
                    minD = d
            probability.append(minD)
        total = sum(probability)
        for j in range(size):
            probability[j] /= total
        meanPts.append(numpy.random.choice(numpy.arange(0, size), p=probability))

    means = list()
    for pt in meanPts:
        means.append([xCoord[pt], yCoord[pt]])
    return means


def kMeans(k):
    means = getInitialMeans(k)
    clusters = getClusters(means, k)
    SSE = calSSE(k, clusters, means)
    print("when k = " + str(k) + " sum of squared error = " + str(SSE))
    return clusters


def calSSE(k, clusters, means):
    SSE = 0
    for i in range(k):
        cluster = clusters[i]
        mean = means[i]
        for pt in cluster:
            SSE += util.euclideanDistanceSquare(xCoord[pt], yCoord[pt], mean[0], mean[1])
    return SSE


def plotCluster(clusters, k):
    for cluster in clusters:
        x = list()
        y = list()
        for point in cluster:
            x.append(xCoord[point])
            y.append(yCoord[point])
        plt.scatter(x, y, s=1)

    plt.title(str(k) + ' means clusters')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(str(k) + ' means clusters.png')
    plt.show()


xCoord, yCoord, size = util.readDataPoint("a3dataset.txt")
for k in [3, 6, 9]:
    start = time.time()
    clusters = kMeans(k)
    print("time taken = " + str(time.time()-start) + "s")
    plotCluster(clusters, k)
