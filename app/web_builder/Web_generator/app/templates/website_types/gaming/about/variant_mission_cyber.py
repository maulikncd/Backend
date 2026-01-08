from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "The Next Level of Gaming")
    content = props.get("content", "We are more than just a platform. We are a community of players dedicated to pushing the boundaries of what's possible in the digital arena.")
    
    return f'''
    <section class="gaming-about gaming-about-mission" id="about">
        <div class="container">
            <div class="about-grid">
                <div class="about-content animate-on-scroll">
                    <div class="section-tag">Since 2018</div>
                    <h2 class="about-title">{title}</h2>
                    <p class="about-text">{content}</p>
                    <div class="mission-points">
                        <div class="point">
                            <span class="p-icon">🎮</span>
                            <div class="p-text">
                                <h6>Pro Level Access</h6>
                                <p>Unlocking elite features for every player.</p>
                            </div>
                        </div>
                        <div class="point">
                            <span class="p-icon">🛡️</span>
                            <div class="p-text">
                                <h6>Secured Fair Play</h6>
                                <p>Advanced anti-cheat and verified rankings.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="about-visual animate-on-scroll">
                    <div class="visual-card">
                        <div class="card-glow"></div>
                        <div class="stat-circle">
                            <span class="stat-num">98%</span>
                            <span class="stat-txt">Uptime</span>
                        </div>
                        <div class="stat-bar">
                            <span>Players worldwide</span>
                            <div class="bar"><div class="fill" style="width: 85%"></div></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-about-mission {{
        padding: 120px 24px;
        background: {colors.get("background", "#0A0A0F")};
        overflow: hidden;
    }}
    .about-grid {{
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        gap: 80px;
        align-items: center;
    }}
    .section-tag {{ color: {colors.get("primary", "#00FF88")}; font-weight: 800; text-transform: uppercase; letter-spacing: 4px; border-left: 3px solid {colors.get("primary", "#00FF88")}; padding-left: 15px; margin-bottom: 30px; }}
    .about-title {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: #fff;
        margin-bottom: 30px;
        line-height: 1.1;
    }}
    .about-text {{ color: #888; font-size: 1.2rem; line-height: 1.7; margin-bottom: 50px; }}
    .mission-points {{ display: flex; flex-direction: column; gap: 30px; }}
    .point {{ display: flex; gap: 20px; }}
    .p-icon {{ font-size: 2rem; }}
    .p-text h6 {{ color: #fff; font-size: 1.1rem; margin-bottom: 5px; }}
    .p-text p {{ color: #666; font-size: 0.95rem; }}
    .about-visual {{ position: relative; }}
    .visual-card {{
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.05);
        padding: 60px;
        border-radius: 20px;
        position: relative;
    }}
    .card-glow {{
        position: absolute;
        inset: 40px;
        background: {colors.get("primary", "#00FF88")}10;
        filter: blur(50px);
        z-index: -1;
    }}
    .stat-circle {{
        width: 150px;
        height: 150px;
        border: 5px solid {colors.get("primary", "#00FF88")};
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 0 auto 40px;
        box-shadow: 0 0 30px {colors.get("primary", "#00FF88")}40;
    }}
    .stat-num {{ font-size: 2.5rem; font-weight: 800; color: #fff; }}
    .stat-txt {{ font-size: 0.8rem; color: #888; text-transform: uppercase; }}
    .stat-bar {{ color: #888; font-size: 0.9rem; }}
    .bar {{ height: 8px; background: rgba(255,255,255,0.05); border-radius: 10px; margin-top: 10px; overflow: hidden; }}
    .fill {{ height: 100%; background: {colors.get("primary", "#00FF88")}; box-shadow: 0 0 10px {colors.get("primary", "#00FF88")}; }}
    @media (max-width: 900px) {{ .about-grid {{ grid-template-columns: 1fr; gap: 60px; }} }}
    </style>
    '''
