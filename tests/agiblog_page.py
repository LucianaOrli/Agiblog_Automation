from playwright.sync_api import Page

class AgiBlogPage:
    def __init__(self, page: Page):
        self.page = page
        # Seletor CSS da lupa e do campo de busca (mais estável que placeholder)
        self.btn_lupa = page.locator("#search-open").first
        self.campo_busca = page.locator(".search-field").first 
        self.msg_nenhum_resultado = page.locator(".no-results, .not-found, text='Nenhum resultado'").first

    def acessar_home(self):
        self.page.goto("https://blog.agibank.com.br/") # URL atualizada

    def clicar_lupa(self):
        self.btn_lupa.click()

    def realizar_busca(self, termo):
        # Garante que o campo apareça antes de escrever
        self.campo_busca.wait_for(state="visible")
        self.campo_busca.fill(termo)
        self.page.keyboard.press("Enter")

    def clicar_pesquisar_vazio(self):
        self.page.keyboard.press("Enter")
