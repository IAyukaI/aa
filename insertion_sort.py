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


filename = input("Nazwa pliku: ")
numbers = read_numbers(filename)

if numbers:
    start = time.time()
    insertion_sorted = insertion_sort(numbers)
    insertion_time = time.time() - start
    write_numbers("insertion_sorted.txt", insertion_sorted)

    print(f"Czas sortowania przez wstawianie: {insertion_time:.6f} sekundy")

else:
    print("Brak liczb.")
