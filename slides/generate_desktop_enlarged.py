import os

HTML_SLIDE_1 = """<!DOCTYPE html>
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
    padding: 70px 90px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .top-pill {
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 14px 32px;
    border-radius: 9999px;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .hero-box {
    margin: 20px 0;
  }
  .main-title {
    font-size: 110px;
    font-weight: 900;
    line-height: 0.95;
    letter-spacing: -4px;
    color: #FFFFFF;
    margin-bottom: 24px;
  }
  .subtitle {
    font-size: 40px;
    font-weight: 600;
    color: #F3E8FF;
    line-height: 1.3;
    margin-bottom: 35px;
    max-width: 1500px;
  }
  .badge-tag {
    display: inline-block;
    background: #280a52;
    color: #FFFFFF;
    padding: 18px 42px;
    border-radius: 9999px;
    font-size: 24px;
    font-weight: 800;
    box-shadow: 0 15px 35px rgba(40, 10, 82, 0.5);
  }
  .badge-tag span { color: #FFC800; }
  .bottom-card {
    background: #331163;
    border: 2px solid rgba(255, 255, 255, 0.2);
    border-radius: 28px;
    padding: 28px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .team-names {
    font-size: 26px;
    font-weight: 800;
    color: #FFFFFF;
  }
  .team-names span { color: #E9D5FF; font-weight: 600; }
  .inst-name {
    font-size: 22px;
    font-weight: 700;
    color: #DDD6FE;
  }
</style>
</head>
<body>
  <div class="top-pill">Sistemas de Apoio à Decisão • UFS</div>
  <div class="hero-box">
    <h1 class="main-title">KNIME Analytics Platform</h1>
    <p class="subtitle">Automação Analítica e Predição de Churn em Telecomunicações</p>
    <div class="badge-tag">Case Prático: <span>Predição & Retenção de Churn (1.200 Contratos)</span></div>
  </div>
  <div class="bottom-card">
    <div class="team-names">Equipe Técnica: <span>Brenno Phelipe • David Santos • Gabriel Lima • Paulo Henrique</span></div>
    <div class="inst-name">UFS • DSI / SAD 2026</div>
  </div>
</body>
</html>"""

HTML_SLIDE_2 = """<!DOCTYPE html>
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
    padding: 12px 28px;
    border-radius: 9999px;
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 68px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 45px;
    max-width: 1600px;
  }
  .grid-container {
    display: grid;
    grid-template-columns: 0.95fr 1.05fr;
    gap: 45px;
    align-items: stretch;
  }
  .hero-metric-box {
    background: #331163;
    border: 3px solid rgba(255, 255, 255, 0.2);
    border-radius: 40px;
    padding: 50px 40px;
    box-shadow: 0 25px 60px rgba(40, 10, 82, 0.5);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    height: 640px;
  }
  .metric-number {
    font-size: 190px;
    font-weight: 900;
    line-height: 0.85;
    letter-spacing: -6px;
    color: #FFFFFF;
  }
  .metric-label {
    font-size: 34px;
    font-weight: 700;
    color: #DDD6FE;
    margin-top: 24px;
  }
  .metric-sub {
    font-size: 26px;
    font-weight: 800;
    color: #FFC800;
    margin-top: 12px;
  }
  .cards-column {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 640px;
    gap: 20px;
  }
  .card-item {
    background: #331163;
    border: 2px solid rgba(255, 255, 255, 0.2);
    border-radius: 30px;
    padding: 34px 40px;
    display: flex;
    align-items: center;
    gap: 24px;
    flex: 1;
    box-shadow: 0 15px 35px rgba(40, 10, 82, 0.35);
  }
  .card-dot {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: #EF4444;
    flex-shrink: 0;
  }
  .card-text {
    font-size: 28px;
    color: #FFFFFF;
    line-height: 1.35;
  }
  .card-text strong { color: #FFFFFF; font-weight: 900; }
</style>
</head>
<body>
  <div class="top-pill">Diagnóstico Crítico do Negócio</div>
  <h2 class="slide-title">26.5% de Churn Reduz a Margem Operacional</h2>

  <div class="grid-container">
    <div class="hero-metric-box">
      <div class="metric-number">26.5%</div>
      <div class="metric-label">Taxa Semestral de Evasão na Base</div>
      <div class="metric-sub">318 Clientes Perdidos sem Intervenção</div>
    </div>

    <div class="cards-column">
      <div class="card-item">
        <div class="card-dot"></div>
        <div class="card-text"><strong>R$ 28.000 / mês:</strong> Perda direta de faturamento recorrente na base.</div>
      </div>
      <div class="card-item">
        <div class="card-dot" style="background: #F59E0B;"></div>
        <div class="card-text"><strong>318 Contas Críticas:</strong> Concentradas no plano mensal sem fibra ótica.</div>
      </div>
      <div class="card-item">
        <div class="card-dot" style="background: #E9D5FF;"></div>
        <div class="card-text"><strong>Decisão Tardia:</strong> Ações manuais reativas perdem mais de 82% dos clientes.</div>
      </div>
    </div>
  </div>
</body>
</html>"""

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
    padding: 12px 28px;
    border-radius: 9999px;
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 68px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 45px;
    max-width: 1600px;
  }
  .pillars-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 36px;
    margin-bottom: 35px;
  }
  .pillar-card {
    background: #331163;
    border: 3px solid rgba(255, 255, 255, 0.2);
    border-radius: 36px;
    padding: 50px 42px;
    box-shadow: 0 25px 60px rgba(40, 10, 82, 0.5);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 610px;
  }
  .pillar-top {
    display: flex;
    flex-direction: column;
    gap: 22px;
  }
  .pillar-badge {
    align-self: flex-start;
    background: rgba(255, 255, 255, 0.15);
    color: #FFC800;
    font-size: 18px;
    font-weight: 900;
    padding: 10px 22px;
    border-radius: 9999px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }
  .pillar-heading {
    font-size: 42px;
    font-weight: 900;
    color: #FFFFFF;
    letter-spacing: -0.5px;
    line-height: 1.15;
  }
  .pillar-desc {
    font-size: 26px;
    color: #E9D5FF;
    line-height: 1.5;
  }
  .pillar-footer {
    border-top: 2px solid rgba(255, 255, 255, 0.18);
    padding-top: 24px;
    font-size: 24px;
    font-weight: 900;
    color: #FFFFFF;
  }
  .bottom-badge {
    background: #280a52;
    padding: 22px 42px;
    border-radius: 24px;
    display: inline-flex;
    align-items: center;
    gap: 20px;
    font-size: 24px;
    color: #FFFFFF;
    font-weight: 700;
  }
  .bottom-badge strong { color: #FFC800; }
</style>
</head>
<body>
  <div class="top-pill">Vantagens Competitivas & Diferenciais</div>
  <h2 class="slide-title">KNIME Reduz Custo em 80% sem Lock-in</h2>

  <div class="pillars-container">
    <div class="pillar-card">
      <div class="pillar-top">
        <div class="pillar-badge">Low-Code Visual</div>
        <h3 class="pillar-heading">Automação Sem Código Frágil</h3>
        <p class="pillar-desc">Fluxos modulares e visuais que unificam ETL e Machine Learning acelerando entregas analíticas.</p>
      </div>
      <div class="pillar-footer">⚡ 4x mais rápido no deploy</div>
    </div>

    <div class="pillar-card">
      <div class="pillar-top">
        <div class="pillar-badge">Stack Híbrida</div>
        <h3 class="pillar-heading">Python, R e SQL Nativos</h3>
        <p class="pillar-desc">Conexão transparente com bancos corporativos, scripts customizados e APIs REST sem barreiras.</p>
      </div>
      <div class="pillar-footer">🔗 Zero dependência proprietária</div>
    </div>

    <div class="pillar-card">
      <div class="pillar-top">
        <div class="pillar-badge">Governança</div>
        <h3 class="pillar-heading">Auditabilidade & Aberto</h3>
        <p class="pillar-desc">Workflows versionáveis e auditáveis, garantindo total conformidade LGPD e licença 100% gratuita.</p>
      </div>
      <div class="pillar-footer">🛡️ Custo zero de licença anual</div>
    </div>
  </div>

  <div class="bottom-badge">
    <span style="font-size: 28px;">💡</span>
    <span>Validação no Caso SAD: <strong>87.2% de Acurácia</strong> obtida com a Árvore de Decisão no conjunto de teste.</span>
  </div>
</body>
</html>"""

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
    padding: 50px 70px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .header-box {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .top-pill {
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 10px 24px;
    border-radius: 9999px;
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }
  .slide-title {
    font-size: 64px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
  }
  .steps-bar {
    display: flex;
    gap: 16px;
    margin: 10px 0;
  }
  .step-pill {
    background: #280a52;
    border: 2px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    padding: 14px 22px;
    font-size: 20px;
    font-weight: 800;
    color: #FFFFFF;
    flex: 1;
    text-align: center;
  }
  .step-pill b { color: #FFC800; }
  
  /* Desktop Application Window */
  .desktop-window {
    background: #1e0b38;
    border: 3px solid rgba(255, 255, 255, 0.25);
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0 30px 70px rgba(20, 5, 50, 0.65);
    display: flex;
    flex-direction: column;
  }
  .window-header {
    background: #140529;
    padding: 14px 24px;
    display: flex;
    align-items: center;
    gap: 12px;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
  }
  .window-dot { width: 16px; height: 16px; border-radius: 50%; }
  .dot-red { background: #EF4444; }
  .dot-yellow { background: #F59E0B; }
  .dot-green { background: #10B981; }
  .window-title {
    font-size: 18px;
    font-weight: 700;
    color: #DDD6FE;
    margin-left: 12px;
  }
  .window-body {
    background: #FFFFFF;
    height: 520px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
  }
  .window-body img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    background: #FFFFFF;
  }
  .footer-summary {
    background: #280a52;
    padding: 18px 36px;
    border-radius: 20px;
    font-size: 22px;
    font-weight: 800;
    color: #FFFFFF;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .footer-summary b { color: #FFC800; }
</style>
</head>
<body>
  <div class="header-box">
    <div class="top-pill">Arquitetura Prática do Workflow</div>
    <h2 class="slide-title">Pipeline no KNIME: Do Dado à Prescrição</h2>
  </div>

  <div class="steps-bar">
    <div class="step-pill"><b>01.</b> Ingestão (CSV Reader)</div>
    <div class="step-pill"><b>02.</b> Partição 70/30</div>
    <div class="step-pill"><b>03.</b> Árvore de Decisão</div>
    <div class="step-pill"><b>04.</b> Ação Prescritiva</div>
  </div>

  <div class="desktop-window">
    <div class="window-header">
      <div class="window-dot dot-red"></div>
      <div class="window-dot dot-yellow"></div>
      <div class="window-dot dot-green"></div>
      <span class="window-title">KNIME Analytics Platform — Workflow Executável (churn_prediction_sad.knwf)</span>
    </div>
    <div class="window-body">
      <img src="workflow_architecture.png" alt="KNIME Workflow Real">
    </div>
  </div>

  <div class="footer-summary">
    <span>Workflow Executável: <b>churn_prediction_sad.knwf</b></span>
    <span>87.2% de Acurácia Validada • Execução 100% Local e Auditável</span>
  </div>
</body>
</html>"""

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
    padding: 50px 70px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .header-box {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .top-pill {
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    background: #331163;
    color: #E9D5FF;
    padding: 10px 24px;
    border-radius: 9999px;
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }
  .slide-title {
    font-size: 64px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
  }
  .main-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    align-items: stretch;
  }
  
  /* Desktop Dashboard Preview */
  .desktop-window {
    background: #1e0b38;
    border: 3px solid rgba(255, 255, 255, 0.25);
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0 30px 70px rgba(20, 5, 50, 0.65);
    display: flex;
    flex-direction: column;
    height: 680px;
  }
  .window-header {
    background: #140529;
    padding: 14px 24px;
    display: flex;
    align-items: center;
    gap: 12px;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
  }
  .window-dot { width: 16px; height: 16px; border-radius: 50%; }
  .dot-red { background: #EF4444; }
  .dot-yellow { background: #F59E0B; }
  .dot-green { background: #10B981; }
  .window-title { font-size: 18px; font-weight: 700; color: #DDD6FE; margin-left: 12px; }
  .window-body {
    background: #0f172a;
    flex: 1;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .window-body img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  /* Comparison Side */
  .cards-column {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 680px;
    gap: 24px;
  }
  .comp-card {
    border-radius: 28px;
    padding: 36px 40px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex: 1;
    box-shadow: 0 20px 45px rgba(40, 10, 82, 0.4);
  }
  .card-reactive {
    background: #331163;
    border: 3px solid rgba(239, 68, 68, 0.5);
  }
  .card-predictive {
    background: #23084a;
    border: 3px solid #FFC800;
  }
  .comp-badge {
    align-self: flex-start;
    padding: 8px 18px;
    border-radius: 9999px;
    font-size: 16px;
    font-weight: 900;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 14px;
  }
  .comp-badge.danger { background: rgba(239, 68, 68, 0.25); color: #FCA5A5; }
  .comp-badge.success { background: rgba(255, 200, 0, 0.25); color: #FFC800; }
  .comp-title {
    font-size: 34px;
    font-weight: 900;
    color: #FFFFFF;
    margin-bottom: 14px;
  }
  .comp-points {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .comp-point {
    font-size: 24px;
    color: #E9D5FF;
    display: flex;
    align-items: center;
    gap: 14px;
    line-height: 1.35;
  }
  .comp-point strong { color: #FFFFFF; }
  .comp-footer {
    border-top: 2px solid rgba(255, 255, 255, 0.15);
    padding-top: 16px;
    font-size: 26px;
    font-weight: 900;
  }
  .comp-footer.danger { color: #FCA5A5; }
  .comp-footer.success { color: #34D399; }
</style>
</head>
<body>
  <div class="header-box">
    <div class="top-pill">Painel Interativo de Suporte à Decisão (SAD)</div>
    <h2 class="slide-title">Do Modelo Reativo à Retenção Prescritiva</h2>
  </div>

  <div class="main-grid">
    <div class="desktop-window">
      <div class="window-header">
        <div class="window-dot dot-red"></div>
        <div class="window-dot dot-yellow"></div>
        <div class="window-dot dot-green"></div>
        <span class="window-title">Dashboard Gerencial Interativo — Retenção em Telecom</span>
      </div>
      <div class="window-body">
        <img src="dashboard_preview.png" alt="KNIME Dashboard Real">
      </div>
    </div>

    <div class="cards-column">
      <div class="comp-card card-reactive">
        <div>
          <div class="comp-badge danger">Abordagem Tradicional</div>
          <h3 class="comp-title">Reativa e Tardia</h3>
          <div class="comp-points">
            <div class="comp-point">❌ <strong>Ação Tardia:</strong> Contato após pedido de cancelamento.</div>
            <div class="comp-point">❌ <strong>Desconto Genérico:</strong> Corrói a margem e retém pouco.</div>
          </div>
        </div>
        <div class="comp-footer danger">Perda contínua de R$ 28.000 / mês</div>
      </div>

      <div class="comp-card card-predictive">
        <div>
          <div class="comp-badge success">Com KNIME Analytics</div>
          <h3 class="comp-title">Preditiva e Prescritiva</h3>
          <div class="comp-points">
            <div class="comp-point">✅ <strong>Antecipação:</strong> Alerta automático 15 dias antes da evasão.</div>
            <div class="comp-point">✅ <strong>Regras Automatizadas:</strong> Oferta personalizada por propensão.</div>
          </div>
        </div>
        <div class="comp-footer success">Economia líquida de R$ 22.400 / mês</div>
      </div>
    </div>
  </div>
</body>
</html>"""

HTML_SLIDE_6 = """<!DOCTYPE html>
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
    padding: 12px 28px;
    border-radius: 9999px;
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .slide-title {
    font-size: 68px;
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.1;
    color: #FFFFFF;
    margin-bottom: 45px;
    max-width: 1600px;
  }
  .main-grid {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 50px;
    align-items: center;
  }
  .deliverables-box {
    display: flex;
    flex-direction: column;
    gap: 22px;
  }
  .item-card {
    background: #331163;
    border: 3px solid rgba(255, 255, 255, 0.2);
    border-radius: 30px;
    padding: 32px 40px;
    box-shadow: 0 20px 45px rgba(40, 10, 82, 0.4);
  }
  .item-card h4 {
    font-size: 30px;
    font-weight: 900;
    color: #FFFFFF;
    margin-bottom: 8px;
  }
  .item-card p {
    font-size: 22px;
    color: #E9D5FF;
    line-height: 1.45;
  }
  .repo-link-box {
    background: #280a52;
    border-radius: 24px;
    padding: 24px 34px;
    font-size: 24px;
    font-weight: 800;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-top: 10px;
  }
  .repo-link-box span { color: #FFC800; font-weight: 900; }

  /* Giant QR Card Direct (NO PHONE) */
  .qr-card {
    background: #FFFFFF;
    border-radius: 40px;
    padding: 50px 40px;
    box-shadow: 0 35px 80px rgba(20, 5, 50, 0.6);
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    height: 640px;
    justify-content: center;
  }
  .qr-img {
    width: 360px;
    height: 360px;
    display: block;
    border-radius: 16px;
  }
  .qr-title {
    font-size: 34px;
    font-weight: 900;
    color: #1e0b38;
    margin-top: 24px;
  }
  .qr-sub {
    font-size: 22px;
    font-weight: 600;
    color: #6D28D9;
    margin-top: 8px;
  }
</style>
</head>
<body>
  <div class="top-pill">Entrega Obrigatória & Avaliação</div>
  <h2 class="slide-title">Código Aberto, Governança e Retorno Imediato</h2>

  <div class="main-grid">
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

    <div class="qr-card">
      <img class="qr-img" src="qrcode_github.png" alt="QR Code GitHub">
      <div class="qr-title">Aponte a Câmera</div>
      <div class="qr-sub">Código-fonte, dados e workflow no GitHub</div>
    </div>
  </div>
</body>
</html>"""

files = {
    "slides/desktop_enlarged_html/slide_1.html": HTML_SLIDE_1,
    "slides/desktop_enlarged_html/slide_2.html": HTML_SLIDE_2,
    "slides/desktop_enlarged_html/slide_3.html": HTML_SLIDE_3,
    "slides/desktop_enlarged_html/slide_4.html": HTML_SLIDE_4,
    "slides/desktop_enlarged_html/slide_5.html": HTML_SLIDE_5,
    "slides/desktop_enlarged_html/slide_6.html": HTML_SLIDE_6,
}

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("Desktop enlarged slide HTML files created!")
