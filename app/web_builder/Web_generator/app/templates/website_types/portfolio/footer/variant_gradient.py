from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Dark Gradient - Dark gradient footer"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="portfolio-footer-gradient" id="footer">
        <div class="footer-container">
            <div class="footer-top">
                <div class="brand-section">
                    <h3>{name}</h3>
                    <p>Creating digital experiences</p>
                </div>
                <div class="links-section">
                    <a href="#">GitHub</a>
                    <a href="#">LinkedIn</a>
                    <a href="#">Twitter</a>
                    <a href="#">Email</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2024 {name}. Built with ❤️ and lots of ☕</p>
            </div>
        </div>
    </footer>
    
    <style>
    .portfolio-footer-gradient {{ padding: 80px 24px 40px; background: linear-gradient(180deg, {background}, {text}08); }}
    .footer-container {{ max-width: 1000px; margin: 0 auto; }}
    .footer-top {{ display: flex; justify-content: space-between; align-items: center; padding-bottom: 40px; border-bottom: 1px solid {text}10; margin-bottom: 40px; }}
    .brand-section h3 {{ font-size: 1.5rem; font-weight: 800; color: {text}; margin-bottom: 4px; }}
    .brand-section p {{ color: {secondary}; }}
    .links-section {{ display: flex; gap: 24px; }}
    .links-section a {{ color: {text}; text-decoration: none; font-weight: 500; padding: 10px 20px; background: {text}05; border-radius: 100px; transition: all 0.3s ease; }}
    .links-section a:hover {{ background: {primary}15; color: {primary}; }}
    .footer-bottom {{ text-align: center; }}
    .footer-bottom p {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 600px) {{ .footer-top {{ flex-direction: column; gap: 32px; text-align: center; }} .links-section {{ flex-wrap: wrap; justify-content: center; }} }}
    </style>
    '''
