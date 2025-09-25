# Exercício 1: Dada a lista abaixo, filtre apenas os números pares
numeros = [3, 8, 12, 5, 9, 20, 22]
# saída esperada: [8, 12, 20, 22]

def filtrar_pares(numeros: list) -> list:
    numeros_filtrados = []
    for i in numeros:
        if i%2 == 0:
            numeros_filtrados.append(i)
        print(numeros_filtrados)


# Exercício 2: Crie um dicionário com o quadrado de cada número de 1 a 5
# saída esperada: {1:1, 2:4, 3:9, 4:16, 5:25}
def calcular_quadrado() -> dict:
    quadrado_dict = {}
    for i in range(1,5):
        quadrado_dict.update({i:i**2})
        print(i)
        print(quadrado_dict)
    return quadrado_dict

# Exercício 3: Conte quantas vezes cada palavra aparece na lista
palavras = ["gcp", "data", "gcp", "etl", "etl", "etl", "pipeline"]
# saída esperada: {'gcp':2, 'data':1, 'etl':3, 'pipeline':1}

def conta_palavras(palavras_list: list) -> dict:
    qtd_palavras = {}
    for i in palavras:
        if i in qtd_palavras:
            qtd_palavras[i] += 1
        else:
            qtd_palavras.update({i:1})
        print(i)
        print(qtd_palavras)
        return qtd_palavras

# Exercício 04: Inverta uma string (sem usar [::-1])
texto = "engenharia"
# saída esperada: "airahnegne"
def inverter_palavra(palavra: str) -> str:
    palavra_lista = list(palavra)
    palavra_lista.reverse()
    palavra_reverse = ""
    for i in palavra_lista:
        palavra_reverse = palavra_reverse + i
        print(i)
        print(palavra_reverse)
    return palavra_reverse


# Exercício 05: Crie uma lista apenas com os nomes que começam com "A"
nomes = ["Ana", "Amanda", "Bruno", "Carla", "Alfredo"]
# saída esperada: ["Ana", "Amanda", "Alfredo"]
def filtrar_nomes_com_a(lista_nomes: list) -> list:
    nomes_com_a = []
    for i in lista_nomes:
        if i[0] == 'A':
            if i not in nomes_com_a:
                nomes_com_a.append(i)
        print(i)
        print(nomes_com_a)
        return nomes_com_a


# Exercício 06: Dado um dicionário, troque as chaves pelos valores
dicionario = {"a": 1, "b": 2, "c": 3}
# saída esperada: {1: "a", 2: "b", 3: "c"}
def inverter_chave_valor(dicionario: dict) -> dict:
    dict_trocado = {}
    for i in dicionario:
        value = dicionario.get(i)
        dict_trocado.update({value:i})
        print(i)
        print(dict_trocado)


# Exercício 07: Mescle duas listas em um dicionário
chaves = ["nome", "idade", "cidade"]
valores = ["Ana", 25, "São Paulo"]
# saída esperada: {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}

def mesclar_listas(lista_header: list, lista_valores: list) -> dict:
    dict_meclado = {}
    for i in lista_header:
        index_i = chaves.index(i)
        dict_meclado.update({i:lista_valores[index_i]})
        print(i)
        print(dict_meclado)
    return dict_meclado


# Exercício 08: Conte quantas vezes cada letra aparece na string
texto = "banana"
# saída esperada: {"b":1, "a":3, "n":2}

def conta_letras(texto: str) -> dict:
    lista_texto = list(texto)
    dict_texto = {}
    for i in lista_texto:
        if i in dict_texto:
            dict_texto[i] += 1
        else:
            dict_texto.update({i: 1})
        print(i)
        print(dict_texto)
    return dict_texto

# Exercício 09: Remova os valores duplicados da lista
numeros = [1, 2, 2, 3, 4, 4, 5]
# saída esperada: [1, 2, 3, 4, 5]  (ordem não importa)
def filtra_numeros_unicos(numeros: list) -> list:
    lista_numeros_unicos = []
    for i in numeros:
        if i not in lista_numeros_unicos:
            lista_numeros_unicos.append(i)
        print(i)
        print(lista_numeros_unicos)
    return lista_numeros_unicos
    
# Exercício 10: Ordene o dicionário pelas chaves
dados = {"c": 3, "a": 1, "b": 2}
# saída esperada: {"a":1, "b":2, "c":3}

def ordernar_chaves_dict(dados: dict) -> dict:
    lista_chaves = []
    dict_chaves_ordenadas = {}
    for i in dados:
        lista_chaves.append(i)
    lista_chaves.sort()

    for i in lista_chaves:
        valor_chave = dados.get(i)
        dict_chaves_ordenadas.update({i:valor_chave})
    
    print(f'Chaves ordenas: {lista_chaves}')
    print(f'Dict com chaves ordenadas: {dict_chaves_ordenadas}')
    return dict_chaves_ordenadas

