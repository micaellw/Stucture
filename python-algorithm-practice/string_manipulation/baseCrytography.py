import math

def generate_keys_from_quadratic(inputs):
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

    valid_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    def get_closest_valid_a(target):
        return min(valid_a, key=lambda x: abs(x - target))

    if val1 in valid_a:
        return [val1, val2], 'Success'
    elif val2 in valid_a:
        return [val2, val1], 'Success'
    else:
        best_a = get_closest_valid_a(val1)
        return [best_a, val2], f'Auto-adjusted "a" key to {best_a} to fit Affine rules'


# ฟังก์ชันสำหรับทำความสะอาดข้อความ (กรองเฉพาะ a-z)
def clean_text(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(char for char in text.lower() if char in alphabet)


def cipher(text, key, encrypt=True):
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
        a_inv = pow(Akey, -1, 26)
        for i in range(26):
            mapped_index = (a_inv * (i - BKey)) % 26
            mapped_alphabet += alphabet[mapped_index]
            
    translation_table = str.maketrans(alphabet, mapped_alphabet)
    return text.translate(translation_table)

def encrypt(text, shift):
    return cipher(text, shift)
   
def decrypt(text, shift):
    return cipher(text, shift, encrypt=False)


if __name__ == '__main__':
    print("=== Affine Cipher (Quadratic Equation Keys) ===")
    
    # เพิ่มตัวเลือก 'both' สำหรับทำทั้งคู่
    while True:
        mode = input("Select mode ('en'=encrypt / 'de'=decrypt / 'both'=do both): ").strip().lower()
        if mode in ['en', 'de', 'both']:
            break
        else:
            print(">> Please enter 'en', 'de', or 'both'.\n")

    my_text = input("Enter your text: ")
    
    # นำข้อความมาทำความสะอาดก่อน เพื่อให้แสดงผลตรงกับที่นำไปประมวลผลจริง
    cleaned_text = clean_text(my_text)
    
    if not cleaned_text:
        print(">> [Error] No valid English alphabets found to process. Exiting...")
        exit()

    while True:
        try:
            key_input = input("Enter 4 integer keys (e.g., 1 -19 90 6): ")
            raw_inputs = [int(x) for x in key_input.split()]
            
            if len(raw_inputs) == 4:
                break
            else:
                print(">> Please enter exactly 4 numbers.\n")
        except ValueError:
            print(">> Please enter numbers only.\n")
    
    print("-" * 40)
    # แสดงข้อความที่ตัดตัวเลข ช่องว่าง และสัญลักษณ์ออกเรียบร้อยแล้ว
    print(f"Original Text (Cleaned): '{cleaned_text}'")
    
    my_key, status_msg = generate_keys_from_quadratic(raw_inputs)
    
    if my_key is None:
        print(f"\n[Error] {status_msg}")
    else:
        print(f"Generated Keys (a, b): {my_key} [{status_msg}]")
        
        # จัดการผลลัพธ์ตามโหมดที่เลือก
        if mode == 'en':
            encrypted_text = encrypt(cleaned_text, my_key)
            print(f"\n[Result] Encrypted: {encrypted_text}")
            
        elif mode == 'de':
            decrypted_text = decrypt(cleaned_text, my_key)
            print(f"\n[Result] Decrypted: {decrypted_text}")
            
        elif mode == 'both':
            print("\n--- Running Both Modes ---")
            # เข้ารหัสก่อน
            encrypted_text = encrypt(cleaned_text, my_key)
            print(f"[Step 1] Encrypted: {encrypted_text}")
            
            # นำข้อความที่เข้ารหัสแล้ว มาถอดรหัสกลับคืน
            decrypted_text = decrypt(encrypted_text, my_key)
            print(f"[Step 2] Decrypted back to Original: {decrypted_text}")
            
        print("-" * 40)