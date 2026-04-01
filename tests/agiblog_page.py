from playwright.sync_api import Page, expect

class AgiBlogPage:
    def __init__(self, page: Page):
        self.page = page
        # Centralizando todos os seletores (Locators) aqui:
        self.btn_lupa = page.locator("#search-open")
        self.campo_busca = page.locator("input.search-field")
        self.msg_nenhum_resultado = page.get_by_text("Nenhum resultado")
        self.titulo_arquivo = page.locator(".archive-title")
        self.menu_item = page.locator("#menu-main-menu .menu-item a")
        self.primeiro_artigo = page.locator("article h2 a")
        self.titulo_artigo = page.locator("h1.entry-title")
        self.logo_agi = page.locator(".site-logo, .site-branding img")

    def acessar_home(self):
        # Usamos "/" porque o pytest.ini já sabe qual é a URL base
        self.page.goto("/", wait_until="networkidle")

    def pesquisar(self, termo):
        self.btn_lupa.first.click()
        self.campo_busca.first.fill(termo)
        self.page.keyboard.press("Enter")

    def clicar_categoria(self):
        self.menu_item.first.click()

    def clicar_primeiro_artigo(self):
        self.primeiro_artigo.first.click()
