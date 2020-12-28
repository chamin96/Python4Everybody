names = ['peter', 'david', 'alex', 'peter', 'beth', 'alex', 'peter']

name_count = dict()

for name in names:
    if name not in name_count:
        name_count[name] = 1
    else:
        name_count[name] = name_count[name] + 1

print(name_count)


# method two
name_count_2 = dict()

for name in names:
    name_count_2[name] = name_count_2.get(name, 0) + 1

print(name_count_2) 