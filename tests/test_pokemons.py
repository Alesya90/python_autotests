import requests
import pytest

token = '4ce146185ff46efddd78b0282f1b26cf'
host = 'https://api.pokemonbattle.me:9104' #хост для покемонов

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1368})
    assert response.status_code == 200
    
def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1368})   
    assert response.json()['trainer_name'] == 'Alesia'
    
@pytest.mark.parametrize('key, value', [('name', 'cubone'), ('trainer_id','1368'), ('attack', '1.0')])

def test_parts_of_answer(key,  value):
    response = requests.get(f'{host}/pokemons', params = {'trainer_id':1368})
    assert response.json()[2][key] == value

