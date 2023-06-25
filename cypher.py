def encode_message(message):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            # Determine the ASCII value of the character
            ascii_value = ord(char)
            
            # Check if the character is uppercase or lowercase
            if char.isupper():
                base_value = ord('A')
            else:
                base_value = ord('a')
            
            # Calculate the encoded ASCII value
            encoded_ascii = (ascii_value - base_value + 15) % 26 + base_value
            
            # Convert the encoded ASCII value back to a character
            encoded_char = chr(encoded_ascii)
            
            encoded_message += encoded_char
        else:
            # Non-alphabetic characters remain the same
            encoded_message += char
    
    return encoded_message


# Test the function
message = "HyperionDev"
encoded_message = encode_message(message)
print(encoded_message)
