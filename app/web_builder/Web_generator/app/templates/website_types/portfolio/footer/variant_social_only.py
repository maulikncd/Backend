from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Social Only - Minimal social links footer"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="portfolio-footer-social" id="footer">
        <div class="footer-container">
            <div class="social-links">
                <a href="#">GitHub</a>
                <a href="#">LinkedIn</a>
                <a href="#">Twitter</a>
                <a href="#">Email</a>
            </div>
            <p class="copyright">© 2024 {name}. All rights reserved.</p>
        </div>
    </footer>
    
    <style>
    .portfolio-footer-social {{ padding: 60px 24px; background: {background}; border-top: 1px solid {text}10; text-align: center; }}
    .footer-container {{ max-width: 600px; margin: 0 auto; }}
    .social-links {{ display: flex; justify-content: center; gap: 32px; margin-bottom: 24px; }}
    .social-links a {{ color: {text}; text-decoration: none; font-weight: 600; transition: color 0.3s ease; }}
    .social-links a:hover {{ color: {primary}; }}
    .copyright {{ color: {secondary}; font-size: 0.9rem; }}
    </style>
    '''
