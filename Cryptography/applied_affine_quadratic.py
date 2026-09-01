# applied_affine_quadratic.py - Applied Affine Cipher with Quadratic Equation Key Generation
# Developed for Cryptography / Information Security Course

import math


def generate_keys_from_quadratic(inputs):
    """
    Generates Affine Cipher keys (a, b) from the roots of a quadratic equation:
    A*x^2 + B*x + (C - D) = 0
    Ensures key 'a' is coprime to 26 (gcd(a, 26) == 1) for valid modular inverse.
    """
    if not (isinstance(inputs, (list, tuple)) and len(inputs) == 4):
        return None, 'Input must be a list of 4 numbers [A, B, C, D].'

    A, B, C, D = inputs
    
    if A == 0:
        return None, 'A cannot be 0 in a quadratic equation.'

    a_eq = A
    b_eq = B
    c_eq = C - D

    discriminant = (b_eq**2) - (4 * a_eq * c_eq)

    if discriminant < 0:
        discriminant = abs(discriminant)

    root1 = (-b_eq + math.sqrt(discriminant)) / (2 * a_eq)
    root2 = (-b_eq - math.sqrt(discriminant)) / (2 * a_eq)

    r1_int = round(root1)
    r2_int = round(root2)

    val1 = r1_int % 26
    val2 = r2_int % 26

    # Valid values for 'a' such that gcd(a, 26) == 1 (Coprime to 26)
    valid_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    def get_closest_valid_a(target):
        return min(valid_a, key=lambda x: abs(x - target))

    if val1 in valid_a:
        return [val1, val2], 'Success'
    elif val2 in valid_a:
        return [val2, val1], 'Success'
    else:
        best_a = get_closest_valid_a(val1)
        return [best_a, val2], f'Auto-adjusted "a" key to {best_a} to fit Affine rules (gcd(a, 26)=1)'


def clean_text(text):
    """
    Sanitizes text by converting to lowercase and keeping only letters a-z.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(char for char in text.lower() if char in alphabet)


def cipher(text, key, encrypt=True):
    """
    Affine Cipher Core:
    Encryption: C = (a * P + b) mod 26
    Decryption: P = a^(-1) * (C - b) mod 26
    """
    if not (isinstance(key, (list, tuple)) and len(key) == 2):
        return 'Key must be a list or tuple containing two integers (a, b).'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    valid_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    
    Akey, BKey = key

    if not (isinstance(Akey, int) and isinstance(BKey, int)):
        return 'Both keys (a, b) must be integers.'

    if Akey not in valid_a:
        return f'Key "a" (which is {Akey}) must be one of {valid_a}.'

    mapped_alphabet = ''

    if encrypt:
        for i in range(26):
            mapped_index = (Akey * i + BKey) % 26
            mapped_alphabet += alphabet[mapped_index]
    else:
        # Calculate modular multiplicative inverse: a^(-1) mod 26
        a_inv = pow(Akey, -1, 26)
        for i in range(26):
            mapped_index = (a_inv * (i - BKey)) % 26
            mapped_alphabet += alphabet[mapped_index]
            
    translation_table = str.maketrans(alphabet, mapped_alphabet)
    return text.translate(translation_table)


def encrypt(text, key):
    return cipher(text, key, encrypt=True)

   
def decrypt(text, key):
    return cipher(text, key, encrypt=False)


def main():
    print("=" * 60)
    print("  Applied Affine Cipher: Quadratic Key Derivation")
    print("=" * 60)
    
    while True:
        mode = input("Select mode ('en'=encrypt / 'de'=decrypt / 'both'=do both): ").strip().lower()
        if mode in ['en', 'de', 'both']:
            break
        else:
            print(">> Please enter 'en', 'de', or 'both'.\n")

    my_text = input("Enter your text: ")
    cleaned_text = clean_text(my_text)
    
    if not cleaned_text:
        print(">> [Error] No valid English alphabets found to process. Exiting...")
        return

    while True:
        try:
            key_input = input("Enter 4 integer coefficients for Quadratic Eq [A B C D] (e.g., 1 -19 90 6): ")
            raw_inputs = [int(x) for x in key_input.split()]
            
            if len(raw_inputs) == 4:
                break
            else:
                print(">> Please enter exactly 4 numbers.\n")
        except ValueError:
            print(">> Please enter numbers only.\n")
    
    print("-" * 60)
    print(f"Original Text (Cleaned): '{cleaned_text}'")
    
    my_key, status_msg = generate_keys_from_quadratic(raw_inputs)
    
    if my_key is None:
        print(f"\n[Error] {status_msg}")
    else:
        print(f"Generated Keys (a, b)   : {my_key} [{status_msg}]")
        print("-" * 60)
        
        if mode == 'en':
            encrypted_text = encrypt(cleaned_text, my_key)
            print(f"[Result] Encrypted: {encrypted_text}")
            
        elif mode == 'de':
            decrypted_text = decrypt(cleaned_text, my_key)
            print(f"[Result] Decrypted: {decrypted_text}")
            
        elif mode == 'both':
            encrypted_text = encrypt(cleaned_text, my_key)
            print(f"[Step 1] Encrypted Text: {encrypted_text}")
            
            decrypted_text = decrypt(encrypted_text, my_key)
            print(f"[Step 2] Decrypted Back: {decrypted_text}")
            
        print("=" * 60)


if __name__ == '__main__':
    main()
