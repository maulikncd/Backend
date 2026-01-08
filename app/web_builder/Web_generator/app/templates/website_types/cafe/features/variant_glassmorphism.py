from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Glassmorphism Features - Frosted glass effect cards"""
    title = props.get("sectionTitle", props.get("title", "What Makes Us Special"))
    raw_features = props.get("featureList", props.get("features", []))
    primary = colors.get("primary", "#8B7355")
    
    features = []
    for f in raw_features:
        features.append({"title": f.get("title", ""), "desc": f.get("description", f.get("desc", ""))[:70], "icon": f.get("icon", "✨")})
    if not features:
        features = [{"icon": "☕", "title": "Artisan Coffee", "desc": "Hand-crafted with precision"}, {"icon": "🌱", "title": "Farm Fresh", "desc": "Direct trade partnerships"}, {"icon": "❤️", "title": "Made with Love", "desc": "Every cup tells a story"}, {"icon": "🏆", "title": "Award Winning", "desc": "Recognized excellence"}]
    
    items_html = "".join([f'<div class="glass-card"><span class="glass-icon">{f["icon"]}</span><h4>{f["title"]}</h4><p>{f["desc"]}</p></div>' for f in features[:4]])
    
    return f'''
    <section class="features-glass" id="features" style="background-image: url('https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1920')">
        <div class="glass-overlay"></div>
        <div class="glass-container"><h2>{title}</h2><div class="glass-grid">{items_html}</div></div>
    </section>
    <style>
    .features-glass {{ min-height: 100vh; background-size: cover; background-position: center; background-attachment: fixed; position: relative; display: flex; align-items: center; }}
    .glass-overlay {{ position: absolute; inset: 0; background: rgba(0,0,0,0.5); }}
    .glass-container {{ position: relative; z-index: 1; max-width: 1200px; margin: 0 auto; padding: 60px 24px; text-align: center; color: #fff; }}
    .features-glass h2 {{ font-family: 'Playfair Display', serif; font-size: 3.5rem; margin-bottom: 60px; }}
    .glass-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 25px; }}
    .glass-card {{ background: rgba(255,255,255,0.1); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.2); border-radius: 24px; padding: 40px 25px; transition: 0.3s; }}
    .glass-card:hover {{ background: rgba(255,255,255,0.2); transform: translateY(-10px); }}
    .glass-icon {{ font-size: 3rem; display: block; margin-bottom: 20px; }}
    .glass-card h4 {{ font-family: 'Playfair Display', serif; font-size: 1.4rem; margin-bottom: 12px; }}
    .glass-card p {{ font-size: 0.95rem; opacity: 0.8; line-height: 1.5; }}
    @media (max-width: 900px) {{ .glass-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
