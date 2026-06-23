class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def acessar_restaurante(self):
        self.page.get_by_role("link", name="Restaurante Sabor 2").click()

    def adicionar_item(self):
        self.page.get_by_role("button", name="Adicionar").first.click()

    def finalizar_pedido(self):
        self.page.get_by_role("button", name="Finalizar Pedido").click()

    def ver_detalhes(self):
        self.page.get_by_role("button", name="Ver Detalhes").click()

    def pedido_realizado_visivel(self):
        return self.page.get_by_role("heading", name="Pedido Realizado!")