import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,r2_score
from sklearn.ensemble import RandomForestRegressor
import joblib
import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv("clean data.csv")
print(df.sample(10))

x = df[["City","State","College_Type","College_Management","Region_North_South_East_West_Central","Total_no._of_Courses"]]
y = df["Student_Strength"]


# x_train,x_text,y_train,y_text=train_test_split(x,y,test_size=0.2,random_state=20)

# Convert text columns into numeric columns
X = pd.get_dummies(x)

# Save column names
columns = X.columns

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=20)

# Create Model
model = RandomForestRegressor(n_estimators=200,random_state=42)
# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("R2 Score :", r2_score(y_test, y_pred))


# Save Model
joblib.dump(model, "student_strength_model.pkl")

# Save Feature Columns
joblib.dump(columns, "model_columns.pkl")

print("Model Saved Successfully")

