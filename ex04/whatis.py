import sys

sys.argv = sys.argv[1:]

if len(sys.argv) != 1:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)

try:
    num = int(sys.argv[0])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)

if (num % 2) == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
