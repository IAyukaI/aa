import time


def read_numbers(filename):
    try:
        with open(filename) as f:
            return list(map(int, f.read().split()))
    except (FileNotFoundError, ValueError):
        print(f"Error '{filename}'")
        return []


def write_numbers(filename, numbers):
    with open(filename, "w") as f:
        f.write(" ".join(map(str, numbers)))


def selection_sort(arr):
    sorted_arr = arr[:]
    for i in range(len(sorted_arr)):
        min_idx = min(range(i, len(sorted_arr)), key=lambda k: sorted_arr[k])
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr


def bubble_sort(arr):
    sorted_arr = arr[:]
    for i in range(len(sorted_arr)):
        for j in range(len(sorted_arr) - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr


def insertion_sort(arr):
    sorted_arr = arr[:]
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
        j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)





filename = input("Nazwa pliku: ")
numbers = read_numbers(filename)

if numbers:
    start = time.time()
    selection_sorted = selection_sort(numbers)
    selection_time = time.time() - start
    write_numbers("selection_sorted.txt", selection_sorted)

    start = time.time()
    bubble_sorted = bubble_sort(numbers)
    bubble_time = time.time() - start
    write_numbers("bubble_sorted.txt", bubble_sorted)

    start = time.time()
    insertion_sorted = insertion_sort(numbers)
    insertion_time = time.time() - start
    write_numbers("insertion_sorted.txt", insertion_sorted)

    start = time.time()
    quick_sorted = quick_sort(numbers)
    quick_time = time.time() - start
    write_numbers("quick_sorted.txt", quick_sorted)

    print(f"Czas sortowania przez wybór:  {selection_time:.6f} sekundy")
    print(f"Czas sortowania bąbelkowego: {bubble_time:.6f} sekundy")
    print(f"Czas sortowania przez wstawianie: {insertion_time:.6f} sekundy")
    print(f"Czas sortowania quick: {quick_time:.6f} sekundy")

else:
    print("Brak liczb.")
