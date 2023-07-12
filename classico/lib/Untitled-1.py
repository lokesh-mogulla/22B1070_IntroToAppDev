def decodeAscii(bin_string):
    binary_int = int(bin_string, 2);
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = "Bin string cannot be decoded"
    for enc in ['utf-8', 'ascii', 'ansi']:
        try:
            ascii_text = binary_array.decode(encoding=enc)
            break
        except:
            pass
    print(ascii_text)

s = "111010101000100010101010001010001110100011101010000000100010101011100010001011101000111010111011100000001110101110100011101110111000111010100010000000101000101010000000101110001110100000001000111010001010001110111010001110111000101110000"
decodeAscii(s)