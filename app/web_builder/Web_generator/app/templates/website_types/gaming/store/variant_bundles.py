from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bundle Deals - Special bundle offers"""
    title = props.get("title", "Bundle Deals")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-store-bundles" id="store">
        <div class="bundles-container">
            <div class="bundles-header">
                <h2>{title}</h2>
                <p>Save more when you buy together</p>
            </div>
            <div class="bundles-grid">
                <div class="bundle-card">
                    <div class="bundle-badge">Save 40%</div>
                    <img src="https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=800" alt="Bundle">
                    <div class="bundle-content">
                        <h3>Starter Bundle</h3>
                        <div class="bundle-items">
                            <span>• Battle Pass</span>
                            <span>• 1000 Coins</span>
                            <span>• Starter Skin</span>
                        </div>
                        <div class="bundle-pricing">
                            <span class="was">$39.99</span>
                            <span class="now">$23.99</span>
                        </div>
                        <a href="#" class="btn-bundle">Get Bundle</a>
                    </div>
                </div>
                <div class="bundle-card featured">
                    <div class="bundle-badge">Save 50%</div>
                    <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=800" alt="Bundle">
                    <div class="bundle-content">
                        <h3>Pro Bundle</h3>
                        <div class="bundle-items">
                            <span>• Premium Pass</span>
                            <span>• 5000 Coins</span>
                            <span>• 10 Exclusive Skins</span>
                            <span>• VIP Badge</span>
                        </div>
                        <div class="bundle-pricing">
                            <span class="was">$99.99</span>
                            <span class="now">$49.99</span>
                        </div>
                        <a href="#" class="btn-bundle">Get Bundle</a>
                    </div>
                </div>
                <div class="bundle-card">
                    <div class="bundle-badge">Save 45%</div>
                    <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=800" alt="Bundle">
                    <div class="bundle-content">
                        <h3>Ultimate Bundle</h3>
                        <div class="bundle-items">
                            <span>• Everything in Pro</span>
                            <span>• 10000 Coins</span>
                            <span>• Lifetime VIP</span>
                        </div>
                        <div class="bundle-pricing">
                            <span class="was">$199.99</span>
                            <span class="now">$109.99</span>
                        </div>
                        <a href="#" class="btn-bundle">Get Bundle</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-store-bundles {{
        padding: 120px 24px;
        background: {background};
    }}
    .bundles-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .bundles-header {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .bundles-header h2 {{
        font-family: 'Rajdhani', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 800;
        color: {text};
        margin-bottom: 12px;
    }}
    .bundles-header p {{
        color: {secondary};
        font-size: 1.2rem;
    }}
    .bundles-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
    }}
    .bundle-card {{
        background: {text}05;
        border-radius: 24px;
        overflow: hidden;
        position: relative;
        transition: all 0.4s ease;
    }}
    .bundle-card:hover {{
        transform: translateY(-12px);
        box-shadow: 0 40px 80px {primary}20;
    }}
    .bundle-card.featured {{
        border: 2px solid {primary};
    }}
    .bundle-badge {{
        position: absolute;
        top: 20px;
        right: 20px;
        padding: 8px 20px;
        background: {primary};
        color: {background};
        font-weight: 800;
        font-size: 0.9rem;
        border-radius: 100px;
        z-index: 2;
    }}
    .bundle-card img {{
        width: 100%;
        aspect-ratio: 16/10;
        object-fit: cover;
    }}
    .bundle-content {{
        padding: 32px;
    }}
    .bundle-content h3 {{
        font-size: 1.8rem;
        font-weight: 800;
        color: {text};
        margin-bottom: 16px;
    }}
    .bundle-items {{
        display: flex;
        flex-direction: column;
        gap: 8px;
        margin-bottom: 24px;
    }}
    .bundle-items span {{
        color: {secondary};
    }}
    .bundle-pricing {{
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 24px;
    }}
    .was {{
        color: {secondary};
        text-decoration: line-through;
        font-size: 1.2rem;
    }}
    .now {{
        color: {primary};
        font-size: 2rem;
        font-weight: 900;
    }}
    .btn-bundle {{
        display: block;
        padding: 16px;
        background: {primary};
        color: {background};
        text-align: center;
        text-decoration: none;
        font-weight: 700;
        border-radius: 12px;
        transition: all 0.3s ease;
    }}
    .btn-bundle:hover {{
        transform: scale(1.02);
        box-shadow: 0 15px 40px {primary}40;
    }}
    @media (max-width: 900px) {{
        .bundles-grid {{ grid-template-columns: 1fr; max-width: 450px; margin: 0 auto; }}
    }}
    </style>
    '''
