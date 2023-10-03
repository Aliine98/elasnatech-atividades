for i in range(1, 11):
    if i > 5:
        break
    print(i)

x = 1
while x < 11:
    if x == 5:
        x += 1
        continue
    print(x)
    x += 1

for y in range(1, 11):
    if y == 5:
        continue
    print(y)
