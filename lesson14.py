# for letter in "string":
#     if letter == "r":
#         pass
#         print("This is the pass block")
#     else:
#         print("Current Letter: ", letter)
    # print(letter)

# for i in range(10):
#     if(i % 2 == 0):
#         pass
#     else:
#         print(i)

# odd_count = 0
# total_count = 0
# for i in range(10):
#     if(i % 2 == 0):
#         pass
#     else:
#         print(i)
#         odd_count += 1

#     total_count += 1

#     print("Count of odd numbers: ", odd_count)
#     print("Total count of numbers: ", total_count, "\n")

my_str = input("Input a string: ")
digits = 0
letters = 0
for i in my_str:
    if i.isdigit():
        digits = digits + 1
    elif i.isalpha():
        letters = letters + 1
    else:
        pass

print("Digits: ", digits)
print("Letters: ", letters)