import pandas as pd

# Calculates Mean Squared Error
# Predicted is the predicted data, data is a test data
# Returns MSE as an int
def mse(predicted, data):
    sumDifference=0
    if (len(predicted)!=len(data)):
        print("tables not equal, invalid input")
        return -1 # -1 is an impossible MSE
    predictedSort=predicted.sort_values(by=predicted.columns[0], ascending=True)
    dataSort=data.sort_values(by=data.columns[0], ascending=True)
    for i in range(len(predictedSort)): # For every row in data
        difference = predictedSort.iloc[i].iloc[0] 
        difference = difference**2 # Find the difference between the predicted and actual then square it
        sumDifference += difference # Add it to a sum
    meanSumDiff = sumDifference / len(predicted) # Divide the sum by the number of rows
    return meanSumDiff # Return it