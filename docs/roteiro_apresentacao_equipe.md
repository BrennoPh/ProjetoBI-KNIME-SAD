# Roteiro Completo de Fala para a Apresentação — Grupo 12
> **Disciplina:** Sistemas de Apoio à Decisão (SAD) — Projeto BI  
> **Tema:** KNIME Analytics Platform  
> **Duração Total Prevista:** 7 minutos e 45 segundos (Dentro da faixa obrigatória de 5 a 10 min)  
> **Integrantes:** Brenno Phelipe, David Santos, Gabriel Lima, Paulo Henrique

---

## ⏱️ Quadro Geral de Minutagem e Transições

| Bloco | Responsável | Início | Fim | Duração | Tema Principal |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Brenno Phelipe** | 0:00 | 1:45 | 1m 45s | Abertura, Conceito do KNIME, Paradigma em Nós e Problemas que Resolve |
| **2** | **David Santos** | 1:45 | 3:45 | 2m 00s | Tecnologias, Vantagens/Limitações, Mercado e Contexto do Problema (SAD) |
| **3** | **Gabriel Lima** | 3:45 | 5:45 | 2m 00s | Exemplo Prático: Demonstração do Workflow no KNIME e Dashboard |
| **4** | **Paulo Henrique** | 5:45 | 7:45 | 2m 00s | Análise dos Resultados, Apoio à Decisão, Repositório e Encerramento |

---

## 🗣️ Bloco 1 — Brenno Phelipe (0:00 às 1:45)
**Slides de Apoio:** Slides 1 e 2

### Fala Sugerida:
> *"Olá a todos, olá professor. Somos o Grupo 12 e hoje vamos apresentar a pesquisa e a demonstração prática da ferramenta **KNIME Analytics Platform** aplicada a **Sistemas de Apoio à Tomada de Decisão**.*
>
> *Nossa equipe é formada por mim, Brenno Phelipe, pelo David Santos, Gabriel Lima e Paulo Henrique. Todo o código do nosso projeto, o arquivo de workflow executável e a documentação já estão disponíveis publicamente no nosso repositório no GitHub, indicado no slide.*
>
> *(Avança para o Slide 2)*
>
> *Para iniciarmos: o que é o **KNIME**? O KNIME, acrônimo para Konstanz Information Miner, é uma das principais plataformas mundiais de ciência de dados e BI de código aberto.*
>
> *O grande diferencial do KNIME é o seu **paradigma baseado em nós e programação visual**. Em vez de exigir que um analista escreva centenas de linhas de código em Python ou R para tratar um dado ou treinar um algoritmo, no KNIME nós conectamos blocos visuais chamados **Nodes**.*
>
> *Cada nó possui uma porta de entrada, uma lógica interna de processamento e portas de saída. Além disso, a plataforma traz um semáforo intuitivo em cada bloco: vermelho indica que o nó precisa de configuração, amarelo significa que ele está pronto para ser executado, e verde indica sucesso.*
>
> *Quais problemas o KNIME resolve na prática de BI e SAD?*
> 1. *Primeiro, ele **elimina a fragmentação de ferramentas**, unindo em um único ambiente desde a extração e limpeza (ETL) até algoritmos de Machine Learning e relatórios gerenciais.*
> 2. *Segundo, ele **quebra a barreira de entrada da programação**, permitindo que gestores e especialistas do negócio participem diretamente da modelagem dos fluxos analíticos.*
> 3. *E terceiro, ele garante **auditabilidade e reprodutibilidade**, pois qualquer pessoa consegue abrir o fluxo e compreender visualmente a linhagem do dado.*
>
> *Agora, passo a palavra ao David, que vai explicar a arquitetura técnica, vantagens e o caso de negócio que construímos."*

---

## 🗣️ Bloco 2 — David Santos (1:45 às 3:45)
**Slides de Apoio:** Slides 3 e 4

### Fala Sugerida:
> *"Obrigado, Brenno. Falando sobre a engenharia sob o capô do KNIME:*
>
> *(Slide 3)*
>
> *O KNIME é construído primordialmente em **Java** sobre a plataforma **Eclipse RCP**, o que lhe confere uma estrutura modular extremamente robusta baseada em plugins.*
>
> *Mas ele não é um ecossistema fechado — pelo contrário. O KNIME possui **interoperabilidade nativa**: podemos embutir scripts em Python ou R diretamente dentro dos nós, executar consultas SQL diretamente nos bancos de dados corporativos e renderizar visualizações interativas em JavaScript e D3.js. Além disso, conecta-se a clusters de Big Data como Apache Spark.*
>
> *Em relação às **vantagens**:*
> * *Ele é 100% gratuito e open-source em sua versão desktop, sem restrição de linhas ou limitações artificiais.*
> * *Conta com mais de 4.000 nós nativos e uma comunidade global vibrante.*
>
> *Quanto às **limitações**:*
> * *Em processamentos locais com bases de dados gigantescas, ele pode apresentar consumo intensivo de memória RAM se não for bem configurado.*
> * *E funcionalidades de alta disponibilidade em nuvem, governança corporativa e agendamento automático em servidores multiusuário exigem a versão comercial, o KNIME Business Hub.*
>
> *(Avança para o Slide 4)*
>
> *No mercado corporativo, o KNIME é amplamente utilizado por instituições financeiras para detecção de fraudes e risco de crédito, na indústria farmacêutica em triagem de medicamentos, e no varejo para previsão de demanda.*
>
> *Para o nosso trabalho, decidimos aplicar o KNIME em um problema clássico e de altíssimo impacto para Sistemas de Apoio à Decisão: a **Prevenção Preditiva de Churn (Evasão de Clientes) em uma empresa de Telecomunicações**.*
>
> *Perder um cliente custa entre 5 a 7 vezes mais do que conquistar um novo. Nossa base conta com 1.200 clientes rastreados, com taxa média de churn de 41.8%. O desafio do nosso SAD foi identificar preventivamente os fatores que levam à evasão e apoiar os gestores na formulação de planos de retenção.*
>
> *Para mostrar como implementamos isso na prática no KNIME, passo a palavra para o Gabriel."*

---

## 🗣️ Bloco 3 — Gabriel Lima (3:45 às 5:45)
**Slides de Apoio:** Slides 5 e 6

### Fala Sugerida:
> *"Obrigado, David. Vamos agora ao coração prático do nosso projeto: o workflow que construímos dentro do KNIME Analytics Platform.*
>
> *(Slide 5 - Mostrando a arquitetura do workflow)*
>
> *Como vocês podem ver na tela, o nosso fluxo é organizado em três fases lógicas:*
>
> *Na primeira fase, de **Ingestão e Tratamento (ETL)**, utilizamos o nó `CSV Reader` para carregar a base de 1.200 clientes. Em seguida, passamos pelo nó `Missing Value` para higienização e tratamento de possíveis inconsistências, e pelo `Column Filter` para selecionar os atributos preditivos mais relevantes.*
>
> *Na segunda fase, entramos na **Modelagem Preditiva**:*
> * *Utilizamos o nó `Partitioning` para separar os dados de forma estratificada: 70% da base foi separada para treinar o modelo e 30% foi isolada para o teste cego de validação.*
> * *Para o algoritmo preditivo, escolhemos a **Árvore de Decisão** através do nó `Decision Tree Learner`. Escolhemos a árvore porque, em Sistemas de Apoio à Decisão, a interpretabilidade é crucial — o gestor precisa entender a regra de negócio por trás de cada previsão.*
> * *O modelo treinado é então conectado ao nó `Decision Tree Predictor`, que aplica a inteligência sobre os dados de teste e gera a probabilidade de cancelamento de cada cliente.*
>
> *Na terceira fase, passamos pela **Avaliação e Suporte à Decisão**:*
> * *O nó `Scorer` calculou a matriz de confusão e apontou uma **acurácia global de 84.7%**.*
> * *E com o nó `Rule Engine`, convertemos as probabilidades em faixas de risco gerencial: Crítico, Alto, Médio e Baixo.*
>
> *(Avança para o Slide 6 - Mostrando o Dashboard)*
>
> *No KNIME, agrupamos os nós finais em um **Componente Interativo**, gerando este dashboard executivo que combina nós de `Bar Chart` e `Table View` dinâmicos. O gestor pode filtrar interativamente qualquer segmento de clientes e exportar a lista prioritária para a equipe de retenção em segundos.*
>
> *Para detalhar os resultados obtidos e as decisões estratégicas que esse sistema apoia, passo a palavra ao Paulo."*

---

## 🗣️ Bloco 4 — Paulo Henrique (5:45 às 7:45)
**Slides de Apoio:** Slides 7 e 8

### Fala Sugerida:
> *"Obrigado, Gabriel. O ponto central de um Sistema de Apoio à Decisão não é apenas gerar gráficos ou números, mas responder: **quais ações os tomadores de decisão devem adotar a partir dessas informações?***
>
> *(Slide 7)*
>
> *Ao analisar os resultados gerados pelo nosso modelo no KNIME, descobrimos três padrões fundamentais:*
>
> 1. *Primeiro, o **Tipo de Contrato**: clientes com contrato mensal têm uma taxa alarmante de **57.9% de cancelamento**, enquanto clientes com contrato de 2 anos têm apenas **19.6%**. O contrato mensal é a maior porta de saída de receita.*
> 2. *Segundo, o **Gatilho Operacional do SAC**: clientes com até 2 chamadas de suporte mantêm um churn estável de 36%. Porém, quando o cliente atinge **3 ou mais chamadas**, a taxa de evasão dispara para **63.8%**. Esse é o ponto de ruptura.*
> 3. *Terceiro, clientes sem suporte técnico contratado cancelam em **52.7%** dos casos, contra apenas 30.2% dos que possuem suporte.*
>
> *Com esses dados, o nosso SAD recomenda **três decisões gerenciais prioritárias**:*
> * *Decisão 1 (Atendimento): Automatizar um alerta no CRM para que qualquer cliente com 3 chamadas no SAC seja imediatamente atendido por um gestor sênior de retenção com autorização para conceder até 20% de desconto.*
> * *Decisão 2 (Comercial): Criar uma campanha ativa para migrar clientes do plano mensal para o anual, oferecendo 1 mês de gratuidade como incentivo de blindagem.*
> * *Decisão 3 (Produto): Oferecer 3 meses de suporte técnico gratuito para clientes de Fibra Óptica, que representam o maior ticket médio da base.*
>
> *(Avança para o Slide 8)*
>
> *Para concluir: o KNIME Analytics Platform demonstrou ser uma ferramenta completa, poderosa e altamente acessível para a construção de Sistemas de Apoio à Decisão.*
>
> *Convidamos o professor e os colegas a acessarem o nosso repositório no GitHub, onde estão disponíveis o arquivo `.knwf` do workflow, a base tratada, os diagramas e a documentação completa.*
>
> *Agradecemos a atenção de todos e estamos abertos para perguntas e comentários."*

---

## 🎯 Dicas de Ouro para o Grupo Durante a Apresentação

1. **Gestão do Tempo:**
   * Mantenha um cronômetro visível com um dos integrantes da equipe.
   * Se alguém estiver falando mais devagar, os blocos seguintes podem condensar ligeiramente as frases sem perder o conteúdo essencial.
2. **Postura e Transições:**
   * Sempre mencione o nome do colega ao passar a palavra (*"Passo a palavra agora para o David..."*). Isso demonstra entrosamento e organização prévia (critérios pontuados no barema).
3. **Se o Professor Pedir Demonstração Ao Vivo:**
   * Deixe o KNIME aberto em segundo plano com o workflow `churn_prediction_sad.knwf` já carregado e executado (com os nós com status verde).
   * Caso ele queira ver o dashboard, basta clicar com o botão direito no nó final ou componente e abrir o *Interactive View*.
