class LoginPage:

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(
            "https://local-eats-unisenac.vercel.app/static/login.html"
        )

    def preencher_email(self, email):
        self.page.get_by_role(
            "textbox",
            name="teste@teste.com"
        ).fill(email)

    def preencher_senha(self, senha):
        self.page.get_by_role(
            "textbox",
            name="Sua senha secreta"
        ).fill(senha)

    def clicar_entrar(self):
        self.page.locator("#loginForm").get_by_role(
            "button",
            name="Entrar"
        ).click()

        self.page.wait_for_url("**/index.html")

    def realizar_login(self, email, senha):
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_entrar()