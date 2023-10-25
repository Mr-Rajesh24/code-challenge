import re

def evaluate_math_expression(expression):
    if '.' in expression:
        raise ValueError("Float numbers are not allowed.")
    if re.search(r'\d+\.\d+\.\d+', expression):
        raise ValueError("Invalid expression format.")
    expression = expression.replace(',', '')
    try:
        result = eval(expression)
        return result
    except:
        raise ValueError("Invalid expression format.")
