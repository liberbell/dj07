from logging import exception
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

# try:
#     time.sleep(10)
# except KeyboardInterrupt:
#     print("KeyboardInterrupt has occured.")
# time.sleep(10)

#     f = open("nonexists.txt")
# except OSError:
#     print("OS error")
# except FileNotFoundError:
#     print("File not found.")

# try:
#     f = open("nonexists.txt")
# except FileNotFoundError:
#     print("File not found.")
# except OSError:
#     print("OS error")

# var = "xyz"
# try:
#     print(var)
# except NameError:
#     print("The variable is not defined.")
# finally:
#     print("The try except block ended.")

# try:
#     f = open("testfile.txt", "w")
# finally:
#     f.close()
#     print("Done with processing file.")

# try:
#     file = open("testfile.txt", "w")
#     file.write("Writing to the open file.")
#     print("One line writing to the file.")

# except:
#     print("Ooops. something went wrong.")
# else:
#     print("Nothing went wrong.")

# try:
#     a = int(5)
#     b = str("hello")
#     d = a + b + c
# except TypeError:
#     print("Type error was thrown.")
# print(d)

# try:
#     a = str(5)
#     b = str("hello")
#     d = a + b + c
# except TypeError:
#     print("Type error was thrown.")
# except NameError:
#     print("NameError was thrown.")

# try:
#     a = str(5)
#     b = str("hello")
#     c = int(" world")
#     d = a + b + c
# except TypeError:
#     print("Type error was thrown.")
# except NameError:
#     print("NameError was thrown.")
# except ValueError:
#     print("ValueError was thrown.")

number = int(input("Enter a number: "))

# if number > 5:
#     raise Exception("The number shuld not exceed 5. The value of number is: {}".format(number))

try:
    if number > 5:
        raise Exception("The number shuld not exceed 5. The value of number is: {}".format(number))
except Exception as error:
    print("Caught this error. " + repr(error))