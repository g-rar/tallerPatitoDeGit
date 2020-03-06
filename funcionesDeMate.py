def mostrarNumero(n=0):
    print(n)

def sumatoria(n, r=0):
    if n == 0:
        return r
    else:
        return sumatoria(n-1, r+n)

def productorio(n, r=0):
    if n == 0:
        return r
    else:
        return productorio(n-1, r*n)

def obtenerPrimerDigito(n):
    return(int(str(n)[0]))

print(obtenerPrimerDigito(82349587))
num = oct(425)
numDec = int(num, 8)
print(numDec)