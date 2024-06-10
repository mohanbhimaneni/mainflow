import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
data=pd.read_csv("C:/Users/bhmoh/Downloads/heart_failure.csv")
del data['Unnamed: 0']
print(data.head(10))
#scatter plot with age against serum_creatinine without title or labels
plt.scatter(data['age'],data['serum_creatinine'])
plt.show()
#adding title and labels
plt.scatter(data['age'],data['serum_creatinine'])
plt.title('Scatter plot for heart failue')
plt.xlabel('age')
plt.ylabel('serum creatinine')
plt.show()
#line chart for age and serum_sodium
plt.plot(data['age'],data['serum_sodium'])

plt.title("Line plot for heart failure")

plt.xlabel('Age')
plt.ylabel('Serum sodium')

plt.show()
#Bar plot for age and creatinine_phosphokinase
plt.bar(data['age'],data['creatinine_phosphokinase'])

plt.title("Bar plot for heart failure")

plt.xlabel("Age")
plt.ylabel("Creatinine Phosphokinase")

plt.show()
#Histogram

plt.hist(data['age'])

plt.title("Histogram")

plt.show()
