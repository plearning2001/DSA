# Find sub sequences of array using recursion
def printF(ind, empty, a, n):
    print(f"Call: printF(ind={ind}, empty={empty})")  # Log the current function call

    if ind >= n:
        # Base case: we've processed all elements, print the subsequence
        print(f"  Base case reached. Subsequence: {empty}")
        print(f"e -- {empty}")
        return

    # Include the current element a[ind] in the subsequence
    print(f"  Including a[{ind}] = {a[ind]} \n")
    empty.append(a[ind])
    printF(ind + 1, empty, a, n)  # Recurse for the next index

    # Backtracking: Exclude the current element a[ind] from the subsequence
    print(f"  Backtracking: Excluding a[{ind}] = {a[ind]} \n")
    empty.pop()
    printF(ind + 1, empty, a, n)  # Recurse for the next index

# Driver code
a = [1, 2, 3]
n = len(a)
empty = []

# Start the recursion from index 0
printF(0, empty, a, n)
