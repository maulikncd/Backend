from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Luxury Brand - High-end fashion/luxury hero with
    elegant typography and minimal aesthetic
    """
    name = props.get("name", props.get("businessName", "LUXE"))
    tagline = props.get("tagline", "Redefine Your Style")
    collection = props.get("collection", "Spring/Summer 2024")
    cta = props.get("cta", "Shop Collection")
    
    primary = colors.get("primary", "#1A1A1A")
    secondary = colors.get("secondary", "#C9A962")
    bg = colors.get("background", "#FAFAFA")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="luxury-hero" id="hero">
        <div class="hero-split">
            <div class="hero-content">
                <div class="collection-tag">{collection}</div>
                <h1 class="hero-title">{tagline}</h1>
                <div class="hero-cta">
                    <a href="#products" class="cta-link">
                        <span>{cta}</span>
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                            <path d="M5 12h14M12 5l7 7-7 7"/>
                        </svg>
                    </a>
                </div>
            </div>
            
            <div class="hero-image">
                <div class="image-frame">
                    <img src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=800" alt="Collection">
                </div>
                <div class="image-overlay">
                    <span class="new-tag">New Arrivals</span>
                </div>
            </div>
        </div>
        
        <div class="scroll-indicator">
            <span>Scroll</span>
            <div class="scroll-line"></div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@400;500;600&display=swap');
    
    .luxury-hero {{
        min-height: 100vh;
        background: {bg};
        display: flex;
        flex-direction: column;
        position: relative;
    }}
    .hero-split {{
        flex: 1;
        display: grid;
        grid-template-columns: 1fr 1fr;
    }}
    .hero-content {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 120px 80px;
    }}
    .collection-tag {{
        font-family: 'Montserrat', sans-serif;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: {secondary};
        margin-bottom: 30px;
    }}
    .hero-title {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(4rem, 8vw, 7rem);
        font-weight: 400;
        color: {text};
        line-height: 1;
        margin-bottom: 50px;
    }}
    .cta-link {{
        display: inline-flex;
        align-items: center;
        gap: 20px;
        color: {text};
        text-decoration: none;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        padding-bottom: 10px;
        border-bottom: 1px solid {text}30;
        transition: all 0.3s;
    }}
    .cta-link:hover {{
        border-color: {secondary};
        color: {secondary};
    }}
    .cta-link svg {{
        transition: transform 0.3s;
    }}
    .cta-link:hover svg {{
        transform: translateX(10px);
    }}
    .hero-image {{
        position: relative;
        overflow: hidden;
    }}
    .image-frame {{
        height: 100%;
    }}
    .image-frame img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .image-overlay {{
        position: absolute;
        bottom: 60px;
        right: 60px;
    }}
    .new-tag {{
        display: inline-block;
        padding: 16px 32px;
        background: white;
        color: {text};
        font-family: 'Montserrat', sans-serif;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 3px;
    }}
    .scroll-indicator {{
        position: absolute;
        bottom: 40px;
        left: 80px;
        display: flex;
        align-items: center;
        gap: 20px;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 3px;
        color: {text}60;
    }}
    .scroll-line {{
        width: 60px;
        height: 1px;
        background: {text}30;
        position: relative;
    }}
    .scroll-line::after {{
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        width: 20px;
        height: 1px;
        background: {secondary};
        animation: scrollMove 2s infinite;
    }}
    @keyframes scrollMove {{
        0% {{ left: 0; }}
        100% {{ left: 100%; }}
    }}
    @media (max-width: 1024px) {{
        .hero-split {{ grid-template-columns: 1fr; }}
        .hero-content {{ padding: 120px 40px 60px; text-align: center; align-items: center; }}
        .hero-image {{ height: 50vh; }}
        .scroll-indicator {{ left: 50%; transform: translateX(-50%); }}
    }}
    </style>
    '''
