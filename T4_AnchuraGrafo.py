import time
st = time.time()    
from collections import deque

# Definir grafo 
graph = {
    '1': {'2': 7000000,'3': 1500000,'4': 6000000},
    '2': {'1': 7000000,'5': 300000,'6': 9000000,'7': 3500000,'8': 2100000},
    '3': {'1': 1500000, '9': 300000,'10': 1000000},
    '4': {'1': 6000000, '11': 1800000,'12': 3000000,'13': 2100000,'14': 1500000},
    '5': {'2': 300000,'15': 1000000},
    '6': {'2': 9000000,'16': 3700000,'17': 1600000},
    '7': {'2': 3500000,'26': 3700000,'27': 2100000,'28': 1400000,'29': 1200000},
    '8': {'2': 2100000,'39': 1600000,'40': 3000000,'41': 8000000},
    '9': {'3': 30000000,'48': 9000000},
    '10': {'3': 1000000},
    '11': {'4': 18000000},
    '12': {'4': 30000000},
    '13': {'4': 20000001},
    '14': {'4': 15000000},
    '15': {'5': 10000000,'16': 16000000,'17': 50000000},
    '16': {'15': 16000000},
    '17': {'15': 50000000},
    '18': {'6': 37000000,'20': 21000000,'21': 14000000,'22': 12000000},
    '19': {'6': 16000000,'22': 50000000,'23': 30000000,'24': 15000000},
    '20': {'18': 21000000},
    '21':{'18':14000000},
    '22':{'18':12000000},
    '23':{'19':50000000},
    '24':{'19':30000000},
    '25':{'19':15000000},
    '26':{'7':37000000,'30':18000000},
    '27':{'7':21000000,'31':30000000, '32':15000000,'33':18000000},
    '28':{'7':14000000,'34':15000000,'35':10000000},
    '29':{'7':12000000,'37':10000000,'38':80000000},
    '30':{'26':18000000},
    '31':{'27':30000000},
    '32':{'27':15000000},
    '33':{'27':18000000},
    '34':{'28':15000000},
    '35':{'28':10000000},
    '36': {'29':10000000},
    '37': {'29':80000000},
    '38': {'8':16000000,'41':10000000,'42':50000000},
    '39': {'8':30000000,'43':18000000,'44':21000000,'43':15000000},
    '40': {'8':80000000,'46':10000000,'47':12000000},
    '41': {'38':10000000},
    '42': {'38':50000000},
    '43': {'39':18000000},
    '44': {'39':21000000},
    '45': {'39':15000000},
    '46': {'40':10000000},
    '47': {'40':12000000},
    '48': {'9':90000000}
}

#definimos nuestro algoritmo, donde vamos a recibir como parametros:
# 1- que vamos a leer, 2-donde iniciaremos, 3-donde terminaremos
def bfs(graph, start, goal):
    #inicializamos nuestras variables
    queue = deque()
    visited = set()
    distances = {start: 0}
    parents = {start: None}
    total_value = 0
    #esta funcion nos dice que el nodo inicial lo vamos a agregar a la cola exactamente al final
    queue.append(start)
    #despues de agregarlo vamos a marcarlo como leido 
    visited.add(start)

    #mientras nuesta cola tenga nodos para ver
    while queue:
        #Gracias a esta funcion eliminamos este nodo de nuestra cola para visitar
        # y lo vamos a devolver solo que más a la derecha de la cola de visitados
        current = queue.popleft()
 
        #si el sig nodo es nuestro nodo final
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            path.reverse()
            #arroja el camino y el costo total de esta ruta
            return path, total_value
        #en el caso que no sea nuestro nodo final solo lo identifica como nodo vecino
        #ademas de ir contando costo
        for neighbor, value in graph[current].items():
            #si este "nodo vecino" no ha sido visitado o marcado como visitado
            if neighbor not in visited:
                #se va a agregar a la lista/cola correspondiente 
                visited.add(neighbor)
                queue.append(neighbor)
                #se van sumando sus costos
                distances[neighbor] = distances[current] + 1
                # e identificando de que padre viene 
                parents[neighbor] = current
                #agregando dicho valor a nuestra constante que contabiliza el costo de la ruta
                total_value += value

    #nos retornara la lista de estos nodos y el costo total de la ruta
    return [], total_value

start = input("Ingresa el nodo de inicio:") 
goal = input("Ingresa el nodo a buscar: ")

shortest_path, total_value = bfs(graph, start, goal)

if shortest_path:
    print(f"El camino más corto desde {start} hasta {goal} es: {shortest_path}")
    print(f"La suma de los valores de los nodos visitados es: {total_value}")
else:
    print(f"No se encontró un camino desde {start} hasta {goal}.")

print("Process finished --- %s seconds ---" % (time.time()-st))