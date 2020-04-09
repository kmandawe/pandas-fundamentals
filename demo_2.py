import pandas as pd
import os

# Where our data lives
CSV_PATH = os.path.join('/Users/kmandawe/data/pandas-fundamentals/', 'artwork_data.csv')

# Read just 5 rows to see what's there
df = pd.read_csv(CSV_PATH, nrows=5)
print(df)

# Specify and index
df = pd.read_csv(CSV_PATH, nrows=5, index_col='id')
print(df)

# Limit columns
df = pd.read_csv(CSV_PATH, nrows=5, index_col='id', usecols=['id', 'artist'])
print(df)

# All columns that we need
COLS_TO_USE = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

# Proper data loading
df = pd.read_csv(CSV_PATH,
                 usecols=COLS_TO_USE,
                 index_col='id')
print(df)

# Save for later
df.to_pickle(os.path.join('/Users/kmandawe/data/pandas-fundamentals/', 'data_frame.pickle'))

