from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Centered Simple - Clean centered footer"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="portfolio-footer-centered" id="footer">
        <div class="footer-container">
            <h3 class="brand">{name}</h3>
            <nav class="footer-nav">
                <a href="#hero">Home</a>
                <a href="#about">About</a>
                <a href="#projects">Work</a>
                <a href="#skills">Skills</a>
                <a href="#contact">Contact</a>
            </nav>
            <div class="social-links">
                <a href="#">GitHub</a>
                <a href="#">LinkedIn</a>
                <a href="#">Twitter</a>
            </div>
            <p class="copyright">© 2024 {name}. All rights reserved.</p>
        </div>
    </footer>
    
    <style>
    .portfolio-footer-centered {{ padding: 80px 24px 60px; background: {background}; text-align: center; border-top: 1px solid {text}10; }}
    .footer-container {{ max-width: 600px; margin: 0 auto; }}
    .brand {{ font-size: 1.8rem; font-weight: 800; color: {text}; margin-bottom: 32px; }}
    .footer-nav {{ display: flex; justify-content: center; gap: 32px; margin-bottom: 32px; flex-wrap: wrap; }}
    .footer-nav a {{ color: {secondary}; text-decoration: none; font-weight: 500; transition: color 0.3s ease; }}
    .footer-nav a:hover {{ color: {primary}; }}
    .social-links {{ display: flex; justify-content: center; gap: 24px; margin-bottom: 32px; }}
    .social-links a {{ padding: 12px 24px; background: {text}05; color: {text}; text-decoration: none; border-radius: 100px; font-weight: 500; transition: all 0.3s ease; }}
    .social-links a:hover {{ background: {primary}15; color: {primary}; }}
    .copyright {{ color: {secondary}; font-size: 0.9rem; }}
    </style>
    '''
