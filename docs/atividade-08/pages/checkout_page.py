class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def acessar_restaurante(self):
        self.page.get_by_role(
            "link",
            name="Restaurante Sabor 2"
        ).click()

    def adicionar_item(self):
        self.page.get_by_role(
            "button",
            name="Adicionar"
        ).first.click()

    def finalizar_pedido(self):
        self.page.get_by_role(
            "button",
            name="Finalizar Pedido"
        ).click()

        self.page.locator("#orderSuccessModal").wait_for(state="visible")

    def pedido_realizado_visivel(self):
        #return self.page.get_by_role("heading", name="Pedido Realizado!").is_visible()
        #return self.page.url.endswith("orders.html")
        #return self.page.get_by_text("Pedido Realizado!").is_visible()
        #print(self.page.content())
        #return True
        return self.page.locator("#orderSuccessModal").is_visible()