from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Products Grid - Modern product grid with hover effects,
    quick view, add to cart, and filtering
    """
    title = props.get("sectionTitle", props.get("title", "Featured Products"))
    subtitle = props.get("subtitle", "Discover our best sellers")
    products = props.get("products", _get_default_products())
    
    primary = colors.get("primary", "#000000")
    secondary = colors.get("secondary", "#FF4444")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#111111")
    
    # Category tabs
    categories = list(set([p.get("category", "All") for p in products]))
    categories.insert(0, "All")
    
    tabs_html = ""
    for cat in categories[:5]:
        active = "active" if cat == "All" else ""
        tabs_html += f'<button class="filter-tab {active}" data-category="{cat}">{cat}</button>'
    
    products_html = ""
    for product in products[:8]:
        badge_html = ""
        if product.get("badge"):
            badge_html = f'<span class="product-badge badge-{product.get("badgeType", "sale")}">{product.get("badge")}</span>'
        
        rating_html = ""
        if product.get("rating"):
            stars = "★" * int(product.get("rating", 5)) + "☆" * (5 - int(product.get("rating", 5)))
            rating_html = f'<div class="product-rating"><span class="stars">{stars}</span><span class="count">({product.get("reviews", 0)})</span></div>'
        
        products_html += f'''
        <div class="product-card" data-category="{product.get('category', 'All')}">
            <div class="product-image">
                {badge_html}
                <img src="{product.get('image', 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400')}" alt="{product.get('name', 'Product')}">
                <div class="product-actions">
                    <button class="action-btn" title="Quick View">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
                    </button>
                    <button class="action-btn" title="Add to Wishlist">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
                    </button>
                    <button class="action-btn add-cart" title="Add to Cart">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                    </button>
                </div>
            </div>
            <div class="product-info">
                <span class="product-category">{product.get('category', 'Category')}</span>
                <h3 class="product-name">{product.get('name', 'Product Name')}</h3>
                {rating_html}
                <div class="product-price">
                    <span class="current-price">${product.get('price', '99')}</span>
                    {f'<span class="original-price">${product.get("originalPrice")}</span>' if product.get('originalPrice') else ''}
                </div>
            </div>
        </div>
        '''
    
    return f'''
    <section class="products-section" id="products">
        <div class="container">
            <div class="section-header">
                <div class="header-content">
                    <h2 class="section-title">{title}</h2>
                    <p class="section-subtitle">{subtitle}</p>
                </div>
                <div class="filter-tabs">
                    {tabs_html}
                </div>
            </div>
            
            <div class="products-grid">
                {products_html}
            </div>
            
            <div class="section-footer">
                <a href="#" class="view-all-btn">View All Products</a>
            </div>
        </div>
    </section>
    
    <style>
    .products-section {{
        padding: 100px 0;
        background: {bg};
    }}
    .products-section .container {{
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .section-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
        margin-bottom: 50px;
        flex-wrap: wrap;
        gap: 30px;
    }}
    .section-title {{
        font-size: 2.5rem;
        font-weight: 700;
        color: {text};
        margin-bottom: 8px;
    }}
    .section-subtitle {{
        font-size: 1.1rem;
        color: {text}60;
    }}
    .filter-tabs {{
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }}
    .filter-tab {{
        padding: 10px 24px;
        background: transparent;
        border: 1px solid {text}15;
        border-radius: 50px;
        font-size: 0.9rem;
        color: {text}70;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .filter-tab:hover {{
        border-color: {primary};
        color: {primary};
    }}
    .filter-tab.active {{
        background: {primary};
        border-color: {primary};
        color: white;
    }}
    .products-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 30px;
    }}
    .product-card {{
        background: white;
        border-radius: 16px;
        overflow: hidden;
        transition: all 0.3s;
    }}
    .product-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }}
    .product-image {{
        position: relative;
        aspect-ratio: 1;
        overflow: hidden;
        background: #f8f9fa;
    }}
    .product-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .product-card:hover .product-image img {{
        transform: scale(1.08);
    }}
    .product-badge {{
        position: absolute;
        top: 12px;
        left: 12px;
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 700;
        z-index: 2;
    }}
    .badge-sale {{ background: {secondary}; color: white; }}
    .badge-new {{ background: {primary}; color: white; }}
    .badge-hot {{ background: #FF6B35; color: white; }}
    .product-actions {{
        position: absolute;
        right: 12px;
        top: 50%;
        transform: translateY(-50%) translateX(60px);
        display: flex;
        flex-direction: column;
        gap: 8px;
        opacity: 0;
        transition: all 0.3s;
    }}
    .product-card:hover .product-actions {{
        transform: translateY(-50%) translateX(0);
        opacity: 1;
    }}
    .action-btn {{
        width: 44px;
        height: 44px;
        background: white;
        border: none;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s;
        color: {text};
    }}
    .action-btn:hover {{
        background: {primary};
        color: white;
    }}
    .action-btn.add-cart:hover {{
        background: {secondary};
    }}
    .product-info {{
        padding: 20px;
    }}
    .product-category {{
        font-size: 0.8rem;
        color: {text}50;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .product-name {{
        font-size: 1.1rem;
        font-weight: 600;
        color: {text};
        margin: 8px 0;
        line-height: 1.4;
    }}
    .product-rating {{
        display: flex;
        align-items: center;
        gap: 6px;
        margin-bottom: 10px;
    }}
    .stars {{ color: #FFB800; font-size: 0.9rem; }}
    .count {{ font-size: 0.8rem; color: {text}50; }}
    .product-price {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    .current-price {{
        font-size: 1.25rem;
        font-weight: 700;
        color: {text};
    }}
    .original-price {{
        font-size: 1rem;
        color: {text}40;
        text-decoration: line-through;
    }}
    .section-footer {{
        text-align: center;
        margin-top: 50px;
    }}
    .view-all-btn {{
        display: inline-block;
        padding: 16px 48px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 600;
        border-radius: 50px;
        transition: all 0.3s;
    }}
    .view-all-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px {primary}30;
    }}
    @media (max-width: 1200px) {{ .products-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
    @media (max-width: 900px) {{ .products-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 600px) {{
        .products-grid {{ grid-template-columns: 1fr; }}
        .section-header {{ flex-direction: column; align-items: flex-start; }}
    }}
    </style>
    
    <script>
    document.querySelectorAll('.filter-tab').forEach(tab => {{
        tab.addEventListener('click', () => {{
            document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            const category = tab.dataset.category;
            document.querySelectorAll('.product-card').forEach(card => {{
                if (category === 'All' || card.dataset.category === category) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }});
    }});
    </script>
    '''


def _get_default_products() -> List[Dict]:
    return [
        {"name": "Premium Wireless Headphones", "category": "Electronics", "price": "149", "originalPrice": "299", "rating": 5, "reviews": 128, "badge": "Sale", "badgeType": "sale", "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400"},
        {"name": "Smart Watch Pro", "category": "Electronics", "price": "299", "rating": 4, "reviews": 89, "badge": "New", "badgeType": "new", "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=400"},
        {"name": "Leather Crossbody Bag", "category": "Fashion", "price": "89", "rating": 5, "reviews": 256, "image": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=400"},
        {"name": "Running Sneakers", "category": "Fashion", "price": "129", "originalPrice": "159", "rating": 4, "reviews": 342, "badge": "Hot", "badgeType": "hot", "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"},
        {"name": "Minimalist Desk Lamp", "category": "Home", "price": "79", "rating": 5, "reviews": 67, "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400"},
        {"name": "Ceramic Plant Pot Set", "category": "Home", "price": "45", "rating": 4, "reviews": 98, "image": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=400"},
        {"name": "Vintage Sunglasses", "category": "Fashion", "price": "65", "rating": 4, "reviews": 156, "badge": "New", "badgeType": "new", "image": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400"},
        {"name": "Portable Speaker", "category": "Electronics", "price": "99", "originalPrice": "149", "rating": 5, "reviews": 203, "badge": "Sale", "badgeType": "sale", "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400"},
    ]
