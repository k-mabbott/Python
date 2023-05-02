

# x = 1.5

# y = 3 

# sum = y + x / x
# # sum = int(sum)

# print(type(sum),sum)

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(type(int_to_float),int_to_float)
# print(type(float_to_int),float_to_int)
# print(type(int_to_complex),int_to_complex)

# Practice Challenge: Correct the errors!
# first_name = "Alana"
# last_name = "Da Silva"
# age = 36
# profession = "Software Developer"
# years_experience = 5

# greeting = "Hello my name is "

# print(greeting, first_name, last_name) 
# Desired output: Hello my name is Alana Da Silva

# print(f"I am {age} years old") 
# Desired output: I am 36 years old

# print("I work as a {}.".format(profession))
# Desired output: I work as a Software Developer.

# exp_string = "I have worked in the field for {} years."
# print(exp_string.format(years_experience))
# Desired output: I have worked in the field for 5 years.

# print("I started in the field when I was ", str(age - years_experience), " years old.")
# Desired output: I started in the field when I was 31 years old.



# some_nums = [44,56,2,3,12,19,6]
# print("Get started by writing your own code!")

# # Some optional challenges to assess and refine your understanding:

# # Print the length of the list.
# print(len(some_nums))
# # Use antoher python built-in function and print the result.
# some_nums.sort()
# print(some_nums)
# # Remove an item from the list. Remember to verify that it was removed.
# print(some_nums.pop())
# print(some_nums)
# # Utilize a method from the documentation and print the result.
# some_nums.reverse()
# print(some_nums)
# new_nums = sorted(some_nums)
# print(new_nums)



# count = 0
# while count <= 5:
#     print("looping - ", count)
#     count += 1

# for count in range(0,5):
#     print("looping =", count)



# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(each_key)
# # output: name, language

# my_dict = { "name": "Noelle", "language": "Python" }
# for each_key in my_dict:
#     print(my_dict[each_key])
# # output: Noelle, Python


# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#     print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#     print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#     print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    # def showprice()
    def __str__(self):
        return f"this {self.in_stock, self.type}"
        print(self.price)

# skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
# dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
# my_shoe = Shoe("Nike", "Air force 1", 89.99)
# print(skater_shoe.type)	# output: Low-top Trainers
# print(dress_shoe.type)	# output: Ballet Flats
# print(my_shoe.price)	# output: Ballet Flats
# my_shoe.in_stock = False 
# print(str(my_shoe))

# for i, (key, val) in enumerate(entry.items()):
#     entryString += f'{key} - {val}{", " if (i < len(entry) - 1) else ""}'
# print(entryString)






















