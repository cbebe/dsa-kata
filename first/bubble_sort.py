from fem.sort import test_sort


def bubble_sort(arr: list[int]):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


if __name__ == "__main__":
    test_sort(bubble_sort)
    print("OK")
