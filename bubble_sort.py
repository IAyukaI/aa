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


def bubble_sort(arr):
    sorted_arr = arr[:]
    for i in range(len(sorted_arr)):
        for j in range(len(sorted_arr) - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr


filename = input("Nazwa pliku: ")
numbers = read_numbers(filename)

if numbers:
    start = time.time()
    bubble_sorted = bubble_sort(numbers)
    bubble_time = time.time() - start
    write_numbers("bubble_sorted.txt", bubble_sorted)

    print(f"Czas sortowania bąbelkowego: {bubble_time:.6f} sekundy")

else:
    print("Brak liczb.")
