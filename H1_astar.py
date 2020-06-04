import numpy as np
########################### Solving 8 puzzle by Heuristics ###########################

####### Intiating States ######

Start = [[1,2,3],[4,0,6], [7,5,8]]
Goal =  [[1,2,3],[4,5,6],[7,8,0]]

####### Input to function #########

node_s = np.array([Start,0,0])    # [x,f,g] # x= matrix of node # f = heuristics # g = depth
node_f = np.array([Goal])

####### h1 calculating misplaced tiles #########
def h1(Node):
    current_node = Node.flatten()
    end_node = np.copy(Goal)
    end_node = end_node.flatten()
    h1 = 0
    for i in range (9):
        if current_node[i] != 0:                      # omits to check 0 in current node [1 2 3 4 5 6 7 8 0]
            if current_node[i] != end_node[i]:        # [1 2 3 4 5 6 8 7 0] checks current with goal [1 2 3 4 5 6 7 8 0]
             h1 += 1                                  #condition is true increment h1 by 1
    return h1

####### Defining successor list #######

def suc(Node,depth):
    neighbour = []
    Node = Node[0]
    move = np.array(Node)
    i = 0
    j = 0
    while 0 not in move[i]: i += 1
    j = np.argwhere(move==0)
    j = j.flatten()
    j = j[1]
    if i<2: #move down
        move[i][j], move[i+1][j] = move[i+1][j], move[i][j]    #swap position
        down_list = move.tolist()                              # list of array is created
        heuristics = h1(move) + depth+1                        # heuristics evalution f = h + g calculated
        down_shift = (down_list,heuristics,depth+1)            # (x,f,g) x= matrix of node f = heuristics g = depth
        neighbour.append(down_shift)                           # added to neighbour matrix
        move[i][j], move[i + 1][j] = move[i + 1][j], move[i][j] #swap back to origianl positon
    if i > 0: #move up
        move[i][j], move[i-1][j] = move[i-1][j], move[i][j]
        up_list = move.tolist()
        heuristics = h1(move) + depth+1
        up_shift = (up_list,heuristics,depth+1)
        neighbour.append(up_shift)
        move[i][j], move[i - 1][j] = move[i - 1][j], move[i][j]
    if j<2: #move Right
        move[i][j], move[i][j+1] = move[i][j+1], move[i][j]
        right_list = move.tolist()
        heuristics = h1(move) + depth+1
        right_shift = (right_list,heuristics,depth+1)
        neighbour.append(right_shift)
        move[i][j], move[i][j+1] = move[i][j+1], move[i][j]
    if j>0: #move Left
        move[i][j], move[i][j-1] = move[i][j-1], move[i][j]
        left_list = move.tolist()
        heuristics = h1(move) + depth+1
        left_shift =(left_list,heuristics,depth+1)
        neighbour.append(left_shift)
        move[i][j], move[i][j - 1] = move[i][j - 1], move[i][j]
    return neighbour

############ Main Function ##############

def Astar (Start,Goal):
    NodeList = [Start]
    depth = 0
    path = []
    while True:
        if NodeList == []:
            print('NO solution')
            return "No solution"

        Node = NodeList[0]
        path.append(Node[0])
        path1 = np.array(path)
        depth = NodeList[0][2]
        NodeList =NodeList[1:]
        comparison = Node[0] == Goal                      #comparison returns[[t t f],[t t f],[t t t]]
        if comparison.all() == True:                      # When all comparison is true solution printed
            print('Solution found', Node)
            print('Solution found at depth',depth)
            print('path', path1)
            return
        elif comparison.all() != True :
            current_list = suc(Node,depth)
            current_list = current_list + NodeList
            NodeList = sorted(current_list,key=lambda x:x[1]) #sorting the list on ascending order based on heuristics value

Astar(node_s,node_f) #Execution command
