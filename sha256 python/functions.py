
def binary(input):
    bits = ''.join(format(ord(c), '08b') for c in input)

    list_of_bits = []
    for i in bits:
        list_of_bits.append(int(i))
    return list_of_bits

def divider(list_of_binary, chunk_length):
    divided_list = []
    for b in range(0, len(list_of_binary), chunk_length):

        divided_list.append(list_of_binary[b:chunk_length + b])
    return divided_list

def add_zeros(list_of_bits, final_lenght):
    lenght = len(list_of_bits)
    for i in range(lenght, final_lenght):
        list_of_bits.append(0)
    return list_of_bits

def padding(list_of_bits):
    lenght = len(list_of_bits)
    binary_lenght = [int(b) for b in bin(lenght)[2:].zfill(64)]
    list_of_bits.append(1)

    while (len(list_of_bits) + 64) % 512 !=0:
        list_of_bits.append(0)
    list_of_bits = divider(list_of_bits + binary_lenght, 512)
    return list_of_bits
        
def binary_to_int(list_of_bits):
    integer = int("".join(str(x)for x in list_of_bits), 2)
    return integer

def binary_to_hex(list_of_bits):
    integer = int("".join(str(x)for x in list_of_bits), 2)
    hexadecimal = hex(int(integer))[2:]
    return hexadecimal    
if __name__ == '__main__':
    print(binary_to_hex([1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]))
