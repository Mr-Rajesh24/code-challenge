def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  

input_str = input("Enter: ")

input_str = input_str.replace(",", "")

if len(set(input_str)) != len(input_str):
    print("error, duplicates not allowed")
else:
    n = len(input_str)
    a = list(input_str)
    permute(a, 0, n)
