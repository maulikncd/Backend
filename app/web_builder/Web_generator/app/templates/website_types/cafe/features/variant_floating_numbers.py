from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Floating Numbers Features - Large numbers with descriptions"""
    title = props.get("sectionTitle", props.get("title", "Our Strengths"))
    raw_features = props.get("featureList", props.get("features", []))
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    features = []
    for f in raw_features:
        features.append({"title": f.get("title", ""), "desc": f.get("description", f.get("desc", ""))[:70]})
    if not features:
        features = [{"title": "Premium Quality", "desc": "Only the finest beans make it to your cup"}, {"title": "Expert Baristas", "desc": "Years of training and passion"}, {"title": "Cozy Atmosphere", "desc": "Designed for comfort"}, {"title": "Community Focus", "desc": "A gathering place for all"}]
    
    items_html = ""
    for i, f in enumerate(features[:4]):
        items_html += f'<div class="number-card"><span class="big-num">0{i+1}</span><h4>{f["title"]}</h4><p>{f["desc"]}</p></div>'
    
    return f'''
    <section class="features-numbers" id="features"><div class="numbers-container"><h2>{title}</h2><div class="numbers-grid">{items_html}</div></div></section>
    <style>
    .features-numbers {{ padding: 100px 24px; background: #0D0D0D; color: #fff; }}
    .numbers-container {{ max-width: 1200px; margin: 0 auto; text-align: center; }}
    .features-numbers h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; margin-bottom: 70px; }}
    .numbers-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; text-align: left; }}
    .number-card {{ padding: 30px 0; border-top: 1px solid {primary}50; }}
    .big-num {{ font-size: 5rem; font-weight: 800; color: {primary}30; line-height: 1; display: block; margin-bottom: 20px; }}
    .number-card h4 {{ font-family: 'Playfair Display', serif; font-size: 1.4rem; margin-bottom: 12px; }}
    .number-card p {{ color: rgba(255,255,255,0.6); line-height: 1.6; }}
    @media (max-width: 900px) {{ .numbers-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
