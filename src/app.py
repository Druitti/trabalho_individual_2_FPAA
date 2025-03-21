def maxMinSelect(array, left, right):

    if left == right:
        return array[right], array[right]
    
    if right == left + 1:
        if array[left] > array[right]:
            return array[left], array[right]
        else:
            return array[right], array[left]
    
    mid = (left + right) //2
    max1, min1 = maxMinSelect(array, left, mid)
    max2, min2 = maxMinSelect(array, mid + 1, right)
    
    return max(max1, max2), min(min1, min2)


array = [10,1,4,2,6,3,8,5,7,9]
maxValue, minValue = maxMinSelect(array, 0, len(array)-1)
print(f"Menor valor: {minValue}, Maior valor: {maxValue}")
