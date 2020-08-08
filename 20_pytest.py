import pytest
import requests
import logging


base_url = 'http://127.0.0.1:5000/books'


def test_print():
    print("something")



@pytest.mark.parametrize("a", [ ("name"), ("test"), ("test3"), ("test4") ])
def test_add(a):
    new_book = {'name': a[0], 'author': 'Tester'}
    response = requests.post(base_url, json=new_book)
    assert response.status_code == 200, 'Create book should return 200'
    json = response.json()
    assert json['id'], 'A new id should be generated'
    assert json['name'] == a[0], 'New book name should be TestBook'
    assert json['author'] == 'Tester', 'New book author should be Tester'
    assert json['views'] == 0, 'New book views should be 0'
    logging.info(f'New Book: {json}')


@pytest.mark.parametrize("a", [ (1), (2), (3), (4) ])
def test_number(a):
    print(a)

# Ejecutar
# 1. Abrir terminal
# 2. Muevete a la carpeta donde esta el script
# 3. Ejecuta pytest 20_pytest.py -v
