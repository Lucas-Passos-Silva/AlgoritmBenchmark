import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Sai do loop se não houve trocas (já está ordenado)

# Caminho do arquivo com os dados
file_path = "array_data.txt"

# Lê o array do arquivo
with open(file_path, "r") as file:
    data = list(map(int, file.read().strip().split()))

# Cronometrando o tempo
start_time = time.time()

# Ordenação
bubble_sort(data)

end_time = time.time()

print(f"Tempo para ordenar 100.000 de elementos com Bubble Sort: {end_time - start_time:.2f} segundos")
