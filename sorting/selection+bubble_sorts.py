def selection_sort(arr):
         if not arr or len(arr) < 2:
         return arr
    for i in range(len(arr)):
         min_i = i
         for j in range(i + 1, len(arr)):
              if arr[j] < arr[min_i]:
                  min_i = j
         arr[i], arr[min_i] = arr[min_i], arr[i]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
