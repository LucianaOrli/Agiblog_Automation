from playwright.sync_api import Page

class AgiBlogPage:
    def __init__(self, page: Page):
        self.page = page
        # Seletores atualizados para serem mais precisos:
        self.btn_lupa = page.locator("a.search-show") # Tente este seletor de classe
        self.campo_busca = page.get_by_placeholder("Pesquisar …") # Busca pelo texto dentro do campo
        self.msg_nenhum_resultado = page.get_by_text("Nenhum resultado")
        self.titulo_arquivo = page.locator("h1.archive-title")
        self.menu_item = page.locator("#menu-main-menu .menu-item a")
        self.primeiro_artigo = page.locator("article h2 a")
        self.titulo_artigo = page.locator("h1.entry-title")
        self.logo_agi = page.locator(".site-logo img, .site-branding img")
