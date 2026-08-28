def find_two_sum_final(arr, target):
    try:
        val = float(target)
        if not val.is_integer():
            return "Error: Target must be an integer."
        tar = int(val)
        
    except ValueError:
        return "Error: Value Type Error (Must be a number)"
    except Exception as e:
        return f"Unknown Error: {e}"

    seen = {}
    
    for index, num in enumerate(arr):
        if not isinstance(num, (int, float)):
             continue
             
        needed = tar - num
        
        if needed in seen:
            return sorted([seen[needed], index]) # sorted เผื่อความสวยงาม
        else:
            seen[num] = index
            
    return "Target not found"