import math


def minimax(nodeIndex, currentDepth, isMaxTurn, alpha, beta):
    
    if currentDepth==depth:
        return leafNodes[nodeIndex]


    if isMaxTurn:
        # Trying to maximize value
        #         parentIndex 
        #       /             \
        #  parentIndex*2    parentIndex*2+1

        best = MIN_VAL
        
        for i in range(0,2):
            val =  minimax(nodeIndex*2+i, currentDepth+1, False, alpha , beta) 
            best = max(best, val)
            alpha = max(alpha , best)

            # alpha wants to maximize the value, beta wants to minimize 
            # if alpha>=beta , then there is no chance to change alpha value, so we don't need to look into the other leaf
            if alpha >= beta:
                break
        return best


    else:
        # Trying to minimize value
        worst = MAX_VAL
        
        for i in range(0,2):
            val =  minimax(nodeIndex*2+i, currentDepth+1, True, alpha , beta) 
            worst = min(worst, val)
            beta = min(beta , worst)

            # alpha wants to maximize the value, beta wants to minimize 
            # if alpha>=beta , then there is no chance to change beta value, so we don't need to look into the other leaf
            # that's ALPHA BETA PRUNING
            if alpha >= beta:
                break
        return worst

# minimax execution
if __name__=='__main__':
    leafNodes = [-1,3,5,1,-6, -4, 0, 9]
    MAX_VAL  = math.inf
    MIN_VAL = -math.inf

    # total_nodes = 2 ^ depth | => log (total_nodes) = depth * log(2) | ==> depth = log (total_nodes) / log(2)
    depth = math.log(len(leafNodes))/math.log(2)
    print(minimax(0,0,True, MIN_VAL , MAX_VAL)) 
