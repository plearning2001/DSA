def count_paths(rows, cols):
    dp = [[1 for _ in range(cols)] for _ in range(rows)]

    for row in dp:
        print(row)
    print() 

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

            for row in dp:
                print(row)
            print()            

    # Print DP grid (for debugging)
    for row in dp:
        print(row)
    print()

    return dp[rows-1][cols-1]


count_paths(3, 3)