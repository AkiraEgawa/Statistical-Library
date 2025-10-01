import pandas as pd
import numpy as np

# There is a scikit package to just do it, but I want to manually make it

# four fold validation
# pass in a dataframe
# returns 4 training sets and 1 test set
# 80%-20% for training to test
def ffVal(df):
    df = df.sample(frac = 1, random_state = 69).reset_index(drop=True)
    folds = np.array_split(df, 5)
    test_df = folds[0]
    train = folds[1:]
    return [train, test_df]