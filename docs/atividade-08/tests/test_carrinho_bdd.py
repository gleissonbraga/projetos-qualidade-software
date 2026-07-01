from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage
from pages.carrinho_page import CarrinhoPage


scenarios("../features/carrinho.feature")


@given("que o usuário está logado", target_fixture="carrinho_ctx")
def usuario_logado(page):
    login = LoginPage(page)
    login.acessar()
    login.realizar_login(
        "email de alguem do grupo",
        "senha de alguem do grupo"
    )
    return {"page": page, "carrinho": CarrinhoPage(page)}


@when("acessar um restaurante")
def acessar_restaurante(carrinho_ctx):
    carrinho_ctx["carrinho"].acessar_restaurante()


@when("selecionar um produto")
def selecionar_produto(carrinho_ctx):
    carrinho_ctx["carrinho"].selecionar_produto()


@when("adicionar o produto ao carrinho")
def adicionar_carrinho(carrinho_ctx):
    carrinho_ctx["carrinho"].adicionar_item()


@then("o produto deve aparecer no carrinho")
def validar_produto(carrinho_ctx):
    assert carrinho_ctx["carrinho"].produto_no_carrinho()
