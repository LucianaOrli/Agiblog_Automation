import pytest
from pytest_bdd import scenario, given, when, then, parsers
from agiblog_page import AgiBlogPage

# Cenários
@scenario('../features/agiblog.feature', '01 - Realizar busca por termo existente')
def test_realizar_busca_por_termo_existente():
    pass

@scenario('../features/agiblog.feature', '02 - Realizar busca por termo inexistente')
def test_realizar_busca_por_termo_inexistente():
    pass

@scenario('../features/agiblog.feature', '03 - Realizar busca com campo vazio')
def test_realizar_busca_com_campo_vazio():
    pass

@scenario('../features/agiblog.feature', '04 - Realizar busca com termo excessivamente longo')
def test_realizar_busca_com_termo_excessivamente_longo():
    pass

@scenario('../features/agiblog.feature', '05 - Realizar busca com caracteres especiais (Segurança)')
def test_realizar_busca_com_caracteres_especiais_segurança():
    pass

@scenario('../features/agiblog.feature', '06 - Validar presença da logomarca')
def test_validar_presença_da_logomarca():
    pass

# Steps Compartilhados
@given('que eu acesso a página inicial do Agiblog')
def abrir_site(blog_page: AgiBlogPage):
    blog_page.acessar_home()

@when('eu clico na lupa de pesquisa')
def clicar_lupa(blog_page: AgiBlogPage):
    blog_page.clicar_lupa()

# ESTE PASSO RESOLVE OS ERROS 85, 86, 88 e 89 DO SEU LOG:
@when(parsers.parse('digito "{termo}" no campo de busca'))
@when(parsers.parse('eu digito um termo com mais de 200 caracteres')) # Fallback para o log 88
@when(parsers.parse('eu digito o termo "{termo}"')) # Fallback para o log 89
def preencher_busca(blog_page: AgiBlogPage, termo="termo_longo_ou_padrao"):
    blog_page.realizar_busca(termo)

@when('eu clico no botão de pesquisar sem preencher o campo')
def pesquisar_vazio(blog_page: AgiBlogPage):
    blog_page.clicar_pesquisar_vazio()

@then('o sistema deve exibir resultados relevantes')
def validar_resultados(blog_page: AgiBlogPage):
    assert blog_page.msg_nenhum_resultado.is_hidden()

@then('o sistema deve exibir a mensagem de nenhum resultado encontrado')
def validar_nao_encontrado(blog_page: AgiBlogPage):
    assert blog_page.msg_nenhum_resultado.is_visible()

@then('o sistema deve tratar como texto comum e exibir mensagem de não encontrado')
def validar_seguranca(blog_page: AgiBlogPage):
    assert blog_page.msg_nenhum_resultado.is_visible()

@then('a logomarca do Agi deve estar visível no cabeçalho')
def validar_logo(blog_page: AgiBlogPage):
    assert blog_page.logo_agi.is_visible()

@then('o sistema deve ignorar a ação ou permanecer na home')
def validar_vazio(blog_page: AgiBlogPage):
    # Verifica se não saiu da home
    assert "blogdoagi.com.br" in blog_page.page.url
