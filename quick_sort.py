import time

# Função Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Leitura do arquivo gerado
file_path = "array_data.txt"
with open(file_path, "r") as file:
    data = list(map(int, file.read().split()))

# Medir o tempo do Quick Sort
start_time = time.time()
sorted_data = quick_sort(data)
end_time = time.time()

# Resultado
sort_duration = end_time - start_time
sort_duration


print(f"Tempo para ordenar 100.000 de elementos com Quick Sort: {sort_duration:.2f} segundos")
