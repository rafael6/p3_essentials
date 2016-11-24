print('---Fibonacci---')
a, b = 0, 1
while b < 50:
    print(b, end=' ')
    a, b = b, a + b


print('\n---Prime---')
num = 12
for n in range(2, num):
    if num % n == 0:
        print('Not prime')
        break
    else:
        print('Is prime')
        break

