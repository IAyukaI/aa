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
    quick_sorted = quick_sort(numbers)
    quick_time = time.time() - start
    write_numbers("quick_sorted.txt", quick_sorted)

    print(f"Czas sortowania quick: {quick_time:.6f} sekundy")

else:
    print("Brak liczb.")
