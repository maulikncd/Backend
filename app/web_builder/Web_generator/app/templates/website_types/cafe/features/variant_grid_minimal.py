from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    # Support blueprint keys
    title = props.get("sectionTitle", props.get("title", "Why Choose Us"))
    subtitle = props.get("sectionSubtitle", "")
    
    # Blueprint uses 'featureList' key
    raw_features = props.get("featureList", props.get("features", []))
    
    # Transform features to expected format
    features = []
    for f in raw_features:
        features.append({
            "title": f.get("title", "Feature"),
            "desc": f.get("description", f.get("desc", "")),
            "icon": f.get("icon", "✨")
        })
    
    # Fallback if no features provided
    if not features:
        features = [
            {"title": "Organic Beans", "desc": "100% fair trade organic coffee sourced from ethical farmers.", "icon": "🌱"},
            {"title": "Artisan Baked", "desc": "Fresh pastries baked daily in our own kitchen.", "icon": "🥐"},
            {"title": "Free WiFi", "desc": "High-speed internet for all your remote work needs.", "icon": "📶"}
        ]
    
    features_html = ""
    for f in features:
        desc_short = f["desc"][:100] + "..." if len(f["desc"]) > 100 else f["desc"]
        features_html += f'''
        <div class="feature-card animate-on-scroll">
            <span class="feature-icon">{f["icon"]}</span>
            <h4 class="feature-title">{f["title"]}</h4>
            <p class="feature-desc">{desc_short}</p>
        </div>
        '''
    
    return f'''
    <section class="cafe-features-grid" id="features">
        <div class="features-container">
            <h2 class="section-title">{title}</h2>
            {f'<p class="section-subtitle">{subtitle}</p>' if subtitle else ''}
            <div class="features-grid">
                {features_html}
            </div>
        </div>
    </section>
    
    <style>
    .cafe-features-grid {{ padding: 100px 24px; background: #fff; }}
    .features-container {{ max-width: 1200px; margin: 0 auto; text-align: center; }}
    .section-title {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 20px; color: {colors.get("text", "#2D2013")}; }}
    .section-subtitle {{ color: {colors.get("text_muted", "#888")}; font-size: 1.1rem; margin-bottom: 60px; max-width: 600px; margin-left: auto; margin-right: auto; }}
    .features-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 40px; }}
    .feature-card {{ padding: 40px; border-radius: 20px; background: {colors.get("background", "#FFF8F0")}; transition: all 0.3s; }}
    .feature-card:hover {{ transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.08); }}
    .feature-icon {{ font-size: 3rem; margin-bottom: 24px; display: block; }}
    .feature-title {{ font-family: 'Playfair Display', serif; font-size: 1.4rem; margin-bottom: 16px; color: {colors.get("text", "#2D2013")}; }}
    .feature-desc {{ color: {colors.get("text_muted", "#8B7355")}; line-height: 1.7; font-size: 1rem; }}
    </style>
    '''
