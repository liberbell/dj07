# try:
#     print(variable)
# except NameError:
#     print("Variable is not defined.")
# except:
#     print("An unknown error has occured.")

try:
    f = open("nonexits.txt", "r")
except FileNotFoundError:
    print("No such file.")
except:
    print("An unknown error has occured.")

input_var = int(input("Please enter a number:"))