'''
Modes:
'r' = read
'w' = write; if you open a file in write mode, the data is lost!
'w+' = open for write and create the file if it doesn't exist,
'r+' = read & write
'rb' = read binary
'rt' = read text (default)
'a' = append.

read options:
read()  read the file at once.
readlines()  put each line of the file in a list. Be careful with large files such as series of novels

use f.seek(0) To return to begining of file after a f.read()
'''

# Basic

def main():
    f = open('lines.txt')
    for line in f:
        print(line, end='')
    f.close()

    print('Break 1:')

    f = open('lines.txt')
    for line in f.readlines():
        print(line, end='')


    print('Break 2:')

    # Same output as above, but using the read() method
    f = open('lines.txt', 'r')
    if f.mode == 'r':
        content = f.read()
        print(content)
    f.close()


    # Writing
    write_me = 'some text...'
    f = open('example_write.txt', 'w')
    f.write(write_me)
    f.close()

    # Appending
    append_me = 'some appended text...'
    f = open('pito.txt', 'a')
    f.write('\n')
    f.write(append_me)
    f.close()

if __name__ == "__main__": main()

# Read and write line by line; OK for small files.
def main():
    infile = open('lines.txt', 'r')
    outfile = open('new.txt', 'w')
    for line in infile:
        # print to outfile without additional return.
        print(line, file=outfile, end='')  # file=outfile and end='' are optional parameter of the print() method.
    print('Done!')  # Print Done! after the loop ends

if __name__ == "__main__": main()

# Large files using buffer--not an iterable--
def main():
    buffer_size = 50000
    infile = open('bigfile.txt', 'r')
    outfile = open('new_bigfile.txt', 'w') # use 'w+' to create file if it doesn't exist
    buffer = infile.read(buffer_size)  # read the infile to a specified buffer size and assign it to variable buffer.
    while len(buffer):  # while there is something in the buffer
        outfile.write(buffer)  # Emptying the buffer here = write form the buffer
        print('.', end='')
        buffer = infile.read(buffer_size)  # Is filling the buffer here. Read the next buffer
    print()
    print('Done.')

if __name__ == "__main__": main()

# With closes the file for you even if an exception occurs
import timeit

def main():
    with open('lines.txt', 'r+') as fh:
        for line in fh:
            print(line, end='')

def main2():
    with open('lines.txt', 'r+') as fh:
        for line in fh.readlines():  # readlines() put the file in a list where each element is a line
            print(line, end='')

# with & error handling:
try:
    with open("test.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("An IOError has occurred!")

if __name__ == "__main__":
    #timeit.main()
    main()
    print()
    main2()


