import numpy as np
import pandas as pd

my_numpy_array = np.random.rand(3)
print("Regular Numpy:")
print(my_numpy_array)

my_first_series = pd.Series(my_numpy_array)
print("Series:")
print(my_first_series)

my_first_df = pd.DataFrame(np.random.rand(3, 2))
print("DataFrame:")
print(my_first_df)