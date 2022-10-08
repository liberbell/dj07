num = range(10)

# print([x * x for x in num])
# letters = [letter for letter in "anxiety"]
# print(letters)

# list_of_words = ["this", "is", "a", "list", "of", "words"]
# items = [word[0] for word in list_of_words]
# print(items)

# list_of_words = ["this", "is", "a", "list", "of", "words"]
# items = [word[0].upper() for word in list_of_words]
# print(items)

# items = [word.upper() for word in list_of_words]
# print(items)

# print([x * x for x in num if x % 2 != 0])

# number_list = [number for number in range(20) if number % 2 == 0]
# print(number_list)

# multiples_27 = [i for i in range(300) if i % 27 == 0]
# print(multiples_27)

# print([i for i in "MATHEMATICS" if i in ["A", "E", "U", "I", "O"]])

string = "Hello 12345 World"
numbers = [int(x) for x in string if x.isdigit()]
print(numbers)