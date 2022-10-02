# for i in range(1, 10):
#     if i % 2 == 0:
#         print("The number %s is divisible by 2" % i)
#     else:
#         print("The number %s is not divisible by 2" % i)

# num_list = []
# for i in range(1, 21):
#     if (i % 3 == 0 or i % 5 == 0):
#         num_list.append(i)
# print(num_list)

items = []
for i in range(100, 301):
    num_str = str(i)

    first_digit = int(num_str[0])
    second_digit = int(num_str[1])
    third_digit = int(num_str[2])

    if (first_digit % 2 == 0) and (second_digit % 2 == 0) and (third_digit % 2 == 0):