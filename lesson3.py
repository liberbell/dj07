import time
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
# while True:
#     try:
#         input_var = input("Please input a number: ")
#         input_var = int(input_var)
#         break
#     except ValueError:
#         attempts += 1

#         if attempts < 3:
#             print("Ooops: That was not a valid number. Try again...")
#         else:
#             print("You really want to input a string: Fine We'll handle it.")
#             input_var = str(input_var)
#             print(input_var)
#             break

time.sleep(10)