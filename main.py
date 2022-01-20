import time
import json

start = time.time()

file = open("pokemon_full.json")
pokemon = file.read()
print("Количество символов в файле равно", len(pokemon))
file.close()

count = 0
for symbol in pokemon:
    if symbol.isalnum():
        count = count+1
print("Количесто символов без пробелов и знаков препинания равно", count)

max_desc = 0
max_words = 0
pokemon_name = ""
abilities = ""
pokemon_py = json.loads(pokemon)
for profile in pokemon_py:
    desc = profile["description"]
    if len(desc) > max_desc:
        max_desc = len(desc)
        pokemon_name = profile["name"]
    for skills in profile["abilities"]:
        if len(skills.split()) > max_words:
            max_words = len(skills.split())
            abilities = skills
print(pokemon_name, "у этого покемона наиболее длинное описание")
print(abilities, "это умение содержит больше всего слов")

end = time.time()
print('Время выполнения', end-start)