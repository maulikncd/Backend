from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Style - Modern bento grid"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="ecom-footer-bento" id="footer">
        <div class="footer-container">
            <div class="bento-grid">
                <div class="bento-item brand"><h3>{brand}</h3><p>Quality products, delivered fast.</p></div>
                <div class="bento-item links"><a href="#">Shop</a><a href="#">Categories</a><a href="#">Deals</a></div>
                <div class="bento-item links"><a href="#">Help</a><a href="#">Returns</a><a href="#">Contact</a></div>
                <div class="bento-item social"><a href="#">IG</a><a href="#">TW</a><a href="#">FB</a></div>
                <div class="bento-item payment"><span>💳 Secure Checkout</span></div>
            </div>
            <p class="copyright">© 2024 {brand}. All rights reserved.</p>
        </div>
    </footer>
    
    <style>
    .ecom-footer-bento {{ padding: 80px 24px 40px; background: {background}; }}
    .footer-container {{ max-width: 1000px; margin: 0 auto; }}
    .bento-grid {{ display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 16px; margin-bottom: 40px; }}
    .bento-item {{ background: {text}05; border-radius: 20px; padding: 28px; }}
    .bento-item.brand {{ grid-row: span 2; }}
    .brand h3 {{ font-size: 1.5rem; font-weight: 800; color: {text}; margin-bottom: 8px; }}
    .brand p {{ color: {secondary}; }}
    .links {{ display: flex; flex-direction: column; gap: 12px; }}
    .links a {{ color: {secondary}; text-decoration: none; }}
    .social {{ display: flex; gap: 10px; align-items: center; }}
    .social a {{ width: 40px; height: 40px; background: {primary}; color: {background}; text-decoration: none; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: 600; }}
    .payment {{ display: flex; align-items: center; }}
    .payment span {{ color: {secondary}; }}
    .copyright {{ text-align: center; color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 768px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} .bento-item.brand {{ grid-row: span 1; }} }}
    </style>
    '''
