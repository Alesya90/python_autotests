import requests

token = '4ce146185ff46efddd78b0282f1b26cf'
host = 'https://api.pokemonbattle.me:9104' #хост для покемонов

#создание покемона
response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name":"Бульбазавр К",
    "photo":"https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"Content-Type" : 'application/json',
              'trainer_token':token} )

print(response_add_pokemon.text)

#смена имени покемона
response_change_name_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6199",
    "name": "New Бульба",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"Content-Type" : 'application/json',
              'trainer_token':token})

print(response_change_name_pokemon.text)

#поймать покемона в покебол
response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6199"
}, headers = {"Content-Type" : 'application/json',
              'trainer_token':token} )

print(response_add_pokeball.text)