import re


def main():
    fh = open('raven.txt')
    for line in fh:

        #Example 1
        # Returns the lines that includes the words Lenore or Nevermore.| is an or.
        #if re.search('(Len|Neverm)ore', line):
            #print(line, end='')

        #Example 2
        # Returns the word Lenore or Nevermore in each line if a match is found
        #match = re.search('(Len|Neverm)ore', line)
        #if match:
            #print(match.group())

        #Example 3
        #For each string (line), find Lenore and Nevermore and raplace them with ####.
        # This example will return the whole file
        #print(re.sub('(Len|Neverm)ore', '####', line), end='')

        #Example 4
        #For each string (line), find Lenore and Nevermore and raplace them with ####.
        # This example will only return matched lines
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '####'), end='')




if __name__ == "__main__": main()
