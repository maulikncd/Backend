from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """CTA Footer - With call to action"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="portfolio-footer-cta" id="footer">
        <div class="footer-container">
            <div class="cta-section">
                <h2>Have a project in mind?</h2>
                <a href="mailto:hello@example.com" class="cta-btn">Let's Talk →</a>
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
    .portfolio-footer-cta {{ padding: 80px 24px 40px; background: {background}; }}
    .footer-container {{ max-width: 1000px; margin: 0 auto; }}
    .cta-section {{ text-align: center; padding: 80px 40px; background: linear-gradient(135deg, {primary}15, {primary}05); border-radius: 32px; margin-bottom: 60px; }}
    .cta-section h2 {{ font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 900; color: {text}; margin-bottom: 32px; }}
    .cta-btn {{ display: inline-block; padding: 20px 48px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; font-size: 1.2rem; border-radius: 14px; transition: all 0.3s ease; }}
    .cta-btn:hover {{ transform: translateY(-4px); box-shadow: 0 25px 50px {primary}40; }}
    .footer-bottom {{ display: flex; justify-content: space-between; align-items: center; }}
    .brand {{ font-weight: 700; color: {text}; }}
    .social-links {{ display: flex; gap: 24px; }}
    .social-links a {{ color: {secondary}; text-decoration: none; transition: color 0.3s ease; }}
    .social-links a:hover {{ color: {primary}; }}
    .copyright {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 600px) {{ .footer-bottom {{ flex-direction: column; gap: 20px; text-align: center; }} }}
    </style>
    '''
