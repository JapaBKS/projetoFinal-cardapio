cardapio = {
    'Bebidas': {
        'Refrigerantes': [
            {'Nome': 'Coca-Cola', 'Preço': 6},
            {'Nome': 'Pepsi', 'Preço': 6},
            {'Nome': 'Guaraná Jesus', 'Preço': 6},
            {'Nome': 'Fanta Uva', 'Preço': 6}
        ],
        'Alcoólicos': [
            {'Nome': 'Vinho', 'Preço': 60},
            {'Nome': 'Whiskey', 'Preço': 35},
            {'Nome': 'Gin Tônica', 'Preço': 35},
            {'Nome': 'Drinks', 'Preço': 30}
        ],
        'Sucos': [
            {'Nome': 'Abacaxi', 'Preço': 15},
            {'Nome': 'Maracujá', 'Preço': 15},
            {'Nome': 'Limão', 'Preço': 15},
            {'Nome': 'Laranja', 'Preço': 15},
            {'Nome': 'Manga', 'Preço': 15}
        ],
        'Quentes': [
            {'Nome': 'Expresso', 'Preço': 5},
            {'Nome': 'Capuccino', 'Preço': 10},
            {'Nome': 'Mocaccino', 'Preço': 12},
            {'Nome': 'Café Com Leite', 'Preço': 7},
            {'Nome': 'Achocolatado', 'Preço': 10},
            {'Nome': 'Chá', 'Preço': 7}
        ]
    },
    'Entradas': {
        'Vegetarianas': [
            {'Nome': 'Salada', 'Preço': 30},
            {'Nome': 'Batatas Fritas', 'Preço': 30},
            {'Nome': 'Polenta', 'Preço': 25}
        ],
        'Com Derivados De Animais': [
            {'Nome': 'Carpaccio', 'Preço': 50},
            {'Nome': 'Creme De Aipim Com Bacon', 'Preço': 35},
            {'Nome': 'Iscas De Peixe', 'Preço': 40},
            {'Nome': 'Carne De Onça', 'Preço': 35}
        ]
    },
    'Pratos Principais': {
        'Vegetarianas': [
            {'Nome': 'Macarrão Alho E Óleo', 'Preço': 45},
            {'Nome': 'Ratatouille', 'Preço': 60},
            {'Nome': 'Macarrão Ao Molho 4 Queijos', 'Preço': 45},
            {'Nome': 'Lasanha Com Carne De Soja', 'Preço': 50}
        ],
        'Com Derivados De Animais': [
            {'Nome': 'Carré De Cordeiro', 'Preço': 85},
            {'Nome': 'Bife À Parmegiana', 'Preço': 65},
            {'Nome': 'Estrogonofe', 'Preço': 45},
            {'Nome': 'Costelinha Barbecue', 'Preço': 70}
        ]
    },
    'Sobremesas': {
        'Com Lactose': [
            {'Nome': 'Petit Gâteau', 'Preço': 28},
            {'Nome': 'Pudim', 'Preço': 22},
            {'Nome': 'Banana Split', 'Preço': 25},
            {'Nome': 'Torta De Limão', 'Preço': 15}
        ],
        'Sem Lactose': [
            {'Nome': 'Gelatina', 'Preço': 10},
            {'Nome': 'Salada De Frutas', 'Preço': 25},
            {'Nome': 'Crumble De Maçã', 'Preço': 35},
            {'Nome': 'Brigadeiro Vegano', 'Preço': 15}
        ]
    }
}

def adicionar_item_cardapio():
    categoria = input("Digite a categoria (Bebidas/Entradas/Pratos Principais/Sobremesas): ").capitalize()
    if categoria in cardapio:
        subcategoria = input(f"Digite a subcategoria ({'/'.join(cardapio[categoria].keys())}): ").capitalize()
        if subcategoria in cardapio[categoria]:
            nome = input(f"Digite o nome do item: ")
            preco = float(input(f"Digite o preço do item: "))
            cardapio[categoria][subcategoria].append({'Nome': nome, 'Preço': preco})
        else:
            print("Subcategoria inválida.")
    else:
        print("Categoria inválida.")

def remover_item_cardapio():
    categoria = input("Digite a categoria (Bebidas/Entradas/Pratos Principais/Sobremesas): ").capitalize()
    if categoria in cardapio:
        subcategoria = input(f"Digite a subcategoria ({'/'.join(cardapio[categoria].keys())}): ").capitalize()
        if subcategoria in cardapio[categoria]:
            nome = input("Digite o nome do item a ser removido: ")
            item_encontrado = False
            for item in cardapio[categoria][subcategoria]:
                if item['Nome'].lower() == nome.lower():
                    cardapio[categoria][subcategoria].remove(item)
                    item_encontrado = True
                    print("Item removido com sucesso.")
                    break
            if not item_encontrado:
                print("Item não encontrado.")
        else:
            print("Subcategoria inválida.")
    else:
        print("Categoria inválida.")

def substituir_item_cardapio():
    categoria = input("Digite a categoria (Bebidas/Entradas/Pratos Principais/Sobremesas): ").capitalize()
    if categoria in cardapio:
        subcategoria = input(f"Digite a subcategoria ({'/'.join(cardapio[categoria].keys())}): ").capitalize()
        if subcategoria in cardapio[categoria]:
            nome = input("Digite o nome do item a ser substituído: ")
            item_encontrado = False
            for item in cardapio[categoria][subcategoria]:
                if item['Nome'].lower() == nome.lower():
                    novo_nome = input("Digite o novo nome do item: ")
                    novo_preco = float(input("Digite o novo preço do item: "))
                    item['Nome'] = novo_nome
                    item['Preço'] = novo_preco
                    item_encontrado = True
                    print("Item substituído com sucesso.")
                    break
            if not item_encontrado:
                print("Item não encontrado.")
        else:
            print("Subcategoria inválida.")
    else:
        print("Categoria inválida.")

def buscar_item_cardapio():
    termo = input("Digite o nome do item que deseja buscar: ").lower()
    resultados = []
    for categoria, subcategorias in cardapio.items():
        for subcategoria, itens in subcategorias.items():
            for item in itens:
                if termo in item['Nome'].lower():
                    resultados.append({'Categoria': categoria, 'Subcategoria': subcategoria, 'Nome': item['Nome'], 'Preço': item['Preço']})
    if resultados:
        print(f"\nResultados encontrados para '{termo}':")
        for resultado in resultados:
            print(f"Categoria: {resultado['Categoria']}, Subcategoria: {resultado['Subcategoria']}, Nome: {resultado['Nome']}, Preço: {resultado['Preço']}")
    else:
        print(f"Nenhum item encontrado para '{termo}'.")

def mostrar_cardapio():
    print("\nCardápio Completo:")
    for categoria, subcategorias in cardapio.items():
        print(f"\nCategoria: {categoria}")
        for subcategoria, itens in subcategorias.items():
            print(f"  Subcategoria: {subcategoria}")
            for item in itens:
                print(f"    Nome: {item['Nome']}, Preço: {item['Preço']}")

def salvar_cardapio_em_arquivo(cardapio, Cardapio_txt):
    with open(Cardapio_txt, "w", encoding="utf-8") as arquivo:
        for categoria, subcategorias in cardapio.items():
            arquivo.write(f"Categoria: {categoria}\n")
            for subcategoria, itens in subcategorias.items():
                arquivo.write(f"  Subcategoria: {subcategoria}\n")
                for item in itens:
                    arquivo.write(f"    Produto: {item['Nome']}, Preço: R${item['Preço']:.2f}\n")
            arquivo.write("\n")

print('Bem-vindo ao ABCDP Coffee')
while True:
    escolha = input('Digite 0 para sair \n'
                    'Digite 1 para Adicionar um item ao cardápio\n' 
                    'Digite 2 para remover um item do cardápio\n'
                    'Digite 3 para alterar um item do cardápio\n'
                    'Digite 4 para buscar um item do cardápio\n'
                    'Digite 5 para ver o cardápio:\n')
    if escolha == '1':
        adicionar_item_cardapio()
    elif escolha == '2':
        remover_item_cardapio()
    elif escolha == '3':
        substituir_item_cardapio()
    elif escolha == '4':
        buscar_item_cardapio()
    elif escolha == '5':
        mostrar_cardapio()
    elif escolha == '0':
        print('Você saiu.')
        break
    else:
        print("Escolha inválida. Tente novamente.")

salvar_cardapio_em_arquivo(cardapio, "cardapio.txt")
print("Cardápio salvo em 'cardapio.txt'")
