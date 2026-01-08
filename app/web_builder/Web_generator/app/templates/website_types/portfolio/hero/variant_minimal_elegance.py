from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Minimal Elegance - Clean, sophisticated layout with subtle animations,
    elegant typography and refined whitespace
    """
    name = props.get("name", props.get("businessName", "John Doe"))
    title = props.get("title", "Designer & Developer")
    tagline = props.get("tagline", "Crafting digital experiences with precision and purpose")
    cta = props.get("cta", "Explore Work")
    
    primary = colors.get("primary", "#0A0A0A")
    accent = colors.get("secondary", "#6366F1")
    bg = colors.get("background", "#FAFAFA")
    text = colors.get("text", "#0A0A0A")
    
    return f'''
    <section class="minimal-hero" id="hero">
        <div class="hero-inner">
            <div class="hero-left">
                <div class="name-wrapper">
                    <span class="greeting">Hello, I'm</span>
                    <h1 class="hero-name">{name}</h1>
                </div>
                <h2 class="hero-title">{title}</h2>
                <p class="hero-tagline">{tagline}</p>
                
                <a href="#projects" class="cta-minimal">
                    <span class="cta-text">{cta}</span>
                    <span class="cta-arrow">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <path d="M5 12h14M12 5l7 7-7 7"/>
                        </svg>
                    </span>
                </a>
            </div>
            
            <div class="hero-right">
                <div class="image-frame">
                    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600" alt="{name}">
                    <div class="frame-accent"></div>
                </div>
            </div>
        </div>
        
        <div class="hero-footer">
            <div class="footer-left">
                <span class="footer-label">Scroll to discover</span>
            </div>
            <div class="footer-center">
                <div class="mouse-scroll">
                    <div class="mouse">
                        <div class="wheel"></div>
                    </div>
                </div>
            </div>
            <div class="footer-right">
                <span class="footer-label">© 2024</span>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');
    
    .minimal-hero {{
        min-height: 100vh;
        background: {bg};
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 120px 80px 60px;
        position: relative;
    }}
    .hero-inner {{
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        gap: 100px;
        align-items: center;
        max-width: 1400px;
        margin: 0 auto;
        width: 100%;
    }}
    .greeting {{
        display: block;
        font-size: 1rem;
        color: {accent};
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 16px;
        font-weight: 500;
    }}
    .hero-name {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(4rem, 8vw, 7rem);
        font-weight: 600;
        color: {text};
        line-height: 1;
        margin-bottom: 20px;
    }}
    .hero-title {{
        font-size: 1.4rem;
        font-weight: 400;
        color: {text}80;
        margin-bottom: 30px;
        font-family: 'Inter', sans-serif;
    }}
    .hero-tagline {{
        font-size: 1.15rem;
        color: {text}60;
        line-height: 1.8;
        max-width: 450px;
        margin-bottom: 50px;
    }}
    .cta-minimal {{
        display: inline-flex;
        align-items: center;
        gap: 16px;
        color: {text};
        text-decoration: none;
        font-weight: 500;
        font-size: 1rem;
        padding: 20px 0;
        border-bottom: 1px solid {text}30;
        transition: all 0.3s;
    }}
    .cta-minimal:hover {{
        border-color: {accent};
        color: {accent};
    }}
    .cta-arrow {{
        transition: transform 0.3s;
    }}
    .cta-minimal:hover .cta-arrow {{
        transform: translateX(8px);
    }}
    .hero-right {{
        display: flex;
        justify-content: center;
    }}
    .image-frame {{
        position: relative;
        width: 400px;
        height: 500px;
    }}
    .image-frame img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(100%);
        transition: filter 0.5s;
    }}
    .image-frame:hover img {{
        filter: grayscale(0%);
    }}
    .frame-accent {{
        position: absolute;
        width: 100%;
        height: 100%;
        border: 1px solid {accent};
        top: 20px;
        left: 20px;
        transition: all 0.3s;
    }}
    .image-frame:hover .frame-accent {{
        top: 30px;
        left: 30px;
    }}
    .hero-footer {{
        position: absolute;
        bottom: 40px;
        left: 80px;
        right: 80px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .footer-label {{
        font-size: 0.8rem;
        color: {text}50;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .mouse {{
        width: 24px;
        height: 40px;
        border: 1px solid {text}40;
        border-radius: 20px;
        position: relative;
    }}
    .wheel {{
        width: 4px;
        height: 8px;
        background: {accent};
        border-radius: 2px;
        position: absolute;
        top: 8px;
        left: 50%;
        transform: translateX(-50%);
        animation: scroll 2s infinite;
    }}
    @keyframes scroll {{
        0%, 100% {{ opacity: 1; transform: translateX(-50%) translateY(0); }}
        50% {{ opacity: 0.5; transform: translateX(-50%) translateY(10px); }}
    }}
    @media (max-width: 1024px) {{
        .hero-inner {{ grid-template-columns: 1fr; gap: 60px; text-align: center; }}
        .hero-left {{ display: flex; flex-direction: column; align-items: center; }}
        .hero-tagline {{ max-width: 100%; }}
        .image-frame {{ width: 300px; height: 380px; }}
        .frame-accent {{ display: none; }}
    }}
    @media (max-width: 768px) {{
        .minimal-hero {{ padding: 100px 24px 80px; }}
        .hero-footer {{ left: 24px; right: 24px; }}
        .footer-left, .footer-right {{ display: none; }}
    }}
    </style>
    '''
