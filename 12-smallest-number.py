smallest = None

print('Before')

for value in [9, 41, 12, 3, 4, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(value, smallest)

print('After', smallest)