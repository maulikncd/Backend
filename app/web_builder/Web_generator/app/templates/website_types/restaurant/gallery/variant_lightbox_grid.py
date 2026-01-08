from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Lightbox Grid - Grid with lightbox on click"""
    title = props.get("sectionTitle", "Gallery")
    subtitle = props.get("subtitle", "A glimpse into our world")
    
    primary = colors.get("primary", "#2D3436")
    bg = colors.get("background", "#F8F8F8")
    text = colors.get("text", "#1A1A1A")
    
    images = [
        ("https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600", "The Dining Room"),
        ("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600", "Private Events"),
        ("https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600", "Signature Dishes"),
        ("https://images.unsplash.com/photo-1544025162-d76694265947?w=600", "The Kitchen"),
        ("https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=600", "The Bar"),
        ("https://images.unsplash.com/photo-1559339352-11d035aa65de?w=600", "Outdoor Terrace"),
    ]
    
    items_html = ""
    for img, caption in images:
        items_html += f'''
        <div class="lightbox-item" data-src="{img}">
            <img src="{img}" alt="{caption}">
            <div class="item-caption">
                <span>{caption}</span>
                <span class="icon">+</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gallery-lightbox" id="gallery">
        <div class="gallery-container">
            <div class="gallery-header">
                <span class="label">Gallery</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="lightbox-grid">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Inter:wght@400;500&display=swap');
    
    .gallery-lightbox {{
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
    .lightbox-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 25px;
    }}
    .lightbox-item {{
        position: relative;
        overflow: hidden;
        border-radius: 15px;
        cursor: pointer;
    }}
    .lightbox-item img {{
        width: 100%;
        height: 280px;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .lightbox-item:hover img {{
        transform: scale(1.05);
    }}
    .item-caption {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.8), transparent 60%);
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        padding: 25px;
        opacity: 0;
        transition: opacity 0.3s;
    }}
    .lightbox-item:hover .item-caption {{
        opacity: 1;
    }}
    .item-caption span {{
        color: white;
        font-size: 1rem;
    }}
    .item-caption .icon {{
        width: 40px;
        height: 40px;
        background: {primary};
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
    }}
    @media (max-width: 968px) {{
        .lightbox-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .gallery-lightbox {{ padding: 80px 30px; }}
        .lightbox-grid {{ grid-template-columns: 1fr; }}
        .lightbox-item img {{ height: 250px; }}
    }}
    </style>
    '''
