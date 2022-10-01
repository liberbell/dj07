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

string = input("Enter a string:")
count = 0

for i in string:
    count = count + 1
print(count)

numbers = [2, 3, 5, 7]
for num in numbers:
    print(num)
else:
    print("No more item left in the list.")