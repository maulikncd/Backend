from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Split Scroll Hero - A modern split-screen layout where one side holds content
    and the other holds a vertical marquee of images.
    """
    tagline = props.get("tagline", "Urban Collection")
    description = props.get("description", "Redefining streetwear with bold cuts and premium materials.")
    cta = props.get("cta", "Shop New Drop")
    
    bg = colors.get("background", "#F5F5F5")
    text = colors.get("text", "#111111")
    primary = colors.get("primary", "#111111")
    
    images = [
        "https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?w=800",
        "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800",
        "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=800",
        "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=800"
    ]
    
    marquee_html = ""
    for img in images:
        marquee_html += f'<div class="marquee-item"><img src="{img}" alt="Lookbook"></div>'
    # Double it for infinite loop
    for img in images:
        marquee_html += f'<div class="marquee-item"><img src="{img}" alt="Lookbook"></div>'
    
    return f'''
    <section class="split-hero" id="hero">
        <div class="split-content">
            <div class="content-wrapper">
                <div class="new-badge">New Season</div>
                <h1 class="split-title">
                    <span class="line">Street</span>
                    <span class="line outline">Culture</span>
                    <span class="line">2026</span>
                </h1>
                <p class="split-desc">{description}</p>
                <div class="cta-box">
                    <a href="#products" class="btn-solid">{cta}</a>
                    <a href="#about" class="link-arrow">Discover Brand <span>→</span></a>
                </div>
                
                <div class="stats-mini">
                    <div class="stat">
                        <strong>01</strong>
                        <span>Design</span>
                    </div>
                    <div class="stat">
                        <strong>02</strong>
                        <span>Quality</span>
                    </div>
                    <div class="stat">  
                        <strong>03</strong>
                        <span>Legacy</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="split-visual">
            <div class="vertical-marquee">
                <div class="marquee-track">
                    {marquee_html}
                </div>
            </div>
            <div class="visual-overlay"></div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Anton&family=Roboto+Mono:wght@400;500&display=swap');
    
    .split-hero {{
        height: 100vh;
        display: grid;
        grid-template-columns: 1fr 1fr;
        background: {bg};
        color: {text};
        overflow: hidden;
    }}
    
    .split-content {{
        display: flex;
        align-items: center;
        padding: 60px 100px;
        position: relative;
    }}
    
    .new-badge {{
        display: inline-block;
        padding: 5px 10px;
        border: 1px solid {text};
        font-family: 'Roboto Mono', monospace;
        font-size: 0.8rem;
        text-transform: uppercase;
        margin-bottom: 30px;
    }}
    
    .split-title {{
        font-family: 'Anton', sans-serif;
        font-size: clamp(4rem, 8vw, 8rem);
        line-height: 0.9;
        text-transform: uppercase;
        display: flex;
        flex-direction: column;
        margin-bottom: 40px;
    }}
    
    .split-title .line.outline {{
        color: transparent;
        -webkit-text-stroke: 2px {text};
    }}
    
    .split-desc {{
        font-family: 'Roboto Mono', monospace;
        max-width: 400px;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 50px;
        color: {text}90;
    }}
    
    .cta-box {{
        display: flex;
        align-items: center;
        gap: 30px;
        margin-bottom: 80px;
    }}
    
    .btn-solid {{
        padding: 20px 40px;
        background: {primary};
        color: {bg};
        font-family: 'Anton', sans-serif;
        font-size: 1.2rem;
        text-transform: uppercase;
        text-decoration: none;
        letter-spacing: 1px;
        transition: transform 0.3s;
    }}
    
    .btn-solid:hover {{
        transform: translateY(-5px);
    }}
    
    .link-arrow {{
        color: {text};
        text-decoration: none;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    
    .stats-mini {{
        display: flex;
        gap: 40px;
        border-top: 1px solid {text}20;
        padding-top: 30px;
    }}
    
    .stat {{
        display: flex;
        flex-direction: column;
        font-family: 'Roboto Mono', monospace;
        font-size: 0.8rem;
    }}
    
    .stat strong {{
        font-size: 1.2rem;
        margin-bottom: 5px;
    }}
    
    .split-visual {{
        position: relative;
        height: 100%;
        overflow: hidden;
        background: #000;
    }}
    
    .vertical-marquee {{
        height: 100%;
        animation: scrollVert 30s linear infinite;
    }}
    
    .marquee-track {{
        display: flex;
        flex-direction: column;
    }}
    
    .marquee-item {{
        height: 50vh;
        width: 100%;
        position: relative;
    }}
    
    .marquee-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(100%);
        transition: filter 0.5s;
    }}
    
    .split-visual:hover .marquee-item img {{
        filter: grayscale(0%);
    }}
    
    @keyframes scrollVert {{
        0% {{ transform: translateY(0); }}
        100% {{ transform: translateY(-50%); }}
    }}
    
    .visual-overlay {{
        position: absolute;
        inset: 0;
        box-shadow: inset 50px 0 100px -50px {bg};
        pointer-events: none;
    }}
    
    @media (max-width: 1024px) {{
        .split-hero {{ grid-template-columns: 1fr; }}
        .split-visual {{ display: none; }}
        .split-content {{ padding: 60px 40px; justify-content: center; text-align: center; }}
        .split-title {{ align-items: center; }}
        .cta-box {{ justify-content: center; }}
        .stats-mini {{ justify-content: center; }}
    }}
    </style>
    '''
