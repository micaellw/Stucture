GCD Calculator (Java)
    Project Overview :
        โปรเจคนี้พัฒนาอัลกอริทึมสำหรับคำนวณ 

        ตัวหารร่วมมากที่สุด (Greatest Common Divisor – GCD)
        ของจำนวนเต็มสองจำนวน

        พัฒนาโดยใช้ภาษา Java 
        โดยใช้แนวคิดทางคณิตศาสตร์ของ Euclidean Algorithm

    แนวคิดของอัลกอริทึม :
        ใช้หลักการว่า:
            gcd(a, b) = gcd(b, a mod b)
            ทำซ้ำจนกว่าเศษจะเป็น 0
            ค่าที่เหลือจะเป็นค่า GCD

        ตัวอย่าง:
            gcd(48, 18)
            = gcd(18, 12)
            = gcd(12, 6)
            = gcd(6, 0)
            = 6

    Algorithm Logic :
        รับค่าจำนวนเต็มสองค่า a และ b
        ถ้า b = 0 → คืนค่า a
        ถ้าไม่ใช่ → เรียก gcd(b, a % b)
        ทำซ้ำจนกว่าจะถึง base case

    Complexity :
        Time Complexity: O(log n) :
            Space Complexity:
                O(log n) (ถ้าใช้ recursion)
                O(1) (ถ้าใช้ iterative)
            Euclidean Algorithm มีประสิทธิภาพสูงมาก
            เมื่อเทียบกับการลองหารทุกค่าทีละตัว

    Technology :
        Java
        Recursion / Iteration
        Mathematical Algorithm Design
        Modular Arithmetic

    จุดประสงค์ของโปรเจค :
        เข้าใจ Euclidean Algorithm
        ฝึกใช้ Recursion
        เข้าใจ Time Complexity แบบ Logarithmic
        ฝึกคิดเชิงคณิตศาสตร์ใน Algorithm

    สิ่งที่โปรเจคนี้สะท้อน :
        เข้าใจการออกแบบ Algorithm เชิง Optimization
        เข้าใจ Mathematical Proof ที่อยู่เบื้องหลัง
        เข้าใจการลด Time Complexity จาก O(n) → O(log n)

    Developer :
        นักศึกษาวิศวกรรมคอมพิวเตอร์และการสื่อสาร