# Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('C:/Users/rstew/OneDrive/Documents/Diabetes.csv')
data.head()
data.isnull().sum()
y = data['Diabetes_012']

X = data.drop(['Diabetes_012'], axis = 1)
print(f'X : {X.shape}')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)
print(f'X_train : {X_train.shape}')
print(f'y_train : {y_train.shape}')
print(f'X_test : {X_test.shape}')
print(f'y_test : {y_test.shape}')
rf_Model = RandomForestClassifier()
rf_Model.fit(X_train, y_train)
rf_Model.predict(X_test)
rf_Model.predict_proba(X_test)
print("Original Data Frequency Table")
Freq = data.Diabetes_012.value_counts("Diabetes_012")
print(Freq)
data["Smoker"].value_counts("Smoker")
cross = pd.crosstab(index=data["Diabetes_012"], columns=data["Smoker"])
print(cross/cross.sum())
print("Posterior Probability Smoker with Diabetes")
print(str((0.228059*0.449986)/0.217065))
print("Posterior Probability non-Smoker with Diabetes")
print(str((0.208071*0.550014)/0.217065))