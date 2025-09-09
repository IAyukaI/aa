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


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    new_arr = []
    p = q = 0

    while p < len(L) and q < len(R):
        if L[p] <= R[q]:
            new_arr.append(L[p])
            p += 1
        else:
            new_arr.append(R[q])
            q += 1

    while p < len(L):
        new_arr.append(L[p])
        p += 1

    while q < len(R):
        new_arr.append(R[q])
        q += 1

    return new_arr


filename = input("Nazwa pliku: ")
numbers = read_numbers(filename)

if numbers:
    start = time.time()
    merge_sorted = merge_sort(numbers)
    merge_time = time.time() - start
    write_numbers("merge_sorted.txt", merge_sorted)

    print(f"Czas sortowania przez scalanie: {merge_time:.6f} sekundy")
else:
    print("Brak liczb.")
