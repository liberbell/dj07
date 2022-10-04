# places = ["New Zealand", "Norway", "Botswana", "Zimbabwe", "Uzbekistan", "Paraguay"]
# villain_at = "Norway"

# for place in places:
#     if place == villain_at:
#         print("The villain has been captured!")
#         break
# else:
#     print("Teh villain got away.")

# num = int(input("Enter a number: "))
# for i in range(2, num//2):
#     if num % i == 0:
#         print("It is not a prime number.")
#         break
# else:
#     print(num, "is a prime number.")

for i in range(3):
    password = str(input("Enter a password"))
    if password == "secret":
        print("You guessed the password :)")
        break
else:
    print("3 incorrect password attempt.")