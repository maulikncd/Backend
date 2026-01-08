from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Taste the Difference")
    subtitle = props.get("subtitle", "Fresh ingredients, amazing flavors")
    cta = props.get("cta", "Order Online")
    image = props.get("image", "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1920")
    
    return f'''
    <section class="cafe-hero cafe-hero-bleed" id="hero">
        <div class="bleed-bg" style="background-image: url('{image}')"></div>
        <div class="gradient-overlay"></div>
        <div class="content-area">
            <div class="text-block">
                <h1 class="hero-title">{title}</h1>
                <p class="hero-subtitle">{subtitle}</p>
                <a href="#order" class="btn-order">{cta}</a>
            </div>
        </div>
        <div class="side-info">
            <div class="info-item">
                <span class="info-number">01</span>
                <span class="info-text">Fresh Daily</span>
            </div>
            <div class="info-item">
                <span class="info-number">02</span>
                <span class="info-text">Locally Sourced</span>
            </div>
            <div class="info-item">
                <span class="info-number">03</span>
                <span class="info-text">Made with Love</span>
            </div>
        </div>
    </section>
    
    <style>
    .cafe-hero-bleed {{
        min-height: 100vh;
        position: relative;
        display: flex;
        overflow: hidden;
    }}
    .bleed-bg {{
        position: absolute;
        inset: 0;
        background-size: cover;
        background-position: center;
        transform: scale(1.02);
    }}
    .gradient-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(
            90deg,
            rgba(0,0,0,0.8) 0%,
            rgba(0,0,0,0.4) 50%,
            rgba(0,0,0,0.2) 100%
        );
    }}
    .content-area {{
        position: relative;
        z-index: 2;
        flex: 1;
        display: flex;
        align-items: center;
        padding: 80px;
    }}
    .text-block {{
        max-width: 600px;
        animation: slideRight 0.8s ease-out;
    }}
    .cafe-hero-bleed .hero-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(3rem, 6vw, 5rem);
        color: #fff;
        font-weight: 700;
        line-height: 1.1;
        margin-bottom: 20px;
    }}
    .cafe-hero-bleed .hero-subtitle {{
        font-size: 1.2rem;
        color: rgba(255,255,255,0.8);
        margin-bottom: 32px;
        line-height: 1.6;
    }}
    .btn-order {{
        display: inline-block;
        padding: 18px 40px;
        background: {colors.get("primary", "#6F4E37")};
        color: #fff;
        text-decoration: none;
        font-weight: 600;
        border-radius: 4px;
        transition: all 0.3s ease;
    }}
    .btn-order:hover {{
        background: {colors.get("secondary", "#C4A77D")};
        color: {colors.get("text", "#2D2013")};
        transform: translateY(-2px);
    }}
    .side-info {{
        position: absolute;
        right: 60px;
        top: 50%;
        transform: translateY(-50%);
        z-index: 2;
        display: flex;
        flex-direction: column;
        gap: 30px;
    }}
    .info-item {{
        display: flex;
        flex-direction: column;
        gap: 4px;
        text-align: right;
        opacity: 0.9;
    }}
    .info-number {{
        font-size: 0.75rem;
        color: {colors.get("secondary", "#C4A77D")};
        letter-spacing: 2px;
    }}
    .info-text {{
        color: #fff;
        font-weight: 500;
    }}
    @keyframes slideRight {{
        from {{ opacity: 0; transform: translateX(-30px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    @media (max-width: 968px) {{
        .content-area {{
            padding: 40px;
        }}
        .side-info {{
            display: none;
        }}
    }}
    </style>
    '''
