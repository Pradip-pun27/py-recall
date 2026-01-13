import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number1", help = "1st number")
parser.add_argument("number2", help = "2nd number")
parser.add_argument("operation", help = "operation")
args = parser.parse_args()
print(args.number1)
print(args.number2)
print(args.operation)
n1 = int(args.number1)
n2 = int(args.number2)
result = None
if args.operation == "add":
    result = n1 + n2
elif args.operation == "subtract":
    result =  n1 - n2
elif args.operation == "multiply":
    result = n1 * n2
print(f"The result is {result}")


