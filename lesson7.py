for letter in ["H", "E", "L", "L", "O"]:
    print(letter)

for letter in "hello":
    print(letter)

my_string = "Hello World"

for letter in my_string:
    print(letter)

for letter in "10":
    print(letter)

# for digit in 10:
#     print(digit)

for country in "Germany", "Japan", "British":
    print(country)

dogs = ("Pug", "Dorberman", "Golden Retriever")
for dog in dogs:
    print("It`s a", dog)

dog_weights = (
    ("Pub", 20),
    ("Dorberman", 50),
    ("Golden Retriever", 70)
)

for i, (dog, weight) in enumerate(dog_weights):
    print("index %d, is a %d and it weight is %d kg.", i, dog, weight)