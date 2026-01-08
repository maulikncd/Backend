from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal List Features - Clean simple list format"""
    title = props.get("sectionTitle", props.get("title", "What We Offer"))
    raw_features = props.get("featureList", props.get("features", []))
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    features = []
    for f in raw_features:
        features.append({"title": f.get("title", ""), "desc": f.get("description", f.get("desc", ""))[:60]})
    if not features:
        features = [{"title": "Specialty Coffee", "desc": "Single origin and blends"}, {"title": "Fresh Pastries", "desc": "Baked every morning"}, {"title": "Cozy Seating", "desc": "Comfortable work spaces"}, {"title": "Fast WiFi", "desc": "Stay connected"}]
    
    items_html = "".join([f'<div class="list-item"><div class="item-left"><span class="item-dot"></span><h4>{f["title"]}</h4></div><p>{f["desc"]}</p></div>' for f in features[:4]])
    
    return f'''
    <section class="features-minimal-list" id="features"><div class="minimal-container"><div class="minimal-header"><span>Features</span><h2>{title}</h2></div><div class="features-list">{items_html}</div></div></section>
    <style>
    .features-minimal-list {{ padding: 120px 40px; background: #fff; }}
    .minimal-container {{ max-width: 900px; margin: 0 auto; }}
    .minimal-header {{ margin-bottom: 60px; }}
    .minimal-header span {{ color: {primary}; text-transform: uppercase; letter-spacing: 4px; font-size: 0.85rem; }}
    .minimal-header h2 {{ font-family: 'Playfair Display', serif; font-size: 3.5rem; color: {text}; margin-top: 15px; }}
    .list-item {{ display: flex; justify-content: space-between; align-items: center; padding: 35px 0; border-bottom: 1px solid #eee; }}
    .item-left {{ display: flex; align-items: center; gap: 20px; }}
    .item-dot {{ width: 12px; height: 12px; background: {primary}; border-radius: 50%; }}
    .list-item h4 {{ font-family: 'Playfair Display', serif; font-size: 1.5rem; color: {text}; }}
    .list-item p {{ color: #888; max-width: 300px; text-align: right; }}
    @media (max-width: 768px) {{ .list-item {{ flex-direction: column; align-items: flex-start; gap: 15px; }} .list-item p {{ text-align: left; }} }}
    </style>
    '''
