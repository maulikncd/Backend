from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Dark Luxe - Ultra premium dark theme with gold accents
    and cinematic video background
    """
    name = props.get("name", props.get("businessName", "Noir"))
    tagline = props.get("tagline", "Culinary Excellence")
    description = props.get("description", "An unforgettable dining experience")
    cta = props.get("cta", "Reserve Your Table")
    
    primary = colors.get("primary", "#D4AF37")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="hero-dark-luxe" id="hero">
        <div class="video-bg">
            <video autoplay muted loop playsinline>
                <source src="https://assets.mixkit.co/videos/preview/mixkit-top-view-of-a-table-at-a-restaurant-42343-large.mp4" type="video/mp4">
            </video>
            <div class="video-overlay"></div>
        </div>
        
        <div class="hero-container">
            <div class="decorative-frame">
                <div class="corner corner-tl"></div>
                <div class="corner corner-tr"></div>
                <div class="corner corner-bl"></div>
                <div class="corner corner-br"></div>
            </div>
            
            <div class="hero-content">
                <div class="brand-mark">✦</div>
                <h1 class="hero-name">{name}</h1>
                <div class="divider"></div>
                <p class="hero-tagline">{tagline}</p>
                <p class="hero-desc">{description}</p>
                
                <a href="#reservation" class="btn-luxe">{cta}</a>
            </div>
        </div>
        
        <div class="bottom-bar">
            <div class="info-item">
                <span class="label">Hours</span>
                <span class="value">Tue-Sun 6PM-12AM</span>
            </div>
            <div class="info-item">
                <span class="label">Location</span>
                <span class="value">Manhattan, NYC</span>
            </div>
            <div class="info-item">
                <span class="label">Contact</span>
                <span class="value">+1 (555) 123-4567</span>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Montserrat:wght@300;400;500&display=swap');
    
    .hero-dark-luxe {{
        min-height: 100vh;
        position: relative;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }}
    .video-bg {{
        position: absolute;
        inset: 0;
    }}
    .video-bg video {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .video-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to bottom, 
            rgba(0,0,0,0.7) 0%,
            rgba(0,0,0,0.5) 50%,
            rgba(0,0,0,0.8) 100%);
    }}
    .hero-container {{
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        z-index: 2;
        padding: 100px 40px;
    }}
    .decorative-frame {{
        position: absolute;
        width: 90%;
        max-width: 900px;
        height: 70%;
        pointer-events: none;
    }}
    .corner {{
        position: absolute;
        width: 60px;
        height: 60px;
        border: 2px solid {primary}50;
    }}
    .corner-tl {{ top: 0; left: 0; border-right: none; border-bottom: none; }}
    .corner-tr {{ top: 0; right: 0; border-left: none; border-bottom: none; }}
    .corner-bl {{ bottom: 0; left: 0; border-right: none; border-top: none; }}
    .corner-br {{ bottom: 0; right: 0; border-left: none; border-top: none; }}
    .hero-content {{
        text-align: center;
        max-width: 700px;
    }}
    .brand-mark {{
        font-size: 2rem;
        color: {primary};
        margin-bottom: 30px;
    }}
    .hero-name {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(4rem, 12vw, 10rem);
        font-weight: 400;
        color: {text};
        letter-spacing: 20px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }}
    .divider {{
        width: 100px;
        height: 1px;
        background: linear-gradient(90deg, transparent, {primary}, transparent);
        margin: 0 auto 30px;
    }}
    .hero-tagline {{
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: {primary};
        font-style: italic;
        margin-bottom: 20px;
    }}
    .hero-desc {{
        font-family: 'Montserrat', sans-serif;
        font-size: 1rem;
        color: {text}80;
        letter-spacing: 2px;
        margin-bottom: 50px;
    }}
    .btn-luxe {{
        display: inline-block;
        padding: 20px 60px;
        background: transparent;
        border: 1px solid {primary};
        color: {primary};
        text-decoration: none;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        transition: all 0.4s;
    }}
    .btn-luxe:hover {{
        background: {primary};
        color: #0A0A0A;
    }}
    .bottom-bar {{
        position: relative;
        z-index: 2;
        display: flex;
        justify-content: center;
        gap: 80px;
        padding: 40px;
        border-top: 1px solid {text}15;
        flex-wrap: wrap;
    }}
    .info-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
    }}
    .info-item .label {{
        font-size: 0.75rem;
        color: {primary};
        letter-spacing: 2px;
        text-transform: uppercase;
    }}
    .info-item .value {{
        font-size: 0.95rem;
        color: {text}90;
    }}
    @media (max-width: 768px) {{
        .hero-name {{ letter-spacing: 5px; }}
        .bottom-bar {{ gap: 40px; }}
    }}
    </style>
    '''
