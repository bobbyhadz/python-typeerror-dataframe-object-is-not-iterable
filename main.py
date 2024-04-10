# TypeError: 'DataFrame' object is not callable error

# Use square when getting a subset of a DataFrame's rows and columns

import pandas as pd


data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bobby', 'Carl'],
    'salary': [100, 200, 300],
}


df = pd.DataFrame(data)

print(df['name']) # ✅ Using square brackets []