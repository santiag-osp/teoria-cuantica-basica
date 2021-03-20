import numpy as np
from numpy import linalg as lin


#sistema cuantico
def posicionprob(vector, posicion):
    var1 = (vector[posicion].real**2+vector[posicion].imag**2)
    var2 = (lin.norm(vector, axis=0))**2
    chance = var1/var2
    return chance

def transitionVector(ket, ket1):
    inter = np.inner(ket1, ket)
    norma1 = lin.norm(ket, axis=0)
    norma2 = lin.norm(ket1, axis=0)
    inner = inter/(norma1*norma2)
    return inner

#retos de programacion

def hermitian(matrix, ket):
    if(matrix == np.conj(np.transpose(matrix))).all():
        matrix1 = np.conj(np.dot(matrix, ket))
        media = np.inner(matrix1, ket)
        matrixM = media * np.identity(len(matrix))
        var = np.dot(matrix - matrixM, matrix - matrixM)
        varianza = np.inner(np.conj(ket), np.dot(var - ket))
        return "varianza = " + varianza, "media =" + media
    else:
        return "la matriz no es hermitiana"

def observablesVarPropios(observable, ket):
    val = lin.eig(observable)
    vectores = lin.eig(observable)
    resp = []
    for objeto in vectores:
        resp += [lin.norm(np.inner(np.conj(ket), lin.norm(objeto, axis=0)))**2]
    return resp

def finalState(ket, matricesUN):
    for objeto in matricesUN:
        ket = np.dot(objeto, ket)
    return ket

#problemas planteados
#problema 4.3.1: Consider a particle in initial spin up. Apply Sx to it and determine
#the probability that the resulting state is still spin up.

def problema1(spins):
    norma = lin.norm(spins, axis=0)
    up = np.dot(spins[0], np.conj(spins[0]))
    prob = up/norma**2
    return prob

#problema 4.3.2 Perform the same calculations as in the last example, using Exercise 4.3.1.
#Then draw the probability distribution of the eigenvalues as in the previous example.



#problema 4.4.1 Verify that are unitary matrices. Multiply them and verify that their product is also unitary.
def problema3(matrix1, matrix2):
    matrix1_ = np.conj(np.transpose(matrix1))
    matrix2_ = np.conj(np.transpose(matrix2))
    uni1 = np.dot(matrix1, matrix1_)
    uni2 = np.dot(matrix2, matrix2_)
    matrix3 = np.dot(matrix1, matrix2)
    matrix3_ = np.conj(np.transpose(matrix3))
    uni3 = np.dot(matrix3, matrix3_)
    return "primera matriz es hermitiana:",np.round(uni1,1), "segunga matriz es hermitiana:", np.round(uni2, 1), "multiplicacion  matriz es hermitiana:", np.round(uni3, 1)

#problema 4.4.2 Go back to Example 3.3.2 (quantum billiard ball), keep the same
#initial state vector [1, 0, 0, 0]T, but change the unitary map to Determine the state of the system
# after three time steps. What is the chance ofthe quantum ball to be found at point 3?

def problema4(matriz, vector):
    n = 0
    while n < 3:
        vector = np.dot(matriz, vector)
        n+= 1
    return vector[2]

#se va a definir un main donde va a mostrar las soluciones de los problemas
#que representamos en python

def main():
    print("1 .primero se va a mostrar la solucion del problema uno")
    print(problema1([complex(3,4), complex(7,2)]))
    print("3. se va a mostrar el tercer problema")
    print(problema3(np.array([[0,1],[1,0]]), np.array([[(2**(1/2))/2,(2**(1/2))/2],[(2**(1/2))/2,(-2**(1/2))/2]])))
    print("4. se va a mostrar el cuarto problema")
    matriz = np.array([[0,1/2,1/2,0],[-1/2,0,0,1/2],[1/2,0,0,-1/2],[0,1/2,1/2,0]])
    vector = np.array([1,0,0,0])
    print(problema4(matriz, vector))
main()