from collections import Counter

def are_anagrams(str1, str2):
    
    change1 = str1.replace(" ", "").lower()
    change2 = str2.replace(" ", "").lower()
 
    return Counter(change1) == Counter(change2)