import itertools


# Dataset
poke_types = ['Contrung','Lua','Ma', 'Co', 'Nuoc']
list_a = ['Bulbasaur', 'Charmander', 'Squirtle', 'Bulbasaur']
list_b = ['Caterpie', 'Pidgey', 'Squirtle']

in_common = []
set_a, set_b = set(list_a), set(list_b)

for pokemon_a in list_a:
    for pokemon_b in list_b:
        if pokemon_a == pokemon_b:
            in_common.append(pokemon_b)

print(in_common)