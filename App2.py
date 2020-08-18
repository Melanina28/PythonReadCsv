import numpy as np
import pandas as p
import threading 
#,index_col=None, header=None

def lectura():
    vec = np.array([0])
    df = p.read_csv('https://docs.google.com/spreadsheets/d/1dVSzbkNbhTfvjSnpQgszYhOvQFjYFDQJYozFNSqPGqE/gviz/tq?tqx=out:csv&sheet=prueba')
    matriz=np.asanyarray(df)
    print(len(matriz))
    vec = np.insert(vec, 1, len(matriz))
    print(vec[1])
    numero =  input()
    df = p.read_csv('https://docs.google.com/spreadsheets/d/1dVSzbkNbhTfvjSnpQgszYhOvQFjYFDQJYozFNSqPGqE/gviz/tq?tqx=out:csv&sheet=prueba')
    matriz=np.asanyarray(df)
    vec = np.insert(vec, 2, len(matriz))
    print(vec)
    if  vec[1] < vec[2]:
        total = vec[2]-vec[1]
        total = int(total * -1) 
        print(total)
        print(matriz[total:,:5])
            
lectura()

