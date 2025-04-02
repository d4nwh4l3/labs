def product_of_digits(x):
    x = abs(x)
    
    if x < 10: #base case
        return x
    
    return (x % 10) * product_of_digits(x // 10)

def array_to_string(a, index):
    if index >= len(a): #base case 1
        return ""
    
    if index == len(a) - 1: #base case 2
        return str(a[index])
    
    return str(a[index]) + "," + array_to_string(a, index + 1)

def log(base, value):
    if value <= 0 or base <= 1:
        raise ValueError("Value must be greater than 0 and base must be greater than 1")
    
    if value < base: #base case
        return 0
    
    return 1 + log(base, value // base)