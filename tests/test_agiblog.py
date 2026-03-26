import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect

scenarios('../features/agiblog.feature')

@pytest.fixture(autouse=True)
def setup(page: Page):
    # Dá mais tempo para o site carregar (60 segundos)
    page.set_default_timeout(60000)
    page.set_viewport_size({"width": 1280, "height": 720})

@given('que eu acesso a página inicial do Agiblog')
def abrir_site(page: Page):
    page.goto("https://blogdoagi.com.br/", wait_until="domcontentloaded")

@when('eu clico na lupa de pesquisa')
def clicar_lupa(page: Page):
    # Tenta clicar na lupa pelo ID ou pela classe de busca
    page.locator("#search-open").first.click()

@when('eu digito "empréstimo" no campo de busca')
def digitar_termo(page: Page):
    page.locator("input.search-field").first.fill("empréstimo")

@when('eu digito "termo_inexistente_lux_2026"')
def digitar_termo_inexistente(page: Page):
    page.locator("input.search-field").first.fill("termo_inexistente_lux_2026")

@when('eu pressiono a tecla Enter')
def dar_enter(page: Page):
    page.keyboard.press("Enter")

@when('eu seleciono uma categoria no menu principal')
def selecionar_categoria(page: Page):
    page.locator("#menu-main-menu .menu-item a").first.click()

@when('eu clico no primeiro artigo da lista')
def clicar_artigo(page: Page):
    page.locator("article h2 a").first.click()

@then('o sistema deve exibir resultados relacionados ao termo')
def verificar_resultados(page: Page):
    expect(page.locator(".archive-title")).to_be_visible()

@then('o sistema deve exibir a mensagem "Nenhum resultado"')
def verificar_vazio(page: Page):
    # Busca por qualquer texto que contenha "Nenhum resultado"
    expect(page.get_by_text("Nenhum resultado")).to_be_visible()

@then('a página da categoria deve carregar com sucesso')
def verificar_categoria(page: Page):
    expect(page).not_to_have_url("https://blogdoagi.com.br/")

@then('o título do artigo deve estar visível e legível')
def verificar_titulo_artigo(page: Page):
    expect(page.locator("h1.entry-title")).to_be_visible()

@then('a logomarca do Agi deve estar visível no topo da página')
def verificar_logo(page: Page):
    expect(page.locator(".site-logo, .site-branding img").first).to_be_visible()
