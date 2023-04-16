dt = {5: 4, 1: 6, 6: 3}

# Sort the dictionary by value
sorteddt = {k: v for k, v in sorted(dt.items(), key=lambda item: item[1])}

print(sorteddt)
