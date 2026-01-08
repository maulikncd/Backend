from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Glitch Art Hero - Edgy, high-energy hero with glitch effects,
    brutalist layout, and neon accents. Perfect for streetwear or gaming merch.
    """
    tagline = props.get("tagline", "BREAK THE NORM")
    description = props.get("description", "Exclusive drops. Limited edition. No compromise.")
    cta = props.get("cta", "SHOP DROP")
    
    bg = colors.get("background", "#050505")
    text = colors.get("text", "#EEEEEE")
    primary = colors.get("primary", "#00FF41") # Matrix/Neon Green or user pref
    secondary = "#FF0055"
    
    return f'''
    <section class="glitch-hero" id="hero">
        <div class="glitch-container">
            <h1 class="glitch-title" data-text="{tagline}">{tagline}</h1>
            
            <div class="hero-subtext">
                <p>{description}</p>
                <div class="glitch-cta-wrapper">
                    <a href="#products" class="btn-glitch">{cta}</a>
                </div>
            </div>
            
            <div class="visual-stack">
                <img src="https://images.unsplash.com/photo-1523398002811-999ca8dec234?w=600" class="stack-img img-1" alt="Fashion">
                <img src="https://images.unsplash.com/photo-1550246140-5119980d7b8d?w=600" class="stack-img img-2" alt="Fashion">
                <div class="graphic-shape"></div>
            </div>
            
            <div class="runway-strip">
                <span>NEW ARRIVALS 2026 // NEW ARRIVALS 2026 // NEW ARRIVALS 2026 //</span>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Space+Mono&display=swap');
    
    .glitch-hero {{
        min-height: 100vh;
        background: {bg};
        color: {text};
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
        padding: 40px;
    }}
    
    .glitch-container {{
        max-width: 1400px;
        width: 100%;
        display: grid;
        grid-template-columns: 1.5fr 1fr;
        gap: 60px;
        align-items: center;
        z-index: 2;
    }}
    
    .glitch-title {{
        font-family: 'Syncopate', sans-serif;
        font-size: clamp(3rem, 7vw, 7rem);
        font-weight: 700;
        text-transform: uppercase;
        position: relative;
        line-height: 0.9;
        margin-bottom: 40px;
    }}
    
    .glitch-title::before,
    .glitch-title::after {{
        content: attr(data-text);
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0.8;
    }}
    
    .glitch-title::before {{
        color: {primary};
        z-index: -1;
        animation: glitch-anim-1 2s infinite linear alternate-reverse;
    }}
    
    .glitch-title::after {{
        color: {secondary};
        z-index: -2;
        animation: glitch-anim-2 3s infinite linear alternate-reverse;
    }}
    
    @keyframes glitch-anim-1 {{
        0% {{ clip-path: inset(20% 0 80% 0); transform: translate(-2px, 1px); }}
        20% {{ clip-path: inset(60% 0 10% 0); transform: translate(2px, -1px); }}
        40% {{ clip-path: inset(40% 0 50% 0); transform: translate(-2px, 2px); }}
        60% {{ clip-path: inset(80% 0 5% 0); transform: translate(2px, -2px); }}
        80% {{ clip-path: inset(10% 0 70% 0); transform: translate(-1px, 1px); }}
        100% {{ clip-path: inset(30% 0 20% 0); transform: translate(1px, -1px); }}
    }}
    
    @keyframes glitch-anim-2 {{
        0% {{ clip-path: inset(10% 0 60% 0); transform: translate(2px, -1px); }}
        20% {{ clip-path: inset(80% 0 5% 0); transform: translate(-2px, 2px); }}
        40% {{ clip-path: inset(30% 0 20% 0); transform: translate(1px, 1px); }}
        60% {{ clip-path: inset(10% 0 80% 0); transform: translate(-1px, -2px); }}
        80% {{ clip-path: inset(40% 0 10% 0); transform: translate(2px, 1px); }}
        100% {{ clip-path: inset(50% 0 30% 0); transform: translate(-2px, -1px); }}
    }}
    
    .hero-subtext {{
        font-family: 'Space Mono', monospace;
        font-size: 1.1rem;
        max-width: 400px;
    }}
    
    .btn-glitch {{
        display: inline-block;
        margin-top: 30px;
        padding: 15px 40px;
        background: {text};
        color: {bg};
        text-transform: uppercase;
        font-weight: 700;
        text-decoration: none;
        clip-path: polygon(10% 0, 100% 0, 100% 80%, 90% 100%, 0 100%, 0 20%);
        transition: all 0.2s;
    }}
    
    .btn-glitch:hover {{
        background: {primary};
        color: black;
        transform: translate(-4px, -4px);
        box-shadow: 4px 4px 0 {secondary};
    }}
    
    .visual-stack {{
        position: relative;
        height: 500px;
        width: 100%;
    }}
    
    .stack-img {{
        position: absolute;
        width: 300px;
        height: 400px;
        object-fit: cover;
        filter: grayscale(100%) contrast(1.2);
        border: 2px solid {text};
        transition: all 0.4s;
    }}
    
    .img-1 {{
        top: 0;
        right: 20%;
        z-index: 2;
    }}
    
    .img-1:hover {{
        filter: grayscale(0%);
        transform: scale(1.05);
        z-index: 10;
    }}
    
    .img-2 {{
        bottom: 0;
        left: 20%;
        z-index: 1;
    }}
    
    .img-2:hover {{
        filter: grayscale(0%);
        transform: scale(1.05);
        z-index: 10;
    }}
    
    .graphic-shape {{
        position: absolute;
        top: 20%;
        left: 40%;
        width: 200px;
        height: 200px;
        border: 1px solid {primary};
        transform: rotate(45deg);
        z-index: 0;
    }}
    
    .runway-strip {{
        position: absolute;
        bottom: 40px;
        left: 0;
        width: 100%;
        background: {primary};
        color: black;
        font-family: 'Syncopate', sans-serif;
        font-weight: 700;
        white-space: nowrap;
        padding: 10px 0;
        transform: rotate(-2deg) scale(1.1);
        overflow: hidden;
    }}
    
    .runway-strip span {{
        display: inline-block;
        padding-left: 100%;
        animation: marquee 10s linear infinite;
    }}
    
    @keyframes marquee {{
        0% {{ transform: translate(0, 0); }}
        100% {{ transform: translate(-100%, 0); }}
    }}
    
    @media (max-width: 1024px) {{
        .glitch-container {{ grid-template-columns: 1fr; }}
        .visual-stack {{ height: 400px; margin-top: 40px; display: none; }}
        .glitch-title {{ font-size: 3rem; }}
    }}
    </style>
    '''
