import numpy as np
import pandas as pd
data=pd.read_csv("C:/Users/bhmoh/Downloads/heart_failure_clinical_research_dataset.csv")
print(data)
data.isnull()
data.isnull().sum()
data.notnull()
data.isnull().sum().sum()
data1=data.fillna(value=0)
print(data1)
data2=data.fillna(method="pad")
print(data2)
data3=data.fillna(method="bfill")
print(data3)
import matplotlib.pyplot as plt
from scipy import stats
data1.columns
data1.drop("anaemia",axis=1,inplace=True)
data1.columns
Q1=data1.quantile(0.25)
Q3=data1.quantile(0.75)
IQR=Q3-Q1
IQR