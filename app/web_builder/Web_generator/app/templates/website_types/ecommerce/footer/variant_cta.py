from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """CTA Footer - With call to action"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="ecom-footer-cta" id="footer">
        <div class="footer-container">
            <div class="cta-section">
                <h2>Ready to Shop?</h2>
                <p>Explore our collection of quality products</p>
                <a href="#products" class="cta-btn">Start Shopping →</a>
            </div>
            <div class="footer-bottom">
                <span class="brand">{brand}</span>
                <div class="links"><a href="#">Shop</a><a href="#">About</a><a href="#">Help</a><a href="#">Contact</a></div>
                <p>© 2024</p>
            </div>
        </div>
    </footer>
    
    <style>
    .ecom-footer-cta {{ padding: 80px 24px 40px; background: {background}; }}
    .footer-container {{ max-width: 900px; margin: 0 auto; }}
    .cta-section {{ text-align: center; padding: 60px; background: linear-gradient(135deg, {primary}15, {primary}05); border-radius: 32px; margin-bottom: 40px; }}
    .cta-section h2 {{ font-size: 2.5rem; font-weight: 900; color: {text}; margin-bottom: 12px; }}
    .cta-section p {{ color: {secondary}; margin-bottom: 28px; }}
    .cta-btn {{ display: inline-block; padding: 18px 40px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; font-size: 1.1rem; border-radius: 14px; }}
    .footer-bottom {{ display: flex; justify-content: space-between; align-items: center; }}
    .brand {{ font-weight: 700; color: {text}; }}
    .links {{ display: flex; gap: 24px; }}
    .links a {{ color: {secondary}; text-decoration: none; }}
    .footer-bottom p {{ color: {secondary}; font-size: 0.9rem; }}
    </style>
    '''
