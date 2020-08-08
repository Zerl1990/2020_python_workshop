A = 3
B = 4

# id function return the memory address for the variables
print(80 * '*')
print('Boolean operator example')
print(f'{A} != {B}: {A != B}')  # A is not equal to B
print(f'{A} == {B}: {A == B}')  # A is equal to B
print(f'{A} > {B}: {A > B}')   # A is greater than B
print(f'{A} >= {B}: {A >= B}')  # A is greater or equal to B
print(f'{A} < {B}: {A < B}')   # A is less than B
print(f'{A} <= {B}: {A <= B}')  # A is less or equal to B
print(f'{id(A)} is {id(B)}: {A is B}')  # A is  B (Point to the same object)
print(f'{id(A)} is not {id(B)}: {A is not B}')  # A is not B (Point to a different object)


# The is operator compares if two variables are pointing to the memory address
# Example for is operator
first_obj = 'test1'
second_obj = 'test2'


# id function return the memory address for the variables
print(80 * '*')
print(f'Objects are different at the begging: {first_obj is not second_obj}')
print(f'First object id: {id(first_obj)}')
print(f'Second object id: {id(second_obj)}')
print(f'First object id: {id(first_obj)}')
print(f'First obj value: {first_obj}')
print(f'Second object id: {id(second_obj)}')
print(f'Second object value: {second_obj}')


first_obj = second_obj
print(80 * '*')
print(f'After the assignment objects are equal: {first_obj is second_obj}')
print(f'First object id: {id(first_obj)}')
print(f'First obj value: {first_obj}')
print(f'Second object id: {id(second_obj)}')
print(f'Second object value: {second_obj}')

