def ordenar_numeros(n):
    return (n % 2, -n if n % 2 else n)

N = int(input())

numeros = []

for _ in range(N):
    numeros.append(int(input()))

numeros.sort(key=ordenar_numeros)

for num in numeros:
    print(num)
