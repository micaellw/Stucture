# Java Algorithms & Data Structures Collection
**คลังรวมการทดลองและโครงงานเชิงขั้นตอนวิธีในรายวิชา Discrete Mathematics และ Data Structures & Algorithms**

---

## 📌 บทนำและภาพรวมของโปรเจกต์ (Overview)

โปรเจกต์นี้เป็นการรวบรวมแบบฝึกหัดและการพัฒนาโปรแกรมด้วยภาษา **Java** เพื่อประยุกต์ใช้ทฤษฎีทาง **คณิตศาสตร์ไม่ต่อเนื่อง (Discrete Mathematics)** และ **โครงสร้างข้อมูลและขั้นตอนวิธี (Data Structures & Algorithms)** เข้ากับการเขียนโปรแกรมจริง (Hands-on Implementation)

โดยเน้นการสร้างโครงสร้างข้อมูลพื้นฐานจากศูนย์ (From Scratch) โดยไม่พึ่งพา Standard Library สำเร็จรูป เช่น การสร้าง **Linked List**, **Stack**, การจัดการตัวชี้ (Pointers/References), การคำนวณความสัมพันธ์เวียนเกิด (**Recursion & Recurrence Relations**), และขั้นตอนวิธีทางทฤษฎีจำนวน (**Number Theory**)

---

## 📂 โครงสร้างสารบัญอัลกอริทึม (Table of Algorithms)

```
Java-Algorithms/
│
├── GCD/                   # 1. Extended Euclidean Algorithm & Linear Diophantine Equation
│   ├── src/GCD.java       # หา ห.ร.ม. และแก้สมการ ax + by = c
│   └── README.md
│
├── IF/                    # 2. Infix to Postfix Converter & Expression Evaluator
│   ├── src/
│   │   ├── IF.java              # Main Entry Point
│   │   ├── InFixToPosFix.java   # อัลกอริทึมแปลง Infix -> Postfix
│   │   ├── CalculatePosFix.java # คำนวณผลลัพธ์ของ Postfix Expression
│   │   └── Linklist.java        # Custom Stack Data Structure (Linked List-based)
│   └── README.md
│
├── Prime0/                # 3. Sieve of Eratosthenes with Custom Singly Linked List
│   ├── src/
│   │   ├── Prime0.java    # อัลกอริทึมหาจำนวนเฉพาะด้วยตะแกรงเอราทอสเทนีส
│   │   └── LinkNode.java  # Singly Linked List Node พร้อมฟังก์ชันลบโหนด (Node Deletion)
│   └── README.md
│
└── TowersOfHanoi/         # 4. Interactive Towers of Hanoi with GUI & Recursion
    ├── src/TowersOfHanoi.java  # หอคอยฮานอย (Java Swing GUI + Thread + Recursive Solver)
    └── README.md
```

---

## 🧠 รายละเอียดเชิงวิชาการในแต่ละโมดูล (Detailed Modules)

---

### 1. 📐 GCD & Linear Diophantine Equations (`GCD/`)

- **รายวิชาที่เกี่ยวข้อง:** Discrete Mathematics (ทฤษฎีจำนวน - Number Theory)
- **แนวคิดและทฤษฎีหลัก:**
  - **ขั้นตอนวิธีแบบยุคลิดขยาย (Extended Euclidean Algorithm):** หาค่าตัวหารร่วมมาก $\gcd(a, b)$ พร้อมทั้งสัมประสิทธิ์ของเบซูต์ (Bézout's coefficients) $s, t$ ที่ทำให้ $as + bt = \gcd(a, b)$
  - **สมการไดโอแฟนไทน์เชิงเส้น (Linear Diophantine Equation):** แก้สมการในรูป:
    $$ax + by = c$$
    สมการจะมีผลเฉลยเป็นจำนวนเต็มก็ต่อเมื่อ $\gcd(a, b) \mid c$ (หาร $c$ ลงตัว)
  - **การหาชุดคำตอบทั่วไป (General Solutions):**
    $$x = x_0 + \left(\frac{b}{\gcd(a, b)}\right)n$$
    $$y = y_0 - \left(\frac{a}{\gcd(a, b)}\right)n$$
    โดยโปรแกรมจะคำนวณหาขอบเขตของช่วงจำนวนเต็ม $n$ ($n_1 \le n \le n_2$) และแจกแจงค่า $(x, y)$ ที่สอดคล้องทั้งหมดออกมาอย่างสมบูรณ์

---

### 2. 🧮 Expression Parsing: Infix to Postfix & Evaluation (`IF/`)

- **รายวิชาที่เกี่ยวข้อง:** Data Structures (โครงสร้างข้อมูล Stack และ Linked List) & Compiler Theory
- **แนวคิดและทฤษฎีหลัก:**
  - **โครงสร้างข้อมูล Stack (LIFO - Last In First Out):** พัฒนาคลาส `Linklist.java` ขึ้นเองโดยใช้ **Node Pointer** ในการจัดการ `push()` และ `pop()` โดยไม่ใช้ `java.util.Stack`
  - **การแปลงนิพจน์ (Infix to Postfix Conversion):**
    - จัดการลำดับความสำคัญของตัวดำเนินการ (Operator Precedence):
      - ยกกำลัง `^` (ลำดับความสำคัญสูงสุด = 3)
      - คูณ/หาร `*`, `/` (ลำดับความสำคัญ = 2)
      - บวก/ลบ `+`, `-` (ลำดับความสำคัญ = 1)
      - วงเล็บ `( ... )`
    - ตรวจสอบความถูกต้องของวงเล็บเปิด-ปิด (Bracket Error Detection)
  - **การคำนวณค่านิพจน์ Postfix (Postfix Expression Evaluation):**
    - วนลูปอ่านโทเค็น (Operand / Operator) แล้วประมวลผลผ่าน Stack เพื่อคำนวณผลลัพธ์สุดท้ายออกมาในรูปทศนิยมสองตำแหน่ง

---

### 3. 🔢 Prime Number Sieve with Linked List (`Prime0/`)

- **รายวิชาที่เกี่ยวข้อง:** Discrete Mathematics & Data Structures
- **แนวคิดและทฤษฎีหลัก:**
  - **ตะแกรงเอราทอสเทนีส (Sieve of Eratosthenes):** อัลกอริทึมค้นหาจำนวนเฉพาะทั้งหมดที่มีค่าน้อยกว่าหรือเท่ากับ $p$ ด้วยการตัดพหุคูณของจำนวนเฉพาะออกไป โดยตรวจสอบตัวหารจนถึงขอบเขต $\sqrt{p}$
  - **การจัดการหน่วยความจำด้วย Linked List (`LinkNode.java`):**
    - สร้าง Single Linked List เก็บค่าตัวเลขตั้งแต่ $2$ ถึง $p$
    - เมื่อพบตัวเลขที่ไม่ใช่จำนวนเฉพาะ (Composite Number) จะสั่งตัดโหนดทิ้งด้วยฟังก์ชัน `Del(LinkNode x, int y)` ซึ่งเป็นการเปลี่ยนทิศทาง Pointer ($O(1)$ Re-linking)
  - **การส่งออกผลลัพธ์ (File I/O & Automation):**
    - บันทึกรายการจำนวนเฉพาะที่ค้นพบลงในไฟล์ `output.txt` และเรียกโปรแกรม `notepad.exe` ขึ้นมาแสดงผลโดยอัตโนมัติ

---

### 4. 🗼 Interactive Towers of Hanoi with GUI (`TowersOfHanoi/`)

- **รายวิชาที่เกี่ยวข้อง:** Discrete Mathematics (ความสัมพันธ์เวียนเกิด) & Data Structures (การเวียนเกิด - Recursion)
- **แนวคิดและทฤษฎีหลัก:**
  - **ความสัมพันธ์เวียนเกิด (Recurrence Relation):**
    $$H(n) = 2H(n-1) + 1 \quad \text{โดยที่ } H(1) = 1$$
    ผลเฉลยปิด (Closed-form Solution):
    $$H(n) = 2^n - 1$$
    *(คำนวณหาจำนวนครั้งที่น้อยที่สุดในการย้ายแผ่นจาน $n$ แผ่น)*
  - **ขั้นตอนวิธีแบบแบ่งแยกและเอาชนะ (Divide and Conquer Algorithm):**
    1. ย้ายแผ่นจาน $n-1$ แผ่นจากเสาต้นทางไปยังเสาพัก
    2. ย้ายแผ่นจานที่ใหญ่ที่สุดแผ่นที่ $n$ ไปยังเสาปลายทาง
    3. ย้ายแผ่นจาน $n-1$ แผ่นจากเสาพักไปยังเสาปลายทาง
  - **กราฟิกและการโต้ตอบ (Interactive GUI & Multi-threading):**
    - พัฒนาด้วย **Java Swing & AWT** แสดงภาพเสา (Pegs) และจาน (Disks) สีสันชัดเจน
    - รองรับทั้งโหมดผู้เล่นย้ายจานเอง (Manual Play) และโหมดแก้ปัญหาอัตโนมัติ (Auto Solve Animation) ผ่าน Background Thread (`Runnable`)

---

## 🛠️ ขั้นตอนการคอมไพล์และการรัน (Compilation & Execution)

### ความต้องการของระบบ (Prerequisites)
- **Java Development Kit (JDK):** เวอร์ชัน 8 หรือใหม่กว่า (แนะนำ JDK 17 / JDK 21)

---

### 1. รันโปรแกรม GCD & Diophantine Equation
```bash
javac -d bin GCD/src/GCD.java
java -cp bin gcd.GCD
```

### 2. รันโปรแกรม Infix to Postfix Converter
```bash
javac -d bin IF/src/*.java
java -cp bin pkgif.IF
```

### 3. รันโปรแกรม Prime Number Sieve
```bash
javac -d bin Prime0/src/*.java
java -cp bin prime0.Prime0
```

### 4. รันโปรแกรม Towers of Hanoi (GUI)
```bash
javac -d bin TowersOfHanoi/src/TowersOfHanoi.java
java -cp bin TowersOfHanoi
```

---

## 📚 สรุปความรู้เชิงทฤษฎีที่ได้นำมาประยุกต์ใช้ (Theoretical Concepts Covered)

| หมวดหมู่วิชา | ทฤษฎีและหัวข้อสำคัญที่นำมาใช้ในโค้ด |
| :--- | :--- |
| **Discrete Mathematics** | • Extended Euclidean Algorithm & Bézout's Identity<br>• Linear Diophantine Equations ($ax + by = c$)<br>• Sieve of Eratosthenes & Prime Factorization Boundary ($\sqrt{p}$)<br>• Recurrence Relations ($H(n) = 2H(n-1) + 1 = 2^n - 1$)<br>• Mathematical Induction Proof Concepts |
| **Data Structures & Algorithms** | • Custom Singly Linked List Implementation<br>• Node Pointer Manipulation & Dynamic Node Deletion ($O(1)$)<br>• Custom Stack Data Structure (Push / Pop / IsEmpty)<br>• Expression Parsing & Shunting-yard / Postfix Evaluation<br>• Divide & Conquer Recursive Algorithms<br>• Multi-threading & Java Event-driven GUI Programming |
