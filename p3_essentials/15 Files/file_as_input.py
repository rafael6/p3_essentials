__author__ = 'rafael'

# Takes a file as input for numbers as input and average.
# Execute as follow: python file_as_input.py < num.txt

print("Type integers, each followed by Enter; or ^D or ^Z to finish")

total = 0
count = 0

while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break

if count:
    print("count=",count, "total=",total,"mean=",total/count)