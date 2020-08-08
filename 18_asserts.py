import requests


# Retrieve cities from MX
url = 'https://api.openaq.org/v1/cities?country=MX'
response = requests.get(url)


# Validate response
assert response.status_code == 200, "Response status should be 200"


# Get json response
json = response.json()


# Validate that we have meta and results
assert "meta" in json, 'Meta should be part of response'
assert "results" in json, 'Results should be part of response'


# Iterate results and validate format
# Results is a list of dictionaries, each dictionary contains info about a city
for city in json['results']:
    print(f'Run validations for {city}')
    assert "country" in city, f'Country should be part of the result: {city}'
    assert city['country'] == "MX", f'City country should be MX'
    assert 'name' in city, f'Name should be part of the the result: {city}'
    assert 'count' in city, f'Name should be part of the the result: {city}'
    assert 'locations' in city, f'Name should be part of the the result: {city}'

