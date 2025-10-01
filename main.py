from library import *
import pandas as pd

# This is a showcase and testing for code from the library

# Steps:

# Read peng_scaled
df = pd.read_csv("csv/peng_scaled.csv")
df = df.iloc[:, [1,2]]
# Split it into training and testing
folds = fourFold(df)
train = folds[0]
test = folds[1]
maxK = 50 # maxK is the highest K we'll test
mseList = []

# for reach train and test, do knn with k ranging from 1 to 20
for k in range(1,maxK+1): # for ever k 1 through 20
    squareErr = 0
    numRows = 0
    for trainFold in train: # for every training fold
        for i in range(len(trainFold)): # For every input in the training fold
            squareErr += (knn(trainFold, k, trainFold.iloc[i,0])-trainFold.iloc[i,1])**2
            numRows += 1
    # Record the error for each of them
    meanSquareErr = squareErr/numRows
    mseList.append(meanSquareErr)




# Find the k with lowest error from train
bestK = mseList.index(min(mseList))+1

# Use that k on test
squareErr = 0
for rowNum in range(len(test)):
    squareErr += (knn(test.copy(),bestK,test.iloc[rowNum,0])-test.iloc[i,1])**2
MSE = squareErr/len(test)


# compare it to linear regression MSE
lnMSE = 0
line = lnreg(test.copy())
for rowNum in range(len(test)):
    lnMSE += (lineCalc(line[0],line[1],test.iloc[rowNum,0])-test.iloc[i,1])**2
lnMSE /= len(test)
print(MSE)
print(lnMSE)

if MSE < lnMSE:
    better = "KNN"
else:
    better = "linear regression"

print(f"Best K is: {bestK}")
print(better + " is better for this dataset")