import os

HTML_SLIDE_1 = """<!DOCTYPE html>
<html lang="pt-BR">
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
    left: 120px;
    top: 180px;
    width: 860px;
    z-index: 10;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #331163;
    color: #E9D5FF;
    padding: 10px 22px;
    border-radius: 9999px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 28px;
  }
  .main-title {
    font-size: 96px;
    font-weight: 800;
    line-height: 0.98;
    letter-spacing: -3px;
    color: #FFFFFF;
    margin-bottom: 20px;
  }
  .subtitle {
    font-size: 32px;
    font-weight: 400;
    color: #F3E8FF;
    line-height: 1.35;
    margin-bottom: 36px;
    max-width: 760px;
  }
  .action-badge {
    display: inline-block;
    background: #280a52;
    color: #FFFFFF;
    padding: 14px 34px;
    border-radius: 9999px;
    font-size: 20px;
    font-weight: 600;
    box-shadow: 0 10px 25px rgba(40, 10, 82, 0.4);
    margin-bottom: 70px;
  }
  .authors-bar {
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    padding-top: 24px;
    font-size: 17px;
    color: #E9D5FF;
    letter-spacing: 0.5px;
  }
  .authors-bar strong {
    color: #FFFFFF;
  }
  
  /* Smartphone Showcase Right */
  .phones-container {
    position: absolute;
    right: 80px;
    top: 90px;
    width: 860px;
    height: 900px;
  }
  .phone-back {
    position: absolute;
    right: 320px;
    top: 100px;
    width: 330px;
    height: 680px;
    background: #180933;
    border-radius: 46px;
    border: 9px solid #2a1154;
    box-shadow: 0 35px 70px -15px rgba(20, 5, 50, 0.65);
    transform: rotate(-12deg);
    overflow: hidden;
    padding: 20px 18px;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .phone-front {
    position: absolute;
    right: 90px;
    top: 180px;
    width: 350px;
    height: 720px;
    background: #1c0a3d;
    border-radius: 50px;
    border: 10px solid #331463;
    box-shadow: 0 45px 85px -15px rgba(15, 3, 40, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.1) inset;
    transform: rotate(-4deg);
    overflow: hidden;
    padding: 24px 20px;
    display: flex;
    flex-direction: column;
    z-index: 5;
  }
  .notch {
    width: 110px;
    height: 22px;
    background: #0f0422;
    border-radius: 12px;
    margin: 0 auto 20px auto;
  }
  .app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  .app-header .app-title {
    font-size: 18px;
    font-weight: 700;
    color: #FFFFFF;
  }
  .app-header .app-tag {
    background: #FFC800;
    color: #000000;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 6px;
  }
  .app-stat-card {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 18px;
    margin-bottom: 14px;
  }
  .app-stat-val {
    font-size: 38px;
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1;
  }
  .app-stat-lbl {
    font-size: 13px;
    color: #DDD6FE;
    margin-top: 6px;
  }
  .mini-node {
    background: rgba(46, 16, 101, 0.7);
    border-left: 4px solid #FFC800;
    padding: 12px 14px;
    border-radius: 12px;
    font-size: 13px;
    margin-bottom: 10px;
  }
  .mini-node b { color: #FFFFFF; display: block; font-size: 14px; margin-bottom: 2px; }
  .mini-node span { color: #DDD6FE; }
</style>
</head>
<body>
  <div class="left-content">
    <div class="top-pill">Sistemas de Apoio à Decisão • UFS</div>
    <h1 class="main-title">KNIME<br>Analytics</h1>
    <p class="subtitle">Automação Analítica e Predição Preditiva de Churn em Telecomunicações</p>
    <div class="action-badge">Case Prático • Grupo 12</div>
    <div class="authors-bar">
      <strong>Equipe:</strong> Brenno Phelipe • David Santos • Gabriel Lima • Paulo Henrique
    </div>
  </div>

  <div class="phones-container">
    <div class="phone-back">
      <div class="notch"></div>
      <div class="app-header">
        <span class="app-title">Pipeline KNIME</span>
        <span class="app-tag">WORKFLOW</span>
      </div>
      <div class="mini-node">
        <b>CSV Reader</b>
        <span>1.200 Contratos Telecom</span>
      </div>
      <div class="mini-node">
        <b>Partitioning</b>
        <span>Divisão Estratificada 70/30</span>
      </div>
      <div class="mini-node">
        <b>Decision Tree</b>
        <span>Treino Supervisionado</span>
      </div>
      <div class="mini-node">
        <b>Scorer & Metrics</b>
        <span>Acurácia 87.2%</span>
      </div>
    </div>

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
      <div class="mini-node" style="border-left-color: #10B981; margin-top: auto; padding: 16px;">
        <b style="color: #10B981;">Ação Prescritiva Ativa</b>
        <span>Oferta automatizada disparada para 318 contas de alto risco.</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

HTML_SLIDE_2 = """<!DOCTYPE html>
<html lang="pt-BR">
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
    padding: 100px 120px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 8px 20px;
    border-radius: 9999px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 56px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 60px;
    max-width: 1100px;
  }
  .content-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 80px;
    align-items: center;
  }
  .stat-block {
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  .hero-metric-box {
    background: #331163;
    border-radius: 32px;
    padding: 40px 48px;
    box-shadow: 0 20px 45px rgba(40, 10, 82, 0.4);
    display: inline-block;
  }
  .metric-number {
    font-size: 115px;
    font-weight: 900;
    line-height: 0.95;
    letter-spacing: -4px;
    color: #FFFFFF;
  }
  .metric-label {
    font-size: 22px;
    font-weight: 500;
    color: #DDD6FE;
    margin-top: 10px;
  }
  .telegraphic-cards {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .card-item {
    background: rgba(51, 17, 99, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    padding: 20px 28px;
    display: flex;
    align-items: center;
    gap: 20px;
  }
  .card-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #EF4444;
    flex-shrink: 0;
  }
  .card-text {
    font-size: 20px;
    color: #FFFFFF;
  }
  .card-text strong {
    color: #FFFFFF;
    font-weight: 700;
  }
  
  /* Smartphone Frame */
  .phone-mockup {
    width: 380px;
    height: 640px;
    background: #1c0a3d;
    border-radius: 48px;
    border: 10px solid #331463;
    box-shadow: 0 35px 70px -15px rgba(20, 5, 50, 0.7);
    margin: 0 auto;
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .notch {
    width: 120px;
    height: 24px;
    background: #0f0422;
    border-radius: 12px;
    margin: 0 auto 10px auto;
  }
  .alert-banner {
    background: #EF4444;
    color: #FFFFFF;
    padding: 16px;
    border-radius: 18px;
    font-size: 15px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .alert-body {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .alert-body h4 { font-size: 18px; color: #FFFFFF; }
  .alert-body p { font-size: 14px; color: #DDD6FE; line-height: 1.4; }
  .action-btn {
    background: #FFFFFF;
    color: #1c0a3d;
    padding: 16px;
    border-radius: 16px;
    font-size: 16px;
    font-weight: 800;
    text-align: center;
    margin-top: auto;
  }
</style>
</head>
<body>
  <div class="top-pill">Diagnóstico Crítico • SAD Telecom</div>
  <h2 class="slide-title">26.5% de Churn Corrói a Margem no Modelo Tradicional</h2>

  <div class="content-grid">
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

    <div class="phone-mockup">
      <div class="notch"></div>
      <div class="alert-banner">
        <span>🚨</span> ALERTA DE EVASÃO
      </div>
      <div class="alert-body">
        <h4>Segmento Pré-Pago & Fibra</h4>
        <p>Modelo detectou alta probabilidade de cancelamento antes do encerramento do contrato.</p>
        <p><strong>Impacto:</strong> 318 assinantes em zona de saída imediata.</p>
      </div>
      <div class="action-btn">Acionar Retenção Prescritiva</div>
    </div>
  </div>
</body>
</html>
"""

HTML_SLIDE_3 = """<!DOCTYPE html>
<html lang="pt-BR">
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
    padding: 100px 120px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 8px 20px;
    border-radius: 9999px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 56px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 70px;
    max-width: 1200px;
  }
  .pillars-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    margin-bottom: 50px;
  }
  .pillar-card {
    background: #331163;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 32px;
    padding: 48px 36px;
    box-shadow: 0 20px 45px rgba(40, 10, 82, 0.4);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 480px;
  }
  .pillar-top {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .pillar-badge {
    align-self: flex-start;
    background: rgba(255, 255, 255, 0.12);
    color: #FFC800;
    font-size: 14px;
    font-weight: 800;
    padding: 6px 14px;
    border-radius: 9999px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .pillar-heading {
    font-size: 32px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.5px;
    line-height: 1.15;
  }
  .pillar-desc {
    font-size: 19px;
    color: #E9D5FF;
    line-height: 1.45;
  }
  .pillar-footer {
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    padding-top: 20px;
    font-size: 16px;
    font-weight: 700;
    color: #FFFFFF;
  }
  .bottom-badge {
    background: #280a52;
    padding: 16px 32px;
    border-radius: 20px;
    display: inline-flex;
    align-items: center;
    gap: 16px;
    font-size: 18px;
    color: #FFFFFF;
  }
  .bottom-badge strong {
    color: #FFC800;
  }
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
    <span>💡</span>
    <span>Validação no Caso SAD: <strong>87.2% de Acurácia</strong> obtida com a Árvore de Decisão no conjunto de teste.</span>
  </div>
</body>
</html>
"""

HTML_SLIDE_4 = """<!DOCTYPE html>
<html lang="pt-BR">
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
    padding: 100px 120px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 8px 20px;
    border-radius: 9999px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 56px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 70px;
    max-width: 1250px;
  }
  .steps-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 28px;
    margin-bottom: 50px;
  }
  .step-card {
    background: #331163;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 28px;
    padding: 36px 28px;
    box-shadow: 0 20px 45px rgba(40, 10, 82, 0.4);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 480px;
    position: relative;
  }
  .step-num {
    font-size: 48px;
    font-weight: 900;
    color: rgba(255, 255, 255, 0.25);
    line-height: 1;
    margin-bottom: 16px;
  }
  .step-node-badge {
    background: #FFC800;
    color: #000000;
    font-size: 12px;
    font-weight: 800;
    padding: 4px 10px;
    border-radius: 6px;
    align-self: flex-start;
    margin-bottom: 16px;
  }
  .step-title {
    font-size: 26px;
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1.2;
    margin-bottom: 12px;
  }
  .step-desc {
    font-size: 16px;
    color: #E9D5FF;
    line-height: 1.45;
  }
  .step-metric {
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    padding-top: 16px;
    font-size: 15px;
    font-weight: 700;
    color: #FFFFFF;
  }
  .footer-summary {
    background: #280a52;
    padding: 18px 36px;
    border-radius: 20px;
    font-size: 18px;
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
</html>
"""

HTML_SLIDE_5 = """<!DOCTYPE html>
<html lang="pt-BR">
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
    padding: 100px 120px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 8px 20px;
    border-radius: 9999px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 56px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 70px;
    max-width: 1200px;
  }
  .split-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
    margin-bottom: 50px;
  }
  .split-card {
    border-radius: 32px;
    padding: 48px;
    box-shadow: 0 20px 45px rgba(40, 10, 82, 0.4);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 500px;
  }
  .card-reactive {
    background: #331163;
    border: 1px solid rgba(239, 68, 68, 0.4);
  }
  .card-predictive {
    background: #23084a;
    border: 2px solid #FFC800;
  }
  .badge-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;
    border-radius: 9999px;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 24px;
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
    font-size: 34px;
    font-weight: 800;
    color: #FFFFFF;
    line-height: 1.15;
    margin-bottom: 28px;
  }
  .bullet-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }
  .bullet-item {
    font-size: 19px;
    color: #E9D5FF;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .bullet-item strong {
    color: #FFFFFF;
  }
  .split-footer {
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 24px;
    font-size: 20px;
    font-weight: 800;
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
          <div class="bullet-item">❌ <strong>Ação Tardia:</strong> Contato após o pedido de cancelamento.</div>
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
</html>
"""

HTML_SLIDE_6 = """<!DOCTYPE html>
<html lang="pt-BR">
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
    padding: 100px 120px;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 8px 20px;
    border-radius: 9999px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 56px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 60px;
    max-width: 1200px;
  }
  .content-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 80px;
    align-items: center;
  }
  .deliverables-box {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .item-card {
    background: #331163;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 22px;
    padding: 24px 30px;
    box-shadow: 0 15px 35px rgba(40, 10, 82, 0.35);
  }
  .item-card h4 {
    font-size: 22px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .item-card p {
    font-size: 17px;
    color: #E9D5FF;
    line-height: 1.4;
  }
  .repo-link-box {
    background: #280a52;
    border-radius: 18px;
    padding: 18px 24px;
    font-size: 18px;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 14px;
    margin-top: 10px;
  }
  .repo-link-box span { color: #FFC800; font-weight: 700; }

  /* Smartphone Frame with QR */
  .phone-mockup {
    width: 380px;
    height: 640px;
    background: #1c0a3d;
    border-radius: 48px;
    border: 10px solid #331463;
    box-shadow: 0 35px 70px -15px rgba(20, 5, 50, 0.7);
    margin: 0 auto;
    padding: 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
  }
  .notch {
    width: 120px;
    height: 24px;
    background: #0f0422;
    border-radius: 12px;
  }
  .qr-wrapper {
    background: #FFFFFF;
    padding: 16px;
    border-radius: 24px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  }
  .qr-img {
    width: 210px;
    height: 210px;
    display: block;
  }
  .phone-info {
    text-align: center;
  }
  .phone-info h5 {
    font-size: 18px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 6px;
  }
  .phone-info p {
    font-size: 13px;
    color: #DDD6FE;
  }
</style>
</head>
<body>
  <div class="top-pill">Entrega Obrigatória & Avaliação</div>
  <h2 class="slide-title">Código Aberto, Governança Total e Retorno Imediato</h2>

  <div class="content-grid">
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
  </div>
</body>
</html>
"""

with open("slides/purple_theme_html/slide_1.html", "w") as f:
    f.write(HTML_SLIDE_1)
with open("slides/purple_theme_html/slide_2.html", "w") as f:
    f.write(HTML_SLIDE_2)
with open("slides/purple_theme_html/slide_3.html", "w") as f:
    f.write(HTML_SLIDE_3)
with open("slides/purple_theme_html/slide_4.html", "w") as f:
    f.write(HTML_SLIDE_4)
with open("slides/purple_theme_html/slide_5.html", "w") as f:
    f.write(HTML_SLIDE_5)
with open("slides/purple_theme_html/slide_6.html", "w") as f:
    f.write(HTML_SLIDE_6)

print("All 6 purple theme slide HTML files created successfully!")
