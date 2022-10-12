# number = 20

# while number < 25:
#     print(number)
#     break
num = 10
# while num in range(10, 100):
#     print(num)

#     if num == 50:
#         break

#     num += 10
# print("out of the loop")
while True:
    num = int(input("Enter a number: "))
    if num % 3 == 0:
        break

print("\nWe are out of the loop since we encoounterd the number:", num)