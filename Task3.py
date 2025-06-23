import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("cleaned_customer_churn.csv")
def get_contract(row):
    if row['Contract_Two year']==1:
        return 'Two year'
    elif row['Contract_One year']==1:
        return 'One year'
    else:
        return 'Month-to-Month'
df['Contract']=df.apply(get_contract,axis=1)
df['Churn']=df['Churn_Yes'].apply(lambda x:'Yes' if x==1 else 'No')
contract_map={'Month-to-Month':0 , 'One year':1 , 'Two year':2}
df['Contract_encoded']=df['Contract'].map(contract_map)
X=df[['tenure','MonthlyCharges','Contract_encoded']]
Kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Segment']=Kmeans.fit_predict(X)
churn_analysis=df.groupby('Segment')['Churn'].value_counts(normalize=True).unstack().fillna(0)
churn_analysis_output=churn_analysis.round(3).reset_index()
print("\nChurn Rate by Segment:\n")
print(churn_analysis_output)