# number = 20

# while number < 25:
#     print(number)
#     break
from pydoc import ispackage
from sys import maxunicode


num = 10
# while num in range(10, 100):
#     print(num)

#     if num == 50:
#         break

#     num += 10
# print("out of the loop")
# while True:
#     num = int(input("Enter a number: "))
#     if num % 3 == 0:
#         break

# print("\nWe are out of the loop since we encoountered the number:", num)

# place = "NewYorkCity"
# place_length = len(place)

# index = 0
# while index in range(place_length):
#     print(place[index])
#     index += 1

#     if place[index] == "C":
#         break
# clean_haystack = ["hay", "hay", "hay", "hay", "hay", "hay", "hay", "hay"]
# unclean_haystack = ["hay", "hay", "hay", "hay", "needle", "hay", "hay", "hay"]
# seaching_for = "needle"
# maximum = len(clean_haystack)
# i = 0

# while i < maximum:
#     if seaching_for == unclean_haystack[i]:
#         print("The %s is at index %i: " % (seaching_for, i))

#         del unclean_haystack[i]
#         print("The updated haystack is: ", unclean_haystack)
#         break
#     i += 1
# else:
#     print("\nThe needle was not found :(")

# max_num = int(input("Enter an integer:"))
# num = 2

# print("Prime number upto %i " % max_num)
# while num < max_num + 1:
#     isPrime = True
#     count = 2

#     while count < num:
#         if num % count == 0:
#             isPrime = False
#             break
#         count += 1

#     if isPrime:
#         print(num)

#     num += 1

# num_value = 10
# while num_value > 0:
#     print("current value is: ", num_value)

#     if num_value == 5:
#         pass
#         print("This is a pass block.")

#     num_value = num_value - 1

# print("bye!")
num_value = int(input("Enter a number: "))
while num_value > 0:
    if num_value < 8 and num_value > 4:
        pass
    else:
        print("current value is :", num_value)

    num_value = num_value - 1
else:
    print("good bye")