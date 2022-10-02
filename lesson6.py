import sys
import argparse

# arg1 = int(sys.argv[1])
# arg2 = int(sys.argv[2])

# print("Addition of two numbers is ", arg1 + arg2)

ap = argparse.ArgumentParser()

ap.add_argument("-a", "--first_operand", required=True, help="first operand")
ap.add_argument("-b", "--second_operand", required=True, help="second operand")

args = vars(ap.parse_args())

a = int(args["first_operand"])
b = int(args["second_operand"])
print("Sum is {}".format(a + b))
print("Sub is {}".format(a - b))
print("Div is {}".format(a / b))
print("Mul is {}".format(a * b))