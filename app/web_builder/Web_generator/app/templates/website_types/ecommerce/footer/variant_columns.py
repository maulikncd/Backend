from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Columns Style - Multi-column footer"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="ecom-footer-columns" id="footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col brand-col"><h3>{brand}</h3><p>Your one-stop shop for quality products.</p></div>
                <div class="footer-col"><h4>Shop</h4><ul><li><a href="#">New Arrivals</a></li><li><a href="#">Categories</a></li><li><a href="#">Deals</a></li><li><a href="#">Gift Cards</a></li></ul></div>
                <div class="footer-col"><h4>Help</h4><ul><li><a href="#">FAQs</a></li><li><a href="#">Shipping</a></li><li><a href="#">Returns</a></li><li><a href="#">Contact</a></li></ul></div>
                <div class="footer-col"><h4>Company</h4><ul><li><a href="#">About Us</a></li><li><a href="#">Careers</a></li><li><a href="#">Blog</a></li><li><a href="#">Press</a></li></ul></div>
            </div>
            <div class="footer-bottom"><p>© 2024 {brand}. All rights reserved.</p><div class="payment-icons">💳 Visa/MC • PayPal • Apple Pay</div></div>
        </div>
    </footer>
    
    <style>
    .ecom-footer-columns {{ padding: 80px 24px 40px; background: {text}03; }}
    .footer-container {{ max-width: 1200px; margin: 0 auto; }}
    .footer-grid {{ display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 60px; margin-bottom: 60px; }}
    .brand-col h3 {{ font-size: 1.5rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .brand-col p {{ color: {secondary}; }}
    .footer-col h4 {{ font-size: 1rem; font-weight: 700; color: {text}; margin-bottom: 20px; }}
    .footer-col ul {{ list-style: none; padding: 0; margin: 0; }}
    .footer-col li {{ margin-bottom: 12px; }}
    .footer-col a {{ color: {secondary}; text-decoration: none; transition: color 0.3s ease; }}
    .footer-col a:hover {{ color: {primary}; }}
    .footer-bottom {{ display: flex; justify-content: space-between; padding-top: 40px; border-top: 1px solid {text}10; }}
    .footer-bottom p {{ color: {secondary}; font-size: 0.9rem; }}
    .payment-icons {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .footer-grid {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
