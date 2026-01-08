from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Masonry Grid - Pinterest-style staggered image layout"""
    title = props.get("title", "Game Gallery")
    subtitle = props.get("subtitle", "Stunning visuals from our universe")
    
    # Dynamic colors from user's palette
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    images = [
        {"url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600", "title": "Esports Arena", "cat": "Event"},
        {"url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600", "title": "Gaming Setup", "cat": "Setup"},
        {"url": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600", "title": "Night Scene", "cat": "Gameplay"},
        {"url": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=600", "title": "Controller", "cat": "Gear"},
        {"url": "https://images.unsplash.com/photo-1542751110-97427bbecf20?w=600", "title": "Tournament", "cat": "Event"},
        {"url": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=600", "title": "RGB Setup", "cat": "Setup"},
    ]
    
    items_html = ""
    for i, img in enumerate(images):
        height = "tall" if i % 3 == 0 else ""
        items_html += f'''
        <div class="masonry-item {height}">
            <img src="{img['url']}" alt="{img['title']}" loading="lazy">
            <div class="item-overlay">
                <span class="item-cat">{img['cat']}</span>
                <h4>{img['title']}</h4>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-gallery-masonry" id="gallery">
        <div class="masonry-container">
            <div class="masonry-header">
                <span class="section-tag">🎮 Gallery</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            <div class="masonry-grid">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-gallery-masonry {{
        padding: 140px 24px;
        background: {background};
    }}
    .masonry-container {{
        max-width: 1400px;
        margin: 0 auto;
    }}
    .masonry-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .section-tag {{
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
    .masonry-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .masonry-header p {{
        font-size: 1.2rem;
        color: {secondary};
    }}
    .masonry-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        grid-auto-rows: 200px;
    }}
    .masonry-item {{
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        cursor: pointer;
    }}
    .masonry-item.tall {{
        grid-row: span 2;
    }}
    .masonry-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .masonry-item:hover img {{
        transform: scale(1.1);
    }}
    .item-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, {background}E6, transparent 60%);
        padding: 24px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        opacity: 0;
        transition: opacity 0.4s ease;
    }}
    .masonry-item:hover .item-overlay {{
        opacity: 1;
    }}
    .item-cat {{
        display: inline-block;
        padding: 6px 16px;
        background: {primary};
        color: {background};
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-radius: 100px;
        margin-bottom: 12px;
        width: fit-content;
    }}
    .item-overlay h4 {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {text};
    }}
    @media (max-width: 900px) {{
        .masonry-grid {{
            grid-template-columns: repeat(2, 1fr);
        }}
    }}
    @media (max-width: 600px) {{
        .masonry-grid {{
            grid-template-columns: 1fr;
        }}
        .masonry-item.tall {{
            grid-row: span 1;
        }}
    }}
    </style>
    '''
