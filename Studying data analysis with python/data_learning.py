import pandas as pd
import numpy as np
import polars as pl


df=pd.read_csv("us-counties.csv")
print(df)

print (df.describe())
