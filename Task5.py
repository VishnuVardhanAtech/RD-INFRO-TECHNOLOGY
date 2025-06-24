import pandas as pd

df=pd.read_csv("cleaned_customer_churn.csv")
df['ChurnBinary']=df['Churn_Yes'].map({"Yes":1,"No":0})
correlation=df.corr(numeric_only=True)['ChurnBinary'].sort_values(ascending=False)
print("Top Features correlated with churn:")
print(correlation.drop("ChurnBinary").head(5))
print("\nData Drive Retention Stragies:")
print("-- High 'MonthlyChurn' correlates with higher churn -> offer discounts or value added bundles")
print("-- Low 'tenure' customers churn more -> improve onboarding and provide loyalty incentives")
print("-- Promote 'One year' or 'Two year' instead of 'month-to-month' plans.")
print("-- Improve service for 'Fiber optic' internet users if correlated with churn.")
print("-- Offer targeted support customers with high service-related issues.")
df['LTV']=df['MonthlyCharges']*df['tenure']
print("\nLifetime Value (LTV) calculated as MonthlyCharges x Tenure")
print("Sample LTVs:")
print(df[["customerID","MonthlyCharges","tenure","LTV"]].head())
ltv_thresold=df["LTV"].quantile(0.75)
high_value_churners=df[(df["Churn_Yes"]=="Yes")&(df['LTV']>ltv_thresold)]
print("\nHigh-Value Customers at risk of Churning:")
print(high_value_churners[['customerID','Contract_One year','Contract_Two year','tenure','MonthlyCharges','LTV']])