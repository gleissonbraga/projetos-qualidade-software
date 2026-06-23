from pages.login_page import LoginPage


def test_login_com_credenciais_invalidas(page):

    login = LoginPage(page)

    login.acessar()

    login.realizar_login(
        "natalia@gmail.com",
        "JanD41@()"
    )

    page.get_by_text("Invalid credentials").wait_for()

    assert page.get_by_text(
        "Invalid credentials"
    ).is_visible()