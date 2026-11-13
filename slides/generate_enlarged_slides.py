import os

# Slide 1 Background (Left content enlarged, no phones)
HTML_SLIDE_1_BG = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 1920px;
    height: 1080px;
    background: #895bf6;
    overflow: hidden;
    position: relative;
    color: #FFFFFF;
  }
  .left-content {
    position: absolute;
    left: 80px;
    top: 110px;
    width: 1000px;
    z-index: 10;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 14px 28px;
    border-radius: 9999px;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 28px;
  }
  .main-title {
    font-size: 115px;
    font-weight: 900;
    line-height: 0.94;
    letter-spacing: -4px;
    color: #FFFFFF;
    margin-bottom: 24px;
  }
  .subtitle {
    font-size: 38px;
    font-weight: 500;
    color: #F3E8FF;
    line-height: 1.3;
    margin-bottom: 40px;
    max-width: 900px;
  }
  .action-badge {
    display: inline-block;
    background: #280a52;
    color: #FFFFFF;
    padding: 18px 42px;
    border-radius: 9999px;
    font-size: 24px;
    font-weight: 700;
    box-shadow: 0 12px 30px rgba(40, 10, 82, 0.45);
    margin-bottom: 80px;
  }
  .authors-bar {
    border-top: 2px solid rgba(255, 255, 255, 0.25);
    padding-top: 28px;
    font-size: 21px;
    color: #E9D5FF;
    letter-spacing: 0.5px;
  }
  .authors-bar strong { color: #FFFFFF; }
</style>
</head>
<body>
  <div class="left-content">
    <div class="top-pill">Sistemas de Apoio à Decisão • UFS</div>
    <h1 class="main-title">KNIME<br>Analytics</h1>
    <p class="subtitle">Automação Analítica e Predição de Churn em Telecomunicações</p>
    <div class="action-badge">Case Prático • Grupo 12</div>
    <div class="authors-bar">
      <strong>Equipe:</strong> Brenno Phelipe • David Santos • Gabriel Lima • Paulo Henrique
    </div>
  </div>
</body>
</html>"""

# Phone 1 (Back) Enlarged (width 440px, height 860px)
HTML_PHONE_BACK = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 480px;
    height: 920px;
    background: transparent;
    overflow: hidden;
    padding: 20px;
  }
  .phone-back {
    width: 440px;
    height: 870px;
    background: #180933;
    border-radius: 54px;
    border: 11px solid #2a1154;
    box-shadow: 0 35px 70px -15px rgba(20, 5, 50, 0.75);
    overflow: hidden;
    padding: 26px 24px;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }
  .notch {
    width: 140px;
    height: 26px;
    background: #0f0422;
    border-radius: 14px;
    margin: 0 auto 20px auto;
  }
  .app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  .app-title { font-size: 22px; font-weight: 800; color: #FFFFFF; }
  .app-tag {
    background: #FFC800;
    color: #000;
    font-size: 13px;
    font-weight: 900;
    padding: 5px 12px;
    border-radius: 8px;
  }
  .mini-node {
    background: rgba(46, 16, 101, 0.75);
    border-left: 6px solid #FFC800;
    padding: 16px 20px;
    border-radius: 16px;
    font-size: 16px;
  }
  .mini-node b { color: #FFFFFF; display: block; font-size: 18px; margin-bottom: 4px; }
  .mini-node span { color: #DDD6FE; font-size: 15px; }
</style>
</head>
<body>
  <div class="phone-back">
    <div class="notch"></div>
    <div class="app-header">
      <span class="app-title">Pipeline KNIME</span>
      <span class="app-tag">WORKFLOW</span>
    </div>
    <div class="mini-node"><b>CSV Reader</b><span>1.200 Contratos Telecom</span></div>
    <div class="mini-node"><b>Partitioning Node</b><span>Divisão Estratificada 70/30</span></div>
    <div class="mini-node"><b>Decision Tree Learner</b><span>Treino Supervisionado</span></div>
    <div class="mini-node"><b>Scorer & Metrics</b><span>Acurácia de 87.2%</span></div>
  </div>
</body>
</html>"""

# Phone 2 (Front) Enlarged (width 470px, height 900px)
HTML_PHONE_FRONT = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 510px;
    height: 950px;
    background: transparent;
    overflow: hidden;
    padding: 20px;
  }
  .phone-front {
    width: 470px;
    height: 900px;
    background: #1c0a3d;
    border-radius: 56px;
    border: 12px solid #331463;
    box-shadow: 0 45px 85px -15px rgba(15, 3, 40, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.15) inset;
    overflow: hidden;
    padding: 28px 24px;
    display: flex;
    flex-direction: column;
  }
  .notch {
    width: 140px;
    height: 26px;
    background: #0f0422;
    border-radius: 14px;
    margin: 0 auto 24px auto;
  }
  .app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
  }
  .app-title { font-size: 24px; font-weight: 800; color: #FFFFFF; }
  .app-tag {
    background: #FFC800;
    color: #000;
    font-size: 13px;
    font-weight: 900;
    padding: 5px 12px;
    border-radius: 8px;
  }
  .app-stat-card {
    background: rgba(255, 255, 255, 0.09);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 20px;
  }
  .app-stat-val { font-size: 52px; font-weight: 900; color: #FFFFFF; line-height: 1; }
  .app-stat-lbl { font-size: 17px; color: #DDD6FE; margin-top: 8px; }
  .mini-node {
    background: rgba(46, 16, 101, 0.8);
    border-left: 6px solid #10B981;
    padding: 22px;
    border-radius: 18px;
    margin-top: auto;
  }
  .mini-node b { color: #10B981; display: block; font-size: 19px; margin-bottom: 4px; }
  .mini-node span { color: #DDD6FE; font-size: 15px; }
</style>
</head>
<body>
  <div class="phone-front">
    <div class="notch"></div>
    <div class="app-header">
      <span class="app-title">SAD Telecom</span>
      <span class="app-tag">PREDITIVO</span>
    </div>
    <div class="app-stat-card">
      <div class="app-stat-val">26.5%</div>
      <div class="app-stat-lbl">Taxa de Churn Diagnosticada</div>
    </div>
    <div class="app-stat-card">
      <div class="app-stat-val">87.2%</div>
      <div class="app-stat-lbl">Acurácia na Retenção Preventiva</div>
    </div>
    <div class="mini-node">
      <b>Ação Prescritiva Ativa</b>
      <span>Gatilho de oferta preventiva disparado para 318 contas críticas.</span>
    </div>
  </div>
</body>
</html>"""

# Slide 2 Background (Enlarged Hero Stat + 3 Big Cards)
HTML_SLIDE_2_BG = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 1920px;
    height: 1080px;
    background: #895bf6;
    overflow: hidden;
    position: relative;
    color: #FFFFFF;
    padding: 60px 80px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 10px 24px;
    border-radius: 9999px;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 64px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 45px;
    max-width: 1400px;
  }
  .stat-block {
    width: 1060px;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  .hero-metric-box {
    background: #331163;
    border-radius: 36px;
    padding: 44px 56px;
    box-shadow: 0 25px 50px rgba(40, 10, 82, 0.45);
    display: inline-block;
  }
  .metric-number {
    font-size: 155px;
    font-weight: 900;
    line-height: 0.9;
    letter-spacing: -5px;
    color: #FFFFFF;
  }
  .metric-label {
    font-size: 28px;
    font-weight: 600;
    color: #DDD6FE;
    margin-top: 14px;
  }
  .telegraphic-cards {
    display: flex;
    flex-direction: column;
    gap: 18px;
  }
  .card-item {
    background: rgba(51, 17, 99, 0.6);
    border: 2px solid rgba(255, 255, 255, 0.18);
    border-radius: 24px;
    padding: 24px 34px;
    display: flex;
    align-items: center;
    gap: 22px;
  }
  .card-dot {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #EF4444;
    flex-shrink: 0;
  }
  .card-text { font-size: 25px; color: #FFFFFF; line-height: 1.3; }
</style>
</head>
<body>
  <div class="top-pill">Diagnóstico Crítico • SAD Telecom</div>
  <h2 class="slide-title">26.5% de Churn Corrói a Margem no Modelo Tradicional</h2>

  <div class="stat-block">
    <div class="hero-metric-box">
      <div class="metric-number">26.5%</div>
      <div class="metric-label">Taxa semestral de cancelamento na base ativa</div>
    </div>
    <div class="telegraphic-cards">
      <div class="card-item">
        <div class="card-dot"></div>
        <div class="card-text"><strong>R$ 28.000 / mês:</strong> Perda direta de faturamento recorrente.</div>
      </div>
      <div class="card-item">
        <div class="card-dot" style="background: #F59E0B;"></div>
        <div class="card-text"><strong>318 Contas Críticas:</strong> Concentradas em clientes sem fibra ótica.</div>
      </div>
      <div class="card-item">
        <div class="card-dot" style="background: #E9D5FF;"></div>
        <div class="card-text"><strong>Abordagem Tardia:</strong> Ações reativas retêm menos de 18% dos clientes.</div>
      </div>
    </div>
  </div>
</body>
</html>"""

# Phone Alert Enlarged (width 490px, height 860px)
HTML_PHONE_ALERT = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 530px;
    height: 900px;
    background: transparent;
    overflow: hidden;
    padding: 20px;
  }
  .phone-mockup {
    width: 490px;
    height: 860px;
    background: #1c0a3d;
    border-radius: 56px;
    border: 12px solid #331463;
    box-shadow: 0 40px 80px -15px rgba(20, 5, 50, 0.85);
    margin: 0 auto;
    padding: 30px;
    display: flex;
    flex-direction: column;
    gap: 26px;
  }
  .notch {
    width: 140px;
    height: 28px;
    background: #0f0422;
    border-radius: 14px;
    margin: 0 auto 14px auto;
  }
  .alert-banner {
    background: #EF4444;
    color: #FFFFFF;
    padding: 20px 24px;
    border-radius: 22px;
    font-size: 20px;
    font-weight: 800;
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .alert-body {
    background: rgba(255, 255, 255, 0.09);
    border-radius: 24px;
    padding: 28px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .alert-body h4 { font-size: 24px; font-weight: 800; color: #FFFFFF; }
  .alert-body p { font-size: 18px; color: #DDD6FE; line-height: 1.45; }
  .action-btn {
    background: #FFFFFF;
    color: #1c0a3d;
    padding: 22px;
    border-radius: 20px;
    font-size: 20px;
    font-weight: 900;
    text-align: center;
    margin-top: auto;
  }
</style>
</head>
<body>
  <div class="phone-mockup">
    <div class="notch"></div>
    <div class="alert-banner">
      <span style="font-size: 24px;">🚨</span> ALERTA DE EVASÃO
    </div>
    <div class="alert-body">
      <h4>Segmento Pré-Pago & Fibra</h4>
      <p>Modelo preditivo detectou alta propensão de cancelamento antes do fim do ciclo.</p>
      <p><strong>Impacto:</strong> 318 assinantes em zona de saída imediata.</p>
    </div>
    <div class="action-btn">Acionar Retenção Prescritiva</div>
  </div>
</body>
</html>"""

# Slide 3 (Enlarged 3 Pillars Filling the Screen)
HTML_SLIDE_3 = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 1920px;
    height: 1080px;
    background: #895bf6;
    overflow: hidden;
    position: relative;
    color: #FFFFFF;
    padding: 60px 80px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 10px 24px;
    border-radius: 9999px;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 64px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 45px;
    max-width: 1500px;
  }
  .pillars-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 36px;
    margin-bottom: 35px;
  }
  .pillar-card {
    background: #331163;
    border: 2px solid rgba(255, 255, 255, 0.18);
    border-radius: 36px;
    padding: 52px 42px;
    box-shadow: 0 25px 50px rgba(40, 10, 82, 0.45);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 610px;
  }
  .pillar-top {
    display: flex;
    flex-direction: column;
    gap: 24px;
  }
  .pillar-badge {
    align-self: flex-start;
    background: rgba(255, 255, 255, 0.15);
    color: #FFC800;
    font-size: 16px;
    font-weight: 900;
    padding: 8px 18px;
    border-radius: 9999px;
    letter-spacing: 1.2px;
    text-transform: uppercase;
  }
  .pillar-heading {
    font-size: 38px;
    font-weight: 900;
    color: #FFFFFF;
    letter-spacing: -0.5px;
    line-height: 1.15;
  }
  .pillar-desc {
    font-size: 22px;
    color: #E9D5FF;
    line-height: 1.5;
  }
  .pillar-footer {
    border-top: 2px solid rgba(255, 255, 255, 0.15);
    padding-top: 24px;
    font-size: 20px;
    font-weight: 800;
    color: #FFFFFF;
  }
  .bottom-badge {
    background: #280a52;
    padding: 20px 40px;
    border-radius: 24px;
    display: inline-flex;
    align-items: center;
    gap: 20px;
    font-size: 22px;
    color: #FFFFFF;
  }
  .bottom-badge strong { color: #FFC800; }
</style>
</head>
<body>
  <div class="top-pill">Arquitetura & Vantagens Competitivas</div>
  <h2 class="slide-title">KNIME Reduz o Custo Analítico em 80% sem Lock-in</h2>

  <div class="pillars-container">
    <div class="pillar-card">
      <div class="pillar-top">
        <div class="pillar-badge">Low-Code Visual</div>
        <h3 class="pillar-heading">Automação Sem Código Frágil</h3>
        <p class="pillar-desc">Fluxos modulares e intuitivos que unificam ETL e Machine Learning sem demandar scripts complexos.</p>
      </div>
      <div class="pillar-footer">⚡ 4x mais rápido no deploy analítico</div>
    </div>

    <div class="pillar-card">
      <div class="pillar-top">
        <div class="pillar-badge">Stack Híbrida</div>
        <h3 class="pillar-heading">Python, R e SQL Nativos</h3>
        <p class="pillar-desc">Conexão transparente com bancos corporativos, bibliotecas de Data Science e APIs REST sem barreiras.</p>
      </div>
      <div class="pillar-footer">🔗 Interoperabilidade sem dependência</div>
    </div>

    <div class="pillar-card">
      <div class="pillar-top">
        <div class="pillar-badge">Governança</div>
        <h3 class="pillar-heading">Auditabilidade & Custo Zero</h3>
        <p class="pillar-desc">Workflows 100% versionáveis e abertos, garantindo conformidade com a LGPD e eliminando licenças proprietárias.</p>
      </div>
      <div class="pillar-footer">🛡️ Zero custo de licença anual</div>
    </div>
  </div>

  <div class="bottom-badge">
    <span style="font-size: 26px;">💡</span>
    <span>Validação no Caso SAD: <strong>87.2% de Acurácia</strong> obtida com a Árvore de Decisão no conjunto de teste.</span>
  </div>
</body>
</html>"""

# Slide 4 (Enlarged 4 Steps Filling the Screen)
HTML_SLIDE_4 = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 1920px;
    height: 1080px;
    background: #895bf6;
    overflow: hidden;
    position: relative;
    color: #FFFFFF;
    padding: 60px 80px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 10px 24px;
    border-radius: 9999px;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 64px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 45px;
    max-width: 1550px;
  }
  .steps-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 26px;
    margin-bottom: 35px;
  }
  .step-card {
    background: #331163;
    border: 2px solid rgba(255, 255, 255, 0.18);
    border-radius: 32px;
    padding: 42px 32px;
    box-shadow: 0 25px 50px rgba(40, 10, 82, 0.45);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 610px;
  }
  .step-num {
    font-size: 64px;
    font-weight: 900;
    color: rgba(255, 255, 255, 0.3);
    line-height: 1;
    margin-bottom: 18px;
  }
  .step-node-badge {
    background: #FFC800;
    color: #000000;
    font-size: 14px;
    font-weight: 900;
    padding: 6px 12px;
    border-radius: 8px;
    align-self: flex-start;
    margin-bottom: 18px;
  }
  .step-title {
    font-size: 32px;
    font-weight: 900;
    color: #FFFFFF;
    line-height: 1.2;
    margin-bottom: 16px;
  }
  .step-desc {
    font-size: 20px;
    color: #E9D5FF;
    line-height: 1.5;
  }
  .step-metric {
    border-top: 2px solid rgba(255, 255, 255, 0.15);
    padding-top: 20px;
    font-size: 18px;
    font-weight: 800;
    color: #FFFFFF;
  }
  .footer-summary {
    background: #280a52;
    padding: 22px 42px;
    border-radius: 24px;
    font-size: 22px;
    color: #FFFFFF;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .footer-summary b { color: #FFC800; }
</style>
</head>
<body>
  <div class="top-pill">Esteira Operacional no KNIME</div>
  <h2 class="slide-title">Pipeline End-to-End: Do Dado Bruto à Ação Prescritiva</h2>

  <div class="steps-grid">
    <div class="step-card">
      <div>
        <div class="step-num">01</div>
        <div class="step-node-badge">CSV Reader + Missing</div>
        <h3 class="step-title">Ingestão & Limpeza</h3>
        <p class="step-desc">Tratamento de 1.200 contratos de clientes, eliminação de valores nulos e tipagem de variáveis.</p>
      </div>
      <div class="step-metric">📦 1.200 Linhas Processadas</div>
    </div>

    <div class="step-card">
      <div>
        <div class="step-num">02</div>
        <div class="step-node-badge">Partitioning Node</div>
        <h3 class="step-title">Divisão 70 / 30</h3>
        <p class="step-desc">Particionamento estratificado para garantir proporção equilibrada de cancelamentos no treino e teste.</p>
      </div>
      <div class="step-metric">⚖️ 840 Treino • 360 Teste</div>
    </div>

    <div class="step-card">
      <div>
        <div class="step-num">03</div>
        <div class="step-node-badge">Decision Tree + Scorer</div>
        <h3 class="step-title">Árvore de Decisão</h3>
        <p class="step-desc">Treinamento de modelo preditivo transparente com cálculo de matriz de confusão e acurácia.</p>
      </div>
      <div class="step-metric">🎯 87.2% de Acurácia</div>
    </div>

    <div class="step-card">
      <div>
        <div class="step-num">04</div>
        <div class="step-node-badge">Rule Engine + View</div>
        <h3 class="step-title">Ação Prescritiva</h3>
        <p class="step-desc">Geração de regras de negócio automatizadas para retenção prioritária de clientes de alto risco.</p>
      </div>
      <div class="step-metric">🚀 R$ 22.400 / mês Preservados</div>
    </div>
  </div>

  <div class="footer-summary">
    <span>Pipeline Executável: <b>churn_prediction_sad.knwf</b></span>
    <span>Sem dependências externas • Execução local reproduzível</span>
  </div>
</body>
</html>"""

# Slide 5 (Enlarged Split 50/50 Filling the Screen)
HTML_SLIDE_5 = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 1920px;
    height: 1080px;
    background: #895bf6;
    overflow: hidden;
    position: relative;
    color: #FFFFFF;
    padding: 60px 80px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 10px 24px;
    border-radius: 9999px;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 64px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 45px;
    max-width: 1400px;
  }
  .split-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
  }
  .split-card {
    border-radius: 36px;
    padding: 56px 48px;
    box-shadow: 0 25px 50px rgba(40, 10, 82, 0.45);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 640px;
  }
  .card-reactive {
    background: #331163;
    border: 2px solid rgba(239, 68, 68, 0.45);
  }
  .card-predictive {
    background: #23084a;
    border: 3px solid #FFC800;
  }
  .badge-tag {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 10px 22px;
    border-radius: 9999px;
    font-size: 16px;
    font-weight: 900;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 28px;
  }
  .badge-reactive {
    background: rgba(239, 68, 68, 0.2);
    color: #FCA5A5;
  }
  .badge-predictive {
    background: rgba(255, 200, 0, 0.2);
    color: #FFC800;
  }
  .split-card h3 {
    font-size: 42px;
    font-weight: 900;
    color: #FFFFFF;
    line-height: 1.15;
    margin-bottom: 32px;
  }
  .bullet-list {
    display: flex;
    flex-direction: column;
    gap: 22px;
  }
  .bullet-item {
    font-size: 24px;
    color: #E9D5FF;
    display: flex;
    align-items: center;
    gap: 16px;
    line-height: 1.4;
  }
  .bullet-item strong { color: #FFFFFF; }
  .split-footer {
    border-top: 2px solid rgba(255, 255, 255, 0.18);
    padding-top: 28px;
    font-size: 26px;
    font-weight: 900;
  }
  .split-footer.danger { color: #FCA5A5; }
  .split-footer.success { color: #34D399; }
</style>
</head>
<body>
  <div class="top-pill">Impacto no Apoio à Decisão</div>
  <h2 class="slide-title">Da Operação Cega à Retenção Prescritiva</h2>

  <div class="split-grid">
    <div class="split-card card-reactive">
      <div>
        <div class="badge-tag badge-reactive">Abordagem Tradicional</div>
        <h3>Reativa e Descentralizada</h3>
        <div class="bullet-list">
          <div class="bullet-item">❌ <strong>Ação Tardia:</strong> Contato após o pedido formal de cancelamento.</div>
          <div class="bullet-item">❌ <strong>Desconto Genérico:</strong> Corrói a margem sem reter o assinante.</div>
          <div class="bullet-item">❌ <strong>Decisão sem Dados:</strong> Perda sem rastreabilidade de causa raiz.</div>
        </div>
      </div>
      <div class="split-footer danger">Perda contínua de R$ 28.000 / mês</div>
    </div>

    <div class="split-card card-predictive">
      <div>
        <div class="badge-tag badge-predictive">Com KNIME Analytics</div>
        <h3>Preditiva e Prescritiva</h3>
        <div class="bullet-list">
          <div class="bullet-item">✅ <strong>Antecipação:</strong> Detecção do risco 15 dias antes da evasão.</div>
          <div class="bullet-item">✅ <strong>Oferta Direcionada:</strong> Regras automáticas por perfil de uso.</div>
          <div class="bullet-item">✅ <strong>Decisão Auditável:</strong> Árvore de decisão clara e justificável.</div>
        </div>
      </div>
      <div class="split-footer success">Economia líquida de R$ 22.400 / mês</div>
    </div>
  </div>
</body>
</html>"""

# Slide 6 Background (Enlarged Deliverables, No Phone)
HTML_SLIDE_6_BG = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 1920px;
    height: 1080px;
    background: #895bf6;
    overflow: hidden;
    position: relative;
    color: #FFFFFF;
    padding: 60px 80px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 10px 24px;
    border-radius: 9999px;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 64px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 45px;
    max-width: 1400px;
  }
  .deliverables-box {
    width: 1060px;
    display: flex;
    flex-direction: column;
    gap: 22px;
  }
  .item-card {
    background: #331163;
    border: 2px solid rgba(255, 255, 255, 0.18);
    border-radius: 28px;
    padding: 30px 38px;
    box-shadow: 0 20px 45px rgba(40, 10, 82, 0.4);
  }
  .item-card h4 {
    font-size: 26px;
    font-weight: 900;
    color: #FFFFFF;
    margin-bottom: 8px;
  }
  .item-card p {
    font-size: 20px;
    color: #E9D5FF;
    line-height: 1.45;
  }
  .repo-link-box {
    background: #280a52;
    border-radius: 22px;
    padding: 22px 32px;
    font-size: 22px;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-top: 10px;
  }
  .repo-link-box span { color: #FFC800; font-weight: 900; }
</style>
</head>
<body>
  <div class="top-pill">Entrega Obrigatória & Avaliação</div>
  <h2 class="slide-title">Código Aberto, Governança Total e Retorno Imediato</h2>

  <div class="deliverables-box">
    <div class="item-card">
      <h4>📁 Workflow KNIME Executável</h4>
      <p>Arquivo <code>churn_prediction_sad.knwf</code> com pipeline completa, visualizações e regras de negócio.</p>
    </div>
    <div class="item-card">
      <h4>📊 Base de Dados & Dicionário</h4>
      <p>1.200 contratos higienizados em CSV e documentação de metadados das variáveis preditivas.</p>
    </div>
    <div class="item-card">
      <h4>📑 100% de Cobertura do Barema</h4>
      <p>Atendimento integral aos requisitos técnicos, práticos e temporais da disciplina de SAD (UFS).</p>
    </div>
    <div class="repo-link-box">
      <span>🔗 GitHub:</span>
      <code>github.com/BrennoPh/ProjetoBI-KNIME-SAD</code>
    </div>
  </div>
</body>
</html>"""

# Phone QR Enlarged (width 490px, height 860px, QR size 280px)
HTML_PHONE_QR = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 530px;
    height: 900px;
    background: transparent;
    overflow: hidden;
    padding: 20px;
  }
  .phone-mockup {
    width: 490px;
    height: 860px;
    background: #1c0a3d;
    border-radius: 56px;
    border: 12px solid #331463;
    box-shadow: 0 40px 80px -15px rgba(20, 5, 50, 0.85);
    margin: 0 auto;
    padding: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
  }
  .notch {
    width: 140px;
    height: 28px;
    background: #0f0422;
    border-radius: 14px;
  }
  .qr-wrapper {
    background: #FFFFFF;
    padding: 20px;
    border-radius: 30px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.35);
  }
  .qr-img { width: 280px; height: 280px; display: block; }
  .phone-info { text-align: center; }
  .phone-info h5 { font-size: 24px; font-weight: 900; color: #FFFFFF; margin-bottom: 8px; }
  .phone-info p { font-size: 16px; color: #DDD6FE; line-height: 1.4; }
</style>
</head>
<body>
  <div class="phone-mockup">
    <div class="notch"></div>
    <div class="qr-wrapper">
      <img class="qr-img" src="../purple_theme_images/qrcode_github.png" alt="QR Code GitHub">
    </div>
    <div class="phone-info">
      <h5>Acesse o Repositório</h5>
      <p>Aponte a câmera para inspecionar o workflow, os dados e a documentação completa.</p>
    </div>
  </div>
</body>
</html>"""

files = {
    "slides/enlarged_html/slide_1_bg.html": HTML_SLIDE_1_BG,
    "slides/enlarged_html/phone_back.html": HTML_PHONE_BACK,
    "slides/enlarged_html/phone_front.html": HTML_PHONE_FRONT,
    "slides/enlarged_html/slide_2_bg.html": HTML_SLIDE_2_BG,
    "slides/enlarged_html/phone_alert.html": HTML_PHONE_ALERT,
    "slides/enlarged_html/slide_3.html": HTML_SLIDE_3,
    "slides/enlarged_html/slide_4.html": HTML_SLIDE_4,
    "slides/enlarged_html/slide_5.html": HTML_SLIDE_5,
    "slides/enlarged_html/slide_6_bg.html": HTML_SLIDE_6_BG,
    "slides/enlarged_html/phone_qr.html": HTML_PHONE_QR,
}

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("Enlarged slide HTML files created!")
