from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Fullscreen Slider - Hero-style fullscreen image slider"""
    title = props.get("title", "Epic Moments")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    slides = [
        {"img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1920", "title": "World Championship 2024", "desc": "The biggest esports event of the year"},
        {"img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=1920", "title": "Pro Gaming Setup", "desc": "Where champions prepare for battle"},
        {"img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=1920", "title": "Night Gaming Session", "desc": "When dedication meets passion"},
    ]
    
    slides_html = ""
    dots_html = ""
    for i, slide in enumerate(slides):
        active = "active" if i == 0 else ""
        slides_html += f'''
        <div class="slide {active}" data-index="{i}">
            <img src="{slide['img']}" alt="{slide['title']}">
            <div class="slide-overlay"></div>
            <div class="slide-content">
                <h3>{slide['title']}</h3>
                <p>{slide['desc']}</p>
            </div>
        </div>
        '''
        dots_html += f'<div class="dot {active}" data-index="{i}"></div>'
    
    return f'''
    <section class="gaming-gallery-fullscreen" id="gallery">
        <div class="slider-wrapper">
            <div class="slides-container">
                {slides_html}
            </div>
            <div class="slider-controls">
                <button class="slider-btn prev">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M15 18l-6-6 6-6"/>
                    </svg>
                </button>
                <div class="dots-container">
                    {dots_html}
                </div>
                <button class="slider-btn next">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 18l6-6-6-6"/>
                    </svg>
                </button>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-gallery-fullscreen {{
        min-height: 100vh;
        background: {background};
        position: relative;
    }}
    .slider-wrapper {{
        position: relative;
        height: 100vh;
        overflow: hidden;
    }}
    .slides-container {{
        position: relative;
        width: 100%;
        height: 100%;
    }}
    .slide {{
        position: absolute;
        inset: 0;
        opacity: 0;
        transition: opacity 0.8s ease;
    }}
    .slide.active {{
        opacity: 1;
    }}
    .slide img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .slide-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, {background}40 30%, transparent 60%);
    }}
    .slide-content {{
        position: absolute;
        bottom: 150px;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        max-width: 800px;
        padding: 0 24px;
    }}
    .slide-content h3 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 6vw, 5rem);
        font-weight: 900;
        color: {text};
        margin-bottom: 16px;
        text-shadow: 0 4px 30px {background};
    }}
    .slide-content p {{
        font-size: 1.3rem;
        color: {secondary};
    }}
    .slider-controls {{
        position: absolute;
        bottom: 60px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        align-items: center;
        gap: 40px;
        z-index: 10;
    }}
    .slider-btn {{
        width: 60px;
        height: 60px;
        background: {background}CC;
        backdrop-filter: blur(10px);
        border: 1px solid {text}20;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .slider-btn svg {{
        width: 24px;
        height: 24px;
        color: {text};
    }}
    .slider-btn:hover {{
        background: {primary};
        border-color: {primary};
        transform: scale(1.1);
    }}
    .slider-btn:hover svg {{
        color: {background};
    }}
    .dots-container {{
        display: flex;
        gap: 12px;
    }}
    .dot {{
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: {text}30;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .dot.active {{
        background: {primary};
        box-shadow: 0 0 20px {primary}60;
        transform: scale(1.2);
    }}
    @media (max-width: 768px) {{
        .slide-content {{
            bottom: 120px;
        }}
        .slider-controls {{
            bottom: 40px;
            gap: 24px;
        }}
        .slider-btn {{
            width: 48px;
            height: 48px;
        }}
    }}
    </style>
    '''
