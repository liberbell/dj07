response = ""
while True:
    response = input("\nWhat is the capital of United Kingdom.")

    if response == "quit":
        print("The correct answer is London. Better luck next time.")
        break

    if response.upper() == "LONDON":
        print("That is the correct answer.")
        break
    else:
        print("That is not the correct answer...Try again.")