import time

# Função para carregar os dados do arquivo
def load_data(file_path):
    with open(file_path, "r") as file:
        data = list(map(int, file.read().split()))
    return data

# Função de ordenação Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Caminho para o arquivo gerado
file_path = "array_data.txt"

# Carregar os dados do arquivo
data = load_data(file_path)

# Medir o tempo de execução do Selection Sort
start_time = time.time()
selection_sort(data)
end_time = time.time()

# Exibir o tempo total
elapsed_time = end_time - start_time
print(f"Tempo de execução do Selection Sort: {elapsed_time:.2f} segundos")
