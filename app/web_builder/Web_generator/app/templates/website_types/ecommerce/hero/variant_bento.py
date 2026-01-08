from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Hero - Modern bento grid"""
    title = props.get("title", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-hero-bento" id="hero">
        <div class="bento-container">
            <div class="bento-grid">
                <div class="bento-item main">
                    <div class="main-content">
                        <span class="tag">New Season</span>
                        <h1>Summer Collection 2024</h1>
                        <p>Discover our latest arrivals</p>
                        <a href="#" class="shop-btn">Shop Now</a>
                    </div>
                </div>
                <div class="bento-item promo">
                    <span class="promo-tag">50% OFF</span>
                    <h3>Flash Sale</h3>
                </div>
                <div class="bento-item stat">
                    <span class="num">1000+</span>
                    <span class="label">Products</span>
                </div>
                <div class="bento-item cat">
                    <h4>Electronics</h4>
                    <span>250+ items →</span>
                </div>
                <div class="bento-item cat">
                    <h4>Fashion</h4>
                    <span>500+ items →</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-hero-bento {{ min-height: 100vh; background: {background}; display: flex; align-items: center; padding: 80px 24px; }}
    .bento-container {{ max-width: 1200px; margin: 0 auto; width: 100%; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(2, 250px); gap: 20px; }}
    .bento-item {{ background: {text}05; border-radius: 24px; padding: 32px; }}
    .bento-item.main {{ grid-column: span 2; grid-row: span 2; background: linear-gradient(135deg, {primary}20, {primary}05); display: flex; align-items: flex-end; }}
    .bento-item.promo {{ background: {primary}; text-align: center; display: flex; flex-direction: column; justify-content: center; }}
    .tag {{ display: inline-block; padding: 8px 20px; background: {background}; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 16px; }}
    .main-content h1 {{ font-size: 2.5rem; font-weight: 900; color: {text}; margin-bottom: 12px; }}
    .main-content p {{ color: {secondary}; margin-bottom: 24px; }}
    .shop-btn {{ display: inline-block; padding: 16px 36px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 12px; }}
    .promo-tag {{ font-size: 3rem; font-weight: 900; color: {background}; }}
    .promo h3 {{ color: {background}; opacity: 0.8; }}
    .stat {{ text-align: center; display: flex; flex-direction: column; justify-content: center; }}
    .stat .num {{ font-size: 3rem; font-weight: 900; color: {primary}; }}
    .stat .label {{ color: {secondary}; }}
    .cat {{ display: flex; flex-direction: column; justify-content: flex-end; cursor: pointer; transition: all 0.3s ease; }}
    .cat:hover {{ background: {primary}15; }}
    .cat h4 {{ font-size: 1.3rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .cat span {{ color: {primary}; font-weight: 500; }}
    @media (max-width: 900px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} .bento-item.main {{ grid-column: span 2; grid-row: span 1; }} }}
    </style>
    '''
