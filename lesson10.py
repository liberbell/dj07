# original_list = [1, 2, 3, 4, 5, 6]
# cubes_list = []

# for i in original_list:
#     cubes_list.append(i ** 3)

# print(cubes_list)

original_list = [["Volkswagen", "Mercedes", "BMW"], ["Honda", "Toyota", "Mazda"]]
flattened_lists = []

for cars_list in original_list:
    for car in cars_list:
        flattened_lists.append(car)