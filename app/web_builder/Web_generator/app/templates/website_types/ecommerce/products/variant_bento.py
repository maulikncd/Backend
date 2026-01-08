from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Products - Bento grid layout"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-products-bento" id="products">
        <div class="bento-container">
            <div class="section-header"><h2>Trending Now</h2></div>
            <div class="bento-grid">
                <div class="bento-item main">
                    <span class="badge">Bestseller</span>
                    <div class="item-footer"><h3>Premium Headphones</h3><span class="price">$299</span></div>
                </div>
                <div class="bento-item"><div class="item-footer"><h4>Smart Watch</h4><span>$449</span></div></div>
                <div class="bento-item"><div class="item-footer"><h4>Wireless Speaker</h4><span>$199</span></div></div>
                <div class="bento-item wide"><div class="item-footer"><h4>Laptop Stand + Mouse Bundle</h4><span>$149</span></div></div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-products-bento {{ padding: 120px 24px; background: {background}; }}
    .bento-container {{ max-width: 1200px; margin: 0 auto; }}
    .section-header {{ margin-bottom: 48px; }}
    .section-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, 300px); gap: 20px; }}
    .bento-item {{ background: linear-gradient(135deg, {primary}20, {primary}05); border-radius: 24px; position: relative; overflow: hidden; padding: 24px; display: flex; flex-direction: column; justify-content: flex-end; cursor: pointer; transition: all 0.4s ease; }}
    .bento-item:hover {{ transform: scale(1.02); }}
    .bento-item.main {{ grid-column: span 2; grid-row: span 2; }}
    .bento-item.wide {{ grid-column: span 2; }}
    .badge {{ position: absolute; top: 20px; left: 20px; padding: 8px 18px; background: {primary}; color: {background}; font-weight: 700; font-size: 0.85rem; border-radius: 100px; }}
    .item-footer {{ background: {background}E6; backdrop-filter: blur(10px); border-radius: 16px; padding: 20px; }}
    .item-footer h3 {{ font-size: 1.5rem; font-weight: 700; color: {text}; margin-bottom: 6px; }}
    .item-footer h4 {{ font-size: 1.1rem; font-weight: 600; color: {text}; margin-bottom: 4px; }}
    .item-footer span {{ color: {primary}; font-weight: 700; }}
    .price {{ font-size: 1.5rem; }}
    @media (max-width: 900px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} .bento-item.main {{ grid-column: span 2; grid-row: span 1; }} }}
    </style>
    '''
