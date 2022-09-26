try:
    print(variable)
except NameError:
    print("Variable is not defined.")
except:
    print("An unknown error has occured.")