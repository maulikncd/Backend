from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Masonry Grid - Pinterest-style masonry layout"""
    title = props.get("sectionTitle", "Gallery")
    subtitle = props.get("subtitle", "Moments captured")
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    images = [
        "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600",
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=400",
        "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=500",
        "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=400",
        "https://images.unsplash.com/photo-1544025162-d76694265947?w=600",
        "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=400",
    ]
    
    items_html = ""
    for i, img in enumerate(images):
        items_html += f'''
        <div class="masonry-item">
            <img src="{img}" alt="Gallery {i+1}">
            <div class="item-overlay"></div>
        </div>
        '''
    
    return f'''
    <section class="gallery-masonry" id="gallery">
        <div class="gallery-container">
            <div class="gallery-header">
                <span class="label">Gallery</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="masonry-grid">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&display=swap');
    
    .gallery-masonry {{
        padding: 120px 60px;
        background: {bg};
    }}
    .gallery-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .gallery-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .gallery-header .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .gallery-header h2 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .gallery-header p {{
        color: {text}70;
        font-size: 1.1rem;
    }}
    .masonry-grid {{
        columns: 3;
        column-gap: 20px;
    }}
    .masonry-item {{
        break-inside: avoid;
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
        border-radius: 15px;
    }}
    .masonry-item img {{
        width: 100%;
        display: block;
        transition: transform 0.5s;
    }}
    .masonry-item:hover img {{
        transform: scale(1.05);
    }}
    .item-overlay {{
        position: absolute;
        inset: 0;
        background: {primary};
        opacity: 0;
        transition: opacity 0.3s;
    }}
    .masonry-item:hover .item-overlay {{
        opacity: 0.2;
    }}
    @media (max-width: 968px) {{
        .masonry-grid {{ columns: 2; }}
    }}
    @media (max-width: 600px) {{
        .gallery-masonry {{ padding: 80px 30px; }}
        .masonry-grid {{ columns: 1; }}
    }}
    </style>
    '''
