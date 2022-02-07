def maximum(num1=12, num2=27, num3=36):
    max_val = num1
    if num2 > max_val:
        max_val = num2
    if num3 > max_val:
        max_val = num3
    return max_val

def minimum(num1=15, num2=9, num3=27):
    min_val = num1
    if num2 < min_val:
        min_val = num2
    if num3 < min_val:
        min_val = num3
    return min_val
    
    
print(f'the maximum valie is {maximum()} and the minimum value is {minimum()}')