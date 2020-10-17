import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import lib.clean
import lib.data_preprocessing as DP

# Extract the Data
df = pd.read_csv('Telco_Customer_Churn.csv')

# Data Cleaning
#print(df.isna().sum())

# Capitalize the column names
df = lib.clean.clean_dataframe(df)

df = lib.clean.group_tenure(df)
print(df['CreatedTenure'].unique())

plt.bar(df['CreatedTenure'].unique(), height = list(df['CreatedTenure'].value_counts()))

# plt.pie(df['CreatedTenure'].unique(), height = list(df['CreatedTenure'].value_counts()))

#plt.show()
print(df.head())

# Data Preprocessing
keep_columns = []
for col in df.columns:
    if col not in ['CreatedTenure', 'Customerid']:
        keep_columns.append(col)

df = df[keep_columns]


#df.drop(columns = ['CreatedTenure', 'Customerid'], axis = 1, inplace =True)
#df = df.iloc[: , 1:21]

print(df.head())

'''
colcol = []
for col in df.columns:
    colcol.append(col)
    print(colcol)
    dfdf = df[colcol]
    dt = dfdf.dtypes
    list(dt[dt == pd.Categorical].index)
    print(colcol)
print(pd.Categorical)
#cat = pd.Categorical(df)
#print(cat)
'''
#print(df.nunique())
pp = DP.PreProcessing(df)

#pp.get_categorical()
#pp.Label_Encoder()
#pp.OHE()
#data = pp.return_df()

#print(data.head())

data2 = pp.LabelEncode_OHE()
print(data2.head())