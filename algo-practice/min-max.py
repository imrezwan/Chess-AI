import math


def minimax(nodeIndex, currentDepth, isMaxTurn):
    
    if currentDepth==depth:
        return leafNodes[nodeIndex]


    if isMaxTurn:
        # Trying to maximize value
        #         parentIndex 
        #       /             \
        #  parentIndex*2    parentIndex*2+1

        return max(
            minimax(nodeIndex*2, currentDepth+1, False),  
            minimax(nodeIndex*2+1, currentDepth+1, False)
        )
    else:
        # Trying to minimize value
        return min(
            minimax(nodeIndex*2, currentDepth+1, True), 
            minimax(nodeIndex*2+1, currentDepth+1, True)
        )


# minimax execution
if __name__=='__main__':
    leafNodes = [-1,3,5,1,-6, -4, 0, 9]

    # total_nodes = 2 ^ depth | => log (total_nodes) = depth * log(2) | ==> depth = log (total_nodes) / log(2)
    depth = math.log(len(leafNodes))/math.log(2)
    print(minimax(0,0,True))
