Hybrid BPSO Feature Selection: High-Performance ML Optimization
English Version | ภาษาไทย

🇬🇧 English Version
    Overview :
    This project implements a High-Performance Feature Selection System using Binary 
    Particle Swarm Optimization (BPSO). By leveraging a hybrid architecture of C++ 
    for the core engine and Python for machine learning workflows, 
    the system achieves massive inference speedups 
    while maintaining high predictive accuracy.

    Key Achievements : 
        - 83.3% Data Reduction: Successfully pruned 30 features down to 5 essential features (Indices: 3, 4, 21, 23, 28).
        - Massive Inference Speedup: * SVM: Improved performance by ~327x (0.464s → 0.001s).
        - KNN: Improved performance by ~670x (1.268s → 0.001s).
        - Accuracy Preservation: Maintained a peak accuracy of 96.49% (SVM) even with significantly fewer features.

    System Architecture :
        The system is built on a "Quality over Quantity" philosophy :
            1.Core Engine (C++17): Handles complex PSO calculations, particle updates, and fitness evaluations using Multi-threading (std::thread) and Atomic operations for maximum efficiency.

            2.Fitness Evaluation: Utilizes the Fisher Score criterion combined with a feature ratio penalty to ensure a lean and effective feature subset.
            Fitness = Avg Fisher Score - (0.05 x Feature Ratio)

            3.Python Integration: Seamlessly exposed to Python via Pybind11, allowing standard Scikit-learn models to consume the optimized data.

🇹🇭 ภาษาไทย
    ภาพรวมโปรเจกต์ :
        ระบบคัดเลือกคุณลักษณะ (Feature Selection) ประสิทธิภาพสูงที่ใช้ Binary Particle Swarm Optimization (BPSO) 
        ในการเฟ้นหาชุดข้อมูลที่สำคัญที่สุด โปรเจกต์นี้ชูจุดเด่นด้วยสถาปัตยกรรมแบบ Hybrid (C++/Python) เพื่อดึงพลังการคำนวณสูงสุดจากฮาร์ดแวร์.

    ความสำเร็จหลัก :
        - การลดขนาดข้อมูล: สามารถลดจำนวนคุณลักษณะจาก 30 เหลือเพียง 5 ตัว ที่สำคัญที่สุด.
        - การเพิ่มความเร็ว (Optimization):
            - SVM: ทำงานเร็วขึ้นกว่าเดิม 327 เท่า.
            - KNN: ทำงานเร็วขึ้นกว่าเดิม 670 เท่า.
        - ความแม่นยำ: รักษาค่า Accuracy ไว้ได้ที่ 96.49% แม้จะใช้ข้อมูลลดลงกว่า 80%.
  
    โครงสร้างทางเทคนิค :
        1.Core Engine (C++): พัฒนาส่วนการคำนวณ PSO ด้วย C++ พร้อมระบบการทำงานแบบขนาน (Multi-threading) เพื่อรองรับข้อมูลขนาดใหญ่.
        2.Fitness Function: ใช้เกณฑ์ Fisher Score ในการตัดสินใจเลือกคุณลักษณะ โดยมีบทลงโทษ (Penalty) สำหรับชุดข้อมูลที่ใหญ่เกินไปเพื่อให้ได้ผลลัพธ์ที่กระชับที่สุด.
        3.Python Integration: เชื่อมต่อโมดูล C++ เข้ากับ Python ผ่าน Pybind11 ทำให้ใช้งานร่วมกับโมดูล Machine Learning อื่นๆ ได้ทันที.

Installation & Usage :
    Prerequisites:
        - C++ Compiler (MSVC for Windows / GCC for Linux)
        - Python 3.11+
        - pybind11, numpy, scikit-learn

Building the Extension :
    Compile the C++ Core into a Python-callable module :
        - python setup.py build_ext --inplace

Running the Benchmark :
    Examine the comparison between original and optimized models :
        - python -m index

Project Structure :
    - ML/Computational_Intelligence: C++ Core PSO Engine and Fitness logic.
    - ML/model: Machine Learning model implementations (SVM, KNN, RF, DT).
    - ML/SetUp: Build configurations for the hybrid system.
    - index.py: Main entry point for performance benchmarking.  