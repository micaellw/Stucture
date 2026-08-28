def cipher(text, key, encrypt=True):

    if not (isinstance(key, (list, tuple)) and len(key) == 2):
        return 'Key must be a list or tuple containing two integers (a, b).'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    valid_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    
    Akey , BKey = key

    if not (isinstance(Akey, int) and isinstance(BKey, int)):
        return 'Both keys (a, b) must be integers.'

    if Akey not in valid_a:
        return f'Key "a" must be one of {valid_a}.'

    mapped_alphabet = ''

    if encrypt:
        for i in range(26):
            mapped_index = (Akey * i + BKey) % 26
            mapped_alphabet += alphabet[mapped_index]
    else:
        a_inv = pow(Akey, -1, 26)
        for i in range(26):
            mapped_index = (a_inv * (i - BKey)) % 26
            mapped_alphabet += alphabet[mapped_index]
            
    translation_table = str.maketrans(alphabet + alphabet.upper(), mapped_alphabet + mapped_alphabet.upper())
    encrypted_text = text.translate(translation_table)

    return encrypted_text



def encrypt(text, shift):
    return cipher(text, shift)
   
def decrypt(text, shift):
    return cipher(text, shift, encrypt=False)

if __name__ == '__main__':
    my_text = "Hello World!"
    my_key = [7, 12] 

    # เข้ารหัส
    encrypted_text = encrypt(my_text, my_key)
    print(f"Encrypted: {encrypted_text}")

    # ถอดรหัส
    decrypted_text = decrypt(encrypted_text, my_key)
    print(f"Decrypted: {decrypted_text}")