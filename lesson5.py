import sys
import argparse

# argment_list = sys.argv
# print("The script has the name ", '"', (sys.argv[0]))
# print("Number of argments of ", (len(sys.argv)))
# print("The Arguments are ", argment_list)

parser = argparse.ArgumentParser()
parser.add_argument("-display")
args = parser.parse_args()

print(args.display)