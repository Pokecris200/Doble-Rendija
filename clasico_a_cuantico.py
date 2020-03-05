from matplotlib import pyplot
import libreria
def potencia (a,b):
    matriz = a
    for i in range (1,b):
        res = libreria.multimat(matriz,a)
        matriz=res
    return matriz

def experimentos(matriz, vector, disparo):
    res1=potencia(matriz,disparo)
    res2=libreria.accion(res1,vector)
    return(res2)
def probabilidad (vector):
    x=[]
    y=[]
    for i in range (len(vector)):
        m=vector[i]
        y=y+[libreria.mod(m[0],m[1])*100]
    for i in range (len(vector)):
        x=x+[i]
    pyplot.title("PROBABILIDAD")
    pyplot.bar(x,height=y)
    pyplot.savefig("experimento.png")
    pyplot.show()
