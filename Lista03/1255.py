def letra_mais_frequente(texto):
    contagem_letras = {}
    
    for caractere in texto:
        if caractere.isalpha():
            caractere_min = caractere.lower()
            contagem_letras[caractere_min] = contagem_letras.get(caractere_min, 0) + 1
    
    max_freq = max(contagem_letras.values())
    
    letras_max_freq = [letra for letra, freq in contagem_letras.items() if freq == max_freq]
    
    letras_max_freq.sort()
    
    print(''.join(letras_max_freq))

num_casos = int(input())

for _ in range(num_casos):
    texto = input()
    
    letra_mais_frequente(texto)
