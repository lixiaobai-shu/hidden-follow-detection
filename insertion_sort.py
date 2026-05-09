def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)
    insertion_sort(data)
    print("排序后:", data)
