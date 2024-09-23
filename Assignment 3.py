#--------------------------------------
# CIS 103: Introduction to Programming
# Assignment 3 "Lists, Tuples, Sets, Dictionaries"
# Instructor: Md Ali
# Student Name: Antonio Valenzuela
# Date: 09/21/24
#--------------------------------------

# LIST
# The following code represents a list, containing the items of various fruits
fruits = ["apple", "banana", "orange", "grape"]
print(fruits)
# Removing and adding banana and strawberry are labeled as remove and append when writing lists
fruits.remove("banana")
print(fruits)
fruits.append("strawberry")
print(fruits)

# TUPLE
# The following code will represent a tuple, containing different colors
colors = ("red", "green", "blue", "yellow")
print (colors)
print ("red")
print ("yellow")
#colors.remove("green", "blue")
# Error has occurred when trying to remove items green and blue because tuples are immutable

# SET
# The following code will represent a set, containing a set of different names
student_names = {"John","Emma","Sophia","James"}
print (student_names)
student_names.add("Oliver")
print (student_names)
student_names.remove("Sophia")
print (student_names)
student_names.add("John")
# Adding items when writing sets is written by using add and remove instead of appen
# Adding "John" the second time results in no change as sets are not allowed to add an existing item

# DICTIONARY
# The following code will represent a dictionary where names are put into key value pairs
student_scores = {
    "John": 85,
    "Emma": 92,
    "Sophia": 78,
    "James": 89,
}
print(student_scores)
x = student_scores["Emma"]
print(x)
student_scores.update ({"Oliver":95,})
student_scores.update ({"Sophia": 82,})
print(student_scores)
# When choosing to change a key value writing dictionary, you will use update
