#!/usr/bin/python3


def main():
    # simple fibonacci series
    # the sum of two elements defines the next set
    a, b = 0, 1
    while b < 50:  # If evaluates to True, the suite is executed. Then back here to re-evaluate. Will continue until evaluates to False
        print(b, end=' ')
        a, b = b, a + b

if __name__ == "__main__": main()


# Example 2 with else statement.
x = 0
while x < 10:
    print('x is now', x)
    x += 1
else:
    print('Done!')


# Example 3 with condition and continue

x = 0
while x < 10:
    print('x is now', x)
    x += 1
    if x == 5:
        print('Reached 5!!!!')
    else:
        continue


# Example 3 with condition and continue and break

x = 0
while x < 10:
    print('x is now', x)
    x += 1
    if x == 5:
        print('Reached 5!!!!')
        break
    else:
        continue