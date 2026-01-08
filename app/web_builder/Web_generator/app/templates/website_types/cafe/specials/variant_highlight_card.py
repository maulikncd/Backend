from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    title = props.get("title", "Daily Specials")
    special_title = props.get("special_title", "Caramel Macchiato")
    special_desc = props.get("special_desc", "Freshly brewed espresso with steamed milk and a drizzle of homemade caramel.")
    price = props.get("price", "$5.50")
    image = props.get("image", "https://images.unsplash.com/photo-1485808191679-5f86510681a2?w=800")
    
    return f'''
    <section class="cafe-specials" id="specials">
        <div class="specials-container">
            <div class="special-card">
                <div class="special-image" style="background-image: url('{image}')"></div>
                <div class="special-content">
                    <span class="special-tag">Limited Time</span>
                    <h2 class="section-title">{title}</h2>
                    <h3 class="item-title">{special_title}</h3>
                    <p class="item-desc">{special_desc}</p>
                    <div class="item-footer">
                        <span class="item-price">{price}</span>
                        <a href="#menu" class="btn-special">Order Now</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .cafe-specials {{ padding: 100px 24px; background: {colors.get("background", "#FFF8F0")}; }}
    .specials-container {{ max-width: 1000px; margin: 0 auto; }}
    .special-card {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        background: #fff;
        border-radius: 24px;
        overflow: hidden;
        box-shadow: 0 40px 80px rgba(0,0,0,0.08);
    }}
    .special-image {{ background-size: cover; background-position: center; min-height: 400px; }}
    .special-content {{ padding: 60px; display: flex; flex-direction: column; justify-content: center; }}
    .special-tag {{ color: {colors.get("primary", "#6F4E37")}; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; margin-bottom: 16px; }}
    .section-title {{ font-family: 'Playfair Display', serif; font-size: 1.2rem; color: #888; margin-bottom: 8px; }}
    .item-title {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 16px; }}
    .item-desc {{ color: {colors.get("text_muted", "#8B7355")}; line-height: 1.7; margin-bottom: 32px; }}
    .item-footer {{ display: flex; align-items: center; gap: 24px; }}
    .item-price {{ font-size: 1.8rem; font-weight: 700; color: {colors.get("text", "#2D2013")}; }}
    .btn-special {{ padding: 12px 32px; background: {colors.get("primary", "#6F4E37")}; color: #fff; text-decoration: none; border-radius: 50px; font-weight: 600; }}
    @media (max-width: 768px) {{ .special-card {{ grid-template-columns: 1fr; }} .special-content {{ padding: 40px; }} }}
    </style>
    '''
