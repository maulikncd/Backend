from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Skin Gallery - Character skins showcase"""
    title = props.get("title", "Skin Gallery")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    skins = [
        {"name": "Shadow Warrior", "rarity": "Legendary", "price": "$24.99", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400"},
        {"name": "Neon Hunter", "rarity": "Epic", "price": "$14.99", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400"},
        {"name": "Cyber Ghost", "rarity": "Legendary", "price": "$24.99", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400"},
        {"name": "Frost Knight", "rarity": "Epic", "price": "$14.99", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=400"},
    ]
    
    cards_html = ""
    for s in skins:
        rarity_class = "legendary" if s["rarity"] == "Legendary" else "epic"
        cards_html += f'''
        <div class="skin-card {rarity_class}">
            <div class="skin-rarity">{s['rarity']}</div>
            <div class="skin-image"><img src="{s['img']}" alt="{s['name']}"></div>
            <div class="skin-info">
                <h3>{s['name']}</h3>
                <span class="skin-price">{s['price']}</span>
                <button class="buy-skin">Add to Cart</button>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-store-skins" id="store">
        <div class="skins-container">
            <div class="skins-header">
                <h2>{title}</h2>
                <div class="rarity-filter">
                    <button class="filter active">All</button>
                    <button class="filter">Legendary</button>
                    <button class="filter">Epic</button>
                    <button class="filter">Rare</button>
                </div>
            </div>
            <div class="skins-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-store-skins {{ padding: 120px 24px; background: {background}; }}
    .skins-container {{ max-width: 1200px; margin: 0 auto; }}
    .skins-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 48px; flex-wrap: wrap; gap: 24px; }}
    .skins-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .rarity-filter {{ display: flex; gap: 8px; }}
    .filter {{ padding: 10px 24px; background: {text}08; border: none; color: {secondary}; font-weight: 600; border-radius: 100px; cursor: pointer; transition: all 0.3s ease; }}
    .filter.active, .filter:hover {{ background: {primary}; color: {background}; }}
    .skins-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .skin-card {{ background: {text}05; border-radius: 20px; overflow: hidden; transition: all 0.4s ease; position: relative; }}
    .skin-card:hover {{ transform: translateY(-8px); }}
    .skin-card.legendary {{ border: 2px solid #ffd700; }}
    .skin-card.epic {{ border: 2px solid #a855f7; }}
    .skin-rarity {{ position: absolute; top: 16px; left: 16px; padding: 6px 14px; font-size: 0.75rem; font-weight: 700; border-radius: 100px; z-index: 2; }}
    .skin-card.legendary .skin-rarity {{ background: #ffd700; color: #000; }}
    .skin-card.epic .skin-rarity {{ background: #a855f7; color: #fff; }}
    .skin-image {{ aspect-ratio: 3/4; }}
    .skin-image img {{ width: 100%; height: 100%; object-fit: cover; }}
    .skin-info {{ padding: 20px; }}
    .skin-info h3 {{ font-size: 1.1rem; font-weight: 700; color: {text}; margin-bottom: 8px; }}
    .skin-price {{ display: block; font-size: 1.3rem; font-weight: 900; color: {primary}; margin-bottom: 16px; }}
    .buy-skin {{ width: 100%; padding: 12px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 10px; cursor: pointer; transition: all 0.3s ease; }}
    .buy-skin:hover {{ transform: scale(1.02); }}
    @media (max-width: 900px) {{ .skins-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
