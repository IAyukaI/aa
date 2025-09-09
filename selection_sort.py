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


filename = input("Nazwa pliku: ")
numbers = read_numbers(filename)

if numbers:
    start = time.time()
    selection_sorted = selection_sort(numbers)
    selection_time = time.time() - start
    write_numbers("selection_sorted.txt", selection_sorted)

    print(f"Czas sortowania przez wybór:  {selection_time:.6f} sekundy")

else:
    print("Brak liczb.")
