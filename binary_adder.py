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

def one_complement(binary):
    # This is the one complement of a binary number (basically just flips the bits of the subtrahend)
    for i in range(len(binary)):
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0
    return binary

def two_complement(binary):
    # This is the two complement of the binary number (basically just flips the bits of the subtrahend and adds 1 to it)
    cin = 1
    i = len(binary) - 1
    result = []
    first = binary
    result = full_adder(first, cin, i, second=None, j=None, two_complement=True)
    return result

def full_subtractor(first, second):
    # This is the full subtractor (Still uses the full adder LOL)
    cin = 0
    result = []
    i = len(first) - 1
    j = len(second) - 1
    result = full_adder(first, cin, i, second, j)
    result = result[-len(first):]  # Ensure the result is the same length as the first operand
    return result


def full_adder(first, cin, i, second=None, j=None, two_complement=False):    
    #Now this is the full adder not the half bs
    result = []
    while i >= 0 or (j is not None and j >= 0):
        a = first[i] if i >= 0 else 0
        if second is not None:
            b = second[j] if j >= 0 else 0
        else:
            b = 0

        first_xor = a ^ b
        first_and = a & b
        sum_bit = first_xor ^ cin
        carry_bit = first_xor & cin
        cout = first_and | carry_bit

        result.append(sum_bit)

        i -= 1
        if two_complement == False:
            j -= 1

        cin = cout

    if cin == 1:
        result.append(cin)

    result.reverse()

    return result 

# # Half adder is basically just two digits (1, 0)
# half_adder(1,1)

# # Half subtraction is still the same, just subtract two digits (1,0) but it has a negative byte
# half_subtractor(0,1)

# This is the full adder and this is basically just full on binary arithmetic (Maybe i can add a decimal converter at some point but )
first = [1, 1, 0, 1]
second = [1, 0, 1, 1]
cin = 0

i = len(first) - 1
j = len(second) - 1
result = []

result = full_adder(first, cin, i, second, j)
power = len(result)
convert_to_decimal = convertion(result, power)
one_complement_result = one_complement(second)
two_complement_result = two_complement(one_complement_result)
subtraction_result = full_subtractor(first, two_complement_result)

print("The 1's complement of the subtrahend is:", one_complement_result)
print("The 2's complement of the subtrahend is:", two_complement_result)
print("The subtraction result is:", subtraction_result)
print("The binary output is:", result)
print("The decimal output is:", convert_to_decimal)