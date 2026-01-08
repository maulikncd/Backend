from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Store - Modern bento grid layout"""
    title = props.get("title", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="gaming-store-bento" id="store">
        <div class="store-container">
            <div class="store-header"><h2>{title}</h2></div>
            <div class="store-bento-grid">
                <div class="bento-item main">
                    <img src="https://images.unsplash.com/photo-1593305841991-05c297ba4575?w=1200" alt="Featured">
                    <div class="bento-overlay">
                        <span class="tag">Featured</span>
                        <h3>Battle Pass S5</h3>
                        <span class="price">$19.99</span>
                        <a href="#" class="btn">Buy Now</a>
                    </div>
                </div>
                <div class="bento-item">
                    <img src="https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=600" alt="Item">
                    <div class="bento-overlay small">
                        <h4>Skin Bundle</h4><span class="price">$14.99</span>
                    </div>
                </div>
                <div class="bento-item">
                    <img src="https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=600" alt="Item">
                    <div class="bento-overlay small">
                        <h4>5000 Coins</h4><span class="price">$49.99</span>
                    </div>
                </div>
                <div class="bento-item wide">
                    <img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=900" alt="Item">
                    <div class="bento-overlay small">
                        <h4>Pro Bundle</h4><span class="price">$29.99</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .gaming-store-bento {{ padding: 120px 24px; background: {background}; }}
    .store-container {{ max-width: 1200px; margin: 0 auto; }}
    .store-header {{ text-align: center; margin-bottom: 60px; }}
    .store-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 3rem; font-weight: 800; color: {text}; }}
    .store-bento-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, 250px); gap: 24px; }}
    .bento-item {{ position: relative; border-radius: 24px; overflow: hidden; cursor: pointer; }}
    .bento-item.main {{ grid-column: span 2; grid-row: span 2; }}
    .bento-item.wide {{ grid-column: span 2; }}
    .bento-item img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }}
    .bento-item:hover img {{ transform: scale(1.1); }}
    .bento-overlay {{ position: absolute; inset: 0; background: linear-gradient(to top, {background}E6, transparent 50%); padding: 32px; display: flex; flex-direction: column; justify-content: flex-end; }}
    .bento-overlay.small {{ padding: 20px; }}
    .tag {{ display: inline-block; padding: 5px 14px; background: {primary}; color: {background}; font-size: 0.75rem; font-weight: 700; border-radius: 100px; margin-bottom: 12px; width: fit-content; }}
    .bento-overlay h3 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 8px; }}
    .bento-overlay h4 {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .price {{ font-size: 1.5rem; font-weight: 900; color: {primary}; }}
    .btn {{ display: inline-block; padding: 14px 32px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 10px; margin-top: 16px; width: fit-content; transition: all 0.3s ease; }}
    .btn:hover {{ transform: scale(1.05); }}
    @media (max-width: 900px) {{ .store-bento-grid {{ grid-template-columns: 1fr 1fr; }} .bento-item.main {{ grid-column: span 2; grid-row: span 1; }} }}
    </style>
    '''
