# Lista com os nomes dos meses
nomes_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
               "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

# Lista para armazenar as temperaturas máximas
temperaturas = []

# Função para validar temperatura
def ler_temperatura():
    while True:
        entrada = input("Digite a temperatura máxima do mês (entre -60°C e 50°C): ")
        entrada = entrada.replace(",", ".")  # Substitui vírgula por ponto
        try:
            temp = float(entrada)
            if -60 <= temp <= 50:
                return temp
            else:
                print("Erro: temperatura fora do intervalo permitido.")
        except ValueError:
            print("Erro: digite um número válido.")

# Coleta de dados
for i in range(12):
    print(f"\n--- Mês {i+1} ({nomes_meses[i].capitalize()}) ---")
    temperatura = ler_temperatura()
    temperaturas.append(temperatura)

# Cálculos
media_anual = sum(temperaturas) / len(temperaturas)
meses_escaldantes = sum(1 for t in temperaturas if t > 33)
indice_max = temperaturas.index(max(temperaturas))
indice_min = temperaturas.index(min(temperaturas))

# Resultados
print("\n===== RESULTADOS =====")
print(f"Temperatura média máxima anual: {media_anual:.2f}°C")
print(f"Quantidade de meses escaldantes (>33°C): {meses_escaldantes}")
print(f"Mês mais escaldante: {nomes_meses[indice_max].capitalize()} ({temperaturas[indice_max]}°C)")
print(f"Mês menos quente: {nomes_meses[indice_min].capitalize()} ({temperaturas[indice_min]}°C)")
