# Initial values of Alpha and Beta
import math

MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta, target_depth):
    if depth == target_depth:
        return values[nodeIndex]

    if maximizingPlayer:

        best = MIN

        # Recur for left and right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, target_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        # Recur for left and
        # right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          True, values, alpha, beta, target_depth)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

values = []
n = int(input("Enter no of leaf nodes : "))
for i in range(n):
    values.append(int(input("enter node value : ")))


target_depth = math.log(n, 2)
print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX, target_depth))
