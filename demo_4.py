import pandas as pd
import os

# Let's load the data for the first time
df = pd.read_pickle(os.path.join('/Users/kmandawe/data/pandas-fundamentals/', 'data_frame.pickle'))

# Demo 1
print(df.artist)
artists = df['artist']
print(pd.unique(artists))
print(len(pd.unique(artists)))
