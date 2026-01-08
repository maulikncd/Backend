from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Columns Layout - Multi-column footer"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="portfolio-footer-columns" id="footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-col brand-col">
                    <h3>{name}</h3>
                    <p>Building digital experiences with passion and precision.</p>
                </div>
                <div class="footer-col">
                    <h4>Navigation</h4>
                    <ul><li><a href="#hero">Home</a></li><li><a href="#about">About</a></li><li><a href="#projects">Projects</a></li><li><a href="#contact">Contact</a></li></ul>
                </div>
                <div class="footer-col">
                    <h4>Social</h4>
                    <ul><li><a href="#">GitHub</a></li><li><a href="#">LinkedIn</a></li><li><a href="#">Twitter</a></li><li><a href="#">Dribbble</a></li></ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul><li><a href="mailto:hello@example.com">hello@example.com</a></li><li><span>San Francisco, CA</span></li></ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2024 {name}. All rights reserved.</p>
            </div>
        </div>
    </footer>
    
    <style>
    .portfolio-footer-columns {{ padding: 80px 24px 40px; background: {text}03; }}
    .footer-container {{ max-width: 1100px; margin: 0 auto; }}
    .footer-grid {{ display: grid; grid-template-columns: 2fr 1fr 1fr 1.5fr; gap: 48px; margin-bottom: 60px; }}
    .brand-col h3 {{ font-size: 1.5rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .brand-col p {{ color: {secondary}; line-height: 1.6; }}
    .footer-col h4 {{ font-size: 1rem; font-weight: 700; color: {text}; margin-bottom: 20px; }}
    .footer-col ul {{ list-style: none; padding: 0; margin: 0; }}
    .footer-col li {{ margin-bottom: 12px; }}
    .footer-col a, .footer-col span {{ color: {secondary}; text-decoration: none; transition: color 0.3s ease; }}
    .footer-col a:hover {{ color: {primary}; }}
    .footer-bottom {{ padding-top: 40px; border-top: 1px solid {text}10; text-align: center; }}
    .footer-bottom p {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .footer-grid {{ grid-template-columns: 1fr 1fr; }} }}
    @media (max-width: 600px) {{ .footer-grid {{ grid-template-columns: 1fr; text-align: center; }} }}
    </style>
    '''
