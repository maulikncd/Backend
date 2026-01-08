from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Style - Two column split"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="ecom-footer-split" id="footer">
        <div class="footer-container">
            <div class="split-top">
                <div class="split-left"><h3>{brand}</h3><p>Quality products, fast delivery, great service.</p><a href="mailto:hello@shop.com">hello@shop.com</a></div>
                <div class="split-right"><div class="link-group"><h4>Shop</h4><a href="#">Products</a><a href="#">Categories</a><a href="#">Deals</a></div><div class="link-group"><h4>Support</h4><a href="#">Help</a><a href="#">Returns</a><a href="#">Contact</a></div></div>
            </div>
            <div class="footer-bottom"><p>© 2024 {brand}. All rights reserved.</p><div class="social"><a href="#">IG</a><a href="#">TW</a><a href="#">FB</a></div></div>
        </div>
    </footer>
    
    <style>
    .ecom-footer-split {{ padding: 80px 24px 40px; background: {text}03; }}
    .footer-container {{ max-width: 1100px; margin: 0 auto; }}
    .split-top {{ display: grid; grid-template-columns: 1.5fr 1fr; gap: 80px; margin-bottom: 60px; }}
    .split-left h3 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 16px; }}
    .split-left p {{ color: {secondary}; margin-bottom: 20px; }}
    .split-left a {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    .split-right {{ display: flex; gap: 60px; }}
    .link-group h4 {{ color: {secondary}; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; }}
    .link-group a {{ display: block; color: {text}; text-decoration: none; padding: 6px 0; }}
    .footer-bottom {{ display: flex; justify-content: space-between; align-items: center; padding-top: 40px; border-top: 1px solid {text}10; }}
    .footer-bottom p {{ color: {secondary}; font-size: 0.9rem; }}
    .social {{ display: flex; gap: 12px; }}
    .social a {{ width: 36px; height: 36px; background: {text}; color: {background}; text-decoration: none; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 600; }}
    @media (max-width: 900px) {{ .split-top {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
