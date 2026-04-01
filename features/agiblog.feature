# language: pt
Funcionalidade: Testes de Busca no Agiblog

  Contexto:
    Dado que eu acesso a página inicial do Agiblog
    Quando eu clico na lupa de pesquisa

  Cenário: 01 - Realizar busca por termo existente
    E eu digito o termo "empréstimo"
    Então o sistema deve exibir resultados relevantes

  Cenário: 02 - Realizar busca por termo inexistente
    E eu digito o termo "termo_inexistente_lux_2026"
    Então o sistema deve exibir a mensagem de nenhum resultado encontrado

  Cenário: 03 - Realizar busca com campo vazio
    E eu clico no botão de pesquisar sem preencher o campo
    Então o sistema deve permanecer na home

  Cenário: 04 - Realizar busca com termo excessivamente longo
    E eu digito o termo "A" repetido duzentas vezes
    Então o sistema deve processar a busca sem erro de servidor

  Cenário: 05 - Realizar busca com caracteres especiais (Segurança)
    E eu digito o termo "<script>alert('xss')</script>"
    Then o sistema deve tratar como texto comum e exibir mensagem de não encontrado
