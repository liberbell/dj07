import numbers
from operator import le


# number = 20
# while number < 25:
#     print(number)
#     number += 1

# while number <= (25 + 5):
#     print(number)
    
#     number += 1
# num = 5
# while num:
#     print("Value of num is: ", num)
#     num = num -1

# print("Good bye.")

# name = "Hepbarn"
# while name == "Hepbarn":
#     print("%s is an amazing soccer player." % name)

#     name = "Eric"
# user_password = ""
# while user_password != "password":
#     user_password = input("Enter pass: ")
# print("\nAccess granted!")

# num = 1
# while num <= 10:
#     print(num ** 2)
#     num += 1

# num_value = int(input("Enter a number: "))
# name = input("Enter your name: ")
# count = 1
# while count <= num_value:
#     print(count, ":", name)

#     count += 1

# num = 0
# while num in range(0, 10):
#     print(num)
#     num += 1

# num = 0
# while num in range(0, 10):
#     if num % 2 == 0:
#         print("even number: ", num)

#     num += 1

# value_int = int(input("Enter an integer: "))
# length = 0

# while value_int > 0:
#     value_int //= 10
#     length += 1
# print("number of digits: ", length)

x, y = 0, 8
while(x < y): x = x + y; print(x, y)