import subprocess, os

# 1. Slide 1 Background (No phones)
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
    left: 120px;
    top: 180px;
    width: 860px;
    z-index: 10;
  }
  .top-pill {
    display: inline-flex;
    align-items: center;
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
  .authors-bar strong { color: #FFFFFF; }
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
</body>
</html>"""

# Phone 1 (Back) Transparent
HTML_PHONE_BACK = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 360px;
    height: 740px;
    background: transparent;
    overflow: hidden;
    padding: 20px;
  }
  .phone-back {
    width: 320px;
    height: 680px;
    background: #180933;
    border-radius: 46px;
    border: 9px solid #2a1154;
    box-shadow: 0 30px 60px -15px rgba(20, 5, 50, 0.7);
    overflow: hidden;
    padding: 20px 18px;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .notch {
    width: 110px;
    height: 20px;
    background: #0f0422;
    border-radius: 10px;
    margin: 0 auto 16px auto;
  }
  .app-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  .app-title { font-size: 16px; font-weight: 700; color: #FFFFFF; }
  .app-tag {
    background: #FFC800;
    color: #000;
    font-size: 10px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 6px;
  }
  .mini-node {
    background: rgba(46, 16, 101, 0.7);
    border-left: 4px solid #FFC800;
    padding: 12px 14px;
    border-radius: 12px;
    font-size: 13px;
  }
  .mini-node b { color: #FFFFFF; display: block; font-size: 14px; margin-bottom: 2px; }
  .mini-node span { color: #DDD6FE; font-size: 12px; }
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
    <div class="mini-node"><b>Partitioning</b><span>Divisão Estratificada 70/30</span></div>
    <div class="mini-node"><b>Decision Tree</b><span>Treino Supervisionado</span></div>
    <div class="mini-node"><b>Scorer & Metrics</b><span>Acurácia 87.2%</span></div>
  </div>
</body>
</html>"""

# Phone 2 (Front) Transparent
HTML_PHONE_FRONT = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 380px;
    height: 760px;
    background: transparent;
    overflow: hidden;
    padding: 20px;
  }
  .phone-front {
    width: 340px;
    height: 710px;
    background: #1c0a3d;
    border-radius: 50px;
    border: 10px solid #331463;
    box-shadow: 0 40px 75px -15px rgba(15, 3, 40, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.1) inset;
    overflow: hidden;
    padding: 24px 20px;
    display: flex;
    flex-direction: column;
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
  .app-title { font-size: 18px; font-weight: 700; color: #FFFFFF; }
  .app-tag {
    background: #FFC800;
    color: #000;
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
  .app-stat-val { font-size: 38px; font-weight: 800; color: #FFFFFF; line-height: 1; }
  .app-stat-lbl { font-size: 13px; color: #DDD6FE; margin-top: 6px; }
  .mini-node {
    background: rgba(46, 16, 101, 0.7);
    border-left: 4px solid #10B981;
    padding: 16px;
    border-radius: 12px;
    margin-top: auto;
  }
  .mini-node b { color: #10B981; display: block; font-size: 14px; margin-bottom: 2px; }
  .mini-node span { color: #DDD6FE; font-size: 12px; }
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
      <span>Oferta automatizada disparada para 318 contas de alto risco.</span>
    </div>
  </div>
</body>
</html>"""

# 2. Slide 2 Background (No phone)
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
  .stat-block {
    width: 880px;
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
  .card-text { font-size: 20px; color: #FFFFFF; }
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

# Phone Alert Transparent
HTML_PHONE_ALERT = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 420px;
    height: 700px;
    background: transparent;
    overflow: hidden;
    padding: 20px;
  }
  .phone-mockup {
    width: 380px;
    height: 650px;
    background: #1c0a3d;
    border-radius: 48px;
    border: 10px solid #331463;
    box-shadow: 0 35px 70px -15px rgba(20, 5, 50, 0.75);
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
</body>
</html>"""

# 6. Slide 6 Background (No phone)
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
  .deliverables-box {
    width: 900px;
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

# Phone QR Transparent
HTML_PHONE_QR = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  body {
    width: 420px;
    height: 700px;
    background: transparent;
    overflow: hidden;
    padding: 20px;
  }
  .phone-mockup {
    width: 380px;
    height: 650px;
    background: #1c0a3d;
    border-radius: 48px;
    border: 10px solid #331463;
    box-shadow: 0 35px 70px -15px rgba(20, 5, 50, 0.75);
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
  .qr-img { width: 210px; height: 210px; display: block; }
  .phone-info { text-align: center; }
  .phone-info h5 { font-size: 18px; font-weight: 800; color: #FFFFFF; margin-bottom: 6px; }
  .phone-info p { font-size: 13px; color: #DDD6FE; }
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
    "slides/layers_html/slide_1_bg.html": HTML_SLIDE_1_BG,
    "slides/layers_html/phone_back.html": HTML_PHONE_BACK,
    "slides/layers_html/phone_front.html": HTML_PHONE_FRONT,
    "slides/layers_html/slide_2_bg.html": HTML_SLIDE_2_BG,
    "slides/layers_html/phone_alert.html": HTML_PHONE_ALERT,
    "slides/layers_html/slide_6_bg.html": HTML_SLIDE_6_BG,
    "slides/layers_html/phone_qr.html": HTML_PHONE_QR,
}

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("Layer HTML files created!")
