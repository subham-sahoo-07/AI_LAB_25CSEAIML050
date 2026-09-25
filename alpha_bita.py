import math

# Alpha-Beta Pruning Function
def alpha_beta_pruning(depth, nodeindex, maximizingplayer, values, alpha, beta, height):
    
    # Base case: leaf node reached
    if depth == height:
        return values[nodeindex]

    if maximizingplayer:
        best = -math.inf

        for i in range(2):
            value = alpha_beta_pruning(
                depth + 1,
                nodeindex * 2 + i,
                False,
                values,
                alpha,
                beta,
                height
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Beta cut-off
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta_pruning(
                depth + 1,
                nodeindex * 2 + i,
                True,
                values,
                alpha,
                beta,
                height
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha cut-off
            if beta <= alpha:
                break

        return best


# Main Program
values = list(map(
    int,
    input("Enter the values of leaf nodes separated by space: ").split()
))

# Check whether number of leaf nodes is valid
if len(values) == 0 or (len(values) & (len(values) - 1)) != 0:
    print("Error: Number of leaf nodes must be a power of 2.")
else:
    # Calculate height automatically
    height = int(math.log2(len(values)))

    result = alpha_beta_pruning(
        0,
        0,
        True,
        values,
        -math.inf,
        math.inf,
        height
    )

    print("The optimal value is:", result)