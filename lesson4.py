num_list = [10, 20, 30, 40, 50]

def main():
    count = 0
    total = 0

    for i in num_list:
        count += count + i
        total += total + i

        print("element is: ", i)
        print("")
        print("sum: ", total)
        print("")