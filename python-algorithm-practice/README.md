# Python Algorithm & Problem-Solving Practice
**คลังรวบรวมแบบฝึกหัดและการศึกษาค้นคว้าเชิงขั้นตอนวิธีด้วยตนเอง (Self-Directed Learning & Problem Solving)**

---

## 📌 บทนำและเป้าหมาย (Overview & Objectives)

Repository นี้เป็นคลังเก็บแบบฝึกหัดและโปรเจกต์ขนาดเล็กที่พัฒนาขึ้นเพื่อ **ศึกษาและฝึกฝนทักษะการแก้ปัญหาเชิงอัลกอริทึม (Algorithmic Thinking & Problem Solving) นอกห้องเรียน** โดยใช้ภาษา **Python**

มุ่งเน้นการฝึกฝนทักษะสำคัญ:
- **การวิเคราะห์และลดความซับซ้อนของขั้นตอนวิธี (Time & Space Complexity Optimization):** พัฒนาจากวิธี Brute-Force $O(n^2)$ ไปสู่การใช้ Hash Table / Dictionary ในระดับ $O(n)$
- **การออกแบบฟังก์ชันที่ดี (Clean Code & Software Engineering Principles):** การใช้ Guard Clauses, Type Validation, Error Handling (`try-except`), และ Separation of Concerns
- **การฝึกฝนโจทย์แนว Technical Interview & Competitive Programming:** เช่น Two Sum, Anagrams, และ Frequency Counting

---

## 📂 โครงสร้างโฟลเดอร์ (Directory Structure)

```
python-algorithm-practice/
│
├── hashing/                        # 1. การประยุกต์ใช้ Hash Table / Dictionary & Optimization
│   ├── two_sum_bruteforce.py       # Two Sum: แนวทาง Brute-force O(n²)
│   ├── two_sum_hashmap.py          # Two Sum: แนวทาง Optimized HashMap O(n)
│   ├── anagram_checker_sort.py     # Anagram: แนวทาง Sorting O(n log n)
│   ├── anagram_checker_counter.py  # Anagram: แนวทาง Frequency Counter O(n)
│   └── manual_counter.py           # ตัวนับความถี่แบบพัฒนาเอง (Manual Dictionary Counter)
│
├── mini_projects/                  # 2. โปรแกรมประยุกต์ตรรกะและการตรวจสอบข้อมูล (Logic & Validation)
│   └── character_status_generator.py # ระบบคำนวณและสุ่มสเตตัสตัวละคร พร้อมระบบ Data Validation
│
└── string_manipulation/            # 3. การประมวลผลสตริงและการเข้ารหัสคลาสสิกขั้นพื้นฐาน (Basic Classical Ciphers)
    ├── caesar_cipher.py            # Caesar Cipher (Shift Cipher ขั้นพื้นฐาน)
    ├── affine_cipher.py            # Affine Cipher (สูตรพื้นฐาน C = (aP + b) mod 26)
    └── Polyalphabetic_Cipher.py    # Polyalphabetic Cipher (การเลื่อนตัวอักษรตามชุดตัวเลข)
```

> **📌 ดูเพิ่มเติมสำหรับส่วนการประยุกต์ขั้นสูง:**  
> สำหรับระบบการเข้ารหัสที่มีการประยุกต์ใช้คณิตศาสตร์ขั้นสูง (เช่น การสร้าง Key จากสมการกำลังสอง Quadratic Equation) ได้รับการแยกออกไปเป็นโฟลเดอร์เฉพาะทางในโปรเจกต์ **`../Cryptography/`** เพื่อใช้ในรายวิชารหัสวิทยาโดยเฉพาะ

---

## 🧠 รายละเอียดและการวิเคราะห์ความซับซ้อน (Algorithm Breakdown & Complexity)

---

### 1. ⚡ หมวด Hashing & Dictionary Optimization (`hashing/`)

การใช้ **Hash Table (Python `dict`)** ในการเข้าถึงข้อมูลด้วยเวลาเฉลี่ย $O(1)$ เพื่อลดเวลาการทำงานรวมจาก Quadratic Time $O(n^2)$ เป็น Linear Time $O(n)$:

#### • Two Sum Problem (`two_sum_bruteforce.py` vs `two_sum_hashmap.py`)
- **โจทย์:** ค้นหาคู่ดัชนีของตัวเลขใน Array ที่มีผลรวมเท่ากับค่าเป้าหมาย `target`
- **เปรียบเทียบแนวทาง:**
  - **Brute-force Approach:** ใช้ Nested Loop วนลูปซ้อน 2 ชั้น $\rightarrow$ **Time Complexity: $O(n^2)$, Space: $O(1)$**
  - **HashMap Approach:** วนลูป 1 รอบ เก็บค่า `target - current_val` ลงใน Dictionary เพื่อค้นหาคู่แบบ $O(1)$ ทันที $\rightarrow$ **Time Complexity: $O(n)$, Space: $O(n)$**

#### • Anagram Checker (`anagram_checker_sort.py` vs `anagram_checker_counter.py`)
- **โจทย์:** ตรวจสอบว่าคำ 2 คำประกอบด้วยตัวอักษรชุดเดียวกันหรือไม่ (เช่น `"listen"` กับ `"silent"`)
- **เปรียบเทียบแนวทาง:**
  - **Sorting Approach:** เรียงลำดับตัวอักษรแล้วเทียบกัน $\rightarrow$ **Time Complexity: $O(n \log n)$, Space: $O(n)$**
  - **Hash Counter Approach:** นับความถี่ตัวอักษรด้วย Dictionary $\rightarrow$ **Time Complexity: $O(n)$, Space: $O(k)$** *(โดย $k$ คือจำนวนตัวอักษรที่แตกต่างกัน)*

#### • Manual Frequency Counter (`manual_counter.py`)
- ฝึกการนับความถี่ของข้อมูลโดยสร้างตรรกะจัดการ Key-Value ด้วยตนเอง เพื่อทำความเข้าใจโครงสร้างภายในของตารางแฮช

---

### 2. 🎮 หมวด Mini Projects & System Logic (`mini_projects/`)

- **Character Status Generator (`character_status_generator.py`):**
  - โปรแกรมจำลองการคำนวณ Status ตัวละครในเกม RPG
  - **หลักการทางวิศวกรรมซอฟต์แวร์ที่ฝึกฝน:**
    - **Data Validation & Sanitization:** ตรวจสอบความถูกต้องของ Input ก่อนนำไปประมวลผล
    - **Guard Clauses:** ลดความซับซ้อนของ Nested If-Else ด้วยการคืนค่าหรือแจ้ง Error ทันทีเมื่อเงื่อนไขไม่ผ่าน
    - **Defensive Programming:** ใช้ `try-except` ป้องกันโปรแกรมแคชจากข้อมูลที่ผิดรูปแบบ

---

### 3. 🔐 หมวด String Manipulation & Basic Ciphers (`string_manipulation/`)

- ศึกษาทฤษฎีการแปลงตัวอักษรผ่านการคำนวณทางคณิตศาสตร์มอดุลาร์ขั้นพื้นฐาน (Modular Arithmetic $\pmod{26}$):
  - **Caesar Cipher:** เลื่อนตำแหน่งตัวอักษรด้วยค่าคงที่ $k$ ($C \equiv (P + k) \pmod{26}$)
  - **Affine Cipher:** แปลงตัวอักษรด้วยฟังก์ชันเชิงเส้น $C \equiv (aP + b) \pmod{26}$
  - **Polyalphabetic Cipher:** เลื่อนตำแหน่งตัวอักษรโดยใช้ชุดตัวเลขหมุนเวียน

---

## 📊 ตารางเปรียบเทียบประสิทธิภาพเชิงอัลกอริทึม (Complexity Comparison)

| ปัญหา / อัลกอริทึม | วิธีการ (Approach) | Time Complexity | Space Complexity | ประสิทธิภาพ |
| :--- | :--- | :--- | :--- | :--- |
| **Two Sum** | Brute-Force (Nested Loop) | $O(n^2)$ | $O(1)$ | 🔴 ช้าเมื่อข้อมูลขนาดใหญ่ |
| **Two Sum** | Hash Map Lookup | **$O(n)$** | $O(n)$ | 🟢 เร็วที่สุด (Optimal) |
| **Anagram Checker** | Sorting (`sorted()`) | $O(n \log n)$ | $O(n)$ | 🟡 ปานกลาง |
| **Anagram Checker** | Hash Counter (`dict`) | **$O(n)$** | $O(k)$ | 🟢 เร็วที่สุด (Optimal) |
| **Affine / Caesar** | Modular Mapping | **$O(n)$** | $O(n)$ | 🟢 เหมาะสมสำหรับ Linear Stream |

---

## 🚀 วิธีการรันตัวอย่างโค้ด (How to Run)

สามารถสั่งรันแต่ละสคริปต์ได้โดยตรงผ่าน Python CLI:

```bash
# ทดสอบ Two Sum (HashMap)
python hashing/two_sum_hashmap.py

# ทดสอบ Anagram Checker
python hashing/anagram_checker_counter.py

# ทดสอบ Character Status Generator
python mini_projects/character_status_generator.py

# ทดสอบ Caesar Cipher
python string_manipulation/caesar_cipher.py
```