import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import ML.SetUp.Main_CI as Main_CI

def prepare_Data_universal(file_path=None, sklearn_dataset=None, target_col=None):
 
    # โหลดข้อมูลและทิ้งค่าว่าง
    if sklearn_dataset is not None:
        # กรณีที่:รับข้อมูลมาจาก sklearn datasets
        # แปลง data เป็น DataFrame เพื่อให้เข้ากระบวนการต่อไปได้
        X_raw = pd.DataFrame(sklearn_dataset.data)
        
        # ใส่ชื่อคอลัมน์ให้สวยงาม (ถ้ามี)
        if hasattr(sklearn_dataset, 'feature_names'):
            X_raw.columns = sklearn_dataset.feature_names
            
        y_raw = pd.Series(sklearn_dataset.target)

    elif file_path is not None:
        df = pd.read_csv(file_path)
        df = df.dropna()
        # ค้นหาคอลัมน์เป้าหมาย (y)
        # ถ้าไม่ได้ระบุชื่อคอลัมน์มา ให้ดึงคอลัมน์สุดท้ายเป็น y อัตโนมัติ
        if target_col is None:
            target_col = df.columns[-1] 
        
        X_raw = df.drop(columns=[target_col]).copy() # แยก Features
        y_raw = df[target_col].copy()                # แยก Label
    
    else:
        # ถ้าไม่ใส่อะไรมาเลยให้แจ้งเตือน
        raise ValueError("❌ ต้องระบุ file_path หรือ sklearn_dataset อย่างใดอย่างหนึ่ง!")

    # เช็ค Type ทีละคอลัมน์ใน X
    for col in X_raw.columns:
        # ถ้าคอลัมน์นั้นเป็น 'object' (ข้อความ) หรือ 'category'
        if X_raw[col].dtype == 'object' or X_raw[col].dtype.name == 'category':
            le = LabelEncoder()
            X_raw[col] = le.fit_transform(X_raw[col])
        else:
            # ถ้าเป็นตัวเลข (int, float) อยู่แล้ว โปรแกรมจะข้ามไปอัตโนมัติ
            pass

    #แปลง y ให้เป็น 0 กับ 1 เสมอ
    y_encoded = LabelEncoder().fit_transform(y_raw)

    #ปรับสเกลให้ตัวเลขทุกคอลัมน์มีมาตรฐานเดียวกัน (Mean=0, SD=1)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_raw)

    
    return X_scaled, y_encoded
