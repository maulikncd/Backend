from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Timeline Features - Vertical timeline layout"""
    title = props.get("sectionTitle", props.get("title", "Our Process"))
    raw_features = props.get("featureList", props.get("features", []))
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    features = []
    for f in raw_features:
        features.append({"title": f.get("title", ""), "desc": f.get("description", f.get("desc", ""))[:100], "icon": f.get("icon", "✨")})
    if not features:
        features = [{"icon": "🌱", "title": "Source", "desc": "We partner with sustainable farms globally"}, {"icon": "🔥", "title": "Roast", "desc": "Small batch roasting for peak flavor"}, {"icon": "☕", "title": "Brew", "desc": "Precision brewing techniques"}, {"icon": "❤️", "title": "Serve", "desc": "Delivered with care and passion"}]
    
    items_html = ""
    for i, f in enumerate(features[:4]):
        side = "left" if i % 2 == 0 else "right"
        items_html += f'<div class="timeline-item {side}"><div class="timeline-dot"><span>{f["icon"]}</span></div><div class="timeline-content"><h4>{f["title"]}</h4><p>{f["desc"]}</p></div></div>'
    
    return f'''
    <section class="features-timeline" id="features"><div class="timeline-container"><h2>{title}</h2><div class="timeline-track">{items_html}</div></div></section>
    <style>
    .features-timeline {{ padding: 100px 24px; background: #FAF7F4; }}
    .timeline-container {{ max-width: 900px; margin: 0 auto; text-align: center; }}
    .features-timeline h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: {text}; margin-bottom: 80px; }}
    .timeline-track {{ position: relative; }}
    .timeline-track::before {{ content: ''; position: absolute; left: 50%; top: 0; bottom: 0; width: 2px; background: {primary}30; transform: translateX(-50%); }}
    .timeline-item {{ display: flex; align-items: center; margin-bottom: 60px; }}
    .timeline-item.left {{ flex-direction: row; }} .timeline-item.right {{ flex-direction: row-reverse; }}
    .timeline-content {{ flex: 1; text-align: left; padding: 30px; background: #fff; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
    .timeline-item.right .timeline-content {{ text-align: right; }}
    .timeline-dot {{ width: 70px; height: 70px; background: {primary}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; margin: 0 30px; z-index: 1; }}
    .timeline-content h4 {{ font-family: 'Playfair Display', serif; font-size: 1.5rem; color: {text}; margin-bottom: 10px; }}
    .timeline-content p {{ color: #888; line-height: 1.6; }}
    @media (max-width: 768px) {{ .timeline-item, .timeline-item.right {{ flex-direction: column; }} .timeline-track::before {{ left: 35px; }} }}
    </style>
    '''
