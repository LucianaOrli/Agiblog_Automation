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

  @busca_vazia
  Cenário: 03 - Realizar busca com campo vazio
    Dado que eu acesso a página inicial do Agiblog
    Quando eu clico na lupa de pesquisa
    E eu clico no botão de pesquisar sem preencher o campo
    Então o sistema deve ignorar a ação ou permanecer na home

  @busca_longa
  Cenário: 04 - Realizar busca com termo excessivamente longo
    Dado que eu acesso a página inicial do Agiblog
    Quando eu clico na lupa de pesquisa
    E eu digito um termo com mais de 200 caracteres
    Então o sistema deve processar a busca sem erro de servidor

  @busca_caracteres
  Cenário: 05 - Realizar busca com caracteres especiais (Segurança)
    Dado que eu acesso a página inicial do Agiblog
    Quando eu clico na lupa de pesquisa
    E eu digito o termo "<script>alert('xss')</script>"
    Então o sistema deve tratar como texto comum e exibir mensagem de não encontrado
  @identidade_visual
  Cenário: 05 - Validar presença da logomarca
    Então a logomarca do Agi deve estar visível no topo da página
