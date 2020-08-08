# Import requests library
import requests

# Define url
url = 'https://api.openaq.org/v1/cities?country=MX'

# Execute a get request to Rest services
response = requests.get(url)

# Print response object
print(f'Response from {url} is {response}')

# Print response status code
print(f'Response status code: {response.status_code}')

# Print raw response content (String)
print(f'Response raw content: {response.raw}')

# Print the response ins json format (Dictionary)
print(f'Response JSON: {response.json()}')

# Print variable type of json response
print(f'Response JSON type: {type(response.json())}')
