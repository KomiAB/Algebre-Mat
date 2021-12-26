g = [[1,2,3,4,5,6,7,8,9,10],[(1,2),(1,6),(3,2),(4,5),(6,5),(6,3),(4,7),(5,4),(5,8),(7,8),(8,10),(8,9),(9,10)]]

def deg(i,g):
    count = 0
    for j in g[1]:
        if j[0] == i or j[1] == i:
            count+=1
    return count

def list_deg(g):
    list = []
    for i in g[0]:
        list.append([i,deg(i,g)])
    list.sort(key=lambda x:x[1])
    list.reverse()
    return list

def adj(i,j,g):
    if (i,j) in g[1] or (j,i) in g[1]:
        return True
    else:
        return False

def coloration(g):
    color = 0
    sommetTraite = 0
    D = list_deg(g)
    n = len(D)
    while sommetTraite < n:
        for i in range(n):
           if len(D[i]) == 2:
               coloPoss = True
               for j in range (i):
                   if len(D[j])==3 and D[j][2] == color and adj(D[i][0],D[j][0],g)==True:
                       coloPoss = False
                       break
               if coloPoss:
                    D[i].append(color)
                    sommetTraite += 1
        color+=1

    print("Nombre de couleurs utilsises :",color)
    print("Sommets ayant la méme couleur :")
    for i in range(color):
        s = "couleur " + str(i) + " : "
        for element in D:
            if element[2] == i:
                s += str(element[0]) + " "
        print(s)
    return ''

print(coloration(g))