# 🚀 Automação de Testes & Performance - BlazeDemo (Lux by Or)

Este repositório contém a suíte de testes funcionais (BDD) e de performance para o portal **BlazeDemo**, focando no fluxo crítico de compra de passagens aéreas.

## 🛠️ Tecnologias Utilizadas
* **Python 3.9+**
* **Playwright**: Automação E2E (End-to-End) de alta performance.
* **Pytest-BDD**: Escrita de cenários em Gherkin para alinhamento com o negócio.
* **Locust**: Framework de testes de carga baseado em eventos, capaz de gerar alta vazão (RPS).

---

## 🎭 1. Testes Funcionais (E2E)
Os cenários foram escritos em **Gherkin** para garantir que o fluxo de compra seja validado do ponto de vista do usuário.

### Como executar:
1. Instale as dependências: `pip install pytest pytest-bdd playwright pytest-html`
2. Instale os browsers: `playwright install`
3. Execute: `pytest tests/test_blaze.py --html=evidencias/Relatorio_Funcional.html --self-contained-html`

---

## 📈 2. Testes de Performance (Carga e Pico)
O objetivo foi validar a resiliência do sistema sob uma carga de **250 Requisições por Segundo (RPS)**.

### Cenário de Teste:
* **Fluxo:** Home -> Reserva -> Seleção -> Confirmação de Compra.
* **Critério de Aceitação:** 250 RPS com 90th Percentile < 2.0s.

### Como executar:
1. Instale o Locust: `pip install locust`
2. Execute o Teste de Carga: 
   `locust -f tests/test_performance_blaze.py --headless -u 100 -r 10 -t 1m --html evidencias/Relatorio_Carga.html --host https://www.blazedemo.com`

---

## 📊 Relatório de Execução e Análise Técnica (IMPORTANTE)

### Resultado Obtido:
* **Vazão Máxima Estável:** ~120 - 150 RPS.
* **90th Percentile:** Variou entre 1.8s e 4.5s sob carga máxima.
* **Status do Critério de Aceitação:** ❌ **Não Satisfeito.**

### Motivação e Conclusão:
1. **Infraestrutura Limitada:** O ambiente `blazedemo.com` é um serviço público para fins didáticos. Ao atingir a marca de 180+ RPS, o servidor apresentou erros `504 Gateway Timeout` e `502 Bad Gateway`.
2. **Degradação de Performance:** O tempo de resposta (90th percentile) excedeu os 2 segundos assim que a concorrência ultrapassou 150 usuários simultâneos, indicando que o escalonamento horizontal (Horizontal Pod Autoscaling) ou o balanceamento de carga do ambiente não suporta a vazão solicitada.
3. **Recomendação:** Para atingir 250 RPS estáveis, seria necessário um ambiente de Staging com recursos de CPU/Memória dedicados e otimização na camada de persistência de dados (Banco de Dados).

---
**Desenvolvido com rigor técnico por Luciana (Lux by Or) 💎🛡️**
