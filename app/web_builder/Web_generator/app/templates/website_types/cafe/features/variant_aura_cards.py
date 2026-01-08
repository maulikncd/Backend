from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium Features - Icon cards with elegant hover effects
    """
    title = props.get("sectionTitle", props.get("title", "Why Choose Us"))
    subtitle = props.get("sectionSubtitle", props.get("subtitle", "What makes us special"))
    
    raw_features = props.get("featureList", props.get("features", []))
    
    features = []
    for f in raw_features:
        features.append({
            "title": f.get("title", "Feature"),
            "desc": f.get("description", f.get("desc", "")),
            "icon": f.get("icon", "✨")
        })
    
    if not features:
        features = [
            {"icon": "☕", "title": "Premium Beans", "desc": "100% arabica beans sourced from the world's finest coffee regions"},
            {"icon": "🥐", "title": "Fresh Baked", "desc": "Our pastries are baked fresh every morning in our artisan kitchen"},
            {"icon": "🌿", "title": "Organic & Local", "desc": "We partner with local farmers for the freshest organic ingredients"},
            {"icon": "💝", "title": "Made with Love", "desc": "Every cup and dish is crafted with passion and attention to detail"}
        ]
    
    primary = colors.get("primary", "#8B7355")
    bg = colors.get("background", "#FAF7F4")
    text = colors.get("text", "#2D2013")
    
    features_html = ""
    for i, f in enumerate(features[:4]):
        desc_short = f["desc"][:100] + "..." if len(f["desc"]) > 100 else f["desc"]
        features_html += f'''
        <div class="feature-card animate-on-scroll" style="--delay: {i * 0.1}s">
            <div class="feature-icon-wrap">
                <span class="feature-icon">{f["icon"]}</span>
            </div>
            <h4 class="feature-title">{f["title"]}</h4>
            <p class="feature-desc">{desc_short}</p>
            <div class="feature-line"></div>
        </div>
        '''
    
    return f'''
    <section class="aura-features" id="features">
        <div class="features-container">
            <div class="features-header">
                <span class="section-badge">Features</span>
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
            </div>
            <div class="features-grid">
                {features_html}
            </div>
        </div>
    </section>
    
    <style>
    .aura-features {{
        padding: 120px 24px;
        background: {bg};
    }}
    .features-container {{ max-width: 1200px; margin: 0 auto; }}
    .features-header {{ text-align: center; margin-bottom: 70px; }}
    .aura-features .section-badge {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}15;
        color: {primary};
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 20px;
    }}
    .aura-features .section-title {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2.5rem, 4vw, 3.5rem);
        color: {text};
        margin-bottom: 16px;
    }}
    .aura-features .section-subtitle {{
        color: #888;
        font-size: 1.1rem;
        max-width: 500px;
        margin: 0 auto;
    }}
    .features-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 30px;
    }}
    .feature-card {{
        background: #fff;
        padding: 40px 30px;
        border-radius: 20px;
        text-align: center;
        transition: all 0.4s;
        animation: fadeInUp 0.6s var(--delay) both;
        position: relative;
        overflow: hidden;
    }}
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    .feature-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 30px 60px rgba(0,0,0,0.08);
    }}
    .feature-icon-wrap {{
        width: 80px;
        height: 80px;
        background: {primary}15;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 24px;
        transition: all 0.3s;
    }}
    .feature-card:hover .feature-icon-wrap {{
        background: {primary};
        transform: scale(1.1);
    }}
    .feature-icon {{ font-size: 2.5rem; transition: filter 0.3s; }}
    .feature-card:hover .feature-icon {{ filter: brightness(100); }}
    .feature-title {{
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        color: {text};
        margin-bottom: 14px;
    }}
    .feature-desc {{
        color: #888;
        font-size: 0.95rem;
        line-height: 1.7;
    }}
    .feature-line {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 3px;
        background: {primary};
        transition: width 0.4s;
    }}
    .feature-card:hover .feature-line {{ width: 100%; }}
    @media (max-width: 1024px) {{
        .features-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
        .features-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
