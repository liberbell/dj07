# for letter in ["H", "E", "L", "L", "O"]:
#     print(letter)

# for letter in "hello":
#     print(letter)

# my_string = "Hello World"

# for letter in my_string:
#     print(letter)

# for letter in "10":
#     print(letter)

# # for digit in 10:
# #     print(digit)

# for country in "Germany", "Japan", "British":
#     print(country)

# dogs = ("Pug", "Dorberman", "Golden Retriever")
# for dog in dogs:
#     print("It`s a", dog)

# dog_weights = (
#     ("Pub", 20),
#     ("Dorberman", 50),
#     ("Golden Retriever", 70)
# )

# for i, (dog, weight) in enumerate(dog_weights):
#     print("index %d, is a %s and it weight is %s kg." % (i, dog, weight))

# friends = ["Alex", "Bob", "Eric"]
# for friend in friends:
#     print("Happy new year ", friend)

# student_scores = {
#     "Alex": 80,
#     "Eric": 75,
#     "Bob": 40,
#     "Elton": 30
# }
# for student in student_scores:
#     print(student)
# print(student_scores.keys())
# for student in student_scores.values():
#     print(student)


# for key in student_scores:
#     print("Key value pair -", key, ":", student_scores[key])

# for student, score in student_scores.items():
#     print("Student: ", student, "\tScore: ", score)

# number = [4, 6, 9, 10]

# for num in number:
#     quotient = num // 2

#     print(quotient, "is the quotient of ", num, "/2")

# mixed_list = [145, 23.4, 2+2j, False, "Hello", (0, 1), [4, -1], {"Bob": "M", "Section": "A"}]

# for item in mixed_list:
#     print("Type of ", item, "is ", type(item))

# num_list = [2, 4, 6, 8]
# for val in num_list:
#     square = val ** 2

#     print("Square of", val, "is", square)

# string = input("Enter a string:")
# count = 0

# for i in string:
#     count = count + 1
# print(count)

# numbers = [2, 3, 5, 7]
# for num in numbers:
#     print(num)
# else:
#     print("No more item left in the list.")

# characters = {"a", "b", "c", "d"}
# for letter in characters:
#     print(letter)
# else:
#     print("No more characters left.")

# us_cities = ["New York", "Nashville", "Seattle"]
# for city in us_cities:
#     if city == "New York":
#         print("New York is present in the list.")

# numbers = [11, 24, 95, 29, 0, 34, 35, 83, 61, 29, 1, 90, 16]
# for num in numbers:
#     if num % 2 == 0:
#         print("The list contains an even number: ", num)

# years = [1998, 2004, 2012, 1988, 2021]
# for year in years:
#     if year % 4 == 0:
#         print(year, " is a leap year.")
#     else:
#         print(year, " is not a leap year.")

# names = [["Bob", "Alex", "Eric"], ["Elton", "Jhon", "George"]]
# for student in names:
#     print(student)

# for sublist in names:
#     for name in sublist:
#         print(name) 

color_list = ["Red", "Green", "Blue"]
object_list = ["Pen", "Marker", "Pencil"]

for color in color_list:
    for object in object_list:
        print(color, object)