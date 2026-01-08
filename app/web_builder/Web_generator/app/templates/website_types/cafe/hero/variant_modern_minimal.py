from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Simply Coffee")
    subtitle = props.get("subtitle", "No frills. Just great coffee.")
    cta = props.get("cta", "Menu")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    text_muted = colors.get("text_muted") or secondary
    
    return f'''
    <section class="cafe-hero cafe-hero-minimal" id="hero">
        <div class="minimal-container">
            <div class="logo-mark">C</div>
            <h1 class="hero-title">{title}</h1>
            <p class="hero-subtitle">{subtitle}</p>
            <a href="#menu" class="btn-minimal">{cta} →</a>
        </div>
        <div class="bottom-bar">
            <div class="bar-item">
                <span class="bar-label">Location</span>
                <span class="bar-value">123 Coffee St</span>
            </div>
            <div class="bar-item">
                <span class="bar-label">Hours</span>
                <span class="bar-value">7AM - 7PM</span>
            </div>
            <div class="bar-item">
                <span class="bar-label">Contact</span>
                <span class="bar-value">hello@cafe.com</span>
            </div>
        </div>
    </section>
    
    <style>
    .cafe-hero-minimal {{
        min-height: 100vh;
        background: {background};
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        position: relative;
    }}
    .minimal-container {{
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 40px;
    }}
    .logo-mark {{
        width: 80px;
        height: 80px;
        border: 2px solid {text};
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 40px;
        color: {text};
    }}
    .cafe-hero-minimal .hero-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-size: clamp(3rem, 8vw, 6rem);
        font-weight: 400;
        color: {text};
        margin-bottom: 16px;
        letter-spacing: -0.02em;
    }}
    .cafe-hero-minimal .hero-subtitle {{
        font-size: 1.1rem;
        color: {text_muted};
        margin-bottom: 40px;
    }}
    .btn-minimal {{
        display: inline-block;
        padding: 16px 32px;
        background: {text};
        color: #fff;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
    }}
    .btn-minimal:hover {{
        transform: translateX(5px);
    }}
    .bottom-bar {{
        width: 100%;
        display: flex;
        justify-content: center;
        gap: 60px;
        padding: 40px;
        border-top: 1px solid rgba(0,0,0,0.1);
    }}
    .bar-item {{
        display: flex;
        flex-direction: column;
        gap: 4px;
    }}
    .bar-label {{
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: {text_muted};
    }}
    .bar-value {{
        font-weight: 500;
        color: {text};
    }}
    @media (max-width: 768px) {{
        .bottom-bar {{
            flex-direction: column;
            gap: 20px;
            text-align: center;
        }}
    }}
    </style>
    '''
