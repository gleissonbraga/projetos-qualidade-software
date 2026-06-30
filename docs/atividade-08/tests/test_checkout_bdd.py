from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

scenarios("../features/checkout.feature")


@given("que o usuário está na página de login", target_fixture="checkout_ctx")
def abrir_login(page):
    login = LoginPage(page)
    login.acessar()
    return {
        "page": page,
        "login": login,
        "checkout": CheckoutPage(page)
    }


@when("realiza login com credenciais válidas")
def realizar_login(checkout_ctx):
    checkout_ctx["login"].realizar_login(
        "email de alguem do grupo",
        "senha de alguem do grupo"
    )


@when("adiciona um item ao carrinho")
def adicionar_item(checkout_ctx):
    checkout_ctx["checkout"].acessar_restaurante()
    checkout_ctx["checkout"].adicionar_item()


@when("finaliza o pedido")
def finalizar_pedido(checkout_ctx):
    checkout_ctx["checkout"].finalizar_pedido()


@then('o sistema exibe a mensagem "Pedido Realizado!"')
def validar_checkout(checkout_ctx):
    assert checkout_ctx["checkout"].pedido_realizado_visivel()
