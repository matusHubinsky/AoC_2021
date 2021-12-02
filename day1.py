o = open("data.txt", 'r')

file = [int(_) for _ in o.readlines()]

a = []
n = 0

for i in range(0, len(file) - 2):
    a.append(file[i] + file[i + 1] + file[i + 2])

for i in range(1, len(a)):
    if (a[i] > a[i - 1]):
        n += 1

# print(a)
print(n)
