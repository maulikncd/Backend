from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Scroll Features - Side-scrolling feature cards"""
    title = props.get("sectionTitle", props.get("title", "Experience"))
    raw_features = props.get("featureList", props.get("features", []))
    primary = colors.get("primary", "#8B7355")
    
    features = []
    for f in raw_features:
        features.append({"title": f.get("title", ""), "desc": f.get("description", f.get("desc", ""))[:80], "icon": f.get("icon", "✨")})
    if not features:
        features = [{"icon": "☕", "title": "Premium Beans", "desc": "Sourced from top farms"}, {"icon": "🥐", "title": "Fresh Daily", "desc": "Baked every morning"}, {"icon": "🌿", "title": "Organic", "desc": "Sustainable practices"}, {"icon": "❤️", "title": "With Love", "desc": "Crafted with care"}]
    
    items_html = "".join([f'<div class="hscroll-card"><span class="card-icon">{f["icon"]}</span><h4>{f["title"]}</h4><p>{f["desc"]}</p></div>' for f in features[:6]])
    
    return f'''
    <section class="features-hscroll" id="features"><div class="hscroll-header"><h2>{title}</h2><span>Scroll →</span></div><div class="hscroll-track">{items_html}</div></section>
    <style>
    .features-hscroll {{ padding: 80px 0; background: #fff; overflow: hidden; }}
    .hscroll-header {{ max-width: 1200px; margin: 0 auto 40px; padding: 0 40px; display: flex; justify-content: space-between; align-items: center; }}
    .hscroll-header h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; }}
    .hscroll-header span {{ color: {primary}; }}
    .hscroll-track {{ display: flex; gap: 30px; padding: 20px 40px; overflow-x: auto; scroll-behavior: smooth; scrollbar-width: none; }}
    .hscroll-track::-webkit-scrollbar {{ display: none; }}
    .hscroll-card {{ flex: 0 0 320px; padding: 50px 40px; background: #FAF7F4; border-radius: 24px; transition: 0.3s; }}
    .hscroll-card:hover {{ transform: translateY(-10px); background: {primary}; color: #fff; }}
    .card-icon {{ font-size: 3rem; display: block; margin-bottom: 25px; }}
    .hscroll-card h4 {{ font-family: 'Playfair Display', serif; font-size: 1.5rem; margin-bottom: 12px; }}
    .hscroll-card p {{ opacity: 0.8; line-height: 1.6; }}
    </style>
    '''
