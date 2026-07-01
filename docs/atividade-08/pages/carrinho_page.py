from playwright.sync_api import Page


class CarrinhoPage:

    def __init__(self, page: Page):
        self.page = page


    def acessar_restaurante(self):
        self.page.get_by_role(
            "link",
            name="Restaurante Sabor 0"
        ).first.click()


    def selecionar_produto(self):
        self.page.get_by_text(
            "Prato Especial 0"
        ).click()


    def adicionar_item(self):
        self.page.get_by_role(
            "button",
            name="Adicionar"
        ).first.click()


    def produto_no_carrinho(self):
        return self.page.get_by_text(
            "Prato Especial 0"
        ).first.is_visible()