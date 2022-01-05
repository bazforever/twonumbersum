def twoNumberSum(array, targetSum):
    # Write your code here.
    emptyArray = []

    for i in range(len(array)):
        for y in range(i + 1, len(array)):
            if array[i] + array[y] == targetSum:
                print("The number  is ", array[i], array[y])
            else:
                if array[i] + array[y] != targetSum:
                    pass


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

twoNumberSum(array, targetSum)











