lst = [1, 2, 3, 4, 5]

gen_comp = (item for item in lst if item > 3)

for item in gen_comp:
    print(item)
