from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Trust Section - With trust badges"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="ecom-footer-trust" id="footer">
        <div class="footer-container">
            <div class="trust-banner">
                <span>🚚 Free Shipping</span>
                <span>🔄 Easy Returns</span>
                <span>🔒 Secure Payment</span>
                <span>💬 24/7 Support</span>
            </div>
            <div class="footer-main">
                <span class="brand">{brand}</span>
                <nav class="footer-nav"><a href="#">Shop</a><a href="#">About</a><a href="#">Help</a><a href="#">Contact</a></nav>
                <div class="payment">💳 Visa • MC • PayPal • Apple Pay</div>
            </div>
            <p class="copyright">© 2024 {brand}. All rights reserved.</p>
        </div>
    </footer>
    
    <style>
    .ecom-footer-trust {{ padding: 60px 24px 40px; background: {background}; }}
    .footer-container {{ max-width: 1000px; margin: 0 auto; }}
    .trust-banner {{ display: flex; justify-content: center; gap: 48px; padding: 24px; background: {primary}10; border-radius: 16px; margin-bottom: 48px; flex-wrap: wrap; }}
    .trust-banner span {{ color: {text}; font-weight: 600; }}
    .footer-main {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px; flex-wrap: wrap; gap: 24px; }}
    .brand {{ font-size: 1.5rem; font-weight: 800; color: {text}; }}
    .footer-nav {{ display: flex; gap: 28px; }}
    .footer-nav a {{ color: {secondary}; text-decoration: none; }}
    .payment {{ color: {secondary}; font-size: 0.9rem; }}
    .copyright {{ text-align: center; color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 768px) {{ .footer-main {{ flex-direction: column; text-align: center; }} }}
    </style>
    '''
