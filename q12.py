my_dict = {"apple": 5, "banana": 2, "orange": 4}

# Sort the dictionary by value
sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}

print(sorted_dict)
