from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Interactive Cards - Hover-activated feature cards with animations"""
    title = props.get("title", "Powerful Features")
    subtitle = props.get("subtitle", "Everything you need to dominate")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    accent = colors.get("accent")
    
    features = [
        {"icon": "⚡", "title": "Lightning Fast", "desc": "Sub-10ms latency for competitive advantage", "stat": "10ms"},
        {"icon": "🛡️", "title": "Secure Gaming", "desc": "Military-grade encryption and anti-cheat", "stat": "256bit"},
        {"icon": "🌐", "title": "Global Servers", "desc": "200+ edge locations worldwide", "stat": "200+"},
        {"icon": "🎮", "title": "Pro Tools", "desc": "Advanced analytics and replay systems", "stat": "50+"},
        {"icon": "🏆", "title": "Tournaments", "desc": "Daily competitions with real prizes", "stat": "$10M+"},
        {"icon": "👥", "title": "Community", "desc": "Connect with millions of players", "stat": "50M+"}
    ]
    
    features_html = ""
    for f in features:
        features_html += f'''
        <div class="interactive-card">
            <div class="card-bg"></div>
            <div class="card-content">
                <div class="card-icon">{f["icon"]}</div>
                <h3>{f["title"]}</h3>
                <p>{f["desc"]}</p>
                <div class="card-stat">
                    <span class="stat-value">{f["stat"]}</span>
                </div>
            </div>
            <div class="card-hover-effect"></div>
        </div>
        '''
    
    return f'''
    <section class="gaming-features-interactive" id="features">
        <div class="features-container">
            <div class="features-header">
                <span class="section-tag">Features</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            <div class="features-grid">
                {features_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-features-interactive {{
        padding: 140px 24px;
        background: {background};
        position: relative;
    }}
    .features-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .features-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .section-tag {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        border-radius: 100px;
        margin-bottom: 24px;
    }}
    .features-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .features-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .features-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
    }}
    .interactive-card {{
        position: relative;
        background: {text}05;
        border: 1px solid {text}08;
        border-radius: 24px;
        padding: 48px 36px;
        overflow: hidden;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
    }}
    .interactive-card:hover {{
        border-color: {primary}50;
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 40px 80px {primary}15;
    }}
    .card-bg {{
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, {primary}05, transparent);
        opacity: 0;
        transition: opacity 0.5s ease;
    }}
    .interactive-card:hover .card-bg {{
        opacity: 1;
    }}
    .card-content {{
        position: relative;
        z-index: 2;
    }}
    .card-icon {{
        font-size: 3rem;
        margin-bottom: 24px;
        transition: transform 0.5s ease;
    }}
    .interactive-card:hover .card-icon {{
        transform: scale(1.2) rotate(5deg);
    }}
    .interactive-card h3 {{
        font-size: 1.5rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 12px;
    }}
    .interactive-card p {{
        color: {secondary};
        font-size: 1rem;
        line-height: 1.7;
        margin-bottom: 24px;
    }}
    .card-stat {{
        padding-top: 20px;
        border-top: 1px solid {text}10;
    }}
    .stat-value {{
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        font-weight: 900;
        color: {primary};
        text-shadow: 0 0 30px {primary}50;
    }}
    .card-hover-effect {{
        position: absolute;
        bottom: -50%;
        left: 50%;
        transform: translateX(-50%);
        width: 200px;
        height: 200px;
        background: {primary};
        filter: blur(80px);
        opacity: 0;
        transition: opacity 0.5s ease;
    }}
    .interactive-card:hover .card-hover-effect {{
        opacity: 0.2;
    }}
    @media (max-width: 900px) {{
        .features-grid {{ grid-template-columns: 1fr 1fr; }}
    }}
    @media (max-width: 600px) {{
        .features-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
