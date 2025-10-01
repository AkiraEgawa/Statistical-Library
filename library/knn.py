import pandas as pd

# Takes a dataframe, the number of nearest neighbors, and the x to estimate
# Dataframe must have 2 columns, column 0 is x and column 1 is y
def knn(df, k, x):
    # basic cleanup
    df.dropna()

    # Find the distance of each point from given x
    df.iloc[:,0]=abs(df.iloc[:,0]-x)
    # Find the k nearest ones
    df=df.sort_values(by=df.columns[0], ascending=True)
    knearest = df[df.columns[1]].head(k)
    # Average their y values
    kMean=knearest.mean()
    # Return said y value
    return kMean