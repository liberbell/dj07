# for letter in "string":
#     if letter == "i":
#         continue
#     print(letter)

# print("The end.")

# my_string = "Students"

# for letter in my_string:
#     if (letter == "e" or letter == "s"):
#         continue
#     else:
#         print(letter)

# for i in range(1, 10):
#     if i % 2 == 0:
#         print("Is %s is an even number?" % i)

#     else:
#         continue
#     print("Yes.")

# for num in range(1, 10):
#     if num % 2 == 0:
#         print("Found an even number: ", num)
#         continue

#     print(num)

# for i in range(1, 12):
#     print()
#     print("Before the continue statement: ", i)
#     if i % 3 == 0:
#         continue
#     print("After the continue statement.", i)
num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
new_dict = dict()

for i, j in zip(months, num_days):
    new_dict.update({i:j})
    if new_dict[i] < 29:
        continue

    else:
        print(i, "month has", new_dict[i], "days.")