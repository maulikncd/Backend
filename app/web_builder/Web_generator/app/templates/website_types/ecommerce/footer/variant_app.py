from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """App Download - With app links"""
    brand = props.get("brand_name", "Shop")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="ecom-footer-app" id="footer">
        <div class="footer-container">
            <div class="app-section">
                <h3>Shop on the Go</h3>
                <p>Download our app for the best experience</p>
                <div class="app-buttons"><a href="#" class="app-btn">📱 App Store</a><a href="#" class="app-btn">🤖 Google Play</a></div>
            </div>
            <div class="footer-links">
                <a href="#">Shop</a><a href="#">About</a><a href="#">Help</a><a href="#">Privacy</a><a href="#">Terms</a>
            </div>
            <p class="copyright">© 2024 {brand}. All rights reserved.</p>
        </div>
    </footer>
    
    <style>
    .ecom-footer-app {{ padding: 80px 24px 40px; background: {text}03; text-align: center; }}
    .footer-container {{ max-width: 600px; margin: 0 auto; }}
    .app-section {{ margin-bottom: 48px; padding-bottom: 48px; border-bottom: 1px solid {text}10; }}
    .app-section h3 {{ font-size: 1.8rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .app-section p {{ color: {secondary}; margin-bottom: 24px; }}
    .app-buttons {{ display: flex; justify-content: center; gap: 16px; }}
    .app-btn {{ padding: 14px 28px; background: {text}; color: {background}; text-decoration: none; font-weight: 600; border-radius: 12px; }}
    .footer-links {{ display: flex; justify-content: center; gap: 28px; margin-bottom: 24px; flex-wrap: wrap; }}
    .footer-links a {{ color: {secondary}; text-decoration: none; }}
    .copyright {{ color: {secondary}; font-size: 0.9rem; }}
    </style>
    '''
