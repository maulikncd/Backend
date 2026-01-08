from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Fullscreen Food - Dramatic full-screen food photography
    with minimal overlay text
    """
    name = props.get("name", props.get("businessName", "Savour"))
    tagline = props.get("tagline", "Taste the Extraordinary")
    description = props.get("description", "Where every dish tells a story")
    cta = props.get("cta", "Make a Reservation")
    
    primary = colors.get("primary", "#FF6B35")
    bg = colors.get("background", "#0F0F0F")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="hero-fullscreen" id="hero">
        <div class="hero-slider">
            <div class="slide active">
                <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=1920" alt="Dish">
            </div>
        </div>
        <div class="hero-overlay"></div>
        
        <div class="hero-content">
            <div class="content-wrapper">
                <div class="hero-top">
                    <span class="hero-label">Fine Dining Experience</span>
                </div>
                
                <h1 class="hero-title">{name}</h1>
                <p class="hero-tagline">{tagline}</p>
                
                <div class="hero-bottom">
                    <a href="#reservation" class="btn-reserve">{cta}</a>
                    <div class="scroll-indicator">
                        <span>Discover</span>
                        <div class="scroll-line"></div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="side-info">
            <div class="info-vertical">
                <span>Open Daily</span>
                <span class="divider"></span>
                <span>5PM - 11PM</span>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Italiana&family=Work+Sans:wght@300;400;500&display=swap');
    
    .hero-fullscreen {{
        min-height: 100vh;
        position: relative;
        display: flex;
        overflow: hidden;
    }}
    .hero-slider {{
        position: absolute;
        inset: 0;
    }}
    .slide {{
        position: absolute;
        inset: 0;
        opacity: 0;
        transition: opacity 1s ease;
    }}
    .slide.active {{ opacity: 1; }}
    .slide img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transform: scale(1.05);
    }}
    .hero-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, 
            rgba(0,0,0,0.8) 0%,
            rgba(0,0,0,0.4) 50%,
            rgba(0,0,0,0.6) 100%);
        z-index: 1;
    }}
    .hero-content {{
        position: relative;
        z-index: 2;
        flex: 1;
        display: flex;
        align-items: center;
        padding: 100px 80px;
    }}
    .content-wrapper {{
        width: 100%;
        max-width: 800px;
    }}
    .hero-top {{
        margin-bottom: 40px;
    }}
    .hero-label {{
        display: inline-block;
        padding: 12px 30px;
        border: 1px solid {primary};
        color: {primary};
        font-size: 0.8rem;
        letter-spacing: 4px;
        text-transform: uppercase;
    }}
    .hero-title {{
        font-family: 'Italiana', serif;
        font-size: clamp(5rem, 15vw, 12rem);
        font-weight: 400;
        color: {text};
        line-height: 0.9;
        margin-bottom: 30px;
    }}
    .hero-tagline {{
        font-family: 'Work Sans', sans-serif;
        font-size: 1.4rem;
        color: {text}90;
        font-weight: 300;
        letter-spacing: 2px;
        margin-bottom: 60px;
    }}
    .hero-bottom {{
        display: flex;
        align-items: center;
        gap: 60px;
    }}
    .btn-reserve {{
        padding: 20px 50px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-size: 0.9rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        transition: all 0.3s;
    }}
    .btn-reserve:hover {{
        transform: translateY(-5px);
        box-shadow: 0 20px 50px {primary}40;
    }}
    .scroll-indicator {{
        display: flex;
        align-items: center;
        gap: 20px;
        color: {text}60;
        font-size: 0.85rem;
        letter-spacing: 2px;
    }}
    .scroll-indicator .scroll-line {{
        width: 80px;
        height: 1px;
        background: {text}40;
        position: relative;
    }}
    .scroll-indicator .scroll-line::after {{
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        width: 30%;
        height: 100%;
        background: {primary};
        animation: scrollLine 2s infinite;
    }}
    @keyframes scrollLine {{
        0% {{ left: 0; }}
        100% {{ left: 70%; }}
    }}
    .side-info {{
        position: absolute;
        right: 40px;
        top: 50%;
        transform: translateY(-50%);
        z-index: 2;
    }}
    .info-vertical {{
        writing-mode: vertical-rl;
        display: flex;
        align-items: center;
        gap: 20px;
        color: {text}60;
        font-size: 0.85rem;
        letter-spacing: 2px;
    }}
    .info-vertical .divider {{
        width: 1px;
        height: 50px;
        background: {text}30;
    }}
    @media (max-width: 768px) {{
        .hero-content {{ padding: 80px 30px; }}
        .side-info {{ display: none; }}
        .hero-bottom {{ flex-direction: column; gap: 30px; align-items: flex-start; }}
    }}
    </style>
    '''
