from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Minimal Zen - Clean, minimal Japanese-inspired design
    with lots of whitespace and subtle animations
    """
    name = props.get("name", props.get("businessName", "Zen"))
    tagline = props.get("tagline", "Pure Flavors")
    description = props.get("description", "Simplicity is the ultimate sophistication")
    cta = props.get("cta", "Reserve")
    
    primary = colors.get("primary", "#2D3436")
    bg = colors.get("background", "#FAFAFA")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="hero-zen" id="hero">
        <div class="zen-container">
            <div class="left-panel">
                <div class="vertical-text">Established 2010</div>
            </div>
            
            <div class="center-content">
                <div class="zen-symbol">禅</div>
                <h1 class="hero-title">{name}</h1>
                <div class="title-underline"></div>
                <p class="hero-tagline">{tagline}</p>
                <p class="hero-desc">{description}</p>
                <a href="#reservation" class="btn-zen">{cta}</a>
            </div>
            
            <div class="right-panel">
                <div class="image-frame">
                    <img src="https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=800" alt="Cuisine">
                    <div class="frame-accent"></div>
                </div>
            </div>
        </div>
        
        <div class="bottom-nav">
            <a href="#menu" class="nav-item">Menu</a>
            <span class="nav-divider"></span>
            <a href="#about" class="nav-item">Story</a>
            <span class="nav-divider"></span>
            <a href="#contact" class="nav-item">Contact</a>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant:wght@300;400;500&family=Karla:wght@300;400&display=swap');
    
    .hero-zen {{
        min-height: 100vh;
        background: {bg};
        display: flex;
        flex-direction: column;
    }}
    .zen-container {{
        flex: 1;
        display: grid;
        grid-template-columns: 100px 1fr 1fr;
        gap: 40px;
        padding: 60px;
        align-items: center;
    }}
    .left-panel {{
        display: flex;
        justify-content: center;
    }}
    .vertical-text {{
        writing-mode: vertical-rl;
        color: {text}40;
        font-size: 0.75rem;
        letter-spacing: 4px;
        text-transform: uppercase;
    }}
    .center-content {{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding: 40px 0;
    }}
    .zen-symbol {{
        font-size: 3rem;
        color: {primary}30;
        margin-bottom: 30px;
    }}
    .hero-title {{
        font-family: 'Cormorant', serif;
        font-size: clamp(4rem, 10vw, 8rem);
        font-weight: 300;
        color: {text};
        letter-spacing: 10px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }}
    .title-underline {{
        width: 60px;
        height: 2px;
        background: {primary};
        margin-bottom: 30px;
    }}
    .hero-tagline {{
        font-family: 'Cormorant', serif;
        font-size: 1.6rem;
        color: {text};
        font-weight: 300;
        margin-bottom: 15px;
    }}
    .hero-desc {{
        font-family: 'Karla', sans-serif;
        font-size: 1rem;
        color: {text}70;
        margin-bottom: 50px;
        max-width: 400px;
        line-height: 1.8;
    }}
    .btn-zen {{
        padding: 18px 50px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        transition: all 0.4s ease;
    }}
    .btn-zen:hover {{
        background: transparent;
        color: {primary};
        box-shadow: inset 0 0 0 2px {primary};
    }}
    .right-panel {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 40px;
    }}
    .image-frame {{
        position: relative;
        max-width: 450px;
    }}
    .image-frame img {{
        width: 100%;
        height: auto;
        display: block;
    }}
    .frame-accent {{
        position: absolute;
        top: -20px;
        right: -20px;
        width: 100%;
        height: 100%;
        border: 2px solid {primary}30;
        z-index: -1;
    }}
    .bottom-nav {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 40px;
        padding: 40px;
        border-top: 1px solid {text}10;
    }}
    .nav-item {{
        color: {text}60;
        text-decoration: none;
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        transition: color 0.3s;
    }}
    .nav-item:hover {{ color: {primary}; }}
    .nav-divider {{
        width: 30px;
        height: 1px;
        background: {text}20;
    }}
    @media (max-width: 968px) {{
        .zen-container {{ 
            grid-template-columns: 1fr;
            text-align: center;
        }}
        .left-panel {{ display: none; }}
        .center-content {{ align-items: center; }}
        .right-panel {{ order: -1; }}
    }}
    </style>
    '''
