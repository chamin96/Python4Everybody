while True:
    line = input('> ')
    if line == 'done':
        break
    if line[0] == '#':
        continue
    print(line)

print('Done!')
