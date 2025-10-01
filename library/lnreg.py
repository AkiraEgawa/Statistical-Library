# This will be linear regression (thankfully, I did some math to just have a singular math function lol)
# Takes a dataframe with 2 columns (first column x, second column y) and returns the a and b for the line y=ax+b
def lnreg(df, x):
    """
    Given datapoints and a line to estimate it as y = ax + b
    a = (mean(xy)-mean(x)mean(y))/(mean(x^2)-mean(x)^2)
    b = mean(y) - a * mean(x)
    """
    # time for code to appear
    dX = df[df.columns[0]]
    dY = df[df.columns[1]]
    dXY = dX * dY
    a = (dXY.mean() - (dX.mean() * dY.mean()))/(((dX)**2).mean() - (dX.mean())**2)
    b = dY.mean() - a * dX.mean()
    return [a,b]


# Takes a, b, and x for a line y=ax+b and returns y
def lineCalc(a, b, x):
    y=a*x+b
    return y