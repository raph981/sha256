import functions
import constants
import calculating_functions
h = ['0x6a09e667', '0xbb67ae85', '0x3c6ef372', '0xa54ff53a', '0x510e527f', '0x9b05688c', '0x1f83d9ab', '0x5be0cd19']
k = ['0x428a2f98', '0x71374491', '0xb5c0fbcf', '0xe9b5dba5', '0x3956c25b', '0x59f111f1', '0x923f82a4','0xab1c5ed5', 
     '0xd807aa98', '0x12835b01', '0x243185be', '0x550c7dc3', '0x72be5d74', '0x80deb1fe','0x9bdc06a7', '0xc19bf174', 
     '0xe49b69c1', '0xefbe4786', '0x0fc19dc6', '0x240ca1cc', '0x2de92c6f','0x4a7484aa', '0x5cb0a9dc', '0x76f988da', 
     '0x983e5152', '0xa831c66d', '0xb00327c8', '0xbf597fc7','0xc6e00bf3', '0xd5a79147', '0x06ca6351', '0x14292967', 
     '0x27b70a85', '0x2e1b2138', '0x4d2c6dfc','0x53380d13', '0x650a7354', '0x766a0abb', '0x81c2c92e', '0x92722c85', 
     '0xa2bfe8a1', '0xa81a664b','0xc24b8b70', '0xc76c51a3', '0xd192e819', '0xd6990624', '0xf40e3585', '0x106aa070', 
     '0x19a4c116','0x1e376c08', '0x2748774c', '0x34b0bcb5', '0x391c0cb3', '0x4ed8aa4a', '0x5b9cca4f', '0x682e6ff3',
     '0x748f82ee', '0x78a5636f', '0x84c87814', '0x8cc70208', '0x90befffa', '0xa4506ceb', '0xbef9a3f7','0xc67178f2']
H = constants.constant_converter(h)
K = constants.constant_converter(k)

def main(input, H, K):   
    
    binary_input = functions.binary(input)                               #get binary from functions
    padded_binary = functions.padding(binary_input)                      #padding of the binary input to a multiple of 512 bits
    initial_Value = H.copy()
    for block in padded_binary:
        
        message_schedule = functions.divider(block, 32)
        while len(message_schedule) < 64:
            message_schedule.append(calculating_functions.new_word(message_schedule))

        for i in range(len(message_schedule)):
            T1 = calculating_functions.temporary_word1(message_schedule[i], K[i], H)
            T2 = calculating_functions.temporary_word2(H)
            H = calculating_functions.compression(H, T1, T2)

        for i in range(len(H)):
            H[i] = calculating_functions.binary_addition(H[i], initial_Value[i])
        initial_Value = H.copy()
    
    
    integer = "".join(str(functions.binary_to_int(x))for x in H)
    hex = "".join(str(functions.binary_to_hex(x))for x in H)
    return H

if __name__ == '__main__':
     print(main(str(2613),H, K))
     i = 0
     
     while True:
        hex_values = "0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c"
        result_string = codecs.decode(hex_values, 'hex').decode('utf-8')
        if int(hash) > 115414672968422429946412118886657223350158095212740534089704277315201526:
            print(f"sha256({i})= {hash}")
            i = i + 1
        else:
            print(f"sha256({i})= {hash}")
            break
         
