def drop_first_last(grades):
    first, *middle, last = grades
    return sum(grades) / float(len(grades))

print(drop_first_last((4,7,2,22,13,78,32,12,11,13,)))