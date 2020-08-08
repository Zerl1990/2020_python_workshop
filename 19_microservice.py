import requests
import logging


logging.basicConfig(level=logging.INFO)


base_url = 'http://127.0.0.1:5000/books'


# Get list of books
response = requests.get(base_url)
assert response.status_code == 200, 'Get all books should return 200'
assert len(response.json()) > 0, "Micro service should have at least one book"
logging.info(f'Books: {response.json()}')


# Get Dracula
response = requests.get(f'{base_url}/1')
assert response.status_code == 200, 'Get book with id 1 should return 200'
json = response.json()
assert json['name'] == 'Dracula', 'Book[1] name should be dracula'
assert json['author'] == 'Bram Stoker', 'Book[1] author should be Bram Stoker'
logging.info(f'Book[1]: {json}')

# Create a new entry
new_book = {'name': 'TestBook', 'author': 'Tester'}
response = requests.post(base_url, json=new_book)
assert response.status_code == 200, 'Create book should return 200'
json = response.json()
new_book_id = json['id']
assert json['id'], 'A new id should be generated'
assert json['name'] == 'TestBook', 'New book name should be TestBook'
assert json['author'] == 'Tester', 'New book author should be Tester'
assert json['views'] == 0, 'New book views should be 0'
logging.info(f'New Book: {json}')


# Edit book
response = requests.put(f'{base_url}/{new_book_id}', json={'views': 530})
assert response.status_code == 200, 'Edit book should return 200'
json = response.json()
assert json['id'] == new_book_id, f'Edited book id should equal to {new_book_id}'
assert json['views'] == 530, f'New total views should be 530'
logging.info(f'New Book After Editing: {json}')


# Delete book
response = requests.delete(f'{base_url}/{new_book_id}')
assert response.status_code == 200, 'Delete book should return 200'


# Try to get book should return 404
response = requests.get(f'{base_url}/{new_book_id}')
assert response.status_code == 404, 'Delete book should return 404'
