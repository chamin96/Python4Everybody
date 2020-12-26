sum = 0
count = 0

print('Before', count, sum)

for thing in [9, 41, 12, 3, 4, 74, 15]:
    count = count + 1
    sum = sum + thing
    print(sum, thing)

print('After', count, sum)
print('Average', sum / count)