import pandas as pd

data = pd.read_csv('pokemon.csv')

data['Total'] = data[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].sum(axis=1)

mean_stats = data.groupby('Legendary')['Total'].mean()
print(mean_stats)

mean_abilities = data.groupby('Type 1')[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']].mean()
print(mean_abilities)