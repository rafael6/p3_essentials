def main():
    buffer_size = 50000
    infile = open('olives.jpg', 'rb') # Python default is to use utf8, but this is binary, so we rb, read as binary
    outfile = open('new.jpeg', 'wb')
    buffer = infile.read(buffer_size) # Buffer is a binary object not a text object; so, buffer is a must
    while len(buffer):
        outfile.write(buffer)
        print('.', end='')
        buffer = infile.read(buffer_size) # Read the next buffer
    infile.close()  # I added this
    outfile.close()  # I added this
    print()
    print('Done.')


if __name__ == "__main__": main()

# read binary file example
handle = open("test.pdf", "rb")