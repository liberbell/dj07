import sys
import argparse

# arg1 = int(sys.argv[1])
# arg2 = int(sys.argv[2])

# print("Addition of two numbers is ", arg1 + arg2)

ap = argparse.ArgumentParser()

ap.add_argument("-a", "--first_operand", required=True, help="first operand")