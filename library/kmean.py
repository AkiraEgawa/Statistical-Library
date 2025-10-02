import pandas as pd
import numpy as np

# Given a dataframe with 3 columns (0 is x, 1 is y, 2 is cluster), determine the mean of the n'th cluster
def meanCluster(df, nCluster):
    subset = df[df["cluster"] == nCluster] # Filter out the proper cluster
    meanX = subset.iloc[:, 0].mean()
    meanY = subset.iloc[:, 1].mean()
    return [meanX,meanY]

# Given 2 vectors of equal length, calculate the euclidean distance squared between them
def dist(v1, v2):
    if (len(v1) != len(v2)):
        print("Vectors exist in separate dimensions")
        return -1 # -1 is an impossible euclidean distance while using real numbers
    length = len(v1)
    deltaSquare = []
    for i in range(length):
        deltaSquare.append((v1[i]-v2[i])**2)
    return np.sum(deltaSquare)

# Given pointO as length 2 array, and otherPoint as a vector holding length 2 arrays of points
# Returns array of distance of pointO from each of the otherPoint
def pointDist(pointO, otherPoint):
    distArr = []
    for i in range(len(otherPoint)):
        distArr.append(dist(pointO, otherPoint[i]))
    return distArr

# Given a dataframe and the number of clusters, will repeat cluster formation until the mean Delta Distance of centroids is less or equal to min Dist
# Cluster is int
# DF is a dataframe, 2 columns (0 is x, 1 is y)
# minDist is an int or a decimal
# Will return df with 3 columns, 3rd column will be the number saying which cluster it is (1-cluster number)
def kmean(numCluster, df, minDist):
    df["cluster"] = np.random.randint(1, numCluster+1, size = len(df)) # randomly assign a cluster to each point
    centroid = []
    newCentroid = [None] * numCluster
    deltaDist = minDist + 1 # Just placeholder value to make sure first while loop always goes through (don't need to account for integer limit hopefully, why would it be that big???)
    deltaDistArr = [None] * numCluster
    for cluster in range(1, numCluster+1): # For each cluster, assign centroid to the average of x and y
        centroid.append(meanCluster(df,cluster))
    while deltaDist >= minDist:
        # Find distance of each point from each centroid
        for entry in range(len(df)):
            df.loc[entry, "distance"] = pointDist([df.iloc[entry, 0], df.iloc[entry, 1]], centroid)
        # Reassign each point to closest centroid
            df.loc[entry, "cluster"] = df.loc[entry, "distance"].index(min(df["distance"]))
            
        # Find new centroid
        for cluster in range(numCluster):
            newCentroid[cluster] = meanCluster(df, cluster+1)
            # update distance of each centroid from new centroid
            deltaDistArr[cluster] = dist(newCentroid[cluster], centroid[cluster])
            # assign newCentroid to centroid
            for i in range(2):
                centroid[cluster][i] = newCentroid[cluster][i]
        deltaDist = (np.sum(deltaDistArr))/numCluster
    return df