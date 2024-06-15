import sys

hex_to_dec_dict = {
    'a':'10',
    'b':'11',
    'c':'12',
    'd':'13',
    'e':'14',
    'f':'15'
}

hex_to_bin_dict = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'a':'1010',
    'b':'1011',
    'c':'1100',
    'd':'1101',
    'e':'1110',
    'f':'1111'
}

def hex_to_bin(x):
    """ hexadecimal to binary """
    result_bin = ""
    y = list(x[2:])
    for hex_bit in y:
        if not hex_bit.isdigit():
            result_bin += hex_to_bin_dict[hex_bit.lower()] # find binary value of hex letters
        else:
            result_bin += hex_to_bin_dict[hex_bit] # find binary string corresponding to hex numerical value
    
    for i in range(len(result_bin)):
        if int(result_bin[i]) == 1: # remove trailing zeroes
            result_bin = result_bin[i:] # i is the location of the first 1 in the binary string
            break
    
    return result_bin

def hex_to_dec(x):
    """ hexadecimal to decimal """
    x_bin = hex_to_bin(x)
    x_dec = bin_to_dec(f'0b{x_bin}')

    return x_dec

def bin_to_dec(x):
    """ binary to decimal """
    result_dec = 0
    y = list(x[2:])
    for i in range(0,len(y)):
        if y[i] == '1': # i is the location of the first 1 in the binary number
            y = y[i:] # remove trailing zeroes from binary number
            break
    y.reverse()
    for i in range(len(y)):
        if y[i] not in ['0','1']:
            print(f"\n {x} is not a binary number!\n")
            sys.exit()
        
        digit = int(y[i])
        result_dec += digit*(2**(i)) # simply sum the values of the digits multiplied by 2 to the power of the digit's position

    return result_dec

def bin_to_hex(x):
    """ binary to hexadecimal """
    result_hex = ""
    y = list(x[2:])
    for i in range(0,len(y)):
        if y[i] == '1': # i is the location of the first 1 in the binary number
            y = y[i:] # remove trailing zeroes from binary number
            break
    y.reverse()

    if len(y)%4 != 0: # for converting from binary to hexadecimal, if the binary string is not a multiple of 4, it will need trailing zeroes added
        factor = 0
        while 4*factor < len(y):
            factor += 1
        num_zeros_front = 4*factor-len(y)

        y.reverse()
        for i in range(num_zeros_front):
            y.insert(0,'0') # insert the number of trailing zeroes required
    elif len(y)%4 == 0:
        y.reverse()
    
    new_binary_num = ""
    for i in y:
        new_binary_num += str(i) # create the new binary string with added zeroes

    hex_digits = []
    for i in range(int(len(new_binary_num)/4)):
        hex_digits.append(str(new_binary_num[4*i:4*(i+1)])) # split the number into chunks of size 4 (for conversion to hex using hex_to_bin dictionary)

    for i in hex_digits:
        for j in hex_to_bin_dict.keys(): # look through the hexadecimal characters
            if hex_to_bin_dict[j] == i: # if the value corresponding to a particular key is the same as one of the length-4 chunks in the binary number
                result_hex += j # add that value to the hex result
    
    for i in range(len(result_hex)):
        if result_hex[i] != '0': # remove trailing zeroes from hex result
            result_hex = result_hex[i:] # redefine hex result starting from the position of the first non-zero digit
            break

    return result_hex # return the results

def dec_to_bin(x):
    """ decimal to binary """
    x = int(x)
    powers = []
    while x > 0:
        power = 0
        while x - 2**power > 0:
            power += 1
        if x != 2**power:
            power -= 1
        powers.append(power)
        x -= 2**power
    
    result = [0 for i in range(powers[0] + 1)]
    for i, j in enumerate(result):
        result[i] = "1" if i in powers else "0"
    result.reverse()
    
    return "".join(result)

def dec_to_hex(x):
    """ decimal to hexadecimal """
    x_bin = dec_to_bin(x)
    x_hex = bin_to_hex(f'0b{x_bin}')

    return x_hex

if __name__ == "__main__":
    x = str(sys.argv[1])
    if '0x' in x:
        d = hex_to_dec(x)
        b = hex_to_bin(x)
        print(f"\nDecimal = {d}, Binary = 0b{b}\n")
    elif '0b' in x:
        d = bin_to_dec(x)
        h = bin_to_hex(x)
        print(f"\nDecimal = {d}, Hexadecimal = 0x{h}\n")
    else:
        b = dec_to_bin(x)
        h = dec_to_hex(x)
        print(f"\nBinary = 0b{b}, Hexadecimal = 0x{h}\n")