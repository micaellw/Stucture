# Computer Science & Applied Algorithms Monorepo
**คลังรวบรวมโครงงานเชิงวิชาการ การพัฒนาโครงสร้างข้อมูล และการทดลองอัลกอริทึมประสิทธิภาพสูง**

---

## 📌 ภาพรวมคลังโปรเจกต์ (Repository Overview)

Repository นี้เป็นพื้นที่รวบรวมองค์ความรู้ โครงงานทางวิชาการ (Academic Projects) และการศึกษาค้นคว้าด้วยตนเอง (Self-Directed Learning) ด้าน **วิทยาการคอมพิวเตอร์ (Computer Science)** โดยครอบคลุมตั้งแต่โครงสร้างข้อมูลระดับพื้นฐาน การคำนวณทางคณิตศาสตร์ไม่ต่อเนื่อง รหัสวิทยา ไปจนถึงการเพิ่มประสิทธิภาพโมเดลการเรียนรู้ของเครื่อง (Machine Learning Optimization)

---

## 🗺️ แผนผังและสารบัญโปรเจกต์หลัก (Project Index & Navigation)

```
Stucture/ (Workspace Root)
│
├── 🤖 AI_Model_testing/           # 1. Machine Learning: Hybrid BPSO Feature Selection & Benchmarking
├── ☕ Java-Algorithms/             # 2. Discrete Math & Data Structures: Custom Linked List, Stack & GUI
├── 🐍 python-algorithm-practice/  # 3. Self-Study Problem Solving: Hashing O(n), Clean Code & Basic Ciphers
└── 🔐 Cryptography/               # 4. Information Security: Applied Quadratic Affine Cipher & Key Derivation
```

---

## 📂 รายละเอียดและวัตถุประสงค์ของแต่ละโปรเจกต์ (Project Summaries)

| โฟลเดอร์โปรเจกต์ | รายวิชา / บริบท | ภาษา & เทคโนโลยี | ไฮไลท์และผลงานสำคัญ |
| :--- | :--- | :--- | :--- |
| [**`AI_Model_testing/`**](AI_Model_testing/README.md) | **Machine Learning** & Computational Intelligence | `Python`, `C++17`, `Pybind11`, `Scikit-Learn`, `Seaborn` | • การคัดเลือกคุณลักษณะด้วย **Binary Particle Swarm Optimization (BPSO)**<br>• พิสูจน์ความเร็ว C++ Multi-threading เหนือกว่า Pure Python ถึง **70x – 500x+**<br>• ศึกษามิติ **Accuracy vs Inference Latency Trade-off** ของโมเดล AI (KNN, SVM, RF, DT)<br>• ระบบ Render กราฟ Dashboard วิเคราะห์เชิงลึกอัตโนมัติ (300 DPI) |
| [**`Java-Algorithms/`**](Java-Algorithms/README.md) | **Discrete Mathematics** & **Data Structures** | `Java (JDK 17+)`, `Java Swing / AWT` | • **GCD / Linear Diophantine Equation:** แก้สมการ $ax + by = c$ ด้วย Extended Euclidean<br>• **IF (Expression Parsing):** สร้าง **Stack Linked List** จากศูนย์ แปลง Infix $\rightarrow$ Postfix<br>• **Prime0:** ตะแกรงเอราทอสเทนีสผ่านการตัดโหนด Singly Linked List ($O(1)$ Re-linking)<br>• **Towers of Hanoi:** พิสูจน์ความสัมพันธ์เวียนเกิด $2^n - 1$ พร้อม Interactive GUI Animation |
| [**`python-algorithm-practice/`**](python-algorithm-practice/README.md) | **Self-Study** (LeetCode & Problem Solving) | `Python 3.11+` | • การลดความซับซ้อนจาก $O(n^2)$ สู่ **$O(n)$ HashMap Optimization** (Two Sum, Anagrams)<br>• การสร้าง Frequency Counter จากศูนย์โดยไม่พึ่ง Library สำเร็จรูป<br>• การประยุกต์ **Clean Code Principles:** Guard Clauses, Data Sanitization, Defensive Programming |
| [**`Cryptography/`**](Cryptography/README.md) | **Cryptography** & Information Security | `Python 3.11+`, `Modular Arithmetic` | • การสร้างกุญแจ Affine Cipher จากรากของสมการกำลังสอง (**Quadratic Key Derivation**)<br>• การตรวจสอบเงื่อนไขจำนวนเฉพาะสัมพัทธ์ $\gcd(a, 26) = 1$ และการหา Modular Inverse ($a^{-1}$)<br>• แผนผังการศึกษา Classical Ciphers, Symmetric (AES/DES), และ Asymmetric Cryptography (RSA) |

---

## 🛠️ ความต้องการและการติดตั้งระบบ (Environment Setup)

### 1. ความต้องการของระบบ (Prerequisites)
- **Python:** 3.11 ขึ้นไป
- **Java:** JDK 17 หรือใหม่กว่า
- **C++ Compiler:** MSVC (Visual Studio 2022 บน Windows) หรือ GCC/Clang บน Linux

### 2. การติดตั้ง Dependencies สำหรับโปรเจกต์ Python
```bash
# ติดตั้งไลบรารีที่จำเป็นสำหรับ Machine Learning & Benchmarking
cd AI_Model_testing
pip install -r requirements.txt
cd ..
```

### 3. การคอมไพล์โมดูล C++ ในส่วน Machine Learning
```bash
cd AI_Model_testing/ML/SetUp
python setup.py build_ext --inplace
cd ../../..
```

---

## 🚀 สรุปคำสั่งสำหรับการรันแต่ละส่วน (Quick Start)

### 🤖 1. รันส่วน Machine Learning Benchmark
```bash
# รันการทดสอบเปรียบเทียบ BPSO ทั่วไป
python AI_Model_testing/index.py

# รัน Benchmark เชิงสถิติเต็มรูปแบบพร้อมสร้างกราฟความละเอียดสูง
python AI_Model_testing/benchmark_comparison.py
```

### ☕ 2. รันส่วน Java Algorithms & Data Structures
```bash
# คอมไพล์และรัน Towers of Hanoi (GUI)
javac -d bin Java-Algorithms/TowersOfHanoi/src/TowersOfHanoi.java
java -cp bin TowersOfHanoi

# คอมไพล์และรัน Infix to Postfix Parser
javac -d bin Java-Algorithms/IF/src/*.java
java -cp bin pkgif.IF
```

### 🐍 3. รันส่วน Python Algorithm Practice
```bash
python python-algorithm-practice/hashing/two_sum_hashmap.py
python python-algorithm-practice/mini_projects/character_status_generator.py
```

### 🔐 4. รันส่วน Applied Cryptography
```bash
python Cryptography/applied_affine_quadratic.py
```

---

## 📚 สรุปแนวคิดทางวิทยาการคอมพิวเตอร์ที่ครอบคลุมใน Repository นี้

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    Computer Science Knowledge Areas                     │
├──────────────────────────┬──────────────────────────┬───────────────────┤
│    Machine Learning      │   Data Structures & Math │    Cryptography   │
├──────────────────────────┼──────────────────────────┼───────────────────┤
│ • Swarm Intelligence     │ • Linked List / Pointers │ • Classical Cipher│
│ • Fisher Score Criterion │ • Stack (LIFO Parsing)   │ • Modular Inverse │
│ • Multi-threading (C++)  │ • Diophantine Equations  │ • Quadratic Roots │
│ • Accuracy vs Latency    │ • Recurrence Relations   │ • Key Derivation  │
│ • Model Evaluation       │ • Sieve of Eratosthenes  │ • Coprime Rules   │
└──────────────────────────┴──────────────────────────┴───────────────────┘
```
