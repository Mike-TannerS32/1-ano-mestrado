import pandas as pd 
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("housing.zip")
print(df.head())
#df = df.drop('ocean_proximity', axis=1)
#sns.pairplot(df)
#plt.hist(df)
#plt.show()

intervalos = [0,1.5,3.0,4.5,6.0]
df['salary_category'] = pd.cut(df['median_income'], bins=intervalos,labels=False,right=False)
#df = df.dropna()

X = df.drop(['ocean_proximity', 'salary_category'], axis=1)
y = df['salary_category']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
print(df['salary_category'].value_counts(normalize=True))
print(y_train.value_counts(normalize=True))
print(y_test.value_counts(normalize=True))



#print(lm.intercept_)


''' 
plt.figure(figsize=(10,6))
plt.scatter(df['longitude'],df['latitude'],s= df['population']/100, c='blue',alpha=0.5)
plt.title('Areas mais densas')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df['population'],df['median_house_value'],alpha=0.5)
plt.xlabel('Population')
plt.ylabel('Median_house_value')
plt.show()


df=df.drop('ocean_proximity',axis=1)
corr = df.corr()
corr_preco_med = corr['median_house_value'].sort_values(ascending=False)
print(corr_preco_med)

atr_mais_corr = corr_preco_med[1:6].index.tolist()
pd.plotting.scatter_matrix(df[atr_mais_corr], figsize=(12,8))
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df['median_income'], df['median_house_value'],alpha=0.5)
plt.title('Correlação com o preço mediano')
plt.xlabel('Atributo com alta correlação')
plt.ylabel('Preço Mediano')
plt.show()
'''
valores_falta = df.isnull().sum()
print("Valores em falta por atributo:")
print(valores_falta)

mediana = df.drop('ocean_proximity',axis=0).median()
dados_preench= df.fillna(mediana)
print(dados_preench)


ocean_proximity = df['ocean_proximity']
encoder = OneHotEncoder()

ocean_encoded = encoder.fit_transform(ocean_proximity)
ocean_encoded_df = pd.DataFrame(ocean_encoded.toarray(), columns=encoder.get_feature_names_out(['ocean_proximity']))
dados_encoded = pd.concat([dados_preench.drop('ocean_proximity', axis=0), ocean_encoded_df], axis=1 )
print(dados_encoded)

# não faz sentido atribuir um valor numérico diferente a cada valor de "ocean proximity" 
#porque é uma proximidade relativa e não um valor absoluto