# language: pt
Funcionalidade: Testes de Busca no Agiblog

  Contexto:
    Dado que eu acesso a página inicial do Agiblog
    Quando eu clico na lupa de pesquisa

  Cenário: 01 - Realizar busca por termo existente
    Quando eu digito o termo "empréstimo"
    Então o sistema deve exibir resultados relevantes

  Cenário: 02 - Realizar busca por termo inexistente
    Quando eu digito o termo "termo_inexistente_lux_2026"
    Então o sistema deve exibir a mensagem de nenhum resultado encontrado

  Cenário: 03 - Realizar busca com campo vazio
    Quando eu clico no botão de pesquisar sem preencher o campo
    Então o sistema deve permanecer na home

  Cenário: 04 - Realizar busca com termo excessivamente longo
    Quando eu digito o termo "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    Então o sistema deve processar a busca sem erro de servidor
