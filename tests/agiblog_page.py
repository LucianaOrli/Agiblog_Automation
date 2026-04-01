from playwright.sync_api import Page

class AgiBlogPage:
    def __init__(self, page: Page):
        self.page = page
        # A linha estratégica DEVE ficar aqui:
        self.btn_lupa = page.locator("#search-open, .search-show, .ast-search-menu-icon, [aria-label='Link de pesquisa']")
        # ... (restante dos seletores)
        self.campo_busca = page.get_by_placeholder("Pesquisar …") # Busca pelo texto dentro do campo
        self.msg_nenhum_resultado = page.get_by_text("Nenhum resultado")
        self.titulo_arquivo = page.locator("h1.archive-title")
        self.menu_item = page.locator("#menu-main-menu .menu-item a")
        self.primeiro_artigo = page.locator("article h2 a")
        self.titulo_artigo = page.locator("h1.entry-title")
        self.logo_agi = page.locator(".site-logo img, .site-branding img")
