from typing import Dict, Any, List

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Categories Grid - Shop by category section with
    modern card layout and hover effects
    """
    title = props.get("sectionTitle", props.get("title", "Shop by Category"))
    categories = props.get("categories", _get_default_categories())
    
    primary = colors.get("primary", "#000000")
    secondary = colors.get("secondary", "#FF4444")
    bg = colors.get("background", "#F8F9FA")
    text = colors.get("text", "#111111")
    
    categories_html = ""
    for i, cat in enumerate(categories[:6]):
        size = "large" if i < 2 else "small"
        categories_html += f'''
        <a href="#" class="category-card size-{size}">
            <div class="category-image">
                <img src="{cat.get('image', 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600')}" alt="{cat.get('name', 'Category')}">
            </div>
            <div class="category-overlay">
                <span class="category-count">{cat.get('count', '50+')} Products</span>
                <h3 class="category-name">{cat.get('name', 'Category')}</h3>
                <span class="category-cta">Shop Now →</span>
            </div>
        </a>
        '''
    
    return f'''
    <section class="categories-section" id="categories">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">{title}</h2>
            </div>
            
            <div class="categories-grid">
                {categories_html}
            </div>
        </div>
    </section>
    
    <style>
    .categories-section {{
        padding: 100px 0;
        background: {bg};
    }}
    .categories-section .container {{
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .section-header {{
        text-align: center;
        margin-bottom: 50px;
    }}
    .section-title {{
        font-size: 2.5rem;
        font-weight: 700;
        color: {text};
    }}
    .categories-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(2, 280px);
        gap: 24px;
    }}
    .category-card {{
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        text-decoration: none;
    }}
    .category-card.size-large {{
        grid-column: span 2;
        grid-row: span 2;
    }}
    .category-image {{
        position: absolute;
        inset: 0;
    }}
    .category-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .category-card:hover .category-image img {{
        transform: scale(1.1);
    }}
    .category-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
        padding: 30px;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        transition: background 0.3s;
    }}
    .category-card:hover .category-overlay {{
        background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.3));
    }}
    .category-count {{
        font-size: 0.85rem;
        color: rgba(255,255,255,0.7);
        margin-bottom: 8px;
    }}
    .category-name {{
        font-size: 1.5rem;
        font-weight: 700;
        color: white;
        margin: 0 0 12px;
    }}
    .category-card.size-large .category-name {{
        font-size: 2rem;
    }}
    .category-cta {{
        font-size: 0.9rem;
        color: {secondary};
        font-weight: 600;
        opacity: 0;
        transform: translateY(10px);
        transition: all 0.3s;
    }}
    .category-card:hover .category-cta {{
        opacity: 1;
        transform: translateY(0);
    }}
    @media (max-width: 1024px) {{
        .categories-grid {{
            grid-template-columns: repeat(2, 1fr);
            grid-template-rows: auto;
        }}
        .category-card.size-large {{ grid-column: span 2; grid-row: span 1; height: 350px; }}
        .category-card.size-small {{ height: 250px; }}
    }}
    @media (max-width: 640px) {{
        .categories-grid {{ grid-template-columns: 1fr; }}
        .category-card.size-large {{ grid-column: span 1; height: 300px; }}
    }}
    </style>
    '''


def _get_default_categories() -> List[Dict]:
    return [
        {"name": "Electronics", "count": "150+", "image": "https://images.unsplash.com/photo-1498049794561-7780e7231661?w=800"},
        {"name": "Fashion", "count": "300+", "image": "https://images.unsplash.com/photo-1445205170230-053b83016050?w=800"},
        {"name": "Home & Living", "count": "200+", "image": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600"},
        {"name": "Sports", "count": "100+", "image": "https://images.unsplash.com/photo-1461896836934- voices-fitness?w=600"},
        {"name": "Beauty", "count": "80+", "image": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=600"},
        {"name": "Accessories", "count": "120+", "image": "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=600"},
    ]
