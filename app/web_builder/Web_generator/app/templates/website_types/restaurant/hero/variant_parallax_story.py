from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Parallax Story - Multi-layer parallax with storytelling elements
    """
    name = props.get("name", props.get("businessName", "Artisan"))
    tagline = props.get("tagline", "Crafted With Passion")
    description = props.get("description", "Every ingredient has a story")
    cta = props.get("cta", "Experience It")
    
    primary = colors.get("primary", "#8B4513")
    bg = colors.get("background", "#0D0D0D")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="hero-parallax" id="hero">
        <div class="parallax-layer layer-bg">
            <img src="https://images.unsplash.com/photo-1600891964092-4316c288032e?w=1920" alt="Background">
        </div>
        <div class="parallax-layer layer-mid">
            <img src="https://images.unsplash.com/photo-1546833998-877b37c2e5c6?w=800" alt="Food" class="floating-dish">
        </div>
        <div class="parallax-overlay"></div>
        
        <div class="hero-content">
            <div class="content-block">
                <div class="eyebrow">Since 2015</div>
                <h1 class="title">{name}</h1>
                <p class="tagline">{tagline}</p>
                <div class="separator">
                    <span></span>
                    <span class="sep-icon">◆</span>
                    <span></span>
                </div>
                <p class="desc">{description}</p>
                <a href="#reservation" class="btn-parallax">{cta}</a>
            </div>
        </div>
        
        <div class="stats-bar">
            <div class="stat">
                <div class="stat-num">15+</div>
                <div class="stat-label">Years Experience</div>
            </div>
            <div class="stat">
                <div class="stat-num">50K+</div>
                <div class="stat-label">Happy Guests</div>
            </div>
            <div class="stat">
                <div class="stat-num">120+</div>
                <div class="stat-label">Signature Dishes</div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Poppins:wght@300;400;500&display=swap');
    
    .hero-parallax {{
        min-height: 100vh;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }}
    .parallax-layer {{
        position: absolute;
        inset: 0;
    }}
    .layer-bg img {{
        width: 100%;
        height: 110%;
        object-fit: cover;
    }}
    .layer-mid {{
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding-right: 10%;
    }}
    .floating-dish {{
        width: 400px;
        height: 400px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0 30px 80px rgba(0,0,0,0.5);
        animation: floatDish 6s ease-in-out infinite;
    }}
    @keyframes floatDish {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-20px); }}
    }}
    .parallax-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 60%, transparent 100%);
        z-index: 1;
    }}
    .hero-content {{
        position: relative;
        z-index: 2;
        flex: 1;
        display: flex;
        align-items: center;
        padding: 100px 80px;
    }}
    .content-block {{
        max-width: 600px;
    }}
    .eyebrow {{
        display: inline-block;
        padding: 10px 25px;
        background: {primary};
        color: white;
        font-size: 0.8rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }}
    .title {{
        font-family: 'Cinzel', serif;
        font-size: clamp(4rem, 10vw, 7rem);
        font-weight: 400;
        color: {text};
        margin-bottom: 20px;
        line-height: 1.1;
    }}
    .tagline {{
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        color: {primary};
        font-weight: 300;
        margin-bottom: 25px;
    }}
    .separator {{
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 25px;
    }}
    .separator span:not(.sep-icon) {{
        width: 50px;
        height: 1px;
        background: {text}30;
    }}
    .sep-icon {{
        color: {primary};
        font-size: 0.8rem;
    }}
    .desc {{
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        color: {text}80;
        line-height: 1.8;
        margin-bottom: 40px;
    }}
    .btn-parallax {{
        display: inline-block;
        padding: 20px 50px;
        background: transparent;
        border: 2px solid {primary};
        color: {primary};
        text-decoration: none;
        font-size: 0.9rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        transition: all 0.4s;
    }}
    .btn-parallax:hover {{
        background: {primary};
        color: white;
    }}
    .stats-bar {{
        position: relative;
        z-index: 2;
        display: flex;
        justify-content: center;
        gap: 100px;
        padding: 50px;
        background: rgba(0,0,0,0.8);
        backdrop-filter: blur(10px);
    }}
    .stat {{
        text-align: center;
    }}
    .stat-num {{
        font-family: 'Cinzel', serif;
        font-size: 2.5rem;
        color: {primary};
        margin-bottom: 8px;
    }}
    .stat-label {{
        font-size: 0.85rem;
        color: {text}70;
        letter-spacing: 1px;
    }}
    @media (max-width: 968px) {{
        .floating-dish {{ display: none; }}
        .parallax-overlay {{ background: rgba(0,0,0,0.7); }}
        .hero-content {{ padding: 80px 30px; }}
        .stats-bar {{ gap: 40px; flex-wrap: wrap; }}
    }}
    </style>
    '''
