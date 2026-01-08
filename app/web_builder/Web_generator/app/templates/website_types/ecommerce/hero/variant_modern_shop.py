from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Modern Shop - Clean e-commerce hero with featured product,
    sale banner and shopping CTAs
    """
    name = props.get("name", props.get("businessName", "ShopHub"))
    tagline = props.get("tagline", "Shop the Latest Trends")
    description = props.get("description", "Discover premium products at unbeatable prices. Free shipping on orders over $50.")
    cta = props.get("cta", "Shop Now")
    sale_text = props.get("saleText", "Up to 50% Off")
    
    primary = colors.get("primary", "#000000")
    secondary = colors.get("secondary", "#FF4444")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#111111")
    
    return f'''
    <section class="shop-hero" id="hero">
        <div class="hero-container">
            <div class="hero-content">
                <div class="sale-badge">
                    <span class="badge-icon">🔥</span>
                    <span>{sale_text}</span>
                </div>
                
                <h1 class="hero-title">{tagline}</h1>
                <p class="hero-desc">{description}</p>
                
                <div class="cta-group">
                    <a href="#products" class="btn-primary">{cta}</a>
                    <a href="#categories" class="btn-secondary">Browse Categories</a>
                </div>
                
                <div class="trust-badges">
                    <div class="trust-item">
                        <span class="trust-icon">🚚</span>
                        <span>Free Shipping</span>
                    </div>
                    <div class="trust-item">
                        <span class="trust-icon">↩️</span>
                        <span>Easy Returns</span>
                    </div>
                    <div class="trust-item">
                        <span class="trust-icon">🔒</span>
                        <span>Secure Checkout</span>
                    </div>
                </div>
            </div>
            
            <div class="hero-products">
                <div class="featured-product">
                    <div class="product-badge">Best Seller</div>
                    <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600" alt="Featured Product">
                    <div class="product-info">
                        <span class="product-category">Electronics</span>
                        <h3 class="product-name">Premium Headphones</h3>
                        <div class="product-pricing">
                            <span class="price-current">$149</span>
                            <span class="price-original">$299</span>
                        </div>
                    </div>
                </div>
                
                <div class="floating-products">
                    <div class="mini-product">
                        <img src="https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=200" alt="Product">
                        <span class="mini-price">$79</span>
                    </div>
                    <div class="mini-product">
                        <img src="https://images.unsplash.com/photo-1585386959984-a4155224a1ad?w=200" alt="Product">
                        <span class="mini-price">$129</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    .shop-hero {{
        min-height: 100vh;
        background: {bg};
        display: flex;
        align-items: center;
        padding: 120px 60px;
        position: relative;
        overflow: hidden;
    }}
    .hero-container {{
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
    }}
    .sale-badge {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 12px 24px;
        background: {secondary};
        color: white;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 700;
        margin-bottom: 30px;
        animation: pulse 2s infinite;
    }}
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.02); }}
    }}
    .hero-title {{
        font-family: 'Inter', sans-serif;
        font-size: clamp(3rem, 5vw, 4.5rem);
        font-weight: 800;
        color: {text};
        line-height: 1.1;
        margin-bottom: 24px;
    }}
    .hero-desc {{
        font-size: 1.2rem;
        color: {text}80;
        line-height: 1.8;
        margin-bottom: 40px;
        max-width: 500px;
    }}
    .cta-group {{
        display: flex;
        gap: 16px;
        margin-bottom: 50px;
        flex-wrap: wrap;
    }}
    .btn-primary {{
        padding: 18px 40px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 700;
        border-radius: 12px;
        transition: all 0.3s;
        box-shadow: 0 4px 20px {primary}30;
    }}
    .btn-primary:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 30px {primary}40;
    }}
    .btn-secondary {{
        padding: 18px 40px;
        background: transparent;
        border: 2px solid {text}20;
        color: {text};
        text-decoration: none;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s;
    }}
    .btn-secondary:hover {{
        border-color: {primary};
        color: {primary};
    }}
    .trust-badges {{
        display: flex;
        gap: 30px;
        flex-wrap: wrap;
    }}
    .trust-item {{
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.95rem;
        color: {text}70;
    }}
    .trust-icon {{ font-size: 1.2rem; }}
    .hero-products {{
        position: relative;
    }}
    .featured-product {{
        background: #f8f9fa;
        border-radius: 30px;
        padding: 30px;
        position: relative;
        overflow: hidden;
    }}
    .product-badge {{
        position: absolute;
        top: 20px;
        left: 20px;
        padding: 8px 16px;
        background: {secondary};
        color: white;
        font-size: 0.8rem;
        font-weight: 700;
        border-radius: 50px;
    }}
    .featured-product img {{
        width: 100%;
        height: 350px;
        object-fit: contain;
        margin-bottom: 24px;
    }}
    .product-info {{
        text-align: center;
    }}
    .product-category {{
        font-size: 0.85rem;
        color: {text}50;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .product-name {{
        font-size: 1.5rem;
        font-weight: 700;
        color: {text};
        margin: 8px 0 16px;
    }}
    .product-pricing {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 12px;
    }}
    .price-current {{
        font-size: 1.8rem;
        font-weight: 800;
        color: {secondary};
    }}
    .price-original {{
        font-size: 1.2rem;
        color: {text}40;
        text-decoration: line-through;
    }}
    .floating-products {{
        position: absolute;
        top: 20%;
        right: -80px;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }}
    .mini-product {{
        background: white;
        border-radius: 16px;
        padding: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
        animation: floatY 3s ease-in-out infinite;
    }}
    .mini-product:nth-child(2) {{ animation-delay: 1.5s; }}
    @keyframes floatY {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-10px); }}
    }}
    .mini-product img {{
        width: 80px;
        height: 80px;
        object-fit: contain;
    }}
    .mini-price {{
        display: block;
        font-weight: 700;
        color: {text};
        margin-top: 8px;
    }}
    @media (max-width: 1024px) {{
        .hero-container {{ grid-template-columns: 1fr; gap: 60px; }}
        .floating-products {{ display: none; }}
        .shop-hero {{ padding: 120px 40px; }}
    }}
    @media (max-width: 640px) {{
        .shop-hero {{ padding: 100px 24px; }}
        .trust-badges {{ flex-direction: column; gap: 16px; }}
    }}
    </style>
    '''
