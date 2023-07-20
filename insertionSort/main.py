def insertion_sort(array):
    def swap(i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    for i in range(1, len(array)):
        curr_idx = i
        j = curr_idx - 1
        while j >= 0 and array[j] > array[curr_idx]:
            swap(curr_idx, j, array)
            j -= 1
            curr_idx -=1
    print(array)
    return array

def check_sorted(array, our_sort):
    correct_result = sorted(array)
    return all([our_sort[i] == correct_result[i] for i in range(len(array))])


arr1 = [5, 4, 3, 2, 1]
assert check_sorted(arr1, insertion_sort(arr1)) is True

arr2 = [1, 2, 3, 4, 5]
assert check_sorted(arr2, insertion_sort(arr2)) is True

arr3 = [1, 2, 3, 11, -1, 999, 0, 0, 0, 0, 0, -123123123]
assert check_sorted(arr3, insertion_sort(arr3)) is True

arr3 = []
assert check_sorted(arr3, insertion_sort(arr3)) is True
