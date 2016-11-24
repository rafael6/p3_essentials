def main():
    print('Dictionary are mutable')
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    '''
    d = dict(
        one=1, two=2, three=3, four=4, five='five'
    )
    '''
    print(d)
    d['seven'] = 7 # add a key/value pair to dic
    print(d)
    for k in sorted(d.keys()): # To order a dict using its keys
        print(k, d[k])


if __name__ == "__main__": main()
