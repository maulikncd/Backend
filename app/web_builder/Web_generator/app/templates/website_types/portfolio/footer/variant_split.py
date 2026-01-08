from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Footer - Two column split"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="portfolio-footer-split" id="footer">
        <div class="footer-container">
            <div class="split-grid">
                <div class="split-left">
                    <h3>{name}</h3>
                    <p>Developer & Designer building digital products.</p>
                    <a href="mailto:hello@example.com" class="email-link">hello@example.com</a>
                </div>
                <div class="split-right">
                    <div class="link-group">
                        <h4>Links</h4>
                        <a href="#hero">Home</a>
                        <a href="#about">About</a>
                        <a href="#projects">Work</a>
                        <a href="#contact">Contact</a>
                    </div>
                    <div class="link-group">
                        <h4>Social</h4>
                        <a href="#">GitHub</a>
                        <a href="#">LinkedIn</a>
                        <a href="#">Twitter</a>
                        <a href="#">Dribbble</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom"><p>© 2024 {name}. Made with ❤️</p></div>
        </div>
    </footer>
    
    <style>
    .portfolio-footer-split {{ padding: 80px 24px 40px; background: {text}03; }}
    .footer-container {{ max-width: 1100px; margin: 0 auto; }}
    .split-grid {{ display: grid; grid-template-columns: 1.5fr 1fr; gap: 80px; margin-bottom: 60px; }}
    .split-left h3 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .split-left p {{ color: {secondary}; margin-bottom: 24px; }}
    .email-link {{ color: {primary}; text-decoration: none; font-weight: 600; font-size: 1.2rem; }}
    .split-right {{ display: flex; gap: 60px; }}
    .link-group h4 {{ font-size: 0.9rem; font-weight: 700; color: {secondary}; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px; }}
    .link-group a {{ display: block; color: {text}; text-decoration: none; padding: 8px 0; transition: color 0.3s ease; }}
    .link-group a:hover {{ color: {primary}; }}
    .footer-bottom {{ padding-top: 40px; border-top: 1px solid {text}10; }}
    .footer-bottom p {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .split-grid {{ grid-template-columns: 1fr; gap: 40px; }} .split-right {{ justify-content: flex-start; }} }}
    </style>
    '''
