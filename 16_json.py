# Response from server
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


# Print response type
print(f'My response type: {type(my_dictionary)}')


# Print dictionary information
print(my_dictionary)



