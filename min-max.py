import math

def Minmax(current_depth, node, max_term, score, total_depth):
    if (current_depth == total_depth):
        return score[node]
    if (max_term):
        return max(Minmax(current_depth + 1, node * 2, False, score, total_depth),
                   Minmax(current_depth + 1, node * 2 + 1, False, score, total_depth))

    else:
        return min(Minmax(current_depth + 1, node * 2, True, score, total_depth),
                   Minmax(current_depth + 1, node * 2 + 1, True, score, total_depth))

score = []
n = int(input("Enter total no of leaf nodes : "))
for i in range(n):
    score.append(int(input("Enter leaf node : ")))

total_depth = math.log(len(score), 2)
current_depth = int(input("Enter current depth value : "))
node_value = int(input("Enter node value : "))
max_term = True

print("The answer is : ", end = " ")
answer = Minmax(current_depth, node_value, max_term, score, total_depth)
print(answer)


