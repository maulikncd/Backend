from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Product - Single product focus"""
    title = props.get("title", "New Arrival")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-hero-minimal" id="hero">
        <div class="minimal-container">
            <div class="product-showcase">
                <div class="product-image"><span>Product</span></div>
            </div>
            <div class="product-info">
                <span class="tag">New Arrival</span>
                <h1>Premium Collection</h1>
                <p class="price">$299 <span class="old">$399</span></p>
                <p class="desc">Crafted with precision, designed for excellence. Experience the difference.</p>
                <div class="actions">
                    <a href="#" class="btn-buy">Add to Cart</a>
                    <a href="#" class="btn-view">Learn More</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-hero-minimal {{ min-height: 100vh; background: {background}; display: flex; align-items: center; padding: 80px 24px; }}
    .minimal-container {{ max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }}
    .product-image {{ width: 100%; aspect-ratio: 1; background: linear-gradient(135deg, {primary}15, {primary}05); border-radius: 32px; display: flex; align-items: center; justify-content: center; font-size: 2rem; color: {primary}40; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .product-info h1 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 900; color: {text}; margin-bottom: 20px; }}
    .price {{ font-size: 2rem; font-weight: 900; color: {primary}; margin-bottom: 20px; }}
    .price .old {{ text-decoration: line-through; color: {secondary}; font-size: 1.3rem; margin-left: 12px; }}
    .desc {{ color: {secondary}; font-size: 1.1rem; line-height: 1.7; margin-bottom: 40px; }}
    .actions {{ display: flex; gap: 16px; }}
    .btn-buy {{ padding: 18px 40px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 12px; transition: all 0.3s ease; }}
    .btn-buy:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px {primary}40; }}
    .btn-view {{ padding: 18px 40px; background: transparent; border: 2px solid {text}20; color: {text}; text-decoration: none; font-weight: 700; border-radius: 12px; transition: all 0.3s ease; }}
    .btn-view:hover {{ border-color: {primary}; color: {primary}; }}
    @media (max-width: 900px) {{ .minimal-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
