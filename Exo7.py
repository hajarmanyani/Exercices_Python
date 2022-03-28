"""
EXERCICE 7
"""

def binary_int(binary):
    valint,i,a=0,0,0
    while (binary != 0):
        a=binary%10
        valint+=a*pow(2,i)
        binary=binary//10
        i+=1
    print(valint)

print("Le nombre en décimal equivalent est : \t")
binary_int(101)
