from pages.login_page import LoginPage

def test_login_com_senha_vazia(page):

    login = LoginPage(page)

    login.acessar()

    login.preencher_email(
        "nataliamorandirm@gmail.com"
    )

    login.clicar_entrar()

    assert page.url.endswith("login.html")