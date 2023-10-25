a = int(input())
def is_reversible_number(number):
    number_str = str(number)
    return number_str == number_str[::-1]


print(is_reversible_number(a))
