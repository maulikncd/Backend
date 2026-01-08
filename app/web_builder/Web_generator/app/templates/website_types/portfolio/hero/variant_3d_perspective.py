from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    3D Perspective - Futuristic hero with 3D card effects,
    neon accents and immersive depth
    """
    name = props.get("name", props.get("businessName", "Mike Dev"))
    title = props.get("title", "Creative Developer")
    tagline = props.get("tagline", "Where code meets creativity")
    cta = props.get("cta", "Explore Work")
    
    primary = colors.get("primary", "#00F5FF")
    secondary = colors.get("secondary", "#FF00E5")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="perspective-hero" id="hero">
        <div class="perspective-bg">
            <div class="grid-floor"></div>
            <div class="neon-line line-1"></div>
            <div class="neon-line line-2"></div>
        </div>
        
        <div class="hero-content">
            <div class="intro-badge">
                <span class="badge-icon">⚡</span>
                <span>Creative Developer</span>
            </div>
            
            <h1 class="hero-title">
                <span class="title-line">{name}</span>
            </h1>
            
            <p class="hero-tagline">{tagline}</p>
            
            <div class="cta-section">
                <a href="#projects" class="neon-btn">{cta}</a>
                <div class="stats-row">
                    <div class="stat">
                        <span class="stat-num">8+</span>
                        <span class="stat-text">Years Exp</span>
                    </div>
                    <div class="stat">
                        <span class="stat-num">100+</span>
                        <span class="stat-text">Projects</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="floating-elements">
            <div class="float-card card-1">
                <div class="card-inner">
                    <span class="card-label">Latest Work</span>
                    <span class="card-title">E-Commerce App</span>
                </div>
            </div>
            <div class="float-card card-2">
                <div class="card-inner">
                    <span class="card-label">Tech</span>
                    <span class="card-title">React • Node</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@400;500;600;700&display=swap');
    
    .perspective-hero {{
        min-height: 100vh;
        background: {bg};
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 120px 40px;
        position: relative;
        overflow: hidden;
        perspective: 1000px;
    }}
    .perspective-bg {{
        position: absolute;
        inset: 0;
        transform-style: preserve-3d;
    }}
    .grid-floor {{
        position: absolute;
        bottom: 0;
        left: -50%;
        right: -50%;
        height: 60%;
        background: 
            linear-gradient(90deg, {primary}20 1px, transparent 1px),
            linear-gradient(0deg, {primary}20 1px, transparent 1px);
        background-size: 80px 80px;
        transform: rotateX(70deg);
        transform-origin: bottom;
    }}
    .neon-line {{
        position: absolute;
        height: 2px;
        background: linear-gradient(90deg, transparent, {primary}, transparent);
        animation: neonPulse 3s ease-in-out infinite;
    }}
    .line-1 {{
        top: 30%;
        left: 0;
        right: 0;
    }}
    .line-2 {{
        bottom: 30%;
        left: 0;
        right: 0;
        animation-delay: 1.5s;
    }}
    @keyframes neonPulse {{
        0%, 100% {{ opacity: 0.3; }}
        50% {{ opacity: 1; }}
    }}
    .hero-content {{
        position: relative;
        z-index: 2;
        text-align: center;
    }}
    .intro-badge {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 12px 24px;
        border: 1px solid {primary}50;
        border-radius: 50px;
        color: {primary};
        font-family: 'Rajdhani', sans-serif;
        font-size: 0.95rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 40px;
    }}
    .hero-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(3rem, 10vw, 8rem);
        font-weight: 900;
        margin-bottom: 24px;
    }}
    .title-line {{
        background: linear-gradient(135deg, {text}, {primary});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 80px {primary}50;
    }}
    .hero-tagline {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.4rem;
        color: rgba(255,255,255,0.6);
        margin-bottom: 50px;
        letter-spacing: 3px;
        text-transform: uppercase;
    }}
    .cta-section {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 60px;
        flex-wrap: wrap;
    }}
    .neon-btn {{
        padding: 20px 50px;
        background: transparent;
        border: 2px solid {primary};
        color: {primary};
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-decoration: none;
        position: relative;
        overflow: hidden;
        transition: all 0.3s;
    }}
    .neon-btn::before {{
        content: '';
        position: absolute;
        inset: 0;
        background: {primary};
        transform: translateX(-100%);
        transition: transform 0.3s;
    }}
    .neon-btn:hover {{
        color: {bg};
        box-shadow: 0 0 40px {primary}60;
    }}
    .neon-btn:hover::before {{
        transform: translateX(0);
    }}
    .neon-btn span {{
        position: relative;
        z-index: 1;
    }}
    .stats-row {{
        display: flex;
        gap: 40px;
    }}
    .stat {{
        text-align: center;
    }}
    .stat-num {{
        display: block;
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: {text};
    }}
    .stat-text {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 0.85rem;
        color: rgba(255,255,255,0.4);
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .floating-elements {{
        position: absolute;
        inset: 0;
        pointer-events: none;
    }}
    .float-card {{
        position: absolute;
        padding: 20px 30px;
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(10px);
        border: 1px solid {primary}30;
        animation: floatCard 6s ease-in-out infinite;
    }}
    .card-1 {{
        top: 25%;
        left: 10%;
    }}
    .card-2 {{
        bottom: 25%;
        right: 10%;
        animation-delay: 2s;
    }}
    @keyframes floatCard {{
        0%, 100% {{ transform: translateY(0) rotateY(0deg); }}
        50% {{ transform: translateY(-20px) rotateY(5deg); }}
    }}
    .card-label {{
        display: block;
        font-size: 0.75rem;
        color: {primary};
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 6px;
    }}
    .card-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 1rem;
        color: {text};
    }}
    @media (max-width: 1024px) {{
        .float-card {{ display: none; }}
    }}
    @media (max-width: 640px) {{
        .perspective-hero {{ padding: 100px 20px; }}
        .cta-section {{ flex-direction: column; gap: 30px; }}
    }}
    </style>
    '''
