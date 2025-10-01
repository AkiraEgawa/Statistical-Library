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
print(dfTest)
for i in range(len(dfTest)):
    dfTest.loc[i,"bill_scaled"] = lineCalc(line[0], line[1], df.iloc[i,0])
print(dfTest)

meanSquaredError = mse(dfTest, df)
print(meanSquaredError)