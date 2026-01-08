from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """With Newsletter - Footer with signup"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="ecom-footer-newsletter" id="footer">
        <div class="footer-container">
            <div class="nl-section">
                <h3>Subscribe & Save 10%</h3>
                <p>Get exclusive deals and new arrivals in your inbox</p>
                <form class="nl-form"><input type="email" placeholder="Email address"><button>Subscribe</button></form>
            </div>
            <div class="footer-bottom">
                <span class="brand">{brand}</span>
                <div class="links"><a href="#">Shop</a><a href="#">About</a><a href="#">Help</a><a href="#">Contact</a></div>
                <p>© 2024 All rights reserved.</p>
            </div>
        </div>
    </footer>
    
    <style>
    .ecom-footer-newsletter {{ padding: 80px 24px 40px; background: {background}; }}
    .footer-container {{ max-width: 800px; margin: 0 auto; }}
    .nl-section {{ text-align: center; padding-bottom: 60px; margin-bottom: 40px; border-bottom: 1px solid {text}10; }}
    .nl-section h3 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .nl-section p {{ color: {secondary}; margin-bottom: 28px; }}
    .nl-form {{ display: flex; gap: 12px; max-width: 450px; margin: 0 auto; }}
    .nl-form input {{ flex: 1; padding: 16px 20px; background: {text}05; border: 1px solid {text}15; border-radius: 12px; color: {text}; }}
    .nl-form button {{ padding: 16px 32px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 12px; cursor: pointer; }}
    .footer-bottom {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; }}
    .brand {{ font-weight: 700; color: {text}; }}
    .links {{ display: flex; gap: 24px; }}
    .links a {{ color: {secondary}; text-decoration: none; }}
    .footer-bottom p {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 768px) {{ .footer-bottom {{ flex-direction: column; text-align: center; }} .nl-form {{ flex-direction: column; }} }}
    </style>
    '''
