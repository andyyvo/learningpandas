import pandas as pd

#
# creating the pokemon data frame
#
print('Data Table\n')

pkmn_df = pd.read_csv('pokemon_data_gen1_to_gen6.csv')

print(pkmn_df.head(3))

# print(pkmn_df.tail(3))

print()

#
# reading data in pandas
#

## read headers
print('Headers\n')
print(pkmn_df.columns)
print()

## read each column
print('Getting Data from Column ____\n')
print(pkmn_df[['Name', 'Type 1', 'Generation']]) #put a column name
print()

## read each row
print('Getting Data from Row ____\n')
# print(pkmn_df.iloc[545])
# print(pkmn_df.iloc[1:4])
# print()

# OR

#for index, row in pkmn_df.iterrows():
#    print(index, row['Name'])
#print()

# OR

print(pkmn_df.loc[pkmn_df['Type 1'] == 'Fire'])

## read a specific location (r,c)
print('Getting Data from Specific Pokemon\n')
print(pkmn_df.iloc[2,1])
print()