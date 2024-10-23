import functions
from constants import binary_to_list
def shift_right(binary, n):
    return n * [0] + binary[: -n]

def rotr(binary, n):
    return binary[-n :] + binary[: -n]

def binary_addition(binary1, binary2):
    output = []
    if len(binary1) > len(binary2):
        long_binary = binary1
    else:
        long_binary = binary2
    min_lenght = min(len(binary1), len(binary2))
    max_lenght = max(len(binary1), len(binary2))
    lenght_diff = max_lenght - min_lenght
    übertrag = 0
    for i in range(min_lenght):        
        i = i + 1
        if übertrag + int(binary1[-i]) + int(binary2[-i]) == 0:
            output.insert(0, 0)
            übertrag = 0
        elif übertrag + int(binary1[-i]) + int(binary2[-i]) == 1:
            output.insert(0, 1)
            übertrag = 0
        elif übertrag + int(binary1[-i]) + int(binary2[-i]) == 2:
            output.insert(0, 0)
            übertrag = 1
        elif übertrag + int(binary1[-i]) + int(binary2[-i]) == 3:
            output.insert(0, 1)
            übertrag = 1
    for i in range(lenght_diff):
        i = i + 1
        if übertrag == 0:
            return long_binary[:lenght_diff - i - 1] + output
        else:    
            if übertrag + int(long_binary[lenght_diff - i]) == 0:
                output.insert(0, 0)
                übertrag = 0
            elif übertrag + int(long_binary[lenght_diff - i]) == 1:
                output.insert(0, 1)
                übertrag = 0
            elif übertrag + int(long_binary[lenght_diff - i]) == 2:
                output.insert(0, 0)
                übertrag = 1
            
    return output

def xor(binary1, binary2):                              #input lists must be same length and contain int
    output = []
    for i in range(len(binary1)):
        if binary1[i] + binary2[i] == 0 or binary1[i] + binary2[i] == 2:
            output.append(0)
        elif binary1[i] + binary2[i] == 1:
            output.append(1)
    return output

def sigma0(input):
    return xor(xor(rotr(input, 7), rotr(input, 18)), shift_right(input, 3))

def sigma1(input):
    return xor(xor(rotr(input, 17), rotr(input, 19)), shift_right(input, 10))

def SIGMA0(input):
    return xor(xor(rotr(input, 2), rotr(input, 13)), rotr(input, 22))

def SIGMA1(input):
    return xor(xor(rotr(input, 6), rotr(input, 11)), rotr(input, 25))

def choice(input1, input2, input3):
    output = []
    for i in range(len(input1)):
        if input1[i] == 1:
            output.append(input2[i])
        elif input1[i] == 0:
            output.append(input3[i])
    return output

def majority(input1, input2, input3):
    output = []
    for i in range(len(input1)):
        if input1[i] + input2[i] + input3[i] >= 2:
            output.append(1)
        else:
            output.append(0)
    return output
def new_word(message_schedule):
    first_two = binary_addition(message_schedule[-16], sigma0(message_schedule[-15]))
    last_two = binary_addition(message_schedule[-7], sigma1(message_schedule[-2]))
    return binary_addition(first_two, last_two)

def temporary_word1(word, constant, H):
    number1 = binary_addition(choice(H[4], H[5] ,H[6]), SIGMA1(H[4]))
    number2 = binary_addition(H[7], binary_addition(constant, word))
    return binary_addition(number1, number2)

def temporary_word2(H):
    return binary_addition(SIGMA0(H[0]), majority(H[0], H[1], H[2]))

def compression(H, temporary_word1, temporary_word2):
    H.insert(0, binary_addition(temporary_word1, temporary_word2))
    H[4] = binary_addition(H[4], temporary_word1)
    H.pop()
    return H



if __name__ == '__main__':
    print(majority(binary_to_list("1100101"), binary_to_list("0001011"), binary_to_list("0100100")))
