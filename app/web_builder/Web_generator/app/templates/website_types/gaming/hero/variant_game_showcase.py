from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "CYBERPUNK 2077")
    subtitle = props.get("subtitle", "Enhanced Edition Now Available")
    cta = props.get("cta", "BUY NOW")
    image = props.get("image", "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-hero gaming-hero-showcase" id="hero">
        <div class="showcase-bg" style="background-image: url('{image}')"></div>
        <div class="showcase-overlay"></div>
        <div class="hero-content">
            <div class="hero-labels">
                <span class="label">PC</span>
                <span class="label">PS5</span>
                <span class="label">XBOX</span>
            </div>
            <h1 class="hero-title">{title}</h1>
            <p class="hero-subtitle">{subtitle}</p>
            <div class="hero-actions">
                <a href="#buy" class="btn-showcase primary">{cta}</a>
                <a href="#more" class="btn-showcase secondary">Learn More</a>
            </div>
            <div class="showcase-items">
                <div class="item">
                    <span class="item-title">Rating</span>
                    <span class="item-value">9.5/10</span>
                </div>
                <div class="item">
                    <span class="item-title">Players</span>
                    <span class="item-value">10M+</span>
                </div>
                <div class="item">
                    <span class="item-title">Awards</span>
                    <span class="item-value">50+</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-hero-showcase {{
        min-height: 100vh;
        position: relative;
        display: flex;
        align-items: center;
        padding-left: 10%;
        overflow: hidden;
        background: {background};
    }}
    .showcase-bg {{
        position: absolute;
        inset: 0;
        background-size: cover;
        background-position: center;
        opacity: 0.6;
        transition: 0.5s;
    }}
    .showcase-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, {background} 20%, transparent 80%);
    }}
    .gaming-hero-showcase .hero-content {{
        position: relative;
        z-index: 2;
        max-width: 600px;
    }}
    .hero-labels {{ display: flex; gap: 10px; margin-bottom: 20px; }}
    .label {{
        background: {primary}20;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: 700;
        color: {text};
    }}
    .gaming-hero-showcase .hero-title {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(3rem, 8vw, 6rem);
        font-weight: 800;
        line-height: 1;
        margin-bottom: 20px;
        color: {text};
        text-transform: uppercase;
    }}
    .gaming-hero-showcase .hero-subtitle {{
        font-size: 1.2rem;
        color: {secondary};
        margin-bottom: 40px;
        max-width: 400px;
    }}
    .hero-actions {{ display: flex; gap: 20px; margin-bottom: 60px; }}
    .btn-showcase {{
        padding: 15px 40px;
        font-weight: 700;
        text-transform: uppercase;
        text-decoration: none;
        transition: 0.3s;
    }}
    .btn-showcase.primary {{
        background: {primary};
        color: {background};
    }}
    .btn-showcase.secondary {{
        border: 2px solid {text};
        color: {text};
    }}
    .showcase-items {{ display: flex; gap: 40px; }}
    .item {{ display: flex; flex-direction: column; }}
    .item-title {{ font-size: 0.8rem; color: {secondary}; text-transform: uppercase; }}
    .item-value {{ font-size: 1.5rem; font-weight: 700; color: {text}; }}
    </style>
    '''
