from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Featured Products - Large hero with sidebar"""
    title = props.get("title", "Game Store")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-store-featured" id="store">
        <div class="store-container">
            <div class="store-header">
                <span class="tag">🛒 Store</span>
                <h2>{title}</h2>
            </div>
            <div class="store-layout">
                <div class="featured-product">
                    <div class="product-badge">🔥 Hot Deal</div>
                    <img src="https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=800" alt="Featured">
                    <div class="product-info">
                        <h3>Legendary Battle Pass</h3>
                        <p>100+ exclusive rewards, skins, and items</p>
                        <div class="price-row">
                            <span class="old-price">$29.99</span>
                            <span class="new-price">$19.99</span>
                        </div>
                        <a href="#" class="btn-buy">Buy Now</a>
                    </div>
                </div>
                <div class="product-sidebar">
                    <h4>Popular Items</h4>
                    <div class="mini-product">
                        <img src="https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=200" alt="Product">
                        <div class="mini-info">
                            <span>Shadow Skin Pack</span>
                            <strong>$9.99</strong>
                        </div>
                    </div>
                    <div class="mini-product">
                        <img src="https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=200" alt="Product">
                        <div class="mini-info">
                            <span>1000 Coins</span>
                            <strong>$4.99</strong>
                        </div>
                    </div>
                    <div class="mini-product">
                        <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=200" alt="Product">
                        <div class="mini-info">
                            <span>Pro Starter Kit</span>
                            <strong>$14.99</strong>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-store-featured {{
        padding: 120px 24px;
        background: {background};
    }}
    .store-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .store-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .tag {{
        display: inline-block;
        padding: 10px 24px;
        background: {primary}15;
        color: {primary};
        font-weight: 700;
        border-radius: 100px;
        margin-bottom: 20px;
    }}
    .store-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
    }}
    .store-layout {{
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 40px;
    }}
    .featured-product {{
        background: {text}05;
        border-radius: 24px;
        padding: 40px;
        position: relative;
    }}
    .product-badge {{
        position: absolute;
        top: 24px;
        right: 24px;
        padding: 8px 20px;
        background: #ff3b3b;
        color: white;
        font-weight: 700;
        font-size: 0.9rem;
        border-radius: 100px;
    }}
    .featured-product img {{
        width: 100%;
        aspect-ratio: 16/9;
        object-fit: cover;
        border-radius: 16px;
        margin-bottom: 32px;
    }}
    .product-info h3 {{
        font-size: 2rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 12px;
    }}
    .product-info p {{
        color: {secondary};
        margin-bottom: 24px;
    }}
    .price-row {{
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 24px;
    }}
    .old-price {{
        color: {secondary};
        text-decoration: line-through;
        font-size: 1.2rem;
    }}
    .new-price {{
        color: {primary};
        font-size: 2.5rem;
        font-weight: 900;
    }}
    .btn-buy {{
        display: inline-block;
        padding: 16px 48px;
        background: {primary};
        color: {background};
        text-decoration: none;
        font-weight: 700;
        border-radius: 12px;
        transition: all 0.3s ease;
    }}
    .btn-buy:hover {{
        transform: scale(1.05);
        box-shadow: 0 20px 50px {primary}40;
    }}
    .product-sidebar h4 {{
        color: {text};
        font-weight: 700;
        margin-bottom: 24px;
        padding-bottom: 16px;
        border-bottom: 2px solid {primary};
    }}
    .mini-product {{
        display: flex;
        gap: 16px;
        padding: 16px;
        background: {text}05;
        border-radius: 12px;
        margin-bottom: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .mini-product:hover {{
        background: {primary}10;
    }}
    .mini-product img {{
        width: 60px;
        height: 60px;
        object-fit: cover;
        border-radius: 8px;
    }}
    .mini-info {{
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .mini-info span {{
        color: {text};
        font-weight: 600;
        margin-bottom: 4px;
    }}
    .mini-info strong {{
        color: {primary};
    }}
    @media (max-width: 900px) {{
        .store-layout {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
