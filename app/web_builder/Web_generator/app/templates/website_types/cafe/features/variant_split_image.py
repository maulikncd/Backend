from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Image Features - Image on side with feature list"""
    title = props.get("sectionTitle", props.get("title", "What We Offer"))
    raw_features = props.get("featureList", props.get("features", []))
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    features = []
    for f in raw_features:
        features.append({"title": f.get("title", ""), "desc": f.get("description", f.get("desc", ""))[:80], "icon": f.get("icon", "✓")})
    if not features:
        features = [{"icon": "✓", "title": "Organic Coffee", "desc": "Certified organic beans"}, {"icon": "✓", "title": "Fresh Pastries", "desc": "Baked daily"}, {"icon": "✓", "title": "Cozy Space", "desc": "Perfect for work or relaxation"}, {"icon": "✓", "title": "Free WiFi", "desc": "High-speed connection"}]
    
    items_html = "".join([f'<div class="feat-row"><span class="feat-check">{f["icon"]}</span><div><h4>{f["title"]}</h4><p>{f["desc"]}</p></div></div>' for f in features[:4]])
    
    return f'''
    <section class="features-split-img" id="features"><div class="split-grid"><div class="split-image" style="background-image: url('https://images.unsplash.com/photo-1493857671505-72967e2e2760?w=800')"></div><div class="split-features"><h2>{title}</h2><div class="features-list">{items_html}</div></div></div></section>
    <style>
    .features-split-img {{ min-height: 100vh; display: flex; }}
    .split-grid {{ display: grid; grid-template-columns: 1fr 1fr; width: 100%; }}
    .split-image {{ background-size: cover; background-position: center; }}
    .split-features {{ padding: 80px 60px; display: flex; flex-direction: column; justify-content: center; background: #fff; }}
    .split-features h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: {text}; margin-bottom: 50px; }}
    .feat-row {{ display: flex; gap: 20px; margin-bottom: 35px; align-items: flex-start; }}
    .feat-check {{ width: 45px; height: 45px; background: {primary}; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; flex-shrink: 0; }}
    .feat-row h4 {{ font-family: 'Playfair Display', serif; font-size: 1.3rem; color: {text}; margin-bottom: 6px; }}
    .feat-row p {{ color: #888; font-size: 0.95rem; }}
    @media (max-width: 900px) {{ .split-grid {{ grid-template-columns: 1fr; }} .split-image {{ height: 400px; }} }}
    </style>
    '''
