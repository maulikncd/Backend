from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """3D Hover Cards - Cards with 3D tilt effect on hover"""
    title = props.get("title", "Featured Media")
    subtitle = props.get("subtitle", "Experience gaming in a new dimension")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    items = [
        {"img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600", "title": "Esports Championship", "views": "125K"},
        {"img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600", "title": "Gaming Setup Tour", "views": "89K"},
        {"img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600", "title": "Night Session", "views": "67K"},
        {"img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=600", "title": "Pro Gear Review", "views": "234K"},
    ]
    
    cards_html = ""
    for item in items:
        cards_html += f'''
        <div class="hover-card-3d">
            <div class="card-inner">
                <div class="card-face">
                    <img src="{item['img']}" alt="{item['title']}">
                    <div class="card-gradient"></div>
                    <div class="card-info">
                        <h3>{item['title']}</h3>
                        <span class="views">👁️ {item['views']} views</span>
                    </div>
                    <div class="card-shine"></div>
                </div>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-gallery-3d" id="gallery">
        <div class="gallery-3d-container">
            <div class="gallery-header">
                <span class="tag-line">✨ Featured</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            <div class="cards-grid">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-gallery-3d {{
        padding: 140px 24px;
        background: {background};
        perspective: 1000px;
    }}
    .gallery-3d-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .gallery-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    .tag-line {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 2px;
        border-radius: 100px;
        margin-bottom: 24px;
    }}
    .gallery-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .gallery-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .cards-grid {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 40px;
    }}
    .hover-card-3d {{
        perspective: 1000px;
    }}
    .card-inner {{
        position: relative;
        transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        transform-style: preserve-3d;
    }}
    .hover-card-3d:hover .card-inner {{
        transform: rotateY(-5deg) rotateX(5deg) scale(1.02);
    }}
    .card-face {{
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        aspect-ratio: 16/10;
        box-shadow: 0 30px 60px {background};
    }}
    .card-face img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .card-gradient {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 60%);
    }}
    .card-info {{
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 32px;
    }}
    .card-info h3 {{
        font-size: 1.5rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 8px;
    }}
    .views {{
        font-size: 0.9rem;
        color: {secondary};
    }}
    .card-shine {{
        position: absolute;
        inset: 0;
        background: linear-gradient(
            135deg,
            transparent 40%,
            {primary}10 45%,
            {primary}20 50%,
            {primary}10 55%,
            transparent 60%
        );
        opacity: 0;
        transition: opacity 0.4s ease;
    }}
    .hover-card-3d:hover .card-shine {{
        opacity: 1;
    }}
    @media (max-width: 768px) {{
        .cards-grid {{
            grid-template-columns: 1fr;
        }}
    }}
    </style>
    '''
