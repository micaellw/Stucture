def manual_count1(text):
    counts = {}
    
    for char in text: 
        if char in counts:
            counts[char]+=1
        else: 
            counts[char]=1
               
    return counts


def manual_count2(text):
    counts = {}
    for char in text: 
        counts[char] = counts.get(char, 0) + 1
               
    return counts