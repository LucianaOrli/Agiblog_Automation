import pytest
import sys
import os
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import Page, expect

# --- AJUSTE DE SENIOR: Garante que o Python encontre o arquivo agiblog_page.py ---
sys.path.append(os.path.dirname(__file__))
from agiblog_page import AgiBlogPage 

# Localização do arquivo de funcionalidade (feature)
scenarios('../features/agiblog.feature')

@pytest.fixture
def blog_page(page: Page):
    """Instancia a Page Object para ser usada nos steps."""
    return AgiBlogPage(page)

@given('que eu acesso a página inicial do Agiblog')
def abrir_site(blog_page: AgiBlogPage):
    blog_page.acessar_home()

@when('eu clico na lupa de pesquisa')
def clicar_lupa(blog_page: AgiBlogPage):
    # O motorista (teste) dá a ordem para o GPS (page) agir:
    blog_page.btn_lupa.first.click()
    
@when('eu digito "empréstimo" no campo de busca')
def digitar_termo(blog_page: AgiBlogPage):
    blog_page.campo_busca.first.fill("empréstimo")

@when('eu digito "termo_inexistente_lux_2026"')
def digitar_termo_inexistente(blog_page: AgiBlogPage):
    blog_page.campo_busca.first.fill("termo_inexistente_lux_2026")

@when('eu pressiono a tecla Enter')
def dar_enter(blog_page: AgiBlogPage):
    blog_page.page.keyboard.press("Enter")

@when('eu seleciono uma categoria no menu principal')
def selecionar_categoria(blog_page: AgiBlogPage):
    blog_page.clicar_categoria()

@when('eu clico no primeiro artigo da lista')
def clicar_artigo(blog_page: AgiBlogPage):
    blog_page.clicar_primeiro_artigo()

@then('o sistema deve exibir resultados relacionados ao termo')
def verificar_resultados(blog_page: AgiBlogPage):
    expect(blog_page.titulo_arquivo).to_be_visible()

@then('o sistema deve exibir a mensagem "Nenhum resultado"')
def verificar_vazio(blog_page: AgiBlogPage):
    expect(blog_page.msg_nenhum_resultado).to_be_visible()

@then('a página da categoria deve carregar com sucesso')
def verificar_categoria(blog_page: AgiBlogPage):
    # Verifica se a URL mudou (não é mais a home)
    expect(blog_page.page).not_to_have_url("/")

@then('o título do artigo deve estar visível e legível')
def verificar_titulo_artigo(blog_page: AgiBlogPage):
    expect(blog_page.titulo_artigo).to_be_visible()

@then('a logomarca do Agi deve estar visível no topo da página')
def verificar_logo(blog_page: AgiBlogPage):
    expect(blog_page.logo_agi.first).to_be_visible()
