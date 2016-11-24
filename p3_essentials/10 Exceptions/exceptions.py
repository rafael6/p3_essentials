
def divide(x, y):

    # The try clause is executed first
    # If not exceptions, the except clause(s) is skipped
    try:
        result = x / y

    # if an exception is not matched and there is an error, the program just stop its execution!!!
    # if this exception is matched, the except clause is executed and program continues.
    except ZeroDivisionError:
        print("division by zero!")

    # else is optional,and can be included in the try block
    # else is often used to print the 'operation was successful'
    # If there are no exceptions, execute this block
    else:
        print("result is", result)

    # Finally is often used as a clean-up action
    # A finally clause is always executed before leaving the try statement, whether an exception has occurred or not.
    finally:
        print("executing finally clause")

# no exceptions: try clause executes, if there is an else or finally they also execute, program continues
#divide(2, 1)

#a matched exception: else will not executes, finally always complete, program continues
#divide(2, 0)

#an unmatched exception, else will no execute, finally always executes, program stops!!!
#divide("2", "1")


# Example 1
def main():
    try:
        fh = open('xlines.txt')
    except FileNotFoundError as e:  # We can specify several except statements.
        print('Could not open the file', e)
    else:
        for line in fh: print(line.strip())  # we can also put this line in the 'try' and avoid this else.

if __name__ == "__main__":
    main()
