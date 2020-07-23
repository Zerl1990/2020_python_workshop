
print(f'Loop while counter is less than 10')
counter = 0
while counter < 10:
    print(f'Counter is {counter}')
    counter += 1
print(f'Counter is greater or equal to 10')


print("Loop from 0 to 9")
for number in range(10):
    print(number)


my_tuple = (1, 2, 3, 4, 5)
print("Iterate all elements in my tuple")
for number in my_tuple:
    print(f'Tuple number: {number}')


my_list = [1, 2, 3, 4, 5]
print("Iterate all elements in my list")
for number in my_list:
    print(f'List number: {number}')


my_dict = {"key1": "value1", "key2": "value2"}
print("Iterate all elements in my dictionary")
for key, value in my_dict.items():
    print(f'Dictionary value {key}={value}')

