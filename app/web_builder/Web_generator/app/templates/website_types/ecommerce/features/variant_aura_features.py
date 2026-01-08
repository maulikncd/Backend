from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium Features - sophisticated grid with hover-reveal details
    and premium iconography.
    """
    features = props.get("features", [])
    if not features:
        features = [
            {"title": "Global Shipping", "desc": "Complimentary delivery to 150+ countries.", "icon": "✈️"},
            {"title": "Lifetime Warranty", "desc": "Protection for your investment, forever.", "icon": "🛡️"},
            {"title": "Personal Concierge", "desc": "24/7 Styling advice and order support.", "icon": "💎"},
        ]
        
    primary = colors.get("primary", "#D4AF37")
    bg = colors.get("background", "#0F0F0F") # Dark
    text = colors.get("text", "#FFFFFF")
    
    feature_html = ""
    for idx, feat in enumerate(features):
        feature_html += f'''
        <div class="aura-feature-card">
            <div class="feature-icon-wrapper">
                <span class="feature-icon">{feat.get("icon")}</span>
                <div class="icon-glow"></div>
            </div>
            <h3 class="feature-title">{feat.get("title")}</h3>
            <p class="feature-desc">{feat.get("desc")}</p>
            <div class="card-border"></div>
        </div>
        '''

    return f'''
    <section class="aura-features" id="features">
        <div class="container">
            <div class="features-wrapper">
                {feature_html}
            </div>
        </div>
    </section>
    
    <style>
    .aura-features {{
        padding: 80px 0;
        background-color: {bg};
        position: relative;
    }}
    
    .features-wrapper {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
    }}
    
    .aura-feature-card {{
        background: radial-gradient(circle at top right, rgba(255,255,255,0.05), rgba(255,255,255,0.01));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.05);
        padding: 40px 30px;
        border-radius: 20px;
        position: relative;
        overflow: hidden;
        transition: transform 0.3s;
        text-align: center;
    }}
    
    .aura-feature-card:hover {{
        transform: translateY(-5px);
        border-color: rgba(255,255,255,0.1);
    }}
    
    .feature-icon-wrapper {{
        position: relative;
        width: 80px;
        height: 80px;
        margin: 0 auto 24px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: rgba(255,255,255,0.03);
    }}
    
    .feature-icon {{
        font-size: 2.5rem;
        position: relative;
        z-index: 2;
    }}
    
    .icon-glow {{
        position: absolute;
        inset: 0;
        background: {primary};
        filter: blur(20px);
        opacity: 0;
        transition: opacity 0.4s;
        border-radius: 50%;
    }}
    
    .aura-feature-card:hover .icon-glow {{
        opacity: 0.2;
    }}
    
    .feature-title {{
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: {text};
        margin-bottom: 12px;
    }}
    
    .feature-desc {{
        color: rgba(255,255,255,0.6);
        line-height: 1.6;
        font-size: 0.95rem;
    }}
    
    .card-border {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, transparent, {primary}, transparent);
        transform: scaleX(0);
        transition: transform 0.5s;
    }}
    
    .aura-feature-card:hover .card-border {{
        transform: scaleX(1);
    }}
    </style>
    '''
