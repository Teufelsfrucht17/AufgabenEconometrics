
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy.stats as stats


df = pd.read_excel("SPX.xlsx")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

dfNV = pd.read_excel("NVDA.xlsx")
dfNV["Date"] = pd.to_datetime(df["Date"])
dfNV = dfNV.sort_values("Date")

print(df.head())
print(dfNV.head())


df = df.merge(dfNV, how="left", on="Date")

df["returnsSPX"] = (df["SPX"] / df["SPX"].shift(1)) -1
df["returnsNV"] = (df["NVDA"] / df["NVDA"].shift(1)) -1

df.dropna(inplace=True)

print(df.head())

meanSPX = df["returnsSPX"].mean()
meanNV = df["returnsNV"].mean()
stdSPX = df["returnsSPX"].std()
stdNV = df["returnsNV"].std()
varSPX = df["returnsSPX"].var()
varNV = df["returnsNV"].var()
skewSPX = df["returnsSPX"].skew()
skewNV = df["returnsNV"].skew()
kurtosisSPX = df["returnsSPX"].kurtosis()
kurtosisNV = df["returnsNV"].kurtosis()

print(meanSPX,meanNV,stdSPX,stdNV,varSPX,varNV,skewSPX,skewNV,kurtosisSPX,kurtosisNV)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('SPX', color=color)
ax1.plot(df['Date'], df['SPX'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'

ax2.set_ylabel('NVDA', color=color)
ax2.plot(df['Date'], df['NVDA'], color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.plot(df['Date'], df['NVDA'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()

plt.plot(df['Date'], df['returnsNV'])
plt.plot(df['Date'], df['returnsSPX'])

plt.show()


plt.scatter(df["Date"], df['returnsNV'])
plt.scatter(df["Date"], df['returnsSPX'])
plt.show()


ols = sm.regression.linear_model.OLS(df['returnsNV'], df['returnsSPX']).fit()

print(ols.summary())