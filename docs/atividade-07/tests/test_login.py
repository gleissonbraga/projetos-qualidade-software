from pages.login_page import LoginPage
import time

def test_login_com_sucesso(page):

    login = LoginPage(page)

    login.acessar()

    login.realizar_login(
        "nataliamorandirm@gmail.com",
        "JanD41@()"
    )

    assert login.login_sucesso_visivel()