import numpy as np
import pandas as p
import threading 
#,index_col=None, header=None

def lectura():
    i = 0
    vec = np.array([0])
    print(vec)
    # threading.Timer(5.0, lectura).start() 
    
    while True:
        if vec[0] == 0:
            df = p.read_csv('https://docs.google.com/spreadsheets/d/1dVSzbkNbhTfvjSnpQgszYhOvQFjYFDQJYozFNSqPGqE/gviz/tq?tqx=out:csv&sheet=prueba')
            matriz=np.asanyarray(df)
            # vec = np.insert(vec, 0, 1)
            vec = np.insert(vec, 0, len(matriz))
            print("entro primera")
            print(vec)
            i = i + 1
        else:
            if vec[0] > 0:     
                df = p.read_excel('ejemplo2.xlsx')
                matriz=np.asanyarray(df)
                vec = np.insert(vec, i, len(matriz))
                print("esta en la segunda")
                if vec[i] > vec[i-1]:
                    print("si jalo ")
                    print(vec)
            
lectura()

