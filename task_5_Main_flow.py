import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/Users/bhmoh/Downloads/heart.csv")
print(df.head())
print(df.tail())
print(df.columns.values)
print(df.isna().sum())
print(df.info())
df.hist(bins=50,grid=True, figsize=(20,15))
plt.show()
print(df.describe())
questions=['1. How many people have heart disease and how many people doesn\'t?',
           '2. People of which sex has most heart disease?',
           '3. People of which sex has which type of chest pain most?',
           '4. People with which chest pain are most prone to have heart disease?',
           '5. Does cholestrol level affect heart disease?',
           '6. How much cholestrol level affect the heart disease?',
           '7. What would be the minimum age to get a heart disease?'
          ]
print(questions[0])
#1st question
print(df.target.value_counts())
df.target.value_counts().plot(kind='bar',color=['red','blue'])
plt.title('Heart Disease values')
plt.xlabel('Heart disease')
plt.ylabel('Count')
plt.show()
df.target.value_counts().plot(kind='pie',figsize=(8,6))
plt.legend(['With heart disease','Without heart disease'])
plt.show()
print(questions[1])
print(df.sex.value_counts())
df.sex.value_counts().plot(kind='pie',figsize=(8,6))
plt.title("Male Female ratio")
plt.legend(['Male','Female'])
plt.show()
print(pd.crosstab(df.target,df.sex))
sns.countplot(x='target',data=df,hue='sex')
plt.title("Heart Disease Frequency for each sex")
plt.xlabel('Disease')
plt.show()
print(questions[2])
print(df.cp.value_counts())
df.cp.value_counts().plot(kind='bar',color=['salmon','lightskyblue','springgreen','khaki'])
plt.title('Chest pain type vs count')
plt.show()
print(pd.crosstab(df.sex,df.cp))
pd.crosstab(df.sex,df.cp).plot(kind='bar',color=['coral','lightskyblue','plum','khaki'])
plt.title('Type of chest pain for sex')
plt.xlabel("Gender (0-F,1-M)")
plt.show()
print(questions[3])
print(pd.crosstab(df.cp,df.target))
sns.countplot(x='cp',data=df,hue='target')
plt.show()
sns.displot(x='age',data=df,bins=30,kde=True)
plt.show()
sns.displot(x='thalach',data=df,bins=30,kde=True,color='blue')
plt.show()
print(questions[4])
print(df.chol.value_counts())
print(np.var(pd.crosstab(df.chol,df.target),axis=0))
print(questions[5])
pd.crosstab(df.chol,df.target).plot(kind='bar',figsize=(500,60))
plt.show()
print(questions[6])
sns.countplot(x='age',data=df,hue='target')
sns.set(rc={"figure.figsize":(40,40)})
plt.show()
