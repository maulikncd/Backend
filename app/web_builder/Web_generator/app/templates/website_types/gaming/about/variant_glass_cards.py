from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Glassmorphism Cards - Modern glass effect with floating elements"""
    title = props.get("title", "Why Choose Us")
    content = props.get("content", "We combine cutting-edge technology with passionate gaming expertise")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    accent = colors.get("accent")
    
    return f'''
    <section class="gaming-about-glass" id="about">
        <div class="glass-bg-elements">
            <div class="floating-orb orb-1"></div>
            <div class="floating-orb orb-2"></div>
            <div class="floating-orb orb-3"></div>
        </div>
        <div class="glass-container">
            <div class="glass-header">
                <span class="mini-tag">About Us</span>
                <h2>{title}</h2>
                <p>{content}</p>
            </div>
            <div class="glass-cards">
                <div class="glass-card">
                    <div class="card-icon">🚀</div>
                    <h3>Lightning Fast</h3>
                    <p>Sub-10ms latency for competitive edge. Our servers deliver unmatched performance.</p>
                    <div class="card-stat">
                        <span class="stat-number">99.9%</span>
                        <span class="stat-label">Uptime</span>
                    </div>
                </div>
                <div class="glass-card featured">
                    <div class="featured-badge">Most Popular</div>
                    <div class="card-icon">⚡</div>
                    <h3>Pro Features</h3>
                    <p>Access advanced analytics, replay systems, and professional coaching tools.</p>
                    <div class="card-stat">
                        <span class="stat-number">500+</span>
                        <span class="stat-label">Features</span>
                    </div>
                </div>
                <div class="glass-card">
                    <div class="card-icon">🛡️</div>
                    <h3>Secure Gaming</h3>
                    <p>Enterprise-grade security with advanced anti-cheat and fraud protection.</p>
                    <div class="card-stat">
                        <span class="stat-number">24/7</span>
                        <span class="stat-label">Protection</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-about-glass {{
        padding: 140px 24px;
        background: {background};
        position: relative;
        overflow: hidden;
    }}
    .glass-bg-elements {{
        position: absolute;
        inset: 0;
        pointer-events: none;
        overflow: hidden;
    }}
    .floating-orb {{
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
        opacity: 0.4;
        animation: floatOrb 20s ease-in-out infinite;
    }}
    .orb-1 {{
        width: 400px;
        height: 400px;
        background: {primary};
        top: -100px;
        left: -100px;
        animation-delay: 0s;
    }}
    .orb-2 {{
        width: 300px;
        height: 300px;
        background: {secondary};
        bottom: -50px;
        right: -50px;
        animation-delay: -7s;
    }}
    .orb-3 {{
        width: 200px;
        height: 200px;
        background: {accent};
        top: 50%;
        left: 50%;
        animation-delay: -14s;
    }}
    @keyframes floatOrb {{
        0%, 100% {{ transform: translate(0, 0) scale(1); }}
        25% {{ transform: translate(30px, -30px) scale(1.1); }}
        50% {{ transform: translate(-20px, 20px) scale(0.95); }}
        75% {{ transform: translate(20px, 30px) scale(1.05); }}
    }}
    .glass-container {{
        max-width: 1200px;
        margin: 0 auto;
        position: relative;
        z-index: 2;
    }}
    .glass-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .mini-tag {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}20;
        color: {primary};
        font-weight: 700;
        font-size: 0.8rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        border-radius: 100px;
        margin-bottom: 24px;
    }}
    .glass-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 20px;
    }}
    .glass-header p {{
        font-size: 1.2rem;
        color: {secondary};
        max-width: 600px;
        margin: 0 auto;
    }}
    .glass-cards {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
    }}
    .glass-card {{
        background: linear-gradient(135deg, {text}08, {text}02);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid {text}10;
        border-radius: 24px;
        padding: 48px 40px;
        position: relative;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .glass-card:hover {{
        transform: translateY(-12px);
        border-color: {primary}40;
        box-shadow: 0 40px 80px {background}80, 0 0 60px {primary}10;
    }}
    .glass-card.featured {{
        background: linear-gradient(135deg, {primary}15, {primary}05);
        border-color: {primary}40;
        transform: scale(1.05);
    }}
    .glass-card.featured:hover {{
        transform: scale(1.05) translateY(-12px);
    }}
    .featured-badge {{
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        padding: 8px 20px;
        background: {primary};
        color: {background};
        font-weight: 800;
        font-size: 0.75rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        border-radius: 100px;
    }}
    .card-icon {{
        font-size: 3rem;
        margin-bottom: 24px;
    }}
    .glass-card h3 {{
        font-size: 1.5rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .glass-card p {{
        color: {secondary};
        font-size: 1rem;
        line-height: 1.7;
        margin-bottom: 32px;
    }}
    .card-stat {{
        display: flex;
        align-items: baseline;
        gap: 12px;
        padding-top: 24px;
        border-top: 1px solid {text}10;
    }}
    .stat-number {{
        font-size: 2rem;
        font-weight: 900;
        color: {primary};
    }}
    .stat-label {{
        font-size: 0.85rem;
        color: {secondary};
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    @media (max-width: 900px) {{
        .glass-cards {{ grid-template-columns: 1fr; gap: 24px; }}
        .glass-card.featured {{ transform: none; }}
        .glass-card.featured:hover {{ transform: translateY(-12px); }}
    }}
    </style>
    '''
