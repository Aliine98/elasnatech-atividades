# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = list(range(1, 11))
# nums = [x for x in range(1, 11)]

for num in nums:
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é ímpar')
