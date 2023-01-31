str1 = "Alpha"
str2 = "Beta"
str3 = '''gamma string'''
str4 = """delta string"""

# Numbers
num1 = 123
flt = 2.0

# List / Collection of multi datatypes, enclosed in square brackets
first_list = [str1, "DevOps", 47, num1, 1.5]
print(first_list)

# Tuple / Collection of multi datatype, enclosed in round bracket
first_tuple = (str1, "DevOps", 47, num1, 1.5)

# Printing a tuple
print(first_tuple)

# Dictionary / Element  in the dictionary are always in pairs(Key: Value), curly brackets.

first_dictionary = {"Name": "Vinícius", "Weight": 59,
                    "Favorite games": ["Overwatch", "Dark Souls II", "Bioshock Infinite"]}

print(first_dictionary)

print("Variable first_list is a:", type(first_list))
print("Variable first_tuple is a:", type(first_tuple))
print("Variable first_dictionary is a:", type(first_dictionary))

# Boolean
x = True
y = False

print(x)
print(y)
