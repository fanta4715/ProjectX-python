def caesar_cipher_decode(target_text, shift):
    decoded_text = ""
    for char in target_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code -= shift
            if char_code < ord('a'):
                char_code += 26
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            decoded_text += char_code
        else:
            decoded_text += char

    return decoded_text

if __name__ == "__main":
    with open("password.txt", "r") as file:
        encoded_password = file.read().strip()

    for shift in range(1, 27):
        decoded_password = caesar_cipher_decode(encoded_password, shift)
        print(f"Shift {shift}: {decoded_password}")

    shift_to_use = int(input("Enter the shift number for the correct decryption: "))
    if shift_to_use >= 1 and shift_to_use <= 26:
        result_text = caesar_cipher_decode(encoded_password, shift_to_use)
        with open("result.txt", "w") as result_file:
            result_file.write(result_text)
        print(f"Result saved to result.txt")
    else:
        print("Invalid shift number. It should be between 1 and 26.")
