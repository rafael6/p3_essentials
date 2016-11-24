'''
# Before the implementing raise
def main():
    try:
        for line in readfile('xlines.txt'):
            print(line.strip())
    except FileNotFoundError as e:  #The except is on the caller not on the place where it failed.
    # If we put this exception at the trigger function below , the target function will return
    # NonType after it catches the exception and this function is not set to catch a NoneType error
        print('Cannot read the file.', e)

def readfile(filename):
    fh = open(filename)  # This is where it failed; the trigger
    return fh.readlines()

if __name__ == "__main__": main()


'''
# raise
def main():
    try:
        for line in readfile('lines.txt'):
            print(line.strip())
    except FileNotFoundError as e:
        print('Cannot read the file.', e)
    except ValueError as e:
        print('File must end with .txt', e) # This is where the user-define exception is caught (in the caller)


def readfile(filename):
    if filename.endswith('txt'):
        fh = open(filename) # FileNotFoundError trigger
        return fh.readlines()
    else:
        raise ValueError('File name must end with .txt.')  # User-define exception definition.


if __name__ == "__main__": main()
