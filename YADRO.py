string = list(input())

curly_b1 = 0
curly_b2 = 0
square_b1 = 0
square_b2 = 0
parentheses_1 = 0
parentheses_2 = 0

for it in string:
    if it == "{":
        curly_b1 = curly_b1 + 1
    if it == "{":
        curly_b2 = curly_b2 + 1
    if it == "[":
        square_b1 = square_b1 + 1
    if it == "]":
        square_b2 = square_b2 + 1
    if it == "(":
        parentheses_1 = parentheses_1 + 1
    if it == ")":
        parentheses_2 = parentheses_2 + 1

if curly_b1 == curly_b1 and square_b1 == square_b2 and parentheses_1 == parentheses_2:
    print("True")
else:
    print("False")
