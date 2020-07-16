import pandas as pd

#
# creating the pokemon data frame
#

pkmn_df = pd.read_csv('pokemon_data_gen1_to_gen6.csv')

## filtering data

# filtering grass AND poison
#pkmn_df.loc[(pkmn_df['Type 1'] == 'Grass') & (pkmn_df['Type 2'] == 'Poison')]
#print(pkmn_df.loc[(pkmn_df['Type 1'] == 'Grass') & (pkmn_df['Type 2'] == 'Poison')])

# filter grass OR poison
#pkmn_df.loc[(pkmn_df['Type 1'] == 'Grass') | (pkmn_df['Type 2'] == 'Poison')]
#print(pkmn_df.loc[(pkmn_df['Type 1'] == 'Grass') | (pkmn_df['Type 2'] == 'Poison')])

# filter HP greater than X and is legendary
#pkmn_df.loc[(pkmn_df['HP'] > 80) & (pkmn_df['Legendary'] == True)]
#print(pkmn_df.loc[(pkmn_df['HP'] > 80) & (pkmn_df['Legendary'] == True)])

## I can save filter as a dataframe and save that as a csv file
#new_df = pkmn_df.loc[(pkmn_df['Legendary'] == True)]
#new_df.reset_index(drop=True, inplace=True) #inplace=True means you don't need to reassign new_df = new_df...
#print(new_df)
#new_df.to_csv('legendary_filter.csv')

## filter based on textual patterns (i.e. data contains 'Mega')

# filtering all mega (use str.contains('...'))
#pkmn_df.loc[pkmn_df['Name'].str.contains('Mega')]
#print(pkmn_df.loc[pkmn_df['Name'].str.contains('Mega ')]) #space bc Meganium

# filtering not megas (use ~)
#pkmn_df.loc[~pkmn_df['Name'].str.contains('Mega')]
#print(pkmn_df.loc[~pkmn_df['Name'].str.contains('Mega ')])



## filtering using regular expressions
import re
# Regex documentation: https://docs.python.org/3/library/re.html

# filtering fire or grass in type 1 (regex=True)
#pkmn_df.loc[pkmn_df['Type 1'].str.contains('Fire|Grass', regex=True)]
#print(pkmn_df.loc[pkmn_df['Type 1'].str.contains('Fire|Grass', regex=True)])

# to ignore casing (use flags=re.I)
#pkmn_df.loc[pkmn_df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
#print(pkmn_df.loc[pkmn_df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])

# filter pokemon who begin with 'Pi'
#pkmn_df.loc[pkmn_df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
#print(pkmn_df.loc[pkmn_df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])
# Note: ^ means begins with ..
#       * means 0 or more
#       Go to documentation above to find more



## conditional changes

# change 'Fire' to 'FIRE'
#pkmn_df.loc[pkmn_df['Type 1'] == 'Fire', 'Type 1'] = 'FIRE'
#print(pkmn_df)
# change it back
#pkmn_df.loc[pkmn_df['Type 1'] == 'FIRE', 'Type 1'] = 'Fire'
#print(pkmn_df)

# change all 'Fire' Type 1 pokemon to Legendary
#pkmn_df.loc[pkmn_df['Type 1'] == 'Fire', 'Legendary'] = True
#print(pkmn_df.loc[pkmn_df['Type 1'] == 'Fire'])

# changing multiple sections based on condition
pkmn_df.loc[pkmn_df['Total'] > 600, ['Generation,' 'Legendary']] = 'TEST VALUE'
print(pkmn_df)