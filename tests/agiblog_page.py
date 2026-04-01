from playwright.sync_api import Page

class AgiBlogPage:
    def __init__(self, page: Page):
        self.page = page
        # Seletores (Os ingredientes)
        self.btn_lupa = page.locator("#search-open, .search-show, .ast-search-menu-icon, [aria-label='Link de pesquisa']")
        self.campo_busca = page.get_by_placeholder("Pesquisar …")
        self.msg_nenhum_resultado = page.get_by_text("Nenhum resultado")
        self.titulo_arquivo = page.locator("h1.archive-title")
        self.menu_item = page.locator("#menu-main-menu .menu-item a")
        self.primeiro_artigo = page.locator("article h2 a")
        self.titulo_artigo = page.locator("h1.entry-title")
        self.logo_agi = page.locator(".site-logo img, .site-branding img")

    # Ações (O modo de preparo)
    def acessar_home(self):
        self.page.goto("https://blogdoagi.com.br/")

    def clicar_lupa(self):
        self.btn_lupa.first.click()

    def realizar_busca(self, termo):
        # Limpa o campo se houver algo e digita o novo termo
        self.campo_busca.fill("")
        self.campo_busca.fill(termo)
        self.page.keyboard.press("Enter")

    def clicar_pesquisar_vazio(self):
        # Simula clicar no botão de busca sem digitar nada
        self.page.keyboard.press("Enter")
