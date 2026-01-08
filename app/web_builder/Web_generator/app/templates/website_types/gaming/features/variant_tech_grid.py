from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Game Features")
    features = props.get("features", [
        {"title": "High Performance", "desc": "Optimized for 240+ FPS on all platforms.", "icon": "⚡"},
        {"title": "Global Servers", "desc": "Low latency nodes in 50+ countries.", "icon": "🌐"},
        {"title": "Daily Tournaments", "desc": "Compete every day for massive prize pools.", "icon": "🏆"},
        {"title": "Pro Community", "desc": "Join millions of players in our active discord.", "icon": "🤝"}
    ])
    
    primary = colors.get("primary", "#00FF88")
    bg = colors.get("background", "#0A0A0F")
    
    # Build feature cards separately to avoid f-string nesting issues
    feature_cards = ""
    for f in features:
        feature_cards += f'''
            <div class="feature-card animate-on-scroll">
                <div class="card-borders"></div>
                <span class="feature-icon">{f["icon"]}</span>
                <h3 class="feature-title">{f["title"]}</h3>
                <p class="feature-desc">{f["desc"]}</p>
            </div>
        '''
    
    return f'''
    <section class="gaming-features gaming-features-grid" id="features">
        <div class="container">
            <h2 class="section-title text-center animate-on-scroll">{title}</h2>
            <div class="features-grid">
                {feature_cards}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-features-grid {{
        padding: 120px 24px;
        background: {bg};
        position: relative;
    }}
    .container {{ max-width: 1300px; margin: 0 auto; }}
    .section-title {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        color: #fff;
        margin-bottom: 80px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .features-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
    }}
    .feature-card {{
        background: rgba(255,255,255,0.02);
        padding: 50px 40px;
        position: relative;
        transition: 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        border: 1px solid rgba(255,255,255,0.05);
    }}
    .feature-card:hover {{
        background: rgba(255,255,255,0.05);
        transform: translateY(-10px);
        border-color: {primary}40;
    }}
    .card-borders {{
        position: absolute;
        inset: 0;
        pointer-events: none;
    }}
    .card-borders::before, .card-borders::after {{
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        border: 2px solid transparent;
        transition: 0.4s;
    }}
    .card-borders::before {{ top: -1px; left: -1px; border-top-color: {primary}00; border-left-color: {primary}00; }}
    .card-borders::after {{ bottom: -1px; right: -1px; border-bottom-color: {primary}00; border-right-color: {primary}00; }}
    .feature-card:hover .card-borders::before {{ border-top-color: {primary}; border-left-color: {primary}; }}
    .feature-card:hover .card-borders::after {{ border-bottom-color: {primary}; border-right-color: {primary}; }}
    .feature-icon {{ font-size: 3rem; margin-bottom: 24px; display: block; }}
    .feature-title {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #fff;
        margin-bottom: 16px;
    }}
    .feature-desc {{ color: #888; line-height: 1.6; }}
    </style>
    '''
