# language: pt
Funcionalidade: Busca e Navegação no Blog do Agi
  Como um usuário do Agiblog
  Eu quero pesquisar por conteúdos e navegar pelas categorias
  Para garantir que a plataforma está funcional.

  Contexto:
    Dado que eu acesso a página inicial do Agiblog

  @busca_sucesso
  Cenário: 01 - Realizar busca por termo existente
    Quando eu clico na lupa de pesquisa
    E digito "empréstimo" no campo de busca
    E pressiono a tecla Enter
    Então o sistema deve exibir resultados relacionados ao termo

  @busca_vazio
  Cenário: 02 - Realizar busca por termo inexistente
    Quando eu clico na lupa de pesquisa
    E digito "termo_inexistente_lux_2026"
    E pressiono a tecla Enter
    Então o sistema deve exibir a mensagem "Nenhum resultado"

  @navegacao_menu
  Cenário: 03 - Validar acesso ao menu de categorias
    Quando eu seleciono uma categoria no menu principal
    Então a página da categoria deve carregar com sucesso

  @artigo_clique
  Cenário: 04 - Verificar leitura de artigo
    Quando eu clico no primeiro artigo da lista
    Então o título do artigo deve estar visível e legível

  @identidade_visual
  Cenário: 05 - Validar presença da logomarca
    Então a logomarca do Agi deve estar visível no topo da página
