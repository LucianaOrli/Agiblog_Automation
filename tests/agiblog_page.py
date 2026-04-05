from playwright.sync_api import Page

class AgiBlogPage:
    def __init__(self, page: Page):
        self.page = page
        # Seletor resiliente
        self.btn_lupa = page.locator("#search-open, .search-toggle, [aria-label='Abrir pesquisa']").first
        self.campo_busca = page.locator(".search-field").first 
        self.msg_nenhum_resultado = page.locator(".no-results, .not-found, text='Nenhum resultado'").first

    def acessar_home(self):
        self.page.goto("https://blog.agibank.com.br/")

    def clicar_lupa(self):
        self.btn_lupa.wait_for(state="visible", timeout=10000)
        self.btn_lupa.click()

    def realizar_busca(self, termo):
        self.campo_busca.wait_for(state="visible")
        self.campo_busca.fill(termo)
        self.page.keyboard.press("Enter")

    def clicar_pesquisar_vazio(self):
        self.campo_busca.wait_for(state="visible")
        self.page.keyboard.press("Enter")
