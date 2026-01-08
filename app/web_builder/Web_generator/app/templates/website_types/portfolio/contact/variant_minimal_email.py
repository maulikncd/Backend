from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Email - Just email focused"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-contact-minimal" id="contact">
        <div class="minimal-container">
            <h2>Say Hello</h2>
            <a href="mailto:hello@example.com" class="email-link">hello@example.com</a>
            <p>Or find me on</p>
            <div class="social-row">
                <a href="#">GitHub</a>
                <span>•</span>
                <a href="#">LinkedIn</a>
                <span>•</span>
                <a href="#">Twitter</a>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-contact-minimal {{ padding: 160px 24px; background: {background}; text-align: center; }}
    .minimal-container {{ max-width: 600px; margin: 0 auto; }}
    .minimal-container h2 {{ font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; color: {text}; margin-bottom: 24px; }}
    .email-link {{ display: block; font-size: clamp(1.5rem, 4vw, 2.5rem); font-weight: 700; color: {primary}; text-decoration: none; margin-bottom: 48px; transition: opacity 0.3s ease; }}
    .email-link:hover {{ opacity: 0.7; }}
    .minimal-container p {{ color: {secondary}; margin-bottom: 16px; }}
    .social-row {{ display: flex; justify-content: center; gap: 16px; }}
    .social-row a {{ color: {text}; text-decoration: none; font-weight: 600; transition: color 0.3s ease; }}
    .social-row a:hover {{ color: {primary}; }}
    .social-row span {{ color: {secondary}; }}
    </style>
    '''
