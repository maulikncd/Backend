from typing import Dict, Any, List

def _normalize_item(item) -> Dict[str, Any]:
    if isinstance(item, str):
        return {"name": item, "category": "Menu", "price": "", "description": "", "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400"}
    elif isinstance(item, dict):
        return item
    return {"name": str(item), "category": "Menu", "price": "", "description": "", "image": ""}

def _get_default_menu() -> List[Dict]:
    return [
        {"name": "Truffle Risotto", "category": "Mains", "price": "$48", "description": "Arborio rice, black truffle, parmesan", "image": "https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=400"},
        {"name": "Grilled Lobster", "category": "Mains", "price": "$65", "description": "Maine lobster, garlic butter", "image": "https://images.unsplash.com/photo-1553247407-23251ce81f59?w=400"},
        {"name": "Beef Tartare", "category": "Starters", "price": "$24", "description": "Hand-cut beef, capers, quail egg", "image": "https://images.unsplash.com/photo-1588168333986-5078d3ae3976?w=400"},
        {"name": "Duck Confit", "category": "Mains", "price": "$42", "description": "Slow-cooked duck leg, orange glaze", "image": "https://images.unsplash.com/photo-1432139555190-58524dae6a55?w=400"},
    ]

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Image Cards - Cards with large food images"""
    title = props.get("sectionTitle", props.get("title", "Our Menu"))
    subtitle = props.get("subtitle", "Feast for the eyes and palate")
    raw_items = props.get("menuItems", props.get("items", _get_default_menu()))
    menu_items = [_normalize_item(item) for item in raw_items]
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    items_html = ""
    for item in menu_items[:6]:
        items_html += f'''
        <div class="image-card">
            <div class="card-image">
                <img src="{item.get('image', 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400')}" alt="{item.get('name', 'Dish')}">
                <div class="image-overlay"></div>
            </div>
            <div class="card-content">
                <div class="content-top">
                    <span class="category">{item.get('category', 'Menu')}</span>
                    <span class="price">{item.get('price', '$0')}</span>
                </div>
                <h3 class="name">{item.get('name', 'Dish')}</h3>
                <p class="desc">{item.get('description', '')}</p>
            </div>
        </div>
        '''
    
    return f'''
    <section class="menu-image-cards" id="menu">
        <div class="menu-container">
            <div class="menu-header">
                <span class="label">Culinary Creations</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="cards-grid">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Lato:wght@400&display=swap');
    
    .menu-image-cards {{
        padding: 120px 60px;
        background: {bg};
    }}
    .menu-container {{
        max-width: 1300px;
        margin: 0 auto;
    }}
    .menu-header {{
        text-align: center;
        margin-bottom: 70px;
    }}
    .menu-header .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .menu-header h2 {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(3rem, 6vw, 5rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .menu-header p {{
        color: {text}80;
        font-size: 1.1rem;
    }}
    .cards-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
    }}
    .image-card {{
        background: rgba(255,255,255,0.03);
        border-radius: 20px;
        overflow: hidden;
        transition: all 0.4s;
    }}
    .image-card:hover {{
        transform: translateY(-10px);
    }}
    .card-image {{
        position: relative;
        height: 250px;
        overflow: hidden;
    }}
    .card-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s;
    }}
    .image-card:hover .card-image img {{
        transform: scale(1.1);
    }}
    .image-overlay {{
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.5), transparent);
    }}
    .card-content {{
        padding: 25px;
    }}
    .content-top {{
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }}
    .category {{
        color: {primary};
        font-size: 0.75rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }}
    .price {{
        font-size: 1.2rem;
        font-weight: 600;
        color: {primary};
    }}
    .name {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.5rem;
        color: {text};
        margin-bottom: 10px;
    }}
    .desc {{
        color: {text}70;
        font-size: 0.9rem;
        line-height: 1.6;
    }}
    @media (max-width: 968px) {{
        .cards-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .menu-image-cards {{ padding: 80px 30px; }}
        .cards-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
