import pandas as pd
import os

# Let's load the data for the first time
df = pd.read_pickle(os.path.join('/Users/kmandawe/data/pandas-fundamentals/', 'data_frame.pickle'))

# Demo 1
print(df.artist)
artists = df['artist']
print(pd.unique(artists))
print(len(pd.unique(artists)))

# Demo 2
s = df['artist'] == 'Bacon, Francis'
print(s)
print(s.value_counts())

# Other way
artist_counts = df['artist'].value_counts()
print(artist_counts)
print(artist_counts['Bacon, Francis'])

# Demo 3
print(df.loc[1035, 'artist'])
print(df.iloc[0, 0])
print(df.iloc[0,:])
print(df.iloc[0:2, 0:2])

# Try multiplication
# print(df['height'] * df['width'])
print()
print(df['width'].sort_values().head())
print()
print(df['width'].sort_values().tail())

# Try to convert
# pd.to_numeric(df['width'])

pd_numeric = pd.to_numeric(df['width'], errors='coerce')
print(pd_numeric)
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')

pd.to_numeric(df['height'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors='coerce')

print("Multiplication:")
print(df['height'] * df['width'])
print(df['units'].value_counts())

# Assign - create new columns with size
area = df['height'] * df['width']
df = df.assign(area=area)
print(df)
print()
print('Max:')
print(df['area'].max())
print()
print("Index Max:")
print(df['area'].idxmax())
print()
print("Loc:")
print(df.loc[df['area'].idxmax(), :])