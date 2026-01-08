from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium Products - A sophisticated product showcase with glassmorphism cards,
    hover effects, and neon accents.
    """
    products = props.get("products", [])
    if not products:
        products = [
            {"name": "Nebula Watch", "price": "$594", "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600"},
            {"name": "Void Speaker", "price": "$382", "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=600"},
            {"name": "Eclipse Glasses", "price": "$299", "image": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=600"},
            {"name": "Cosmic Scent", "price": "$125", "image": "https://images.unsplash.com/photo-1528740561666-dc24705f08a7?w=600"},
        ]
        
    primary = colors.get("primary", "#D4AF37")
    bg = colors.get("background", "#0F0F0F")
    text = colors.get("text", "#FFFFFF")
    
    product_html = ""
    for prod in products:
        product_html += f'''
        <div class="aura-card">
            <div class="card-image-wrapper">
                <img src="{prod.get("image")}" alt="{prod.get("name")}">
                <div class="card-overlay">
                    <button class="quick-add">Add to Cart</button>
                </div>
            </div>
            <div class="card-details">
                <h3>{prod.get("name")}</h3>
                <div class="price-row">
                    <span class="price">{prod.get("price")}</span>
                    <div class="rating">★★★★★</div>
                </div>
            </div>
        </div>
        '''

    return f'''
    <section class="aura-products" id="products">
        <div class="container">
            <div class="section-header">
                <span class="section-sub">Selected For You</span>
                <h2 class="section-title">Curated Essentials</h2>
            </div>
            
            <div class="products-grid">
                {product_html}
            </div>
            
            <div class="view-all-wrapper">
                <a href="#" class="btn-view-all">View All</a>
            </div>
        </div>
    </section>
    
    <style>
    .aura-products {{
        padding: 120px 0;
        background-color: {bg};
        color: {text};
        font-family: 'Outfit', sans-serif;
        position: relative;
    }}
    
    .aura-products::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    }}
    
    .section-header {{
        text-align: center;
        margin-bottom: 80px;
    }}
    
    .section-sub {{
        display: block;
        font-size: 0.9rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: {primary};
        margin-bottom: 16px;
    }}
    
    .section-title {{
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        background: linear-gradient(to right, #fff, rgba(255,255,255,0.5));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    
    .products-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 40px;
        margin-bottom: 60px;
    }}
    
    .aura-card {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 15px;
        transition: all 0.4s ease;
    }}
    
    .aura-card:hover {{
        background: rgba(255, 255, 255, 0.05);
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        border-color: rgba(255, 255, 255, 0.15);
    }}
    
    .card-image-wrapper {{
        position: relative;
        border-radius: 15px;
        overflow: hidden;
        aspect-ratio: 1;
        margin-bottom: 20px;
    }}
    
    .card-image-wrapper img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s ease;
    }}
    
    .aura-card:hover .card-image-wrapper img {{
        transform: scale(1.1);
    }}
    
    .card-overlay {{
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.4);
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s;
    }}
    
    .aura-card:hover .card-overlay {{
        opacity: 1;
    }}
    
    .quick-add {{
        background: {primary};
        color: black;
        border: none;
        padding: 12px 24px;
        border-radius: 30px;
        font-weight: 600;
        transform: translateY(20px);
        transition: transform 0.3s;
        cursor: pointer;
    }}
    
    .aura-card:hover .quick-add {{
        transform: translateY(0);
    }}
    
    .card-details h3 {{
        font-family: 'Playfair Display', serif;
        font-size: 1.25rem;
        margin-bottom: 8px;
    }}
    
    .price-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    
    .price {{
        color: {primary};
        font-weight: 700;
        font-size: 1.1rem;
    }}
    
    .rating {{
        font-size: 0.8rem;
        color: #F59E0B;
        letter-spacing: 2px;
    }}
    
    .view-all-wrapper {{
        text-align: center;
    }}
    
    .btn-view-all {{
        display: inline-block;
        padding: 16px 48px;
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
        text-decoration: none;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
        transition: all 0.3s;
    }}
    
    .btn-view-all:hover {{
        background: {primary};
        border-color: {primary};
        color: black;
    }}
    
    @media (max-width: 640px) {{
        .section-title {{ font-size: 2.5rem; }}
        .products-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
