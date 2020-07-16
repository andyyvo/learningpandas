import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# alternatively
#pd.options.display.max_columns = None
#pd.options.display.max_rows = None

#
# creating the pokemon data frame
#

for new_df in pd.read_csv('modified_pokemon_data.csv', chunksize=5):
    print('CHUNK DF')
    print(new_df)

## working with large mounts of data
