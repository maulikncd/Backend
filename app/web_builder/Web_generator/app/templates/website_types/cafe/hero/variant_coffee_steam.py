from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Crafted with Love")
    subtitle = props.get("subtitle", "Premium coffee, baked fresh daily")
    cta = props.get("cta", "Order Now")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="cafe-hero cafe-hero-steam" id="hero">
        <div class="steam-container">
            <div class="steam steam-1"></div>
            <div class="steam steam-2"></div>
            <div class="steam steam-3"></div>
        </div>
        <div class="hero-decoration">
            <div class="coffee-cup">
                <div class="cup-body"></div>
                <div class="cup-handle"></div>
            </div>
        </div>
        <div class="hero-content">
            <span class="hero-tagline">Since 2024</span>
            <h1 class="hero-title">{title}</h1>
            <div class="title-decoration"></div>
            <p class="hero-subtitle">{subtitle}</p>
            <a href="#menu" class="btn-cta">{cta}</a>
        </div>
    </section>
    
    <style>
    .cafe-hero-steam {{
        min-height: 100vh;
        background: linear-gradient(135deg, {background} 0%, {background}D9 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }}
    .steam-container {{
        position: absolute;
        bottom: 30%;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 200px;
        z-index: 1;
    }}
    .steam {{
        position: absolute;
        bottom: 0;
        background: linear-gradient(to top, rgba(255,255,255,0.3), transparent);
        border-radius: 50%;
        filter: blur(10px);
        animation: rise 3s ease-in-out infinite;
    }}
    .steam-1 {{
        left: 20%;
        width: 40px;
        height: 80px;
        animation-delay: 0s;
    }}
    .steam-2 {{
        left: 50%;
        width: 30px;
        height: 100px;
        animation-delay: 0.5s;
    }}
    .steam-3 {{
        left: 70%;
        width: 35px;
        height: 70px;
        animation-delay: 1s;
    }}
    @keyframes rise {{
        0% {{ opacity: 0; transform: translateY(0) scale(1); }}
        50% {{ opacity: 0.5; }}
        100% {{ opacity: 0; transform: translateY(-150px) scale(1.5); }}
    }}
    .hero-decoration {{
        position: absolute;
        bottom: 10%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0.1;
    }}
    .coffee-cup {{
        position: relative;
        width: 120px;
        height: 100px;
    }}
    .cup-body {{
        width: 100px;
        height: 80px;
        background: {secondary};
        border-radius: 0 0 50px 50px;
    }}
    .cup-handle {{
        position: absolute;
        right: -20px;
        top: 10px;
        width: 40px;
        height: 50px;
        border: 8px solid {secondary};
        border-left: none;
        border-radius: 0 25px 25px 0;
    }}
    .cafe-hero-steam .hero-content {{
        position: relative;
        z-index: 2;
        text-align: center;
        padding: 40px;
        animation: fadeIn 1s ease-out;
    }}
    .cafe-hero-steam .hero-tagline {{
        display: block;
        color: {secondary};
        font-size: 0.9rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 20px;
    }}
    .cafe-hero-steam .hero-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(3rem, 8vw, 6rem);
        color: #fff;
        font-weight: 700;
        margin-bottom: 16px;
    }}
    .title-decoration {{
        width: 80px;
        height: 3px;
        background: linear-gradient(90deg, transparent, {secondary}, transparent);
        margin: 0 auto 24px;
    }}
    .cafe-hero-steam .hero-subtitle {{
        font-size: 1.2rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 40px;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }}
    .cafe-hero-steam .btn-cta {{
        display: inline-block;
        padding: 18px 48px;
        background: {primary};
        color: #fff;
        text-decoration: none;
        border-radius: 4px;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        border: 2px solid {primary};
    }}
    .cafe-hero-steam .btn-cta:hover {{
        background: transparent;
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(111, 78, 55, 0.3);
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>
    '''
