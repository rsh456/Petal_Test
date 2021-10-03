#This module contains testing cases for the pokemon_api endpoint

import pytest
from app import app

@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client


def api_get_pokemon(client):
    return client.get('/api/pokemon',follow_redirects=True)

def api_get_pokemon_by_id(client,pokemon_id):
    return client.get('/api/pokemon?id={}'.format(pokemon_id), follow_redirects=True)

def api_get_pokemon_page(client,page):
    return client.get('/api/pokemon_paginated?page={}&per_page=100'.format(page), follow_redirects=True)



def test_api_get_pokemon(client):
    oResponse =api_get_pokemon(client)
    assert oResponse.status_code == 200

def test_api_get_pokemon_by_id(client):
    oResponse =api_get_pokemon_by_id(client,1)
    assert oResponse.status_code == 200
    assert b"Bulbasaur" in oResponse.data

def test_api_get_pokemon_page(client):
    oResponse =api_get_pokemon_page(client,4)
    assert oResponse.status_code == 200