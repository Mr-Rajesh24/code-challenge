def convert_expression(expression):
    parts = expression.split(',')
    if len(parts) == 2 and parts[0].isnumeric() and parts[1].isnumeric():
        num1 = int(parts[0])
        num2 = int(parts[1])
        if num2 == 0:
            return "Error: Division by zero"
        if num1 < num2:
            return "Error: Dividend must be larger than the divisor"
        quotient = num1 // num2
        remainder = num1 % num2
        return f"{quotient},{remainder}"
    else:
        return "Error: Invalid expression format"
A= input("")
result = convert_expression(A)
print(result)
