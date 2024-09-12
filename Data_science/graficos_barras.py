import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('pokemon.csv')

data['Total'] = data[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].sum(axis=1)

meta = data.nlargest(10, 'Total')

plt.figure(figsize=(12, 8))
bars = plt.bar(meta['Name'], meta['Total'], color='skyblue')
plt.xlabel('Pokémon')
plt.ylabel('Total de AtributosS')
plt.title('Top 10 Pokémons Mais Poderosos')
plt.xticks(rotation=45, ha='right')  # rotaciona pra deixar legivel
plt.tight_layout()

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom')

plt.show()