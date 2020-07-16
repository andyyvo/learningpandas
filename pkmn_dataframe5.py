import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# alternatively
#pd.options.display.max_columns = None
#pd.options.display.max_rows = None

#
# creating the pokemon data frame
#

new_df = pd.read_csv('modified_pokemon_data.csv')

## using Groupby functions to do aggregate statistics

# finding mean of all values per type
#new_df.groupby(['Type 1']).mean()
#print(new_df.groupby(['Type 1']).mean())

# sorting means by defense
#new_df.groupby(['Type 1']).mean().sort_values('Defense')
#print(new_df.groupby(['Type 1']).mean().sort_values('Defense'))

# sorting means by defense descending
#new_df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)
#print(new_df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))

# sorting means by attack descending
#new_df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
#print(new_df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

# finding sum of all stats
#new_df.groupby(['Type 1']).sum()
#print(new_df.groupby(['Type 1']).sum())

# finding the count
#new_df['count'] = 1
#new_df.groupby(['Type 1']).count()['count']
#print(new_df.groupby(['Type 1']).count()['count'])

# finding the count with multiple parameters
#new_df.groupby(['Type 1', 'Type 2']).count()['count']
#print(new_df.groupby(['Type 1', 'Type 2']).count()['count'])

#print(new_df)