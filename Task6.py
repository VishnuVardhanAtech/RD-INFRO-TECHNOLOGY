import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv("cleaned_customer_churn.csv")
df['ChurnBinary']=df["Churn_Yes"].map({"Yes":1,"No":0})
df['MonthlyCharges']=pd.to_numeric(df['MonthlyCharges'], errors='coerce')
df['tenure']=pd.to_numeric(df['tenure'], errors='coerce')
df['TotalCharges']=pd.to_numeric(df['TotalCharges'], errors='coerce')


plt.figure(figsize=(8,6))
sns.boxplot(x="Churn_Yes",y="MonthlyCharges",data=df)
plt.title("BoxPlot:MonthlyCharges")
plt.xlabel("Churn (0=No, 1=Yes)")
plt.ylabel("MontghlyCharges ($)")
plt.xticks([0,1],['No','Yes'])
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
sns.violinplot(x="Churn_Yes",y="MonthlyCharges",data=df)
plt.title("Violion Plot:MonthlyCharges")
plt.xlabel("Churn (0=No, 1=Yes)")
plt.ylabel("MontghlyCharges ($)")
plt.xticks([0,1],['No','Yes'])
plt.tight_layout()
plt.show()

numeric_cols=["tenure","MonthlyCharges","TotalCharges","ChurnBinary"]
missing_cols=[col for col in numeric_cols if col not in df.columns]
if missing_cols:
    print(f'Error:Missing columns :{missing_cols}')
    exit()
non_numeric_cols=[col for col in numeric_cols if not pd.api.types.is_numeric_dtype(df[col])]
if non_numeric_cols:
    print(f'Error:Non-Numeric columns :{non_numeric_cols}')
    exit()
plt.figure(figsize=(8,6))
correlation_matrix=df[numeric_cols].corr()
sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',vmin=-1,vmax=1)
plt.title("Heatmap:Correlation btw numeric variables")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
sns.countplot(x="Churn_Yes",data=df)
plt.title("Bar Plot:Count of Customers")
plt.xlabel("Churn (0:No, 1:Yes)")
plt.ylabel("Number of costumers")
plt.xticks([0,1],['No','Yes'])
for i,v in enumerate(df["Churn_Yes"].value_counts()):
    plt.text(i,v,str(v),ha="center",va="bottom")
plt.tight_layout()
plt.show()


