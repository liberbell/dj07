for i in range(1, 10):
    if i % 2 == 0:
        print("The number %s is divisible by 2" % i)
    else:
        print("The number %s is not divisible by 2" % i)

num_list = []
for i in range(1, 21):
    if (i % 3 == 0 or i % 5 == 0):
        num_list.append(i)