from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


def test_checkout_fluxo(page):

    login = LoginPage(page)
    checkout = CheckoutPage(page)

    login.acessar()
    login.realizar_login(
        "nataliamorandirm@gmail.com",
        "JanD41@()"
    )

    checkout.acessar_restaurante()
    checkout.adicionar_item()
    checkout.finalizar_pedido()
    checkout.ver_detalhes()

    assert checkout.pedido_realizado_visivel()