# Sample list of non-empty tuples
sample_list = [(2, 5), (1, 2), (2, 3), (2, 1), (9, 6)]

# Define a custom sorting key function


def sort_by_last_element(tuple):
    # Return the last element of each tuple as the sorting key
    return tuple[-1]


# Sort the list based on the custom key function
sorted_list = sorted(sample_list, key=sort_by_last_element)

# Display the sorted list
print("Sorted list in increasing order by the last element:")
print(sorted_list)
