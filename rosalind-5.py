def hamming():
    s= input("Enter DNA sequence 1:")
    t= input("Enter DNA sequence 2:")
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return print(count)


hamming()