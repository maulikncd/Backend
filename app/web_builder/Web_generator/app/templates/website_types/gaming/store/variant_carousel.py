from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Carousel Store - Horizontal scrolling products"""
    title = props.get("title", "Featured Items")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    products = [
        {"name": "Battle Pass S5", "price": "$19.99", "img": "https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=400"},
        {"name": "Shadow Bundle", "price": "$14.99", "img": "https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=400"},
        {"name": "5000 Coins", "price": "$49.99", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=400"},
        {"name": "Starter Pack", "price": "$9.99", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400"},
        {"name": "Pro Set", "price": "$29.99", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400"},
    ]
    
    cards_html = ""
    for p in products:
        cards_html += f'''
        <div class="carousel-product">
            <div class="product-img">
                <img src="{p['img']}" alt="{p['name']}">
            </div>
            <h3>{p['name']}</h3>
            <span class="price">{p['price']}</span>
            <button class="quick-buy">Quick Buy</button>
        </div>
        '''
    
    return f'''
    <section class="gaming-store-carousel" id="store">
        <div class="carousel-header">
            <h2>{title}</h2>
            <div class="carousel-nav">
                <button class="nav-btn">←</button>
                <button class="nav-btn">→</button>
            </div>
        </div>
        <div class="carousel-track">
            {cards_html}
        </div>
    </section>
    
    <style>
    .gaming-store-carousel {{
        padding: 120px 0;
        background: {background};
    }}
    .carousel-header {{
        max-width: 1400px;
        margin: 0 auto 40px;
        padding: 0 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .carousel-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        color: {text};
    }}
    .carousel-nav {{
        display: flex;
        gap: 12px;
    }}
    .nav-btn {{
        width: 50px;
        height: 50px;
        background: {text}08;
        border: none;
        border-radius: 50%;
        color: {text};
        font-size: 1.3rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .nav-btn:hover {{
        background: {primary};
        color: {background};
    }}
    .carousel-track {{
        display: flex;
        gap: 24px;
        overflow-x: auto;
        padding: 0 24px 20px;
        scroll-snap-type: x mandatory;
        scrollbar-width: none;
    }}
    .carousel-track::-webkit-scrollbar {{
        display: none;
    }}
    .carousel-product {{
        flex-shrink: 0;
        width: 280px;
        background: {text}05;
        border-radius: 20px;
        padding: 20px;
        scroll-snap-align: start;
        transition: all 0.4s ease;
    }}
    .carousel-product:hover {{
        transform: translateY(-8px);
        box-shadow: 0 20px 50px {primary}15;
    }}
    .product-img {{
        aspect-ratio: 1;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 16px;
    }}
    .product-img img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    .carousel-product:hover .product-img img {{
        transform: scale(1.1);
    }}
    .carousel-product h3 {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 8px;
    }}
    .price {{
        display: block;
        font-size: 1.3rem;
        font-weight: 900;
        color: {primary};
        margin-bottom: 16px;
    }}
    .quick-buy {{
        width: 100%;
        padding: 12px;
        background: {primary};
        color: {background};
        border: none;
        font-weight: 700;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .quick-buy:hover {{
        transform: scale(1.02);
    }}
    </style>
    '''
