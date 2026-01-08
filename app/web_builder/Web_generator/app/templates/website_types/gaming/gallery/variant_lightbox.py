from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Lightbox Showcase - Full-screen image viewer with thumbnails"""
    title = props.get("title", "Screenshot Gallery")
    subtitle = props.get("subtitle", "Captured moments of glory")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    images = [
        {"url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1200", "thumb": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=300"},
        {"url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=1200", "thumb": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=300"},
        {"url": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=1200", "thumb": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=300"},
        {"url": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=1200", "thumb": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=300"},
        {"url": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=1200", "thumb": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=300"},
    ]
    
    thumbs_html = ""
    for i, img in enumerate(images):
        active = "active" if i == 0 else ""
        thumbs_html += f'<div class="thumb {active}" data-index="{i}"><img src="{img["thumb"]}" alt="Thumbnail {i+1}"></div>'
    
    return f'''
    <section class="gaming-gallery-lightbox" id="gallery">
        <div class="lightbox-container">
            <div class="lightbox-header">
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            <div class="lightbox-viewer">
                <div class="main-image">
                    <img src="{images[0]['url']}" alt="Featured screenshot" id="mainImage">
                    <div class="image-overlay">
                        <div class="nav-btn prev">‹</div>
                        <div class="nav-btn next">›</div>
                    </div>
                    <div class="image-counter">
                        <span id="currentIndex">1</span> / {len(images)}
                    </div>
                </div>
                <div class="thumb-strip">
                    {thumbs_html}
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-gallery-lightbox {{
        padding: 140px 24px;
        background: {background};
    }}
    .lightbox-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .lightbox-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .lightbox-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .lightbox-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .lightbox-viewer {{
        display: flex;
        flex-direction: column;
        gap: 24px;
    }}
    .main-image {{
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        aspect-ratio: 16/9;
        background: {text}05;
    }}
    .main-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: opacity 0.4s ease;
    }}
    .image-overlay {{
        position: absolute;
        inset: 0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 24px;
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    .main-image:hover .image-overlay {{
        opacity: 1;
    }}
    .nav-btn {{
        width: 60px;
        height: 60px;
        background: {background}CC;
        backdrop-filter: blur(10px);
        border: 1px solid {text}20;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        color: {text};
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .nav-btn:hover {{
        background: {primary};
        color: {background};
        transform: scale(1.1);
    }}
    .image-counter {{
        position: absolute;
        bottom: 24px;
        left: 50%;
        transform: translateX(-50%);
        padding: 8px 20px;
        background: {background}CC;
        backdrop-filter: blur(10px);
        border-radius: 100px;
        color: {text};
        font-size: 0.9rem;
        font-weight: 600;
    }}
    .thumb-strip {{
        display: flex;
        gap: 16px;
        justify-content: center;
        flex-wrap: wrap;
    }}
    .thumb {{
        width: 120px;
        height: 80px;
        border-radius: 12px;
        overflow: hidden;
        cursor: pointer;
        border: 3px solid transparent;
        transition: all 0.3s ease;
        opacity: 0.5;
    }}
    .thumb:hover {{
        opacity: 0.8;
    }}
    .thumb.active {{
        border-color: {primary};
        opacity: 1;
        box-shadow: 0 0 20px {primary}40;
    }}
    .thumb img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    @media (max-width: 768px) {{
        .thumb {{
            width: 80px;
            height: 60px;
        }}
        .nav-btn {{
            width: 48px;
            height: 48px;
            font-size: 1.5rem;
        }}
    }}
    </style>
    '''
