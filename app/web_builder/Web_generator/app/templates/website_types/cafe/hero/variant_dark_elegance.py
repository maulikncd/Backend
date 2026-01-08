from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Dark Elegance - Sophisticated dark theme hero with 
    dramatic lighting and premium feel
    """
    title = props.get("title", "The Art of Coffee")
    subtitle = props.get("subtitle", "Experience perfection in every sip")
    cta = props.get("cta", "Discover Our Story")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="dark-elegance-hero" id="hero">
        <div class="hero-bg-pattern"></div>
        <div class="hero-overlay"></div>
        <div class="hero-container">
            <div class="hero-text-center">
                <div class="decorative-line"></div>
                <span class="hero-tagline">Est. 2024</span>
                <h1 class="hero-title">{title}</h1>
                <p class="hero-subtitle">{subtitle}</p>
                <a href="#menu" class="btn-gold">{cta}</a>
                <div class="decorative-line bottom"></div>
            </div>
        </div>
        <div class="hero-footer">
            <div class="footer-item">
                <span class="footer-icon">📍</span>
                <span>123 Coffee Lane, NYC</span>
            </div>
            <div class="footer-item">
                <span class="footer-icon">🕐</span>
                <span>7AM - 10PM Daily</span>
            </div>
            <div class="footer-item">
                <span class="footer-icon">📞</span>
                <span>+1 (555) 123-4567</span>
            </div>
        </div>
    </section>
    
    <style>
    .dark-elegance-hero {{
        min-height: 100vh;
        background: {background};
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: #fff;
        overflow: hidden;
    }}
    .hero-bg-pattern {{
        position: absolute;
        inset: 0;
        background-image: url("https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=1920");
        background-size: cover;
        background-position: center;
        opacity: 0.3;
    }}
    .hero-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(
            180deg,
            rgba({background}B3) 0%,
            rgba({background}80) 50%,
            rgba({background}E6) 100%
        );
    }}
    .hero-container {{
        position: relative;
        z-index: 2;
        padding: 60px 24px;
    }}
    .hero-text-center {{ max-width: 800px; }}
    .decorative-line {{
        width: 1px;
        height: 80px;
        background: linear-gradient(to bottom, transparent, {primary}, transparent);
        margin: 0 auto 30px;
    }}
    .decorative-line.bottom {{
        margin: 40px auto 0;
        background: linear-gradient(to bottom, {primary}, transparent);
    }}
    .hero-tagline {{
        display: block;
        font-size: 0.9rem;
        letter-spacing: 5px;
        text-transform: uppercase;
        color: {primary};
        margin-bottom: 30px;
    }}
    .dark-elegance-hero .hero-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(3rem, 8vw, 6rem);
        font-weight: 400;
        line-height: 1;
        margin-bottom: 24px;
        letter-spacing: -1px;
    }}
    .dark-elegance-hero .hero-subtitle {{
        font-size: 1.3rem;
        color: rgba(255,255,255,0.7);
        font-weight: 300;
        margin-bottom: 40px;
        letter-spacing: 1px;
    }}
    .btn-gold {{
        display: inline-block;
        padding: 18px 50px;
        background: transparent;
        border: 1px solid {primary};
        color: {primary};
        text-decoration: none;
        font-size: 0.9rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        transition: all 0.4s;
    }}
    .btn-gold:hover {{
        background: {primary};
        color: {background};
    }}
    .hero-footer {{
        position: absolute;
        bottom: 40px;
        left: 0;
        right: 0;
        display: flex;
        justify-content: center;
        gap: 60px;
        z-index: 2;
        flex-wrap: wrap;
        padding: 0 24px;
    }}
    .footer-item {{
        display: flex;
        align-items: center;
        gap: 10px;
        color: rgba(255,255,255,0.6);
        font-size: 0.9rem;
    }}
    .footer-icon {{ font-size: 1.1rem; }}
    @media (max-width: 768px) {{
        .hero-footer {{ gap: 30px; bottom: 20px; }}
        .decorative-line {{ height: 50px; }}
    }}
    </style>
    '''
