from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Grid Features - Modern bento box layout"""
    title = props.get("sectionTitle", "")
    raw_features = props.get("featureList", props.get("features", []))
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    features = []
    for f in raw_features:
        features.append({"title": f.get("title", ""), "desc": f.get("description", f.get("desc", ""))[:60], "icon": f.get("icon", "✨")})
    if not features:
        features = [{"icon": "☕", "title": "Specialty Coffee", "desc": "Expertly crafted drinks"}, {"icon": "🥐", "title": "Fresh Bakes", "desc": "Made in-house daily"}, {"icon": "🌿", "title": "Organic", "desc": "Sustainable sourcing"}, {"icon": "📶", "title": "Free WiFi", "desc": "Work comfortably"}, {"icon": "🎵", "title": "Vibes", "desc": "Curated playlists"}]
    
    return f'''
    <section class="features-bento" id="features">
        <div class="bento-grid">
            <div class="bento-item large" style="background-image: url('https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800')"><div class="bento-overlay"></div><div class="bento-text"><span>{features[0]["icon"]}</span><h4>{features[0]["title"]}</h4></div></div>
            <div class="bento-item"><span>{features[1]["icon"]}</span><h4>{features[1]["title"]}</h4><p>{features[1]["desc"]}</p></div>
            <div class="bento-item accent"><span>{features[2]["icon"]}</span><h4>{features[2]["title"]}</h4><p>{features[2]["desc"]}</p></div>
            <div class="bento-item"><span>{features[3]["icon"]}</span><h4>{features[3]["title"]}</h4><p>{features[3]["desc"]}</p></div>
            <div class="bento-item wide" style="background-image: url('https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=800')"><div class="bento-overlay"></div><div class="bento-text"><span>{features[4]["icon"] if len(features) > 4 else "🎵"}</span><h4>{features[4]["title"] if len(features) > 4 else "Great Atmosphere"}</h4></div></div>
        </div>
    </section>
    <style>
    .features-bento {{ padding: 60px 24px; background: #FAF7F4; }}
    .bento-grid {{ max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(2, 250px); gap: 20px; }}
    .bento-item {{ background: #fff; border-radius: 24px; padding: 30px; display: flex; flex-direction: column; justify-content: flex-end; position: relative; overflow: hidden; }}
    .bento-item.large {{ grid-column: span 2; background-size: cover; background-position: center; color: #fff; }}
    .bento-item.wide {{ grid-column: span 2; background-size: cover; background-position: center; color: #fff; }}
    .bento-item.accent {{ background: {primary}; color: #fff; }}
    .bento-overlay {{ position: absolute; inset: 0; background: rgba(0,0,0,0.4); }}
    .bento-text {{ position: relative; z-index: 1; }}
    .bento-item span {{ font-size: 2.5rem; margin-bottom: 15px; display: block; }}
    .bento-item h4 {{ font-family: 'Playfair Display', serif; font-size: 1.5rem; margin-bottom: 8px; }}
    .bento-item p {{ font-size: 0.9rem; opacity: 0.8; }}
    @media (max-width: 900px) {{ .bento-grid {{ grid-template-columns: repeat(2, 1fr); }} .bento-item.large, .bento-item.wide {{ grid-column: span 2; }} }}
    </style>
    '''
