# Applied Cryptography & Information Security Collection
**คลังรวบรวมอัลกอริทึมและการประยุกต์ใช้ในรายวิชารหัสวิทยาและความมั่นคงปลอดภัยสารสนเทศ (Cryptography & Information Security)**

---

## 📌 บทนำและภาพรวมของโปรเจกต์ (Overview)

โปรเจกต์นี้จัดทำขึ้นเพื่อรวบรวมการศึกษาค้นคว้าและการพัฒนาขั้นตอนวิธีทาง **รหัสวิทยา (Cryptography)** ทั้งการคำนวณทางคณิตศาสตร์มอดุลาร์ (Modular Arithmetic), การเข้ารหัสและถอดรหัสแบบคลาสสิก (Classical Ciphers), และการประยุกต์ใช้สมการคณิตศาสตร์ขั้นสูงในการสร้างและกระจายกุญแจรหัสลับ (Key Generation)

---

## 📂 โครงสร้างโปรเจกต์ (Directory Structure)

```
Cryptography/
│
├── README.md                          # เอกสารประกอบและคู่มือทฤษฎีรหัสวิทยา
├── .gitignore                         # กำหนดไฟล์ที่ไม่ต้องติดตามใน Git
│
└── applied_affine_quadratic.py        # 🔐 การประยุกต์ Affine Cipher ร่วมกับการสร้าง Key จากสมการกำลังสอง (Quadratic Equation)
```

---

## 🧠 ทฤษฎีและการประยุกต์ใช้ (Theoretical Foundations & Applications)

### 1. 🧮 การสืบทอดและสร้างกุญแจจากสมการกำลังสอง (Quadratic Key Derivation)

ในระบบนี้ มีการเชื่อมโยงการสร้างกุญแจคู่ $(a, b)$ ของ Affine Cipher เข้ากับรากของสมการพหุนามกำลังสอง (Quadratic Roots):

$$Ax^2 + Bx + (C - D) = 0$$

- **การคำนวณ Discriminant:**
  $$\Delta = B^2 - 4A(C - D)$$
- **การหารากของสมการ (Quadratic Formula):**
  $$r_{1, 2} = \frac{-B \pm \sqrt{\Delta}}{2A}$$
- **การแปลงเป็นค่ากุญแจในระบบเลขคณิตมอดุลาร์ $\pmod{26}$:**
  $$a \equiv \text{round}(r_1) \pmod{26}$$
  $$b \equiv \text{round}(r_2) \pmod{26}$$

---

### 2. 🔐 ทฤษฎี Affine Cipher และเงื่อนไขจำนวนเฉพาะสัมพัทธ์ (Coprimality Condition)

ในระบบ Affine Cipher กุญแจ $a$ จะสามารถถอดรหัสได้ก็ต่อเมื่อมี **ตัวผกผันการคูณมอดุโล (Modular Multiplicative Inverse: $a^{-1} \pmod{26}$)** ซึ่งเงื่อนไขทางคณิตศาสตร์กำหนดไว้ว่า:

$$\gcd(a, 26) = 1$$

เซตของค่า $a$ ที่เป็นไปได้สำหรับชุดตัวอักษรภาษาอังกฤษ ($m = 26$) คือ:
$$\{1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\}$$

- **สูตรการเข้ารหัส (Encryption):**
  $$C \equiv (a \cdot P + b) \pmod{26}$$
- **สูตรการถอดรหัส (Decryption):**
  $$P \equiv a^{-1} \cdot (C - b) \pmod{26}$$
  *(โดยที่ $a \cdot a^{-1} \equiv 1 \pmod{26}$ หาได้จาก Extended Euclidean Algorithm)*

---

## 🚀 วิธีการรันโปรแกรม (How to Run)

สั่งรันไฟล์ผ่าน Python CLI เพื่อเข้าสู่ Interactive Mode:

```bash
python applied_affine_quadratic.py
```

### ตัวอย่างการทำงาน:
1. **เลือกโหมด:** `en` (เข้ารหัส), `de` (ถอดรหัส), หรือ `both` (ทดสอบทั้งสองขั้นตอน)
2. **ป้อนข้อความ:** เช่น `Hello Cryptography World!` (ระบบจะ Clean Text กรองเฉพาะตัวอักษร a-z อัตโนมัติ)
3. **ป้อนสัมประสิทธิ์สมการ 4 ตัว [A B C D]:** เช่น `1 -19 90 6`
4. **ผลลัพธ์:** ระบบจะคำนวณรากสมการ แปลงเป็นกุญแจ $(a, b)$ ที่ถูกกฎมอดุลาร์ และดำเนินการเข้ารหัส/ถอดรหัสให้ทันที

---

## 🗺️ แผนผังเนื้อหาที่กำลังศึกษาเพิ่มเติม (Upcoming Course Roadmap)

- [ ] **Classical Ciphers:** Playfair Cipher, Hill Cipher (Matrix Multiplication in $\mathbb{Z}_{26}$), Vigenère Cipher, Vernam Cipher (One-Time Pad)
- [ ] **Modern Symmetric Cryptography:** Data Encryption Standard (DES), Advanced Encryption Standard (AES) - S-Box, ShiftRows, MixColumns
- [ ] **Asymmetric Cryptography (Public Key):** RSA Algorithm (Euler's Totient $\phi(n)$), Diffie-Hellman Key Exchange
- [ ] **Cryptographic Hash Functions:** SHA-256, Message Authentication Code (MAC / HMAC)
