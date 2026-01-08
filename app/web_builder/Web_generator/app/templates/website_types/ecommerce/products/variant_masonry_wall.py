from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Masonry Wall Products - A Pinterest-style asymmetrical grid layout for
    showcasing products in a visually interesting way.
    """
    products = props.get("products", [])
    if not products:
        products = [
            {"name": "Studio Lamp", "price": "$120", "image": "https://images.unsplash.com/photo-1507473888900-52e1ad1459ee?w=500"},
            {"name": "Comfort Chair", "price": "$299", "image": "https://images.unsplash.com/photo-1592078615290-033ee584e267?w=500"},
            {"name": "Art Vase", "price": "$89", "image": "https://images.unsplash.com/photo-1578500494198-246f612d3e3d?w=500"},
            {"name": "Oak Table", "price": "$450", "image": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?w=500"},
            {"name": "Wall Clock", "price": "$120", "image": "https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?w=500"},
            {"name": "Sofa Set", "price": "$899", "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500"},
        ]

    bg = colors.get("background", "#F9F9F9")
    
    items_html = ""
    for idx, prod in enumerate(products):
        # Assign different heights randomly or by index for masonry effect
        height_class = "tall" if idx % 3 == 0 else ("short" if idx % 2 == 0 else "medium")
        
        items_html += f'''
        <div class="masonry-item {height_class}">
            <img src="{prod.get("image")}" alt="{prod.get("name")}">
            <div class="masonry-overlay">
                <div class="masonry-info">
                    <h3>{prod.get("name")}</h3>
                    <span>{prod.get("price")}</span>
                    <button class="btn-add">+</button>
                </div>
            </div>
        </div>
        '''
        
    return f'''
    <section class="masonry-products" id="products">
        <div class="container">
            <h2 class="section-title">The Collection</h2>
            <div class="masonry-grid">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    .masonry-products {{
        padding: 100px 0;
        background: {bg};
    }}
    
    .section-title {{
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
        font-size: 2.5rem;
        letter-spacing: 2px;
        margin-bottom: 60px;
        text-transform: uppercase;
    }}
    
    .masonry-grid {{
        column-count: 3;
        column-gap: 20px;
        max-width: 1200px;
        margin: 0 auto;
    }}
    
    .masonry-item {{
        position: relative;
        margin-bottom: 20px;
        border-radius: 12px;
        overflow: hidden;
        break-inside: avoid;
        cursor: pointer;
    }}
    
    .masonry-item img {{
        width: 100%;
        display: block;
        object-fit: cover;
    }}
    
    /* Simulate aspect ratios */
    .tall img {{ height: 500px; }}
    .medium img {{ height: 350px; }}
    .short img {{ height: 250px; }}
    
    .masonry-overlay {{
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.5);
        opacity: 0;
        transition: opacity 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        backdrop-filter: blur(5px);
    }}
    
    .masonry-item:hover .masonry-overlay {{
        opacity: 1;
    }}
    
    .masonry-info {{
        text-align: center;
        color: white;
        transform: translateY(20px);
        transition: transform 0.3s;
    }}
    
    .masonry-item:hover .masonry-info {{
        transform: translateY(0);
    }}
    
    .masonry-info h3 {{
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        margin-bottom: 5px;
    }}
    
    .btn-add {{
        margin-top: 15px;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: none;
        background: white;
        color: black;
        font-size: 1.5rem;
        cursor: pointer;
        transition: transform 0.2s;
    }}
    
    .btn-add:hover {{
        transform: scale(1.1);
    }}
    
    @media (max-width: 900px) {{
        .masonry-grid {{ column-count: 2; }}
    }}
    @media (max-width: 600px) {{
        .masonry-grid {{ column-count: 1; }}
    }}
    </style>
    '''
