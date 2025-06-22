import pandas as pd
import numpy as np

df = pd.read_csv("customer_churn_sample.csv")
print("Initial Data Preview:")
print(df.head())

#convert total charges into numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

#Checking for missing values 
print("\nMissing values before cleaning:")
print(df.isnull().sum())
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)#filling total charges with median
df['OnlineSecurity'].fillna(df['OnlineSecurity'].mode()[0], inplace=True)
df['DeviceProtection'].fillna(df['DeviceProtection'].mode()[0], inplace=True)

#Recheck for missing values
print('\nMissing values after cleaning:')
print(df.isnull().sum())

#encode categorial variables using onehot encoding
df_encoded = pd.get_dummies(df, drop_first=True)
print("\nEncoded data sample:")
print(df_encoded.head())
df_encoded.to_csv("cleaned_customer_churn.csv", index=False)
print("\ncleaned data saved as 'cleaned_customer_churn.csv'")