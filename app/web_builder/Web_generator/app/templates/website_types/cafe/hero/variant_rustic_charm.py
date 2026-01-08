from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Handcrafted Goodness")
    subtitle = props.get("subtitle", "Traditional recipes, modern taste")
    cta = props.get("cta", "Our Story")
    image = props.get("image", "https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=1200")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="cafe-hero cafe-hero-rustic" id="hero">
        <div class="rustic-bg" style="background-image: url('{image}')"></div>
        <div class="rustic-overlay"></div>
        <div class="wood-texture"></div>
        <div class="hero-content">
            <div class="stamp">EST. 2024</div>
            <h1 class="hero-title">{title}</h1>
            <div class="divider">
                <span>❧</span>
            </div>
            <p class="hero-subtitle">{subtitle}</p>
            <a href="#about" class="btn-rustic">{cta}</a>
        </div>
    </section>
    
    <style>
    .cafe-hero-rustic {{
        min-height: 100vh;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }}
    .rustic-bg {{
        position: absolute;
        inset: 0;
        background-size: cover;
        background-position: center;
    }}
    .rustic-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(
            to bottom,
            rgba(62, 39, 35, 0.7) 0%,
            rgba(62, 39, 35, 0.85) 100%
        );
    }}
    .wood-texture {{
        position: absolute;
        inset: 0;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
        opacity: 0.03;
    }}
    .cafe-hero-rustic .hero-content {{
        position: relative;
        z-index: 2;
        padding: 40px;
        animation: fadeIn 1s ease-out;
    }}
    .stamp {{
        display: inline-block;
        padding: 8px 24px;
        border: 2px solid {secondary};
        color: {secondary};
        font-size: 0.85rem;
        letter-spacing: 4px;
        margin-bottom: 24px;
        transform: rotate(-3deg);
    }}
    .cafe-hero-rustic .hero-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(2.5rem, 6vw, 5rem);
        color: #fff;
        font-weight: 700;
        margin-bottom: 20px;
    }}
    .divider {{
        margin-bottom: 20px;
    }}
    .divider span {{
        font-size: 2rem;
        color: {secondary};
    }}
    .cafe-hero-rustic .hero-subtitle {{
        font-size: 1.2rem;
        color: rgba(255,255,255,0.8);
        font-style: italic;
        margin-bottom: 40px;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }}
    .btn-rustic {{
        display: inline-block;
        padding: 16px 40px;
        background: transparent;
        color: #fff;
        text-decoration: none;
        border: 2px solid {secondary};
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 0.9rem;
        transition: all 0.3s ease;
    }}
    .btn-rustic:hover {{
        background: {secondary};
        color: {text};
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>
    '''
