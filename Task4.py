import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , classification_report

df = pd.read_csv("cleaned_customer_churn.csv")
le = LabelEncoder()
for column in df.select_dtypes(include='object').columns:
    df[column]=le.fit_transform(df[column])
X=df.drop("Churn_Yes",axis=1)
y=df["Churn_Yes"]
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Classification Report:\n",classification_report(y_test,y_pred))