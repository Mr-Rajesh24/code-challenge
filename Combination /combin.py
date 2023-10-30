from itertools import permutations

def find_combinations(input_str):
    if len(set(input_str)) != len(input_str):
        return "error, duplicates not allowed"
    
    combinations = [''.join(p) for p in permutations(input_str)]
    return ', '.join(combinations)

user_input = input("Enter a comma-separated list of characters (no duplicates): ")
result = find_combinations(user_input.split(','))
print("Output:", result)
