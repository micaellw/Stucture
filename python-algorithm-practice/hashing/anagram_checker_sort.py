def are_anagrams(str1, str2):

    change1=sorted(str1.replace(" ", "").lower())
    change2=sorted(str2.replace(" ", "").lower())

    str1=(change1==change2)


    return str1