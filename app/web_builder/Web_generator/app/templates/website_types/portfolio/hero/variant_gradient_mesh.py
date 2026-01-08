from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Gradient Mesh - Vibrant animated gradient background with
    modern glassmorphism cards and bold typography
    """
    name = props.get("name", props.get("businessName", "Sarah Creative"))
    title = props.get("title", "UI/UX Designer")
    tagline = props.get("tagline", "Designing beautiful interfaces that users love")
    cta = props.get("cta", "View Portfolio")
    
    primary = colors.get("primary", "#8B5CF6")
    secondary = colors.get("secondary", "#EC4899")
    tertiary = colors.get("accent", "#06B6D4")
    bg = colors.get("background", "#0F0F1A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="gradient-mesh-hero" id="hero">
        <div class="mesh-bg">
            <div class="mesh-gradient"></div>
        </div>
        
        <div class="hero-container">
            <div class="hero-badge">
                <span class="badge-dot"></span>
                Open for Projects
            </div>
            
            <h1 class="hero-name">{name}</h1>
            <h2 class="hero-title">{title}</h2>
            
            <p class="hero-tagline">{tagline}</p>
            
            <div class="hero-buttons">
                <a href="#projects" class="btn-glass">{cta}</a>
                <a href="#about" class="btn-text">About Me →</a>
            </div>
            
            <div class="hero-cards">
                <div class="glass-card">
                    <div class="card-icon">🎨</div>
                    <div class="card-content">
                        <span class="card-number">200+</span>
                        <span class="card-label">Projects</span>
                    </div>
                </div>
                <div class="glass-card">
                    <div class="card-icon">⭐</div>
                    <div class="card-content">
                        <span class="card-number">50+</span>
                        <span class="card-label">Happy Clients</span>
                    </div>
                </div>
                <div class="glass-card">
                    <div class="card-icon">🏆</div>
                    <div class="card-content">
                        <span class="card-number">15</span>
                        <span class="card-label">Awards</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    .gradient-mesh-hero {{
        min-height: 100vh;
        background: {bg};
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 120px 40px;
        position: relative;
        overflow: hidden;
        text-align: center;
    }}
    .mesh-bg {{
        position: absolute;
        inset: 0;
    }}
    .mesh-gradient {{
        position: absolute;
        inset: 0;
        background: 
            radial-gradient(circle at 30% 20%, {primary}40 0%, transparent 50%),
            radial-gradient(circle at 70% 80%, {secondary}40 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, {tertiary}30 0%, transparent 40%);
        animation: meshMove 15s ease-in-out infinite;
    }}
    @keyframes meshMove {{
        0%, 100% {{ transform: scale(1) rotate(0deg); }}
        33% {{ transform: scale(1.1) rotate(2deg); }}
        66% {{ transform: scale(0.95) rotate(-2deg); }}
    }}
    .hero-container {{
        position: relative;
        z-index: 1;
        max-width: 900px;
    }}
    .hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 12px 24px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 50px;
        color: {text};
        font-size: 0.9rem;
        margin-bottom: 40px;
    }}
    .badge-dot {{
        width: 10px;
        height: 10px;
        background: #22C55E;
        border-radius: 50%;
        animation: blink 2s infinite;
    }}
    @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.5; }}
    }}
    .hero-name {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(3.5rem, 10vw, 8rem);
        font-weight: 700;
        background: linear-gradient(135deg, {text}, {primary}, {secondary});
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 5s ease infinite;
        margin-bottom: 16px;
    }}
    @keyframes gradientShift {{
        0%, 100% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
    }}
    .hero-title {{
        font-size: 1.8rem;
        font-weight: 500;
        color: rgba(255,255,255,0.7);
        margin-bottom: 30px;
    }}
    .hero-tagline {{
        font-size: 1.2rem;
        color: rgba(255,255,255,0.5);
        max-width: 600px;
        margin: 0 auto 50px;
        line-height: 1.8;
    }}
    .hero-buttons {{
        display: flex;
        justify-content: center;
        gap: 24px;
        margin-bottom: 80px;
        flex-wrap: wrap;
    }}
    .btn-glass {{
        padding: 18px 40px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 16px;
        color: {text};
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s;
    }}
    .btn-glass:hover {{
        background: {primary};
        border-color: {primary};
        transform: translateY(-3px);
        box-shadow: 0 20px 40px {primary}40;
    }}
    .btn-text {{
        padding: 18px 20px;
        color: rgba(255,255,255,0.7);
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s;
    }}
    .btn-text:hover {{
        color: {text};
    }}
    .hero-cards {{
        display: flex;
        justify-content: center;
        gap: 24px;
        flex-wrap: wrap;
    }}
    .glass-card {{
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 24px 32px;
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        transition: all 0.3s;
    }}
    .glass-card:hover {{
        background: rgba(255,255,255,0.1);
        transform: translateY(-5px);
    }}
    .card-icon {{
        font-size: 2rem;
    }}
    .card-content {{
        text-align: left;
    }}
    .card-number {{
        display: block;
        font-size: 1.8rem;
        font-weight: 700;
        color: {text};
    }}
    .card-label {{
        font-size: 0.85rem;
        color: rgba(255,255,255,0.5);
    }}
    @media (max-width: 640px) {{
        .gradient-mesh-hero {{ padding: 100px 20px; }}
        .hero-cards {{ flex-direction: column; align-items: center; }}
    }}
    </style>
    '''
