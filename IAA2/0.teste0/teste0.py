import pandas as pd
import numpy as np

df = pd.read_csv("archive.zip")

data = df.drop(columns="species")

#print(data.corr())

#print(data.iloc[123].max())

#print(data.tail())
print(data.describe())