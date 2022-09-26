# try:
#     print(variable)
# except NameError:
#     print("Variable is not defined.")
# except:
#     print("An unknown error has occured.")

# try:
#     f = open("nonexits.txt", "r")
# except FileNotFoundError:
#     print("No such file.")
# except:
#     print("An unknown error has occured.")

# input_var = int(input("Please enter a number:"))

# while True:
#     try:
#         input_var = int(input("Please enter a number:"))
#         break
#     except:
#         print("Ooops: That was not a valid number. Try again...")

attempts = 0
while True:
    try:
        input_var = input("Please input a number: ")
        input_var = int(input_var)
        break