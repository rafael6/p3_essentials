import re
'''
Before
def main():
    fh = open('raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')

if __name__ == "__main__": main()
'''


def main():
    # re.compile() More efficient, only need to compile once.
    # re.compile() allow for use other cool methods such as re.IGNORECASE
    fh = open('raven.txt')
    for line in fh:
        pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
        # Find the lines where words Lenore and Nevermore where found
        if re.search(pattern, line):
            # Prints the qualifying lines
            print(line, end='')
            # Replaces Lenore and Nevermore with ####
            # Print the changed lines
            print(pattern.sub('####', line), end='')


if __name__ == "__main__": main()