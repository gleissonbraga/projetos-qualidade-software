import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
    page.get_by_role("textbox", name="teste@teste.com").click()
    page.get_by_role("textbox", name="teste@teste.com").fill("nataliamorandirm@gmail.com")
    page.get_by_role("textbox", name="teste@teste.com").press("Tab")
    page.get_by_role("textbox", name="Sua senha secreta").fill("JanD41@()")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
    page.get_by_role("link", name="Restaurante Sabor 2").click()
    page.get_by_role("button", name=" Adicionar").first.click()
    page.get_by_role("button", name="Finalizar Pedido").click()
    page.get_by_role("button", name="Ver Detalhes").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)