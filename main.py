from library.mse import mse
from library.lnreg import lnreg
from library.lnreg import lineCalc
import pandas as pd

df = pd.read_csv("csv/peng_scaled.csv")
df = df.iloc[:, [1,2]]
df.dropna()
line = lnreg(df)
dfTest=pd.read_csv("csv/peng_scaled.csv")
dfTest = dfTest.iloc[:, [1,2]]
dfTest.dropna()
for i in range(len(dfTest)):
    dfTest.loc[i,1] = lineCalc(line[0], line[1], dfTest.iloc[i].iloc[0])

meanSquaredError = mse(dfTest, df)
print(meanSquaredError)