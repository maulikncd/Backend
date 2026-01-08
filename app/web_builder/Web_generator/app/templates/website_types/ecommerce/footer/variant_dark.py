from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Dark Theme - Dark themed footer"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="ecom-footer-dark" id="footer">
        <div class="footer-container">
            <div class="footer-top">
                <div class="brand-section"><h3>{brand}</h3><p>Quality products, delivered fast.</p><div class="social-links"><a href="#">IG</a><a href="#">TW</a><a href="#">FB</a></div></div>
                <div class="links-section"><div class="link-col"><h4>Shop</h4><a href="#">New</a><a href="#">Sale</a><a href="#">Categories</a></div><div class="link-col"><h4>Support</h4><a href="#">Help</a><a href="#">Returns</a><a href="#">Contact</a></div></div>
            </div>
            <div class="footer-bottom"><p>© 2024 {brand}</p><span>💳 Secure Payment</span></div>
        </div>
    </footer>
    
    <style>
    .ecom-footer-dark {{ padding: 80px 24px 40px; background: {text}; }}
    .footer-container {{ max-width: 1100px; margin: 0 auto; }}
    .footer-top {{ display: flex; justify-content: space-between; margin-bottom: 60px; }}
    .brand-section h3 {{ font-size: 1.8rem; font-weight: 800; color: {background}; margin-bottom: 8px; }}
    .brand-section p {{ color: {background}70; margin-bottom: 20px; }}
    .social-links {{ display: flex; gap: 12px; }}
    .social-links a {{ width: 40px; height: 40px; background: {background}15; color: {background}; text-decoration: none; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: 600; }}
    .links-section {{ display: flex; gap: 80px; }}
    .link-col h4 {{ color: {background}50; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; }}
    .link-col a {{ display: block; color: {background}80; text-decoration: none; padding: 6px 0; }}
    .link-col a:hover {{ color: {primary}; }}
    .footer-bottom {{ display: flex; justify-content: space-between; padding-top: 40px; border-top: 1px solid {background}15; }}
    .footer-bottom p, .footer-bottom span {{ color: {background}50; font-size: 0.9rem; }}
    @media (max-width: 768px) {{ .footer-top {{ flex-direction: column; gap: 40px; }} }}
    </style>
    '''
