🌐 Agiblog Automation - UI & Requirement Analysis (Questão 1)
Objetivo: Automação de testes funcionais para o Blog do Agi, focando na funcionalidade de pesquisa de artigos e integridade da navegação.
URL: https://blogdoagi.com.br/ Critério: Validação de busca funcional, resultados relevantes e tratamento de exceções.

📊 Análise de Engenharia de QA (Arquitetura de Testes):
Para este desafio, realizei uma Análise de Requisitos e de Negócio completa, transformando a automação em uma "documentação viva" para o time.
Cobertura Ampliada: Embora o desafio solicitasse 2 cenários, entreguei 5 cenários estratégicos via Gherkin, garantindo uma cobertura resiliente.
Mapeamento de Requisitos:
RF (Funcionais): Busca por lupa (RF01), digitação (RF02), resultados (RF03) e categorias (RF04).
RNF (Não Funcionais): Performance de busca < 3s (RNF01) e usabilidade intuitiva (RNF02).
RE (Exceção): Busca sem resultados (RE01) e tratamento de campo vazio (RE02).

🎭 Cenários Automatizados (BDD/Gherkin):
Cenário 1: Buscar artigo com palavra-chave válida (Caminho Feliz).
Cenário 2: Buscar artigo inexistente (Validação de mensagem "Nenhum resultado encontrado").
Cenário 3: Filtrar por categoria (Conta Corrente) após busca.
Cenário 4: Fluxo completo de abertura de artigo a partir do resultado.
Cenário 5: Validação de tentativa de busca com campo vazio.

🛠️ Tecnologias Utilizadas:
Python 3.9+
Playwright: Automação de UI de alta performance.
Pytest-BDD: Alinhamento técnico entre QA, Negócio e Desenvolvedores Java.


🚀 Como Executar:
Instalar dependências:
Bash
pip install pytest pytest-bdd playwright
playwright install
      2.   Executar os testes:
             Bash
       pytest tests/
3. Evidências: Vídeos e logs das execuções disponíveis na pasta /evidencias.



Desenvolvido por Luciana (Lux by Or) 💎🛡️

