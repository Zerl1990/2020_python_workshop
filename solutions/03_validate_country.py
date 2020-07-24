my_dictionary = {
  "meta": {
    "name": "openaq-api",
    "license": "CC BY 4.0",
    "website": "https://docs.openaq.org/",
    "page": 1,
    "limit": 100,
    "found": 6
  },
  "results": [
    {
      "country": "MX",
      "name": "BAJA CALIFORNIA NORTE",
      "city": "BAJA CALIFORNIA NORTE",
      "count": 68808,
      "locations": 3
    }
  ]
}

print(f'Response is {my_dictionary}')


# Iterate and search MX
found = False
for result in my_dictionary['results']:
    if result['country'] == 'MX':
        found = True

if found:
    print("MX is included in the response")
else:
    print("MX is not included in the response")


