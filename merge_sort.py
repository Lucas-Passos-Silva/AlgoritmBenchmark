import time

# Função de Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive sorting
        merge_sort(left_half)
        merge_sort(right_half)

        # Merging the halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Carregar o arquivo gerado
file_path = "array_data.txt"
with open(file_path, "r") as file:
    data = list(map(int, file.read().split()))

# Medir o tempo de execução do Merge Sort
start_time = time.time()
merge_sort(data)
end_time = time.time()

# Tempo de execução
execution_time = end_time - start_time
execution_time

print(f"Tempo para ordenar 100.000 de elementos com Merge Sort: {execution_time:.2f} segundos")