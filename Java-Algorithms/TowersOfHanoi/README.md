Towers of Hanoi (Java Implementation)
    Project Overview :
        โปรเจคนี้เป็นการพัฒนาอัลกอริทึม Tower of Hanoi
        ด้วยภาษา Java โดยใช้แนวคิดแบบ Recursive Algorithm

        เป็นตัวอย่างคลาสสิกของอัลกอริทึมที่มีการเติบโตแบบ Exponential
        และใช้สอนเรื่อง Recursion และ Big-O ได้อย่างชัดเจน

    แนวคิดของอัลกอริทึม :
        ปัญหา Tower of Hanoi มีเงื่อนไข:
        ย้ายได้ทีละ 1 จาน
        ห้ามวางจานใหญ่บนจานเล็ก
        ต้องย้ายทั้งหมดจากเสาต้นทางไปยังเสาปลายทาง

    Recursive Strategy:
        move(n):
            move(n-1) ไปเสาช่วย
            ย้ายจานที่ n ไปเสาปลายทาง
            move(n-1) ไปทับ

        Mathematical Model :
            Recurrence Relation:
                T(n) = 2T(n-1) + 1
                Closed-form:
                T(n) = 2ⁿ − 1

    Complexity Analysis :
        Time Complexity: O(2ⁿ)
        Space Complexity: O(n) (จาก Call Stack)
        แม้จำนวนการทำงานจะโตแบบ Exponential
        แต่ Memory โตแบบ Linear ตามความลึกของ Recursion

    สิ่งที่โปรเจคนี้สะท้อน :
        เข้าใจ Recursion เชิงโครงสร้าง
        เข้าใจ Recurrence Relation
        เข้าใจ Exponential Growth
        เข้าใจ Call Stack Behavior
        เข้าใจความแตกต่างระหว่าง Time vs Space Complexity

    Technology Used :
        Java
        Recursive Function
        Mathematical Analysis
        Algorithm Design

    จุดประสงค์ของโปรเจค :
        ฝึกคิดเชิง Recursive
        เข้าใจ Big-O แบบ Exponential
        เข้าใจการออกแบบอัลกอริทึมเชิงคณิตศาสตร์
        สร้างพื้นฐานสำหรับ Algorithm ขั้นสูง

    Developer :
        นักศึกษาวิศวกรรมคอมพิวเตอร์และการสื่อสาร

Known Issue :
    ปัจจุบันโปรแกรมมีการใช้ Thread ในส่วนของการทำงาน
    ซึ่งอาจเกินความจำเป็นสำหรับอัลกอริทึมลักษณะนี้

    อย่างไรก็ตาม สำหรับลักษณะของอัลกอริทึมนี้
    การทำงานเป็นแบบ Sequential Recursive Process
    จึงไม่จำเป็นต้องใช้ Multi-threading