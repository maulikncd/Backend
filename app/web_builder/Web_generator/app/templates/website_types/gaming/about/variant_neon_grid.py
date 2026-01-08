from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Neon Grid - Cyberpunk inspired grid with neon accents"""
    title = props.get("title", "Built for Champions")
    content = props.get("content", "Every feature engineered for competitive excellence")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-about-neon-grid" id="about">
        <div class="neon-grid-bg"></div>
        <div class="neon-container">
            <div class="neon-header">
                <div class="cyber-badge">
                    <span class="pulse-dot"></span>
                    <span>LIVE STATS</span>
                </div>
                <h2>{title}</h2>
                <p>{content}</p>
            </div>
            <div class="stats-grid">
                <div class="stat-block large">
                    <div class="stat-inner">
                        <div class="stat-icon">🎮</div>
                        <div class="stat-content">
                            <div class="stat-number">2.5M+</div>
                            <div class="stat-label">Active Players</div>
                            <div class="stat-bar"><div class="bar-fill" style="width: 92%"></div></div>
                        </div>
                    </div>
                    <div class="stat-glow"></div>
                </div>
                <div class="stat-block">
                    <div class="stat-inner">
                        <div class="stat-number">150+</div>
                        <div class="stat-label">Countries</div>
                    </div>
                </div>
                <div class="stat-block">
                    <div class="stat-inner">
                        <div class="stat-number">99.9%</div>
                        <div class="stat-label">Uptime</div>
                    </div>
                </div>
                <div class="stat-block">
                    <div class="stat-inner">
                        <div class="stat-number">24/7</div>
                        <div class="stat-label">Support</div>
                    </div>
                </div>
                <div class="stat-block large">
                    <div class="stat-inner">
                        <div class="stat-icon">🏆</div>
                        <div class="stat-content">
                            <div class="stat-number">$50M+</div>
                            <div class="stat-label">Prize Pool Awarded</div>
                            <div class="stat-bar"><div class="bar-fill secondary" style="width: 78%"></div></div>
                        </div>
                    </div>
                    <div class="stat-glow secondary"></div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-about-neon-grid {{
        padding: 140px 24px;
        background: {background};
        position: relative;
        overflow: hidden;
    }}
    .neon-grid-bg {{
        position: absolute;
        inset: 0;
        background-image: 
            linear-gradient({primary}08 1px, transparent 1px),
            linear-gradient(90deg, {primary}08 1px, transparent 1px);
        background-size: 60px 60px;
        mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
        -webkit-mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
    }}
    .neon-container {{
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }}
    .neon-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .cyber-badge {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 10px 24px;
        background: {primary}15;
        border: 1px solid {primary}40;
        border-radius: 100px;
        margin-bottom: 32px;
        color: {primary};
        font-weight: 800;
        font-size: 0.8rem;
        letter-spacing: 3px;
    }}
    .pulse-dot {{
        width: 8px;
        height: 8px;
        background: {primary};
        border-radius: 50%;
        animation: pulse 2s infinite;
        box-shadow: 0 0 10px {primary};
    }}
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.5; transform: scale(1.2); }}
    }}
    .neon-header h2 {{
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 900;
        color: {text};
        margin-bottom: 20px;
        text-shadow: 0 0 40px {primary}30;
    }}
    .neon-header p {{
        font-size: 1.2rem;
        color: {secondary};
        max-width: 500px;
        margin: 0 auto;
    }}
    .stats-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 24px;
    }}
    .stat-block {{
        background: linear-gradient(135deg, {text}05, transparent);
        border: 1px solid {primary}20;
        border-radius: 20px;
        padding: 40px 32px;
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
    }}
    .stat-block:hover {{
        border-color: {primary}60;
        transform: translateY(-8px);
        box-shadow: 0 20px 60px {primary}15;
    }}
    .stat-block.large {{
        grid-column: span 2;
    }}
    .stat-inner {{
        position: relative;
        z-index: 2;
    }}
    .stat-block.large .stat-inner {{
        display: flex;
        align-items: center;
        gap: 32px;
    }}
    .stat-icon {{
        font-size: 4rem;
        line-height: 1;
    }}
    .stat-content {{
        flex: 1;
    }}
    .stat-number {{
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 900;
        color: {primary};
        line-height: 1;
        margin-bottom: 8px;
        text-shadow: 0 0 30px {primary}50;
    }}
    .stat-label {{
        font-size: 0.9rem;
        color: {secondary};
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .stat-bar {{
        height: 6px;
        background: {text}10;
        border-radius: 10px;
        margin-top: 20px;
        overflow: hidden;
    }}
    .bar-fill {{
        height: 100%;
        background: linear-gradient(90deg, {primary}, {primary}80);
        border-radius: 10px;
        box-shadow: 0 0 20px {primary}60;
        animation: fillPulse 3s ease-in-out infinite;
    }}
    .bar-fill.secondary {{
        background: linear-gradient(90deg, {secondary}, {secondary}80);
        box-shadow: 0 0 20px {secondary}60;
    }}
    @keyframes fillPulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.7; }}
    }}
    .stat-glow {{
        position: absolute;
        bottom: -50%;
        right: -20%;
        width: 200px;
        height: 200px;
        background: {primary};
        filter: blur(80px);
        opacity: 0.15;
    }}
    .stat-glow.secondary {{
        background: {secondary};
    }}
    @media (max-width: 900px) {{
        .stats-grid {{ grid-template-columns: 1fr 1fr; }}
        .stat-block.large {{ grid-column: span 2; }}
    }}
    @media (max-width: 600px) {{
        .stats-grid {{ grid-template-columns: 1fr; }}
        .stat-block.large {{ grid-column: span 1; }}
        .stat-block.large .stat-inner {{ flex-direction: column; text-align: center; }}
    }}
    </style>
    '''
