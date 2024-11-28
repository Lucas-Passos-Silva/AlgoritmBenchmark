import random

# Define a semente para garantir a mesma sequência de números
random.seed(42)

# Gera um array fixo de 100.000 de elementos aleatórios
data = [random.randint(0, 100000) for _ in range(100_000)]

# Salva o array gerado em um arquivo para usar em outras linguagens
file_path = "array_data.txt"
with open(file_path, "w") as file:
    file.write(" ".join(map(str, data)))

file_path
