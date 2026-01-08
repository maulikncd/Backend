from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Corporate Modern - Professional hero with bold statement,
    client logos and modern corporate aesthetic
    """
    name = props.get("name", props.get("businessName", "Apex Digital"))
    tagline = props.get("tagline", "We Build What's Next")
    description = props.get("description", "A full-service digital agency helping brands grow through strategy, design, and technology.")
    cta = props.get("cta", "Start a Project")
    
    primary = colors.get("primary", "#2563EB")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#0F172A")
    
    return f'''
    <section class="agency-hero" id="hero">
        <div class="hero-container">
            <div class="hero-content">
                <div class="hero-badge">
                    <span class="badge-dot"></span>
                    Top Rated Agency 2024
                </div>
                
                <h1 class="hero-headline">{tagline}</h1>
                <p class="hero-desc">{description}</p>
                
                <div class="cta-group">
                    <a href="#contact" class="btn-primary">{cta}</a>
                    <a href="#work" class="btn-secondary">
                        <span class="play-icon">▶</span>
                        Watch Showreel
                    </a>
                </div>
                
                <div class="client-section">
                    <span class="clients-label">Trusted by industry leaders</span>
                    <div class="client-logos">
                        <span class="client-logo">Google</span>
                        <span class="client-logo">Microsoft</span>
                        <span class="client-logo">Spotify</span>
                        <span class="client-logo">Airbnb</span>
                    </div>
                </div>
            </div>
            
            <div class="hero-visual">
                <div class="visual-grid">
                    <div class="grid-item item-1">
                        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600" alt="Project">
                    </div>
                    <div class="grid-item item-2">
                        <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400" alt="Team">
                    </div>
                    <div class="grid-item item-3">
                        <div class="stat-card">
                            <span class="stat-num">250+</span>
                            <span class="stat-label">Projects Delivered</span>
                        </div>
                    </div>
                    <div class="grid-item item-4">
                        <div class="stat-card accent">
                            <span class="stat-num">98%</span>
                            <span class="stat-label">Client Satisfaction</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    .agency-hero {{
        min-height: 100vh;
        background: {bg};
        display: flex;
        align-items: center;
        padding: 120px 60px;
    }}
    .hero-container {{
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
    }}
    .hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 10px 20px;
        background: {primary}10;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 600;
        color: {primary};
        margin-bottom: 30px;
    }}
    .badge-dot {{
        width: 8px;
        height: 8px;
        background: #22C55E;
        border-radius: 50%;
    }}
    .hero-headline {{
        font-family: 'Inter', sans-serif;
        font-size: clamp(3rem, 5vw, 4.5rem);
        font-weight: 800;
        color: {text};
        line-height: 1.1;
        margin-bottom: 24px;
    }}
    .hero-desc {{
        font-size: 1.2rem;
        color: {text}90;
        line-height: 1.8;
        margin-bottom: 40px;
        max-width: 500px;
    }}
    .cta-group {{
        display: flex;
        gap: 20px;
        margin-bottom: 60px;
        flex-wrap: wrap;
    }}
    .btn-primary {{
        padding: 18px 40px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s;
        box-shadow: 0 4px 20px {primary}30;
    }}
    .btn-primary:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px {primary}40;
    }}
    .btn-secondary {{
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 18px 30px;
        background: transparent;
        color: {text};
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s;
    }}
    .btn-secondary:hover {{ color: {primary}; }}
    .play-icon {{
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: {text}08;
        border-radius: 50%;
        font-size: 0.8rem;
    }}
    .client-section {{
        padding-top: 30px;
        border-top: 1px solid {text}10;
    }}
    .clients-label {{
        display: block;
        font-size: 0.8rem;
        color: {text}50;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }}
    .client-logos {{
        display: flex;
        gap: 40px;
        flex-wrap: wrap;
    }}
    .client-logo {{
        font-size: 1rem;
        font-weight: 700;
        color: {text}40;
    }}
    .hero-visual {{
        position: relative;
    }}
    .visual-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }}
    .grid-item {{
        border-radius: 16px;
        overflow: hidden;
    }}
    .grid-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .item-1 {{
        grid-row: span 2;
        height: 400px;
    }}
    .item-2 {{
        height: 190px;
    }}
    .stat-card {{
        height: 100%;
        padding: 30px;
        background: {text}05;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .stat-card.accent {{
        background: {primary};
    }}
    .stat-num {{
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
    }}
    .stat-card.accent .stat-num {{ color: white; }}
    .stat-label {{
        font-size: 0.9rem;
        color: {text}60;
    }}
    .stat-card.accent .stat-label {{ color: rgba(255,255,255,0.8); }}
    @media (max-width: 1024px) {{
        .hero-container {{ grid-template-columns: 1fr; gap: 60px; }}
        .agency-hero {{ padding: 120px 40px; }}
    }}
    @media (max-width: 640px) {{
        .agency-hero {{ padding: 100px 24px; }}
        .visual-grid {{ grid-template-columns: 1fr; }}
        .item-1 {{ grid-row: span 1; height: 250px; }}
    }}
    </style>
    '''
