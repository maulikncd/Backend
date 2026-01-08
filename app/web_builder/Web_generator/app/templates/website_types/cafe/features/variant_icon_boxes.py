from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Icon Boxes Features - Boxed icons with descriptions"""
    title = props.get("sectionTitle", props.get("title", "Why Us"))
    raw_features = props.get("featureList", props.get("features", []))
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    features = []
    for f in raw_features:
        features.append({"title": f.get("title", ""), "desc": f.get("description", f.get("desc", ""))[:80], "icon": f.get("icon", "✨")})
    if not features:
        features = [{"icon": "☕", "title": "Premium Beans", "desc": "Sourced from the finest farms"}, {"icon": "🥐", "title": "Fresh Baked", "desc": "Made daily in-house"}, {"icon": "💚", "title": "Sustainable", "desc": "Eco-friendly practices"}, {"icon": "🎯", "title": "Perfection", "desc": "Crafted with precision"}]
    
    items_html = "".join([f'<div class="icon-box"><span class="box-icon">{f["icon"]}</span><h4>{f["title"]}</h4><p>{f["desc"]}</p></div>' for f in features[:4]])
    
    return f'''
    <section class="features-iconbox" id="features"><div class="iconbox-container"><h2>{title}</h2><div class="iconbox-grid">{items_html}</div></div></section>
    <style>
    .features-iconbox {{ padding: 100px 24px; background: #fff; }}
    .iconbox-container {{ max-width: 1100px; margin: 0 auto; text-align: center; }}
    .features-iconbox h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: {text}; margin-bottom: 60px; }}
    .iconbox-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; }}
    .icon-box {{ padding: 40px 30px; background: #FAF7F4; border-radius: 20px; transition: 0.3s; }}
    .icon-box:hover {{ transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.08); }}
    .box-icon {{ font-size: 3rem; display: block; margin-bottom: 20px; }}
    .icon-box h4 {{ font-family: 'Playfair Display', serif; font-size: 1.3rem; margin-bottom: 12px; color: {text}; }}
    .icon-box p {{ color: #888; font-size: 0.95rem; line-height: 1.6; }}
    @media (max-width: 900px) {{ .iconbox-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
