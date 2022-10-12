# number = 20

# while number < 25:
#     print(number)
#     break
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
clean_haystack = ["hay", "hay", "hay", "hay", "hay", "hay", "hay", "hay"]
unclean_haystack = ["hay", "hay", "hay", "hay", "needle", "hay", "hay", "hay"]
seaching_for = "needle"
maximum = len(clean_haystack)
i = 0

while i < maximum:
    if seaching_for == clean_haystack[i]:
        print("The %s is at index %i: " % (seaching_for, i))

        del clean_haystack[i]
        break
    i += 1
else:
    print("\nThe needle was not found :(")