# Dicionário de Dados — Prevenção de Churn & SAD

Este dataset foi estruturado para alimentar o pipeline de análise preditiva no **KNIME Analytics Platform**, fornecendo subsídios para tomadas de decisão na área de retenção de clientes.

| Variável | Tipo | Descrição | Importância para o Apoio à Decisão (SAD) |
| :--- | :---: | :--- | :--- |
| **ID_Cliente** | String | Código único identificador do cliente | Rastreabilidade e personalização de ações |
| **Genero** | String | Feminino ou Masculino | Análise demográfica de perfil |
| **Idoso** | Inteiro | 1 se tem mais de 65 anos, 0 caso contrário | Segmentação etária para canais de atendimento |
| **Tem_Parceiro** | String | Sim / Não | Indicador de estabilidade residencial |
| **Tem_Dependentes**| String | Sim / Não | Influência no consumo familiar e sensibilidade a preço |
| **Meses_Contrato** | Inteiro | Tempo de relacionamento com a empresa (1 a 72 meses) | Clientes novos (menor tempo) possuem risco substancialmente maior |
| **Servico_Telefonia**| String | Sim / Não | Aderência ao pacote básico de voz |
| **Servico_Internet** | String | Fibra Óptica, DSL ou Nenhum | Margem de receita e expectativa de estabilidade de sinal |
| **Seguranca_Online**| String | Sim, Não ou Sem Internet | Fator de fidelização por serviços agregados |
| **Suporte_Tecnico** | String | Sim, Não ou Sem Internet | **Crítico:** Falta de suporte técnico eleva atrito após problemas |
| **Tipo_Contrato** | String | Mensal, Anual ou 2 Anos | **Fator Principal:** Contratos mês-a-mês concentram a evasão |
| **Fatura_Digital** | String | Sim / Não | Indicador comportamental e de canal |
| **Forma_Pagamento** | String | Boleto Eletrônico, Boleto Bancário, Cartão de Crédito, Transferência Automática | Boletos avulsos apresentam maior taxa de inadimplência e churn |
| **Valor_Mensal** | Numérico | Mensalidade cobrada em R$ | Permite calcular o valor financeiro sob risco (LTV) |
| **Valor_Total** | Numérico | Total faturado acumulado do cliente em R$ | Valor histórico acumulado |
| **Chamadas_Suporte**| Inteiro | Número de reclamações/chamadas no suporte (0 a 6+) | **Gatilho de Insatisfação:** Clientes com $\ge 3$ chamadas exigem intervenção emergencial |
| **Cancelou_Plano** | String | **Sim** (Churn) ou **Não** (Ativo) — Variável Alvo | Target a ser previsto pelo modelo de Árvore de Decisão |
