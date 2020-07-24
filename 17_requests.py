import requests


url = 'https://api.openaq.org/v1/cities?country=MX'
response = requests.get(url)
print(f'Response from {url} is {response}')

print(f'Response status code: {response.status_code}')
print(f'Response raw content: {response.raw}')
print(f'Response JSON: {response.json()}')
print(f'Response JSON type: {type(response.json())}')