def cipher(text, shift, encrypt=True):

    if not (isinstance(shift, (list, tuple)) and len(shift) >= 4):
        return 'Shift must be a list or tuple containing at least 4 integers.'


    if not all(isinstance(x, int) for x in shift):
        return 'Shift must be an integer value.'

    if any((x < 1 or x > 25) for x in shift):
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift_length = len(shift)

    if not encrypt:
        shift = [-x for x in shift]

    result = []

    for i, char in enumerate(text.lower()):
        current_shift = shift[i % shift_length]

        if char in alphabet:
            new_index = (alphabet.index(char) + current_shift) % 26
            result.append(alphabet[new_index])

        else:
            result.append(char)
            # continue

    return ''.join(result)

def encrypt(text, shift):
    return cipher(text, shift)
   
def decrypt(text, shift):
    return cipher(text, shift, encrypt=False)

if __name__ == '__main__':
    my_shift = [1, 2, 3]
    original_text = "Hello World!"
    print(f"Original: {original_text}")

    encrypted = encrypt(original_text, my_shift)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt(encrypted, my_shift)
    print(f"Decrypted: {decrypted}")

    print("-" * 30)
    
    m = [1, 2, 0, 4, 5] 
    print(f"Test Error Catching with shift {m}:")
    print(encrypt("Test", m))