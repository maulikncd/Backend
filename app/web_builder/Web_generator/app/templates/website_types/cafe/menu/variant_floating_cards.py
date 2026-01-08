from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Floating Cards Menu - 3D hover effect cards with shadows"""
    title = props.get("sectionTitle", props.get("title", "Menu Highlights"))
    raw_items = props.get("items", [])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    bg = colors.get("background", "#F5F5F0")
    
    items = []
    for item in raw_items:
        items.append({
            "name": item.get("name", "Item"),
            "desc": item.get("description", "")[:70],
            "price": item.get("price", "$0"),
            "image": f"https://source.unsplash.com/200x200/?{item.get('name', 'coffee').replace(' ', ',')}"
        })
    
    if not items:
        items = [
            {"name": "Espresso", "desc": "Double shot perfection", "price": "$3.50", "image": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=200"},
            {"name": "Latte Art", "desc": "Instagram worthy", "price": "$5.50", "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=200"},
            {"name": "Croissant", "desc": "Butter layers of joy", "price": "$4.00", "image": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=200"}
        ]
    
    items_html = ""
    for item in items[:9]:
        items_html += f'''
        <div class="float-card">
            <div class="card-head">
                <img src="{item['image']}" alt="{item['name']}">
            </div>
            <div class="card-body">
                <h4>{item["name"]}</h4>
                <p>{item["desc"]}</p>
                <div class="card-footer">
                    <span class="card-price">{item["price"]}</span>
                    <button class="add-btn">+</button>
                </div>
            </div>
        </div>
        '''
    
    return f'''
    <section class="menu-floating" id="menu">
        <div class="floating-container">
            <h2>{title}</h2>
            <div class="floating-grid">
                {items_html}
            </div>
        </div>
    </section>
    
    <style>
    .menu-floating {{ padding: 120px 24px; background: {bg}; }}
    .floating-container {{ max-width: 1200px; margin: 0 auto; text-align: center; }}
    .floating-container h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: {text}; margin-bottom: 60px; }}
    .floating-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 30px; }}
    .float-card {{ background: #fff; border-radius: 24px; overflow: hidden; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); box-shadow: 0 10px 40px rgba(0,0,0,0.05); }}
    .float-card:hover {{ transform: translateY(-15px) scale(1.02); box-shadow: 0 30px 60px rgba(0,0,0,0.12); }}
    .card-head {{ height: 180px; overflow: hidden; }}
    .card-head img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }}
    .float-card:hover .card-head img {{ transform: scale(1.1); }}
    .card-body {{ padding: 24px; text-align: left; }}
    .card-body h4 {{ font-family: 'Playfair Display', serif; font-size: 1.4rem; color: {text}; margin-bottom: 10px; }}
    .card-body p {{ color: #888; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; }}
    .card-footer {{ display: flex; justify-content: space-between; align-items: center; }}
    .card-price {{ font-size: 1.3rem; font-weight: 700; color: {primary}; }}
    .add-btn {{ width: 40px; height: 40px; border-radius: 50%; border: none; background: {primary}; color: #fff; font-size: 1.5rem; cursor: pointer; transition: 0.3s; }}
    .add-btn:hover {{ transform: rotate(90deg); background: {text}; }}
    </style>
    '''
