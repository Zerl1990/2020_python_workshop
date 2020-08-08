# The web service response contains a list of dictionaries. Each dictionary contains:
#   input_a
#   input_b
#   result: The result of computing input_a + input_b
# You want to validate the results from the services.
service_response = [
    {'a': 52, 'b': 8, 'result': 60},
    {'a': 21, 'b': 78, 'result': 23123},
    {'a': 67, 'b': 12, 'result': 231},
    {'a': 12, 'b': 38, 'result': 50}
]

# First, you have to iterate the results
for element in service_response:
    # Calculate the correct result
    expected_result = element['a'] + element['b']

    # Validate the result against calculate result
    if expected_result == element['result']:
        print(f"[PASS] {element['a']} + {element['b']} = {expected_result}")
    else:
        print(f"[FAIL] {element['a']} + {element['b']}, expected {expected_result}, actual {element['result']}")

