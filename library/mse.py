import pandas as pd

# Calculates Mean Squared Error
# Predicted is the predicted data, data is a test data
# Returns MSE as an int
def mse(predicted, data):
    sumDifference=0
    if (len(predicted)!=len(data)):
        print("tables not equal, invalid input")
        return -1 # -1 is an impossible MSE
    for i in range(len(predicted)): # For every row in data
        difference = predicted.iloc[i,1] - data.iloc[i,1]
        difference = difference**2 # Find the difference between the predicted and actual then square it
        sumDifference += difference # Add it to a sum
    meanSumDiff = sumDifference / len(predicted) # Divide the sum by the number of rows
    return meanSumDiff # Return it