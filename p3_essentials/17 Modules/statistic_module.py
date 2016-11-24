import statistics

lst = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]

x = statistics.mean(lst)  # Average
print(x)

x = statistics.median(lst)
print(x)

x = statistics.mode(lst)
print(x)

x = statistics.stdev(lst)
print(x)

x = statistics.variance(lst)
print(x)
