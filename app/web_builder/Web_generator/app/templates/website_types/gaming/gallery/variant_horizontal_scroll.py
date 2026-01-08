from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Immersive Scroll - Horizontal scroll gallery with parallax"""
    title = props.get("title", "Visual Journey")
    subtitle = props.get("subtitle", "Scroll to explore our world")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    images = [
        {"url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800", "title": "Championship Arena", "desc": "Where legends are born"},
        {"url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=800", "title": "Pro Gaming Setup", "desc": "Peak performance gear"},
        {"url": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=800", "title": "Night Gaming", "desc": "The grind never stops"},
        {"url": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=800", "title": "Controller Art", "desc": "Precision in your hands"},
        {"url": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=800", "title": "Tournament Finals", "desc": "Million dollar plays"},
    ]
    
    cards_html = ""
    for img in images:
        cards_html += f'''
        <div class="scroll-card">
            <div class="card-image">
                <img src="{img['url']}" alt="{img['title']}">
                <div class="card-overlay"></div>
            </div>
            <div class="card-content">
                <h3>{img['title']}</h3>
                <p>{img['desc']}</p>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-gallery-scroll" id="gallery">
        <div class="scroll-header">
            <div class="header-content">
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            <div class="scroll-hint">
                <span>Drag to explore</span>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
            </div>
        </div>
        <div class="scroll-container">
            <div class="scroll-track">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-gallery-scroll {{
        padding: 140px 0;
        background: {background};
        overflow: hidden;
    }}
    .scroll-header {{
        max-width: 1200px;
        margin: 0 auto 60px;
        padding: 0 24px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
    }}
    .header-content h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .header-content p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .scroll-hint {{
        display: flex;
        align-items: center;
        gap: 10px;
        color: {secondary};
        font-size: 0.9rem;
    }}
    .scroll-hint svg {{
        width: 20px;
        height: 20px;
        animation: nudge 2s ease-in-out infinite;
    }}
    @keyframes nudge {{
        0%, 100% {{ transform: translateX(0); }}
        50% {{ transform: translateX(10px); }}
    }}
    .scroll-container {{
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
        -ms-overflow-style: none;
    }}
    .scroll-container::-webkit-scrollbar {{
        display: none;
    }}
    .scroll-track {{
        display: flex;
        gap: 32px;
        padding: 0 calc((100vw - 1200px) / 2 + 24px);
    }}
    .scroll-card {{
        flex-shrink: 0;
        width: 450px;
        scroll-snap-align: start;
        position: relative;
        transition: transform 0.4s ease;
    }}
    .scroll-card:hover {{
        transform: scale(1.02);
    }}
    .card-image {{
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        aspect-ratio: 4/5;
    }}
    .card-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s ease;
    }}
    .scroll-card:hover .card-image img {{
        transform: scale(1.1);
    }}
    .card-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 50%);
    }}
    .card-content {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 32px;
    }}
    .card-content h3 {{
        font-size: 1.8rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .card-content p {{
        font-size: 1rem;
        color: {secondary};
    }}
    @media (max-width: 900px) {{
        .scroll-header {{
            flex-direction: column;
            align-items: flex-start;
            gap: 20px;
        }}
        .scroll-track {{
            padding: 0 24px;
        }}
        .scroll-card {{
            width: 320px;
        }}
    }}
    </style>
    '''
