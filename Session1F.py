# Bitwise Operators
# &, |, ^

# Shift Operators
# >>, <<

num1 = 10            # 1 0 1 0
num2 = 8             # 1 0 0 0

num3 = num1 & num2   # 1 0 0 0
num4 = num1 | num2   # 1 0 1 0
num5 = num1 ^ num2   # 0 0 1 0

print("num1:", num1, bin(num1))
print("num2:", num2, bin(num2))
print("num3:", num3, bin(num3))
print("num4:", num4, bin(num4))
print("num5:", num5, bin(num5))

# for shift operators we have base as 2 always
num6 = num2 << 3    # 8 * by 2 power 3
num7 = num2 >> 3    # 8 // by 2 power 3

print("num6:", num6)
print("num7:", num7)

num8 = -11
result = num8 >> 2
print(result)

"""
    8 bit representation of number 8 :)
    0 0 0 0  1 0 0 0
    >> 3
    _ _ _ 0  0 0 0 1
    0 0 0 0  0 0 0 1    -> 1 :)
    
    8 bit representation of number 11 :)
    0 0 0 0  1 0 1 1    ->  11
    1 1 1 1  0 1 0 0
                   1
    1 1 1 1  0 1 0 1    -> -11          

    >> 2
    
    _ _ 1 1  1 1 0 1
    
    1 1 1 1  1 1 0 1
    0 0 0 0  0 0 1 0
                   1
    0 0 0 0  0 0 1 1    -> -3               

"""
