s= input("Enter DNA sequence:")[::-1]
print(s.translate(str.maketrans({'A': 'T', 'T': 'A' , 'G': 'C', 'C': 'G'})))