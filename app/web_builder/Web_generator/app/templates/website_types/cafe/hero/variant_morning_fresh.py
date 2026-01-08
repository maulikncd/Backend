from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Fresh Every Morning")
    subtitle = props.get("subtitle", "Artisan pastries and single-origin coffee")
    cta = props.get("cta", "Our Menu")
    
    return f'''
    <section class="cafe-hero cafe-hero-morning" id="hero">
        <div class="morning-container">
            <div class="hero-top">
                <div class="time-badge">
                    <span class="time-icon">🕕</span>
                    <span>Serving from 6:00 AM</span>
                </div>
                <h1 class="hero-title">{title}</h1>
                <p class="hero-subtitle">{subtitle}</p>
            </div>
            <div class="menu-preview">
                <div class="menu-item">
                    <span class="item-icon">🥐</span>
                    <span class="item-name">Croissants</span>
                    <span class="item-price">$3.50</span>
                </div>
                <div class="menu-item">
                    <span class="item-icon">☕</span>
                    <span class="item-name">Espresso</span>
                    <span class="item-price">$2.50</span>
                </div>
                <div class="menu-item">
                    <span class="item-icon">🥯</span>
                    <span class="item-name">Bagels</span>
                    <span class="item-price">$4.00</span>
                </div>
            </div>
            <a href="#menu" class="btn-cta">{cta}</a>
        </div>
    </section>
    
    <style>
    .cafe-hero-morning {{
        padding: 120px 24px;
        background: {colors.get("background", "#FFF8F0")};
        text-align: center;
        min-height: 80vh;
        display: flex;
        align-items: center;
    }}
    .morning-container {{
        max-width: 800px;
        margin: 0 auto;
    }}
    .time-badge {{
        display: inline-flex;
        align-items: center;
        gap: 12px;
        padding: 10px 24px;
        background: #fff;
        border-radius: 50px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 32px;
        font-size: 0.9rem;
        color: {colors.get("text", "#2D2013")};
    }}
    .time-icon {{
        font-size: 1.2rem;
    }}
    .cafe-hero-morning .hero-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(3rem, 8vw, 5rem);
        color: {colors.get("text", "#2D2013")};
        font-weight: 700;
        margin-bottom: 16px;
    }}
    .cafe-hero-morning .hero-subtitle {{
        font-size: 1.2rem;
        color: {colors.get("text_muted", "#8B7355")};
        margin-bottom: 40px;
    }}
    .menu-preview {{
        display: flex;
        gap: 16px;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 40px;
    }}
    .menu-item {{
        background: #fff;
        padding: 16px 24px;
        border-radius: 12px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
        min-width: 120px;
    }}
    .menu-item:hover {{
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }}
    .item-icon {{
        font-size: 2rem;
    }}
    .item-name {{
        font-weight: 600;
        color: {colors.get("text", "#2D2013")};
    }}
    .item-price {{
        color: {colors.get("primary", "#6F4E37")};
        font-weight: 500;
    }}
    .cafe-hero-morning .btn-cta {{
        display: inline-block;
        padding: 16px 40px;
        background: {colors.get("primary", "#6F4E37")};
        color: #fff;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    .cafe-hero-morning .btn-cta:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 30px {colors.get("primary", "#6F4E37")}30;
    }}
    </style>
    '''
