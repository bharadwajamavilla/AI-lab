SuccList = {'A': [['B', 3], ['C', 2]], 'B': [['D', 2], ['E', 3]], 'C': [['F', 2], [
    'G', 4]], 'D': [['H', 1], ['I', 99]], 'F': [['J', 99]], 'G': [['K', 99], ['L', 3]]}

Start = 'A'
Closed = list()


def Movegen(N):
    new_list = list()
    if N in SuccList.keys():
        new_list = SuccList[N]

    return new_list


def Sort(L):
    L.sort(key=lambda x: x[1])
    return L


def heu(node):
    return node[1]


def Append(L1, L2):
    new_list = list(L1)+list(L2)
    return new_list


def Hill_climb(Start):
    global CLOSED
    N = Start
    child = Movegen
    Sort(child)
    N = [Start, 5]
    print("Start :", N)
    print("Sorted Childlist :", child)
    newNode = child[0]
    CLOSED = [N]

    while heu(newNode) <= heu(N):
        print("********************")
        N = newNode
        print("N :", N)
        CLOSED = Append(CLOSED, [N])
        child = Movegen(N[0])
        Sort(child)
        print("Sorted Child list: ", child)
        print("CLOSED :", CLOSED)
        newNode = child[0]

    Closed = CLOSED


Hill_climb(Start)