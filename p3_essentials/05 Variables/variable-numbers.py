# There are only two types of numbers in python int and floats

def main():
    print('There are only two types of numbers in python int and floats')

    print('\nInteger:')
    num = 42
    print(num)
    print(type(num), num)

    print('\nFloating Point:')
    num = 42 / 9
    print(num)
    print(type(num), num)

    print('\nRound to closest integer:')
    num = round(42 / 9)
    print(num)
    print(type(num), num)

    print('\nRound to two decimal spaces:')
    num = round(42 / 9, 2)
    print(num)
    print(type(num), num)

    print('\nFloor Division returns an integer:')
    num = 42 // 9
    print(num)
    print(type(num), num)

    print('\nModulus (remainder):')
    num = 42 % 9
    print(num)
    print(type(num), num)

    print('\nConvert float to integer:')
    num = int(42.9)
    print(num)
    print(type(num), num)

    print('\nConvert integer to float:')
    num = float(42)
    print(num)
    print(type(num), num)

if __name__ == "__main__": main()
