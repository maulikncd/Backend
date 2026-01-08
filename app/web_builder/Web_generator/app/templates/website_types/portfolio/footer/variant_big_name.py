from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Big Name - Large name as focus"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="portfolio-footer-bigname" id="footer">
        <div class="footer-container">
            <h2 class="big-name">{name}</h2>
            <div class="footer-content">
                <div class="social-links">
                    <a href="#">GitHub</a>
                    <a href="#">LinkedIn</a>
                    <a href="#">Twitter</a>
                    <a href="#">Email</a>
                </div>
                <p class="copyright">© 2024 All rights reserved.</p>
            </div>
        </div>
    </footer>
    
    <style>
    .portfolio-footer-bigname {{ padding: 100px 24px 60px; background: {background}; text-align: center; }}
    .footer-container {{ max-width: 900px; margin: 0 auto; }}
    .big-name {{ font-size: clamp(4rem, 12vw, 10rem); font-weight: 900; color: {text}10; line-height: 1; margin-bottom: 40px; letter-spacing: -4px; }}
    .social-links {{ display: flex; justify-content: center; gap: 32px; margin-bottom: 24px; }}
    .social-links a {{ color: {text}; text-decoration: none; font-weight: 600; transition: color 0.3s ease; }}
    .social-links a:hover {{ color: {primary}; }}
    .copyright {{ color: {secondary}; font-size: 0.9rem; }}
    </style>
    '''
