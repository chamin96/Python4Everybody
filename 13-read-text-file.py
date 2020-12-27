fhand = open('mbox.txt')

# print(fhand)

count = 0

for line in fhand:
    count += 1
    print(line)

print('Line Count:', count)