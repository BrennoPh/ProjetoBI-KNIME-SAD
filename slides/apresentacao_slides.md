# Slides da Apresentação — KNIME Analytics Platform (SAD)
> **Tempo Total Alvo:** 7m30s a 8m00s (Limite do edital: 5 a 10 min)  
> **Disciplina:** Sistemas de Apoio à Decisão (SAD) — Projeto BI  
> **Tema:** Grupo 12 — KNIME Analytics Platform  
> **Integrantes:** Brenno Phelipe, David Santos, Gabriel Lima, Paulo Henrique

---

### Slide 1: Capa e Abertura
* **Título Principal:** KNIME Analytics Platform: Inteligência Analítica e Apoio à Tomada de Decisão
* **Subtítulo:** Estudo de Caso Prático: Previsão e Prevenção de Churn em Telecom
* **Identificação da Disciplina:** Sistemas de Apoio à Decisão (SAD) — Departamento de Computação / UFS
* **Equipe:**
  * Brenno Phelipe Silva dos Santos
  * David Santos Silvino
  * Gabriel Lima Dantas
  * Paulo Henrique dos Santos Reis
* **Link em Destaque:** Repositório no GitHub: `https://github.com/BrennoPh/ProjetoBI-KNIME-SAD`  
* **Apresentação no Canva:** [https://www.canva.com/d/0e9RTsJ5KfAL7Ln](https://www.canva.com/d/0e9RTsJ5KfAL7Ln)
* **Apresentador:** Brenno Phelipe (0:00 - 0:30)

---

### Slide 2: O que é o KNIME Analytics Platform?
* **Finalidade:** Plataforma aberta (*open-source*), líder mundial em Ciência de Dados e Business Intelligence visual.
* **Paradigma de Nós (No-Code / Low-Code):**
  * Cada etapa é um bloco visual (*Node*) conectado por fluxos de dados (*Connectors*).
  * Semáforo de execução intuitivo em cada nó: Vermelho (não configurado), Amarelo (pronto para rodar), Verde (executado com sucesso).
* **Problemas que Procura Resolver:**
  * Fim dos silos de ferramentas (unifica ETL, Mineração, Modelagem Preditiva e BI).
  * Elimina a barreira de codificação para analistas e gestores de negócios.
  * Auditabilidade e reprodutibilidade: o fluxo documenta o raciocínio analítico por si só.
* **Apresentador:** Brenno Phelipe (0:30 - 1:45)

---

### Slide 3: Arquitetura, Tecnologias e Ecossistema
* **Núcleo Tecnológico:**
  * Construído em **Java** sobre o framework modular **Eclipse RCP**.
* **Interoperabilidade Total:**
  * Integração nativa com scripts **Python** e **R** (para bibliotecas avançadas).
  * Suporte a consultas **SQL** diretamente no banco de dados (*in-database processing*).
  * Visualizações interativas renderizadas em **JavaScript / D3.js**.
* **Vantagens Competitivas:**
  * Gratuito sem restrição de linhas ou recursos para uso desktop.
  * Mais de 4.000 nós e extensões comunitárias (Deep Learning, Text Mining, Geospatial).
* **Limitações:**
  * Consumo intensivo de memória RAM ao trabalhar com bases massivas localmente.
  * Recursos corporativos avançados (agendamento em cluster, governança) requerem o *KNIME Business Hub* comercial.
* **Apresentador:** David Santos (1:45 - 3:00)

---

### Slide 4: Aplicações no Mercado & Contexto do Nosso Problema (SAD)
* **Presença no Mercado Global:**
  * **Bancos:** Detecção em tempo real de fraudes financeiras e scoring de crédito.
  * **Farmacêutica / Saúde:** Triagem virtual de compostos e bioinformática.
  * **Varejo / Telecom:** Análise de sobrevivência e evasão de clientes (*churn*).
* **O Problema de Negócio Abordado (O Nosso Caso de SAD):**
  * Empresa de serviços com alta perda de clientes (churn global de **41.8%**).
  * Custo de aquisição é 5 a 7 vezes maior do que a retenção.
  * **Objetivo do SAD:** Identificar com precisão os clientes em risco iminente e fornecer subsídios para intervenção preventiva personalizada.
* **Apresentador:** David Santos (3:00 - 3:45)

---

### Slide 5: Exemplo Prático — O Pipeline no KNIME
* **Visual do Workflow no KNIME:** *(Exibir imagem do `workflow/workflow_architecture.svg`)*
* **Fases do Pipeline:**
  1. **Ingestão & Higienização (ETL):**
     * `CSV Reader` carrega 1.200 registros de clientes.
     * `Missing Value` e `Column Filter` padronizam atributos e isolam ruídos.
  2. **Particionamento & Modelagem:**
     * `Partitioning` divide a base em 70% Treino e 30% Teste.
     * `Decision Tree Learner` extrai regras lógicas com base no índice Gini.
     * `Decision Tree Predictor` aplica o modelo nos 30% restantes.
  3. **Avaliação & Categorização:**
     * `Scorer` mede acurácia global (**84.7%**) e matriz de confusão.
     * `Rule Engine` classifica o risco de cada cliente em Crítico, Alto, Médio e Baixo.
* **Apresentador:** Gabriel Lima (3:45 - 5:15)

---

### Slide 6: Demonstração do Dashboard Interativo no KNIME
* **Recurso de Visualização (Interactive Component):** *(Exibir imagem do `dashboard/dashboard_preview.svg`)*
* **Destaques da Demonstração:**
  * Uso de nós dinâmicos em JavaScript (`Bar Chart` e `Table View`).
  * Capacidade de drill-down: clicar em um segmento e filtrar imediatamente a tabela de clientes afetados.
  * Interface amigável para tomada de decisão em nível de diretoria executiva.
* **Apresentador:** Gabriel Lima (5:15 - 5:45)

---

### Slide 7: Análise dos Resultados e Apoio à Tomada de Decisão (SAD)
* **Descobertas Cruciais Extraídas dos Dados:**
  * **Tipo de Contrato:** Contratos Mensais concentram **57.9% de Churn**, contra apenas 19.6% em contratos de 2 anos.
  * **Gatilho Operacional do SAC:** Ao atingir a 3ª reclamação, a taxa de evasão dispara para **63.8%**.
  * **Falta de Suporte Técnico:** Clientes sem suporte registram **52.7% de cancelamento**.
* **Plano de Ação Gerencial (Decisões Estratégicas):**
  1. **Ação Emergencial:** Clientes com $\ge 3$ chamadas caem em fila VIP de retenção com oferta de 20% de desconto imediato.
  2. **Ação Comercial:** Campanha de migração de plano mensal para anual com 1 mês grátis (blindagem de longo prazo).
  3. **Ação de Produto:** Suporte técnico grátis por 3 meses para clientes de fibra óptica.
* **Apresentador:** Paulo Henrique (5:45 - 7:00)

---

### Slide 8: Conclusão, Repositório GitHub e Referências
* **Conclusão:**
  * O KNIME comprova ser uma solução madura, ágil e robusta para suportar decisões gerenciais complexas, unindo dados brutos a estratégias de alto retorno sobre investimento.
* **Repositório GitHub Aberto:**
  * Código-fonte, workflow `.knwf`, dataset e documentação completa:
  * `https://github.com/BrennoPh/ProjetoBI-KNIME-SAD`  
  * Canva: [https://www.canva.com/d/0e9RTsJ5KfAL7Ln](https://www.canva.com/d/0e9RTsJ5KfAL7Ln)
* **Principais Referências:**
  * Documentação Oficial do KNIME (<https://docs.knime.com/>).
  * Turban, E. et al. *Business Intelligence, Analytics, and Data Science: A Managerial Perspective*.
  * Provost, F. & Fawcett, T. *Data Science para Negócios*.
* **Apresentador:** Paulo Henrique (7:00 - 7:45)
