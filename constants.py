def binary_converter(input_list):
    output_list = []
    for variable in input_list:
        variable = int(variable, 16)
        output_list.append(format(variable, '0>32b'))
    return output_list

def binary_to_list(input):
    output_list = []
    for number in input:
        output_list.append(int(number))

    return output_list
             
def constant_converter(constants):
    output_list = []
    for i in binary_converter(constants):
        output_list.append(binary_to_list(i))
    return output_list
    

if __name__=='__main__':
    print(constant_converter())