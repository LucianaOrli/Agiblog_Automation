class HomePage:
    def __init__(self, page):
        self.page = page
        self.btn_lupa = page.locator("#search-open") # Exemplo de seletor
        self.campo_busca = page.locator(".search-field")
        self.btn_pesquisar = page.locator(".search-submit")

    def realizar_busca(self, termo):
        self.btn_lupa.click()
        self.campo_busca.fill(termo)
        self.page.keyboard.press("Enter")
