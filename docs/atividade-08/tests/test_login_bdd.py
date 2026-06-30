from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage


scenarios("../features/login.feature")


@given("que o usuário está na página de login", target_fixture="login_page")
def abrir_login(page):
    login = LoginPage(page)
    login.acessar()
    return {"page": page, "login": login}


@when("realizar login com usuário válido")
def realizar_login(login_page):
    login_page["login"].realizar_login(
        "email de alguem do grupo",
        "senha de alguem do grupo"
    )


@then("o usuário deve acessar a página inicial")
def validar_login(login_page):
    assert "index" in login_page["page"].url
