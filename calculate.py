import sys
import re

# support ['calculate.py', '2', '+', '2'] or ['calculate.py', '2+2']

if len(sys.argv) != 2 and len(sys.argv) != 4:
    print('Arg len should be 2 or 4')
    sys.exit()

if len(sys.argv) == 4:
    left_operand = sys.argv[1]
    right_operand = sys.argv[3]
    operation = sys.argv[2]
else:
    operands = re.split('\+|-|\*|/|%', sys.argv[1])
    if len(operands) != 2:
        print('Input str must have left operand, operation and right operand')
        sys.exit()
    left_operand = operands[0]
    right_operand = operands[1]
    operation = sys.argv[1][len(left_operand):len(left_operand)+1]

allowed_operations = ['+', '-', '*', '/', '%']

if operation not in allowed_operations:
    print('Operation is not allowed')
    sys.exit()

try:
    left_operand = int(left_operand)
    right_operand = int(right_operand)
except ValueError:
    print('Left and right operands must be int')
    sys.exit()

if (operation == '/' or operation == '%') and right_operand == 0:
    print('Division by zero is not allowed')
    sys.exit()

def calc(left, right, action):
    match action:
        case '+':
            return left + right
        case '-':
            return left - right
        case '*':
            return left * right
        case '/':
            return left / right
        case '%':
            return left % right

print(calc(left_operand, right_operand, operation))
