# 1

# Função inicial
def filtrar(produtos):
    return [produto for produto in produtos if produto['preco'] > 1000]

# a lista
produtos = [
    {'nome': 'Ovo do faustão', 'preco': 2500},
    {'nome': 'senso do raluca', 'preco': 1200},
    {'nome': 'toalha do dudu camargo', 'preco': 50},
    {'nome': 'filme do faustão', 'preco': 1500},
    {'nome': 'old spice cabra macho', 'preco': 300}
]

# Chamando a função
filtrar2 = filtrar(produtos)

# resultado final
print("Produtos caros:")
for produto in filtrar2:
    print(f"{produto['nome']} - R${produto['preco']}")

# 2

# Função inicial
def contagem1(produtos):
    contagem2 = {}
    
    for produto in produtos:
        categoria = produto['categoria']
        if categoria in contagem2:
            contagem2[categoria] += 1
        else:
            contagem2[categoria] = 1
    
    return contagem2

# Lista de jogos
produtos = [
    {'nome': 'Undertale', 'categoria': 'Indie'},
    {'nome': 'Destiny', 'categoria': 'Triple A'},
    {'nome': 'Omori', 'categoria': 'Indie'},
    {'nome': 'Bloodborne', 'categoria': 'Triple A'},
    {'nome': 'Lobotomy Corporation', 'categoria': 'Indie'},
    {'nome': 'God of War', 'categoria': 'Triple A'}
]

# Função atendendo o chamado
contagem = contagem1(produtos)

# Hora da Verdade
print("Contagem de produtos por categoria:")
for categoria, quantidade in contagem.items():
    print(f"{categoria}: {quantidade} produto(s)")

# 3

pedidos = ['pizza', 'hamburguer', 'macaroni', 'pizza', 'sushi', 'sushi', 'hamburguer']

# Usando set para remover duplicatas
pedidos_unicos = list(set(pedidos))

print(pedidos_unicos)

# 4
