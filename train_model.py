import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("dataset/health_data.csv")

X = data[['Age','BMI','BloodPressure','Glucose']]
y = data['Risk']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier()

model.fit(X_train,y_train)

pickle.dump(model,open("health_model.pkl","wb"))

print("Model Saved")
