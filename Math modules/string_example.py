#!/usr/bin/env python3
# This is a Python script that demonstrates string constants and special characters in Python 3.

# String constants can be defined using different types of quotes.
name = 'Fiona'  # Using single quotes
value = "29"  # Using double quotes
helptext = """Is trying to become a python guru"""

# Printing the string constants
print("Name:", name)
print("Value:", value)
print("Help Text:")
print(helptext)

# Using special characters in strings
special_characters = "Special Characters: \n Newline, \t Tab, \\ Backslash, \' Single Quote, \" Double Quote"
print(special_characters)

# Escaping special characters
escaped_characters = "Escaping special characters: \\n Newline, \\t Tab, \\\\ Backslash, \\' Single Quote, \\\" Double Quote"
print(escaped_characters)

# Concatenating strings to create a full name
first_name = 'Fiona'
last_name = 'Githaiga'
full_name = first_name + ' ' + last_name
print("Full Name:", full_name)
