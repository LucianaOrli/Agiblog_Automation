from playwright.sync_api import Page

class AgiBlogPage:
    def __init__(self, page: Page):
        self.page = page
        self.btn_lupa = page.locator("#search-open, .search-show, .ast-search-menu-icon").first
        self.campo_busca = page.get_by_placeholder("Pesquisar …")
        self.msg_nenhum_resultado = page.get_by_text("Nenhum resultado", exact=False)

    def acessar_home(self):
        self.page.goto("https://blogdoagi.com.br/")

    def clicar_lupa(self):
        self.btn_lupa.click()

    def realizar_busca(self, termo):
        self.campo_busca.fill(termo)
        self.page.keyboard.press("Enter")

    def clicar_pesquisar_vazio(self):
        self.page.keyboard.press("Enter")
