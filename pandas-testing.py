import pandas as pd

# Read data from .csv file
data = pd.read_csv('/Users/andresabastante/codigo/pandas-testing/IMDB-Movie-Data.csv')

# Read data with specified explicit index.
# We will use this later in our analysis
data_indexed = pd.read_csv('/Users/andresabastante/codigo/pandas-testing/IMDB-Movie-Data.csv', index_col="Title")

print(data_indexed)
test=data_indexed.loc[['Suicide Squad']][['Genre','Actors','Director','Rating','Revenue (Millions)']]

print(test)
test=data.iloc[10:15][['Title','Rating','Revenue (Millions)']]
print(test)