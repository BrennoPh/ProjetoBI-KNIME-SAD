---
name: canva-pro-slides
description: >-
  Cria apresentações e slides profissionais e de nível executivo diretamente no Canva,
  eliminando completamente vícios típicos de IA (paredes de texto, tópicos genéricos, clichês visuais).
  Ative esta skill quando o usuário pedir para: criar slides no Canva, gerar apresentações,
  montar pitch decks, desenhar decks executivos, criar apresentação para faculdade/empresa,
  ou transformar documentos/ideias em slides limpos, modernos e de alto impacto visual.
---

# Canva Pro Slides — Design Executivo Anti-IA

Esta skill transforma temas, briefs e documentos em apresentações de padrão executivo (estilo McKinsey, Duarte e Apple Keynote) e as cria diretamente no Canva através das ferramentas integradas da plataforma.

---

## 1. Filosofia de Design: Por que slides normais de IA parecem amadores?

| Erro Típico de IA (A Evitar) | Padrão Executivo Pro (Aplicar Sempre) |
| :--- | :--- |
| **Títulos Genéricos e Passivos** ("Introdução", "Visão Geral", "Benefícios", "Resultados") | **Títulos de Ação (Action Titles)** que resumem a conclusão do slide em 1 frase ativa. Se alguém ler só os títulos, entende a história inteira. |
| **Paredes de Texto / Bullets Longos** (5 a 8 tópicos com 3 linhas cada) | **Máximo de 20 a 35 palavras por slide**. Redação telegráfica, direta e paralela. Sem parágrafos. |
| **Tudo tem o mesmo peso visual** (falta de ponto focal) | **Hierarquia Radical (Regra 60-30-10)**: 60% respiro/fundo neutro, 30% estrutura/texto principal, 10% cor de destaque em 1 métrica/chave. |
| **Layouts Monótonos** (sempre lista com ícones em círculos) | **Arquétipos Semânticos**: Cada slide adota um formato (Big Metric, 3 Cards, Split 50/50, ou Fluxo Linear). |
| **Jargões e Buzzwords Vazios** ("alavancar sinergias holísticas", "otimizar paradigmas") | **Fatos Concretos e Dados Quantitativos**: Verbos de ação + números precisos (ex: *"Redução de 35% no Churn"*). |

---

## 2. Os 5 Arquétipos Visuais de Slides

Ao planejar cada slide, atribua obrigatoriamente um arquétipo estrutural:

1. **The Hero Stat (Número Gigante)**:
   - Usado para impacto inicial ou resultados principais.
   - 1 número ou métrica em fonte enorme (ex: `84.5%` ou `12 min`).
   - 1 frase curta logo abaixo explicando a consequência direta.

2. **The 3-Pillar Card Grid (3 Pilares)**:
   - Usado para pilares, funcionalidades, frentes de trabalho ou benefícios.
   - Exatamente 3 colunas (ou cartões).
   - Cada cartão possui: `[Título em Negrito de 2-3 palavras]` + `[Explicação de no máximo 10 palavras]`.

3. **The Split 50/50 (Antes vs Depois / Desafio vs Solução)**:
   - 2 colunas contrastantes com pesos visuais equilibrados.
   - Coluna 1 (Problema / Cenário Atual): Tom neutro/cinza.
   - Coluna 2 (Solução / Proposta): Tom com cor de destaque positiva.

4. **The Linear Process (Fluxo Sequencial)**:
   - 3 a 4 passos horizontais simples (Passo 1 → Passo 2 → Passo 3).
   - Cada passo com numeração clara e uma ação objetiva.

5. **The Executive Quote / Big Takeaway**:
   - Frase marcante entre aspas ou tese central em destaque.
   - Fonte ampla com grande respiro ao redor (whitespace).

---

## 3. Protocolo de Criação Direto no Canva

Quando o usuário solicitar a criação da apresentação, siga este passo a passo:

### Passo 1: Estruturar o Slide Deck (Refinamento do Brief)
Analise o conteúdo do usuário e converta em um roteiro enxuto (geralmente entre 4 a 8 slides para máxima retenção). Para cada slide, formule:
- **Title (Action Title)**: Afirmação conclusiva e forte (≤ 65 caracteres).
- **Description**: Síntese de 1 frase do contexto visual e mensagem central.
- **Points**: Máximo de 2 a 3 pontos telegráficos ou dados concisos.

### Passo 2: Invocar a ferramenta do Canva
Chame a ferramenta MCP `canva_canva:create-design` com o payload estruturado:
```json
{
  "brief": "Apresentação profissional e minimalista estilo executivo/consultoria sobre [TEMA]. Design limpo, muito espaço em branco, tipografia moderna sem serifa, sem sobrecarga de texto, paleta sóbria com 1 cor de destaque.",
  "format": "Presentation",
  "outline": {
    "sections": [
      {
        "title": "KNIME na Prática: Pipeline Preditivo Reduz Tempo de Análise em 70%",
        "description": "Capa executiva de alto impacto com foco em resultado prático.",
        "points": [
          "Estudo de Caso Telecom: Previsão de Churn",
          "Brenno Phelipe, David Santos, Gabriel Lima, Paulo Henrique"
        ]
      },
      {
        "title": "Fim dos Silos: Plataforma Visual Unifica ETL, ML e BI em Fluxo Único",
        "description": "Arquétipo de 3 pilares comparativos.",
        "points": [
          "Visual No-Code: Semáforo intuitivo por nó",
          "Interoperabilidade: Scripts Python/R e SQL integrados",
          "Governança: Reprodutibilidade e auditoria total"
        ]
      }
    ]
  },
  "user_intent": "Criar apresentação executiva e profissional no Canva sem sobrecarga de informação."
}
```

> **Nota para On-Brand**: Se o usuário solicitar explicitamente o uso de um Brand Kit corporativo da sua conta Canva, utilize a ferramenta `canva_canva:generate-design` com `brand_kit_id` e `design_type: "presentation"`.

### Passo 3: Disponibilização do Link
Assim que a ferramenta retornar o `job_id` e a URL do design criado no Canva:
- Forneça o link direto editável no Canva para o usuário.
- Se o usuário desejar alterações pontuais em textos ou números, utilize a skill `canva-edit-design`.

---

## 4. O Prompt Mestre Integrado

Se o usuário desejar gerar o conteúdo via prompt para usar em outros modelos ou no Canva Magic Design, consulte o arquivo de referência:
[master-prompt-template.md](./references/master-prompt-template.md)
