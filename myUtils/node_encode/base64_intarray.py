from myUtils.node_encode.base64_bytearray import to_base64, to_bytearray


def intarray_to_base64str(int_array):
    return to_base64(intarray_to_bytearray(int_array))


def intarray_to_bytearray(int_array):
    my_bytes = bytearray([0] * (max(int_array) // 8 + 1))
    for node in int_array:
        quotient = node // 8
        remainder = node % 8
        my_bytes[quotient] = my_bytes[quotient] | (1 << remainder)
    return my_bytes


def base64str_to_intarray(base64str):
    return bytearray_to_intarray(to_bytearray(base64str))


def bytearray_to_intarray(the_bytearray):
    intarray = []
    for i in range(len(the_bytearray)):
        for j in range(8):
            if the_bytearray[i] & (1 << j) != 0:
                intarray.append(j + 8*i)
    return intarray
