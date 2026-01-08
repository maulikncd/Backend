from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Simple - Clean minimal footer"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="ecom-footer-minimal" id="footer">
        <div class="footer-container">
            <span class="brand">{brand}</span>
            <div class="footer-links"><a href="#">Shop</a><a href="#">About</a><a href="#">Contact</a><a href="#">FAQ</a></div>
            <p class="copyright">© 2024 {brand}. All rights reserved.</p>
        </div>
    </footer>
    
    <style>
    .ecom-footer-minimal {{ padding: 60px 24px; background: {background}; border-top: 1px solid {text}10; text-align: center; }}
    .footer-container {{ max-width: 600px; margin: 0 auto; }}
    .brand {{ font-size: 1.5rem; font-weight: 800; color: {text}; display: block; margin-bottom: 24px; }}
    .footer-links {{ display: flex; justify-content: center; gap: 32px; margin-bottom: 24px; }}
    .footer-links a {{ color: {secondary}; text-decoration: none; font-weight: 500; transition: color 0.3s ease; }}
    .footer-links a:hover {{ color: {primary}; }}
    .copyright {{ color: {secondary}; font-size: 0.9rem; }}
    </style>
    '''
