# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic3 = {5: 50, 6: 60}
dic4 = {6: 30, 8: 15}


# Concatenate dictionaries to create a new one
result_dict = {**dic1, **dic3, **dic4}

# Display the concatenated dictionary
print("Concatenated Dictionary:", result_dict)
