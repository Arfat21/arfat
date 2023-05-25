def selection_sort(arr):
    for i in range (5):
        minpos = i
        for j in range (i,6):
            if arr[j]<=arr(minpos):
                minpos = j
        arr[i],minpos = minpos,arr[i]


arr = [ 3,5,6,7]
selection_sort(arr)
print(arr)
