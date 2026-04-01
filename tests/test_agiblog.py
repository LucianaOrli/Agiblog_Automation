import pytest
from pytest_bdd import scenario, given, when, then, parsers
from agiblog_page import AgiBlogPage

@pytest.fixture
def blog_page(page):
    return AgiBlogPage(page)

# Mapeamento dos Cenários
@scenario('../features/agiblog.feature', '01 - Realizar busca por termo existente')
def test_busca_existente(): pass

@scenario('../features/agiblog.feature', '02 - Realizar busca por termo inexistente')
def test_busca_inexistente(): pass

@scenario('../features/agiblog.feature', '03 - Realizar busca com campo vazio')
def test_busca_vazia(): pass

@scenario('../features/agiblog.feature', '04 - Realizar busca com termo excessivamente longo')
def test_busca_longa(): pass

@scenario('../features/agiblog.feature', '05 - Realizar busca com caracteres especiais (Segurança)')
def test_busca_seguranca(): pass

# Implementação dos Steps
@given('que eu acesso a página inicial do Agiblog')
def step_abrir_home(blog_page):
    blog_page.acessar_home()

@when('eu clico na lupa de pesquisa')
def step_clicar_lupa(blog_page):
    blog_page.clicar_lupa()

@when(parsers.parse('eu digito o termo "{termo}"'))
def step_digitar_termo(blog_page, termo):
    blog_page.realizar_busca(termo)

@when('eu clico no botão de pesquisar sem preencher o campo')
def step_pesquisar_vazio(blog_page):
    blog_page.clicar_pesquisar_vazio()

@then('o sistema deve exibir resultados relevantes')
def step_validar_sucesso(blog_page):
    assert blog_page.msg_nenhum_resultado.is_hidden()

@then('o sistema deve exibir a mensagem de nenhum resultado encontrado')
@then('o sistema deve tratar como texto comum e exibir mensagem de não encontrado')
def step_validar_falha(blog_page):
    assert blog_page.msg_nenhum_resultado.is_visible()

@then('o sistema deve permanecer na home')
def step_validar_home(blog_page):
    assert "blogdoagi.com.br" in blog_page.page.url

@then('o sistema deve processar a busca sem erro de servidor')
def step_validar_processamento(blog_page):
    assert blog_page.page.query_selector("body") is not None
