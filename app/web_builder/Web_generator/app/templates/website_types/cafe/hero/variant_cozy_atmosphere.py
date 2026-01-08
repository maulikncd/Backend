from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Your Cozy Sanctuary")
    subtitle = props.get("subtitle", "Slow down and enjoy the moment")
    cta = props.get("cta", "Our Menu")
    image = props.get("image", "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200")
    
    return f'''
    <section class="cafe-hero cafe-hero-cozy" id="hero">
        <div class="cozy-container">
            <div class="hero-image-wrapper">
                <img src="{image}" alt="Homey Cafe">
                <div class="image-border"></div>
            </div>
            <div class="hero-content">
                <span class="location-tag">📍 Downtown Seattle</span>
                <h1 class="hero-title">{title}</h1>
                <p class="hero-subtitle">{subtitle}</p>
                <div class="hero-footer">
                    <a href="#menu" class="btn-cozy">{cta}</a>
                    <div class="hours">
                        <span>Mon-Fri: 7am - 8pm</span>
                        <span>Sat-Sun: 8am - 9pm</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .cafe-hero-cozy {{
        min-height: 100vh;
        background: {colors.get("background", "#FAF7F2")};
        padding: 120px 24px;
        display: flex;
        align-items: center;
    }}
    .cozy-container {{
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
    }}
    .hero-image-wrapper {{
        position: relative;
    }}
    .hero-image-wrapper img {{
        width: 100%;
        border-radius: 200px 200px 20px 20px;
        box-shadow: 0 40px 80px rgba(111, 78, 55, 0.15);
    }}
    .image-border {{
        position: absolute;
        inset: -20px;
        border: 2px solid {colors.get("primary", "#6F4E37")}30;
        border-radius: 220px 220px 40px 40px;
        z-index: -1;
    }}
    .cafe-hero-cozy .hero-content {{
        animation: fadeIn 1s ease-out;
    }}
    .location-tag {{
        display: inline-block;
        padding: 6px 12px;
        background: #fff;
        border-radius: 4px;
        font-size: 0.85rem;
        font-weight: 500;
        color: {colors.get("primary", "#6F4E37")};
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 24px;
    }}
    .cafe-hero-cozy .hero-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(2.5rem, 5vw, 4.5rem);
        color: {colors.get("text", "#2D2013")};
        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 24px;
    }}
    .cafe-hero-cozy .hero-subtitle {{
        font-size: 1.25rem;
        color: {colors.get("text_muted", "#8B7355")};
        margin-bottom: 40px;
        line-height: 1.6;
    }}
    .hero-footer {{
        display: flex;
        align-items: center;
        gap: 32px;
    }}
    .btn-cozy {{
        display: inline-block;
        padding: 18px 40px;
        background: {colors.get("text", "#2D2013")};
        color: #fff;
        text-decoration: none;
        border-radius: 4px;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    .btn-cozy:hover {{
        background: {colors.get("primary", "#6F4E37")};
        transform: translateY(-2px);
    }}
    .hours {{
        display: flex;
        flex-direction: column;
        font-size: 0.9rem;
        color: {colors.get("text_muted", "#8B7355")};
        border-left: 1px solid rgba(0,0,0,0.1);
        padding-left: 32px;
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @media (max-width: 968px) {{
        .cozy-container {{
            grid-template-columns: 1fr;
            gap: 40px;
            text-align: center;
        }}
        .hero-footer {{
            flex-direction: column;
            gap: 24px;
        }}
        .hours {{
            border-left: none;
            padding-left: 0;
        }}
        .hero-image-wrapper img {{
            border-radius: 100px 100px 20px 20px;
        }}
    }}
    </style>
    '''
