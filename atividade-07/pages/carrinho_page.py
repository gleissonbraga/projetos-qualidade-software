class CarrinhoPage:

    def __init__(self, page):
        self.page = page

    def acessar_restaurante(self, nome="Restaurante Sabor 3"):
        self.page.get_by_role("link", name=nome).click()

    def adicionar_item(self):
        self.page.get_by_role("button", name="Adicionar").first.click()

    def abrir_carrinho(self):
        self.page.get_by_role("button", name="Finalizar Pedido").click()

    def carrinho_visivel(self):
        return self.page.get_by_text("Seu Pedido", exact=True).is_visible()