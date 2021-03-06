import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''


data=data.splitlines()
data = [i.split(',') for i in data]

cols=data[0]
rows=data[1:]
df=pd.DataFrame(rows,columns=cols)

df["Alcohol"]=df["Alcohol"].astype(float)
df["Tobacco"]=df["Tobacco"].astype(float)

print "The mean of the Alcohol dataset is :" ,df["Alcohol"].mean()
print "The mean of the Tobacco dataset is :" ,df["Tobacco"].mean()

print "The median of the Alcohol dataset is :" ,df["Alcohol"].median()
print "The median of the Tobacco dataset is :" ,df["Tobacco"].median()

print "The mode of the Alcohol dataset is :" ,stats.mode(df["Alcohol"])[0][0]
print "The mode of the Tobacco dataset is :" ,stats.mode(df["Tobacco"])[0][0]

print "The variance of the Alcohol dataset is :" ,df["Alcohol"].var()
print "The variance of the Tobacco dataset is :" ,df["Tobacco"].var()

print "The standard deviation of the Alcohol dataset is :" ,df["Alcohol"].std()
print "The standard deviation of the Tobacco dataset is :" ,df["Tobacco"].var()



