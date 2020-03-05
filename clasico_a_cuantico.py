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
        y=y+[m[0]*100]
    for i in range (len(vector)):
        x=x+[i]
    pyplot.title("PROBABILIDAD")
    pyplot.bar(x,height=y)
    pyplot.savefig("experimento.png")
    pyplot.show()
v=[(4/5,0),(1/5,0),(0,0),(0,0),(0,0),(0,0)]
d=[(0,0),(0,0),(1/18,0),(1/9,0),(5/18,0),(5/9,0)],[(0,0),(0,0),(1/9,0),(1/18,0),(5/9,0),(5/18,0)],[(1/9,0),(2/9,0),(1/6,0),(1/3,0),(1/18,0),(1/9,0)],[(2/9,0),(1/9,0),(1/3,0),(1/6,0),(1/9,0),(1/18,0)],[(2/9,0),(4/9,0),(1/9,0),(2/9,0),(0,0),(0,0)],[(4/9,0),(2/9,0),(2/9,0),(1/9,0),(0,0),(0,0)]
g=experimentos (d,v,5)
probabilidad (g)

