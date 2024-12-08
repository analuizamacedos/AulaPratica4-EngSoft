class Supermercado:
    def __init__(self):
        self.carrinho = []

    def adicionar_item(self, item, preco, quantidade):
        if len(self.carrinho) >= 20:
            return "Carrinho cheio! Não é possível adicionar mais itens."
        if quantidade <= 0 or preco <= 0:
            return "Quantidade e preço devem ser maiores que zero."
        self.carrinho.append({"item": item, "preco": preco, "quantidade": quantidade})
        return "Item adicionado com sucesso."

    def total_compra(self):
        return sum(item["preco"] * item["quantidade"] for item in self.carrinho)

    def limpar_carrinho(self):
        self.carrinho = []
        return "Carrinho esvaziado."

    def verificar_carrinho_vazio(self):
        return len(self.carrinho) == 0

    def quantidade_itens(self):
        return len(self.carrinho)

# Função para testes
def realizar_testes():
    mercado = Supermercado()

    # Teste 1: Carrinho vazio no início
    assert mercado.verificar_carrinho_vazio() is True, "Erro: Carrinho deveria estar vazio no início."

    # Teste 2: Adicionar um item
    resultado = mercado.adicionar_item("Maçã", 1.50, 10)
    assert resultado == "Item adicionado com sucesso.", f"Erro ao adicionar item: {resultado}"
    assert mercado.verificar_carrinho_vazio() is False, "Erro: Carrinho não deveria estar vazio."
    assert mercado.quantidade_itens() == 1, "Erro: O carrinho deveria conter 1 item."

    # Teste 3: Adicionar mais itens até o limite
    for i in range(19):  # 19 restantes, totalizando 20
        mercado.adicionar_item(f"Item {i+2}", 2.00, 1)
    assert mercado.quantidade_itens() == 20, "Erro: O carrinho deveria conter 20 itens."
    assert mercado.adicionar_item("Extra", 3.00, 1) == "Carrinho cheio! Não é possível adicionar mais itens."

    # Teste 4: Limpar o carrinho
    mercado.limpar_carrinho()
    assert mercado.verificar_carrinho_vazio() is True, "Erro: Carrinho deveria estar vazio após limpeza."
    assert mercado.quantidade_itens() == 0, "Erro: Carrinho deveria conter 0 itens após limpeza."

    print("Todos os testes passaram!")

# Executar testes
realizar_testes()
