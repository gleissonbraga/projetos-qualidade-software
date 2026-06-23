from pages.login_page import LoginPage
from pages.carrinho_page import CarrinhoPage


def test_adicionar_item_ao_carrinho(page):

    login = LoginPage(page)
    carrinho = CarrinhoPage(page)

    login.acessar()

    login.realizar_login(
        "bragagleisson@gmail.com",
        "86267723"
    )

    carrinho.acessar_restaurante()
    carrinho.adicionar_item()
    carrinho.abrir_carrinho()

    assert carrinho.carrinho_visivel()