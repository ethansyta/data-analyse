import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('titanic3.xls')
data.columns
data = data.drop(['ticket','name','sibsp','fare','parch','cabin','embarked','boat','body','home.dest'], axis=1)
data.head()
data = data.dropna(axis=0)
data.shape
data['pclass'].value_counts().plot.bar()
data['age'].hist()
data.groupby(['sex','pclass']).mean()