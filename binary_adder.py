def convertion(binary, power):
    # Just converts the binary to decimal 
    result = 0
    for i in range(len(binary)):
        result = result + binary[i] * pow(2, power-1)
        power = power - 1
    return result

def half_adder(first, second):
    # This only accepts two inputs (essentially 1 + 1 only)
    sum_bit = first & second
    carry_bit = first ^ second
    print(sum_bit, carry_bit)

def half_subtractor(first, second):
    # This also accepts only two inputs but with another byte that is negative
    negative_bit = 0
    difference = first ^ second
    borrow =  (not first) & second
    if borrow == 1:
        negative_bit = borrow
        borrow = 0
    print(negative_bit, borrow, difference)

def full_adder(first, second, cin, i, j):    
    #Now this is the full adder not the half bs
    result = []
    while i >= 0 or j >= 0:
        a = first[i] if i >= 0 else 0
        b = second[j] if j >= 0 else 0

        first_xor = a ^ b
        first_and = a & b
        sum_bit = first_xor ^ cin
        carry_bit = first_xor & cin
        cout = first_and | carry_bit

        result.append(sum_bit)

        i -= 1
        j -= 1

        cin = cout

    if cin == 0:
        result.append(cin)

    result.reverse()

    return result 

# # Half adder is basically just two digits (1, 0)
# half_adder(1,1)

# # Half subtraction is still the same, just subtract two digits (1,0) but it has a negative byte
# half_subtractor(1,0)

# This is the full adder and this is basically just full on binary arithmetic (Maybe i can add a decimal converter at some point but )
first = [1, 0, 0, 1]
second = [1, 0, 0, 0, 0, 1, 1]
cin = 0

i = len(first) - 1
j = len(second) - 1
result = []

result = full_adder(first, second, cin, i, j)
power = len(result)
convert_to_decimal = convertion(result, power)

print("The binary output is:", result)
print("The decimal output is:", convert_to_decimal)