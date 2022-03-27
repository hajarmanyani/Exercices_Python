"Triangle Pascal"
def Pascal(rows):
    lsp=[1]
    print(lsp)
    for i in range(1,rows):
        lsn=lsp+[1]
        for j in range(len(lsp)-1):
            lsn[j+1]=lsp[j]+lsp[j+1]
        lsp=lsn
        print(lsn,"\n")

"Test"
nrows=int(input("Donner le nombre de lignes maximal"))
Pascal(nrows)