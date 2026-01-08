from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Card Grid - Standard product grid layout"""
    title = props.get("title", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    products = [
        {"name": "Battle Pass Season 5", "price": "$19.99", "img": "https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=400", "tag": "New"},
        {"name": "Shadow Skin Bundle", "price": "$14.99", "img": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=400", "tag": ""},
        {"name": "5000 Game Coins", "price": "$49.99", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=400", "tag": "Best Value"},
        {"name": "Starter Pack", "price": "$9.99", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400", "tag": ""},
        {"name": "Pro Gaming Set", "price": "$29.99", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400", "tag": "Popular"},
        {"name": "1000 Coins", "price": "$9.99", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400", "tag": ""},
    ]
    
    cards_html = ""
    for p in products:
        tag_html = f'<span class="product-tag">{p["tag"]}</span>' if p["tag"] else ""
        cards_html += f'''
        <div class="product-card">
            {tag_html}
            <div class="product-image">
                <img src="{p['img']}" alt="{p['name']}">
            </div>
            <div class="product-details">
                <h3>{p['name']}</h3>
                <span class="price">{p['price']}</span>
                <button class="add-btn">Add to Cart</button>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-store-cards" id="store">
        <div class="store-container">
            <div class="store-header">
                <h2>{title}</h2>
                <div class="filter-tabs">
                    <button class="tab active">All</button>
                    <button class="tab">Bundles</button>
                    <button class="tab">Coins</button>
                    <button class="tab">Skins</button>
                </div>
            </div>
            <div class="products-grid">
                {cards_html}
            </div>
        </div>
    </section>
    
    <style>
    .gaming-store-cards {{
        padding: 120px 24px;
        background: {background};
    }}
    .store-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .store-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 48px;
        flex-wrap: wrap;
        gap: 24px;
    }}
    .store-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
    }}
    .filter-tabs {{
        display: flex;
        gap: 8px;
    }}
    .tab {{
        padding: 10px 24px;
        background: {text}08;
        border: none;
        color: {secondary};
        font-weight: 600;
        border-radius: 100px;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .tab.active, .tab:hover {{
        background: {primary};
        color: {background};
    }}
    .products-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
    }}
    .product-card {{
        background: {text}05;
        border-radius: 20px;
        overflow: hidden;
        position: relative;
        transition: all 0.4s ease;
    }}
    .product-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 30px 60px {primary}15;
    }}
    .product-tag {{
        position: absolute;
        top: 16px;
        left: 16px;
        padding: 6px 14px;
        background: {primary};
        color: {background};
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 100px;
        z-index: 2;
    }}
    .product-image {{
        aspect-ratio: 4/3;
        overflow: hidden;
    }}
    .product-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .product-card:hover .product-image img {{
        transform: scale(1.1);
    }}
    .product-details {{
        padding: 24px;
    }}
    .product-details h3 {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 8px;
    }}
    .price {{
        display: block;
        font-size: 1.5rem;
        font-weight: 900;
        color: {primary};
        margin-bottom: 16px;
    }}
    .add-btn {{
        width: 100%;
        padding: 14px;
        background: {primary};
        color: {background};
        border: none;
        font-weight: 700;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .add-btn:hover {{
        transform: scale(1.02);
        box-shadow: 0 10px 30px {primary}40;
    }}
    @media (max-width: 900px) {{
        .products-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .products-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
