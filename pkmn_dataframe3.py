import pandas as pd

#
# creating the pokemon data frame
#

pkmn_df = pd.read_csv('pokemon_data_gen1_to_gen6.csv')

## making changes to the data

# adding a column
#pkmn_df['Total'] = pkmn_df['HP'] + pkmn_df['Attack'] + pkmn_df['Defense'] + \
    #pkmn_df['Sp. Atk'] + pkmn_df['Sp. Def'] + pkmn_df['Speed']

#print(pkmn_df.head(5))

# removing a column
#pkmn_df = pkmn_df.drop(columns=['Total'])

# adding a column by summing multiple columns to make new column
pkmn_df['Total'] = pkmn_df.iloc[:, 4:10].sum(axis=1) #axis=1 is horizontal, 0 is vertical

# moving the Totals column
cols = list(pkmn_df.columns.values)
pkmn_df = pkmn_df[cols[0:10] + [cols[-1]] + cols[10:12]]

#print(pkmn_df.head(5))

# saving modified csv file
#pkmn_df.to_csv('modified_pokemon_data.csv', index=False)
# saving modified file as excel
#pkmn_df.to_excel('modified_pokemon_data.xlsx', index=False)
# saving modified file as txt
#pkmn_df.to_csv('modified_pokemon_data.txt', index=False, sep='\t')