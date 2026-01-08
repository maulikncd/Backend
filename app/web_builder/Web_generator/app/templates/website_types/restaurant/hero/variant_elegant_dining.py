from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Elegant Dining - Luxurious hero with ambient imagery,
    serif typography and reservation focus
    """
    name = props.get("name", props.get("businessName", "La Maison"))
    tagline = props.get("tagline", "Fine Dining Experience")
    description = props.get("description", "Where culinary artistry meets timeless elegance")
    cta = props.get("cta", "Reserve a Table")
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="restaurant-hero" id="hero">
        <div class="hero-bg">
            <img src="https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1920" alt="Fine Dining">
            <div class="bg-overlay"></div>
        </div>
        
        <div class="hero-content">
            <div class="content-inner">
                <span class="hero-badge">✦ Est. 1995 ✦</span>
                <h1 class="hero-name">{name}</h1>
                <p class="hero-tagline">{tagline}</p>
                <p class="hero-desc">{description}</p>
                
                <div class="cta-group">
                    <a href="#reservation" class="btn-reserve">{cta}</a>
                    <a href="#menu" class="btn-menu">View Menu</a>
                </div>
                
                <div class="hero-info">
                    <div class="info-item">
                        <span class="info-icon">📍</span>
                        <span>123 Gourmet Street, NYC</span>
                    </div>
                    <div class="info-item">
                        <span class="info-icon">🕐</span>
                        <span>Tue-Sun: 6PM - 11PM</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="scroll-hint">
            <span>Scroll to explore</span>
            <div class="scroll-line"></div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Lato:wght@400;700&display=swap');
    
    .restaurant-hero {{
        min-height: 100vh;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }}
    .hero-bg {{
        position: absolute;
        inset: 0;
    }}
    .hero-bg img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .bg-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to bottom, rgba(0,0,0,0.5), rgba(0,0,0,0.8));
    }}
    .hero-content {{
        position: relative;
        z-index: 2;
        text-align: center;
        max-width: 800px;
        padding: 0 40px;
    }}
    .hero-badge {{
        display: inline-block;
        font-size: 0.9rem;
        color: {primary};
        letter-spacing: 4px;
        margin-bottom: 30px;
    }}
    .hero-name {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(4rem, 10vw, 8rem);
        font-weight: 500;
        color: {text};
        line-height: 1;
        margin-bottom: 20px;
        letter-spacing: 5px;
    }}
    .hero-tagline {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.8rem;
        color: {primary};
        margin-bottom: 20px;
        font-style: italic;
    }}
    .hero-desc {{
        font-family: 'Lato', sans-serif;
        font-size: 1.1rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 40px;
        letter-spacing: 1px;
    }}
    .cta-group {{
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 60px;
        flex-wrap: wrap;
    }}
    .btn-reserve {{
        padding: 18px 50px;
        background: {primary};
        color: #0A0A0A;
        text-decoration: none;
        font-family: 'Lato', sans-serif;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        transition: all 0.3s;
    }}
    .btn-reserve:hover {{
        background: {text};
        transform: translateY(-3px);
    }}
    .btn-menu {{
        padding: 18px 50px;
        background: transparent;
        border: 1px solid rgba(255,255,255,0.3);
        color: {text};
        text-decoration: none;
        font-family: 'Lato', sans-serif;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        transition: all 0.3s;
    }}
    .btn-menu:hover {{
        border-color: {primary};
        color: {primary};
    }}
    .hero-info {{
        display: flex;
        justify-content: center;
        gap: 50px;
        flex-wrap: wrap;
    }}
    .info-item {{
        display: flex;
        align-items: center;
        gap: 12px;
        color: rgba(255,255,255,0.6);
        font-size: 0.95rem;
    }}
    .scroll-hint {{
        position: absolute;
        bottom: 40px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        color: rgba(255,255,255,0.4);
        font-size: 0.8rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}
    .scroll-line {{
        width: 1px;
        height: 50px;
        background: linear-gradient(to bottom, {primary}, transparent);
    }}
    @media (max-width: 640px) {{
        .hero-content {{ padding: 0 24px; }}
        .hero-info {{ flex-direction: column; gap: 20px; }}
    }}
    </style>
    '''
