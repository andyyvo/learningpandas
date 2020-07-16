import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# alternatively
#pd.options.display.max_columns = None
#pd.options.display.max_rows = None

#
# creating the pokemon data frame
#

pkmn_df = pd.read_csv('pokemon_data_gen1_to_gen6.csv')

## sorting and describing data

# print(pkmn_df.describe())
# describes the different columns of the pokemon data

# print(pkmn_df.sort_values('Name'))
# sorts pokemon by name

# print(pkmn_df.sort_values('Name', ascending=False))
# sorts pokemon names in descending order

# print(pkmn_df.sort_values(['Type 1', 'HP']))
# sorts pokemon by type 1 alphabetically so bug and then hp in each type

# print(pkmn_df.sort_values(['Type 1', 'HP'], ascending=[1,0]))
# same as above but type 1 is ascending and hp is descending