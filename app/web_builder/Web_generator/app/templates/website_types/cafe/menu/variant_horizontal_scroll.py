from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Scroll Menu - Instagram-like horizontal scrolling cards"""
    title = props.get("sectionTitle", props.get("title", "Popular Items"))
    raw_items = props.get("items", [])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    bg = colors.get("background", "#FAF7F4")
    
    items = []
    for item in raw_items:
        items.append({
            "name": item.get("name", "Item"),
            "desc": item.get("description", "")[:50],
            "price": item.get("price", "$0"),
            "image": f"https://source.unsplash.com/300x400/?{item.get('name', 'food').replace(' ', ',')}"
        })
    
    if not items:
        items = [
            {"name": "Espresso", "desc": "Rich and bold", "price": "$3.50", "image": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=300"},
            {"name": "Latte", "desc": "Smooth and creamy", "price": "$5.00", "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=300"},
            {"name": "Croissant", "desc": "Buttery layers", "price": "$4.00", "image": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=300"},
            {"name": "Pancakes", "desc": "Fluffy stacks", "price": "$12.00", "image": "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=300"}
        ]
    
    items_html = ""
    for item in items[:8]:
        items_html += f'''
        <div class="scroll-card">
            <div class="card-img" style="background-image: url('{item["image"]}')">
                <div class="card-badge">{item["price"]}</div>
            </div>
            <div class="card-info">
                <h4>{item["name"]}</h4>
                <p>{item["desc"]}</p>
            </div>
        </div>
        '''
    
    return f'''
    <section class="menu-scroll" id="menu">
        <div class="scroll-header">
            <h2>{title}</h2>
            <div class="scroll-arrows">
                <button class="arrow-btn prev">←</button>
                <button class="arrow-btn next">→</button>
            </div>
        </div>
        <div class="scroll-track">
            {items_html}
        </div>
    </section>
    
    <style>
    .menu-scroll {{ padding: 100px 0; background: {bg}; overflow: hidden; }}
    .scroll-header {{ max-width: 1200px; margin: 0 auto 50px; padding: 0 40px; display: flex; justify-content: space-between; align-items: center; }}
    .scroll-header h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: {text}; }}
    .scroll-arrows {{ display: flex; gap: 12px; }}
    .arrow-btn {{ width: 50px; height: 50px; border: 2px solid {primary}; background: transparent; border-radius: 50%; font-size: 1.2rem; cursor: pointer; transition: 0.3s; color: {primary}; }}
    .arrow-btn:hover {{ background: {primary}; color: #fff; }}
    .scroll-track {{ display: flex; gap: 30px; padding: 20px 40px; overflow-x: auto; scroll-behavior: smooth; -webkit-overflow-scrolling: touch; scrollbar-width: none; }}
    .scroll-track::-webkit-scrollbar {{ display: none; }}
    .scroll-card {{ flex: 0 0 280px; background: #fff; border-radius: 20px; overflow: hidden; transition: transform 0.3s; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
    .scroll-card:hover {{ transform: translateY(-10px); }}
    .card-img {{ height: 320px; background-size: cover; background-position: center; position: relative; }}
    .card-badge {{ position: absolute; top: 20px; right: 20px; background: #fff; padding: 8px 16px; border-radius: 50px; font-weight: 700; color: {primary}; }}
    .card-info {{ padding: 24px; }}
    .card-info h4 {{ font-family: 'Playfair Display', serif; font-size: 1.4rem; color: {text}; margin-bottom: 8px; }}
    .card-info p {{ color: #888; font-size: 0.95rem; }}
    </style>
    '''
