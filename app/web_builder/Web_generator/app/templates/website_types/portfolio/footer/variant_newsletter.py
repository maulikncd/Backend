from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """With Newsletter - Footer with email signup"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="portfolio-footer-newsletter" id="footer">
        <div class="footer-container">
            <div class="newsletter-section">
                <h3>Stay Updated</h3>
                <p>Get notified about new projects and articles.</p>
                <form class="newsletter-form">
                    <input type="email" placeholder="your@email.com">
                    <button type="submit">Subscribe</button>
                </form>
            </div>
            <div class="footer-bottom">
                <span class="brand">{name}</span>
                <div class="social-links">
                    <a href="#">GitHub</a>
                    <a href="#">LinkedIn</a>
                    <a href="#">Twitter</a>
                </div>
                <span class="copyright">© 2024</span>
            </div>
        </div>
    </footer>
    
    <style>
    .portfolio-footer-newsletter {{ padding: 80px 24px 40px; background: {text}03; }}
    .footer-container {{ max-width: 900px; margin: 0 auto; }}
    .newsletter-section {{ text-align: center; margin-bottom: 60px; padding-bottom: 60px; border-bottom: 1px solid {text}10; }}
    .newsletter-section h3 {{ font-size: 1.8rem; font-weight: 800; color: {text}; margin-bottom: 8px; }}
    .newsletter-section p {{ color: {secondary}; margin-bottom: 24px; }}
    .newsletter-form {{ display: flex; gap: 12px; max-width: 400px; margin: 0 auto; }}
    .newsletter-form input {{ flex: 1; padding: 16px; background: {background}; border: 1px solid {text}15; border-radius: 10px; color: {text}; font-size: 1rem; }}
    .newsletter-form button {{ padding: 16px 32px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 10px; cursor: pointer; transition: all 0.3s ease; }}
    .newsletter-form button:hover {{ transform: scale(1.05); }}
    .footer-bottom {{ display: flex; justify-content: space-between; align-items: center; }}
    .brand {{ font-weight: 700; color: {text}; }}
    .social-links {{ display: flex; gap: 24px; }}
    .social-links a {{ color: {secondary}; text-decoration: none; transition: color 0.3s ease; }}
    .social-links a:hover {{ color: {primary}; }}
    .copyright {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 600px) {{ .footer-bottom {{ flex-direction: column; gap: 20px; text-align: center; }} .newsletter-form {{ flex-direction: column; }} }}
    </style>
    '''
