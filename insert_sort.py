import time

# Função de ordenação Insert Sort
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Leitura do arquivo gerado pelo script anterior
file_path = "array_data.txt"
with open(file_path, "r") as file:
    data = list(map(int, file.read().split()))


# Mede o tempo de execução do Insert Sort
start_time = time.time()
insert_sort(data)
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.2f} segundos")
