Java Data Structure & Expression Engine :
    Project Overview :
        โปรเจคนี้พัฒนาเพื่อฝึกและแสดงความเข้าใจเกี่ยวกับ :
            Data Structure และ Expression Parsing โดยใช้ภาษา Java

        เน้นการเขียนโครงสร้างข้อมูลด้วยตนเอง :
            โดยไม่พึ่งพา Java Collection Framework

    Modules ภายในโปรเจค :
        Infix → Postfix Converter

    ไฟล์หลัก :
        InFixToPosFix.java
        IF.java

    ระบบทำการแปลงนิพจน์ทางคณิตศาสตร์จากรูปแบบ Infix เช่น :
        (A + B) * C

    ให้เป็น Postfix :
        A B + C *

    แนวคิดที่ใช้ :
        Stack Data Structure
        Operator Precedence
        Parenthesis Handling
        Expression Parsing
        Algorithm Complexity
        Time Complexity: O(n)
        Space Complexity: O(n)

    Postfix Evaluation Engine :
        ไฟล์:
            CalculatePosFix.java :
                ระบบคำนวณค่าจาก Postfix Expression โดยใช้ Stack

                หลักการทำงาน :
                    อ่านนิพจน์ทีละตัว
                    ถ้าเป็นตัวเลข → push ลง Stack
                    ถ้าเป็น operator → pop 2 ค่า
                    คำนวณแล้ว push กลับเข้า Stack
                    ค่าสุดท้ายที่เหลือคือผลลัพธ์

    Linked List Implementation :
        ไฟล์ :
            Linklist.java

        พัฒนา Linked List ด้วยตนเอง โดยประกอบด้วย:
            Node Class
            Insert
            Delete
            Search
            Traversal
            ไม่ได้ใช้ java.util.LinkedList

    ทักษะที่สะท้อนจากโปรเจคนี้ :        
        เข้าใจ Stack เชิงโครงสร้าง
        เข้าใจ Stack จริง ๆ ไม่ใช่แค่เรียกใช้สำเร็จรูป
        เข้าใจ Linked List และ pointer logic
        เข้าใจ Expression Parsing Algorithm
        เข้าใจ Algorithm เชิงโครงสร้าง
        เข้าใจ Operator Precedence และ Associativity
        เขียน Data Structure เองโดยไม่พึ่ง Library สำเร็จรูป
        วิเคราะห์ Time / Space Complexity ได้

    Technology :
        Java
        OOP Concept
        Stack Implementation
        Linked List Implementation
        Expression Evaluation Algorithm

    Objective :
        โปรเจคนี้พัฒนาขึ้นเพื่อ:
            ฝึกคิดเชิงตรรกะ
            เข้าใจ Data Structure เชิงลึก
            เตรียมพื้นฐานสำหรับการเรียน Algorithm ขั้นสูง
            สร้างพื้นฐานที่แข็งแรงสำหรับ Software Development

    Developer :
        นักศึกษาวิศวกรรมคอมพิวเตอร์และการสื่อสาร