def neutralise(str1,str2):
    s = ""
    z = '0'
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            s+=str1[i]
        else:
            s+=z
    return s