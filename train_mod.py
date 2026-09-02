import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("loan_data.csv")
df=df.fillna(df.mode().iloc[0])


df['Property_Area'] = df['Property_Area'].map({
    'Rural':0,
    'Semiurban':1,
    'Urban':2
})

df['Loan_Status'] = df['Loan_Status'].map({
    'N':0,
    'Y':1
})


X = df[
[
'ApplicantIncome',
'LoanAmount',
'Loan_Amount_Term',
'Property_Area'
]
]

y = df['Loan_Status']    #means to get ans as yes or no called as target variable

model = RandomForestClassifier()  #a machine learning algorithm used for classification

model.fit(X,y) #here mode is trained with the data and target variable see and learn from the example patterns in our data

joblib.dump(model,'model.pkl') # created model.pkl automatically and saved model in this, brain of my model

print("Model Trained Successfully")



# loan_data.csv
#       ↓
# Read Dataset
#       ↓
# X = Inputs
#       ↓
# y = Loan_Status
#       ↓
# RandomForestClassifier()
#       ↓
# model.fit(X,y)
#       ↓
# Model learns
#       ↓
# joblib.dump()
#       ↓
# model.pkl created