from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Bento Grid Features - Modern, grid-based layout for showcasing distinct features.
    Very popular in tech and SaaS but adapted for premium e-commerce.
    """
    features = props.get("features", [])
    # Ensure enough items for bento
    if not features or len(features) < 4:
        features = [
            {"title": "Global Shipping", "desc": "We ship to over 150 countries worldwide.", "icon": "🌍"},
            {"title": "Artisan Crafted", "desc": "Handmade by master craftsmen in Italy.", "icon": "✋"},
            {"title": "Sustainable", "desc": "100% recycled packaging.", "icon": "♻️"},
            {"title": "24/7 Support", "desc": "Concierge service anytime.", "icon": "🎧"},
        ]
        
    bg = colors.get("background", "#F5F5F7")
    text = colors.get("text", "#1D1D1F")
    
    return f'''
    <section class="bento-features" id="features">
        <div class="container">
            <div class="bento-header">
                <h2>Why Choose Us</h2>
                <p>Excellence in every detail.</p>
            </div>
            
            <div class="bento-grid">
                <div class="bento-item large">
                    <div class="bento-content">
                        <span class="bento-icon">{features[0].get("icon")}</span>
                        <h3>{features[0].get("title")}</h3>
                        <p>{features[0].get("desc")}</p>
                    </div>
                    <div class="bento-bg" style="background-image: url('https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=500');"></div>
                </div>
                
                <div class="bento-item">
                    <div class="bento-content">
                        <span class="bento-icon">{features[1].get("icon")}</span>
                        <h3>{features[1].get("title")}</h3>
                        <p>{features[1].get("desc")}</p>
                    </div>
                </div>
                
                <div class="bento-item">
                    <div class="bento-content">
                        <span class="bento-icon">{features[2].get("icon")}</span>
                        <h3>{features[2].get("title")}</h3>
                        <p>{features[2].get("desc")}</p>
                    </div>
                </div>
                
                <div class="bento-item wide">
                    <div class="bento-content">
                        <span class="bento-icon">{features[3].get("icon")}</span>
                        <h3>{features[3].get("title")}</h3>
                        <p>{features[3].get("desc")}</p>
                    </div>
                     <div class="bento-bg" style="background: linear-gradient(45deg, #111, #333);"></div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .bento-features {{
        padding: 100px 0;
        background: {bg};
        color: {text};
    }}
    
    .bento-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    
    .bento-header h2 {{
        font-size: 3rem;
        font-weight: 700;
        letter-spacing: -1px;
    }}
    
    .bento-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-auto-rows: 250px;
        gap: 24px;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }}
    
    .bento-item {{
        background: white;
        border-radius: 24px;
        padding: 30px;
        position: relative;
        overflow: hidden;
        transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }}
    
    .bento-item:hover {{
        transform: scale(1.02);
        box-shadow: 0 20px 30px rgba(0,0,0,0.1);
        z-index: 2;
    }}
    
    .bento-item.large {{
        grid-column: span 2;
        grid-row: span 2;
        color: white;
    }}
    
    .bento-item.wide {{
        grid-column: span 2;
        color: white;
    }}
    
    .bento-content {{
        position: relative;
        z-index: 2;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    
    .bento-icon {{
        font-size: 2.5rem;
        margin-bottom: 10px;
    }}
    
    .bento-item h3 {{
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 8px;
    }}
    
    .bento-item p {{
        font-size: 1rem;
        opacity: 0.8;
    }}
    
    .bento-bg {{
        position: absolute;
        inset: 0;
        background-size: cover;
        background-position: center;
        z-index: 1;
        transition: transform 0.5s;
    }}
    
    .bento-item.large .bento-bg::after {{
        content: '';
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.4);
    }}
    
    .bento-item:hover .bento-bg {{
        transform: scale(1.1);
    }}
    
    @media (max-width: 1024px) {{
        .bento-grid {{ grid-template-columns: 1fr; grid-auto-rows: auto; }}
        .bento-item.large, .bento-item.wide {{ grid-column: span 1; grid-row: span 1; min-height: 250px; }}
    }}
    </style>
    '''
