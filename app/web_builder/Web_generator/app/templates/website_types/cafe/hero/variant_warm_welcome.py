from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Welcome to Our Cafe")
    subtitle = props.get("subtitle", "Where every cup tells a story")
    cta = props.get("cta", "View Menu")
    cta_secondary = props.get("ctaSecondary", "Reserve Table")
    image = props.get("image", "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="cafe-hero cafe-hero-warm" id="hero">
        <div class="hero-bg" style="background-image: url('{image}')"></div>
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <div class="hero-badge">☕ Est. 2024</div>
            <h1 class="hero-title">{title}</h1>
            <p class="hero-subtitle">{subtitle}</p>
            <div class="hero-cta">
                <a href="#menu" class="btn btn-primary">{cta}</a>
                <a href="#contact" class="btn btn-outline">{cta_secondary}</a>
            </div>
            <div class="hero-features">
                <div class="feature">
                    <span class="feature-icon">🌿</span>
                    <span>Organic Beans</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">🍰</span>
                    <span>Fresh Pastries</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">📶</span>
                    <span>Free WiFi</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .cafe-hero-warm {{
        min-height: 100vh;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        overflow: hidden;
    }}
    .cafe-hero-warm .hero-bg {{
        position: absolute;
        inset: 0;
        background-size: cover;
        background-position: center;
        transform: scale(1.05);
        animation: slowZoom 20s ease-in-out infinite alternate;
    }}
    @keyframes slowZoom {{
        from {{ transform: scale(1); }}
        to {{ transform: scale(1.1); }}
    }}
    .cafe-hero-warm .hero-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(
            to bottom,
            rgba(45, 32, 19, 0.6) 0%,
            rgba(45, 32, 19, 0.8) 100%
        );
    }}
    .cafe-hero-warm .hero-content {{
        position: relative;
        z-index: 2;
        max-width: 800px;
        padding: 40px 24px;
        animation: fadeUp 1s ease-out;
    }}
    .cafe-hero-warm .hero-badge {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}30;
        border: 1px solid {primary}50;
        color: {secondary};
        border-radius: 50px;
        font-size: 0.9rem;
        letter-spacing: 2px;
        margin-bottom: 24px;
    }}
    .cafe-hero-warm .hero-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(2.5rem, 6vw, 5rem);
        font-weight: 700;
        color: #fff;
        margin-bottom: 20px;
        line-height: 1.1;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }}
    .cafe-hero-warm .hero-subtitle {{
        font-size: clamp(1.1rem, 2vw, 1.4rem);
        color: rgba(255,255,255,0.9);
        margin-bottom: 32px;
        font-style: italic;
    }}
    .cafe-hero-warm .hero-cta {{
        display: flex;
        gap: 16px;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 48px;
    }}
    .cafe-hero-warm .btn-primary {{
        background: {primary};
        color: #fff;
        padding: 16px 36px;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid {primary};
    }}
    .cafe-hero-warm .btn-primary:hover {{
        background: transparent;
        transform: translateY(-2px);
    }}
    .cafe-hero-warm .btn-outline {{
        background: transparent;
        color: #fff;
        padding: 16px 36px;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        border: 2px solid rgba(255,255,255,0.5);
        transition: all 0.3s ease;
    }}
    .cafe-hero-warm .btn-outline:hover {{
        background: rgba(255,255,255,0.1);
        border-color: #fff;
    }}
    .cafe-hero-warm .hero-features {{
        display: flex;
        gap: 32px;
        justify-content: center;
        flex-wrap: wrap;
    }}
    .cafe-hero-warm .feature {{
        display: flex;
        align-items: center;
        gap: 8px;
        color: rgba(255,255,255,0.8);
        font-size: 0.95rem;
    }}
    .cafe-hero-warm .feature-icon {{
        font-size: 1.2rem;
    }}
    @keyframes fadeUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @media (max-width: 768px) {{
        .cafe-hero-warm .hero-features {{
            flex-direction: column;
            gap: 16px;
        }}
    }}
    </style>
    '''
