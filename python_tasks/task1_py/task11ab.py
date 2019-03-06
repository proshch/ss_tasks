"""This module for creating script with the following functionality:
create variables of different types: list/tuple/dict/set.
iterate by this data."""


clubs_list = ['AC Milan', 'Roma', 'Bologna', 'Frosinone']
clubs_tuple = ('Liverpool', 'FC Karpaty Lviv', 'Odense')
players_dict = {'GK': 'Dida', 'CB': 'Nesta', 'CM': 'Seedorf'}
managers_set = {'Gattuso', 'Anchelotti', 'Blanc', 'Gattuso', 'Mourinho'}

print('Lists: ')
print(clubs_list[::])

for i, c in enumerate(clubs_list, start=1):
    print(i, c)

print(' - '.join(clubs_list))

print('\nTuples: ')
for item in clubs_tuple:
    print(item)

print(clubs_tuple[2])

print('\nDicts: ')
for key, value in players_dict.items():
    print(key, value)

print(players_dict.get('CM'))
print(players_dict.get('ST', 'Shevchenko'))
players_dict.update({'ST': 'Inzaghi'})
print(players_dict)
print('Players dict keys: ', players_dict.keys())
print('Players dict values: ', players_dict.values())
 

print('\nSets: ')
print('Anchelotti' in managers_set)
