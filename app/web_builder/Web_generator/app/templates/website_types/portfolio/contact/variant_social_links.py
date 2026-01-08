from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Social Links - Focus on social profiles"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    socials = [
        {"icon": "📧", "name": "Email", "handle": "hello@example.com", "link": "mailto:hello@example.com"},
        {"icon": "💻", "name": "GitHub", "handle": "@username", "link": "#"},
        {"icon": "💼", "name": "LinkedIn", "handle": "/in/username", "link": "#"},
        {"icon": "🐦", "name": "Twitter", "handle": "@username", "link": "#"},
        {"icon": "📸", "name": "Instagram", "handle": "@username", "link": "#"},
    ]
    
    links_html = ""
    for s in socials:
        links_html += f'''
        <a href="{s['link']}" class="social-link">
            <span class="social-icon">{s['icon']}</span>
            <div class="social-info"><span class="social-name">{s['name']}</span><span class="social-handle">{s['handle']}</span></div>
            <span class="arrow">→</span>
        </a>
        '''
    
    return f'''
    <section class="portfolio-contact-social" id="contact">
        <div class="social-container">
            <div class="social-header"><h2>Connect With Me</h2></div>
            <div class="social-links">{links_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-contact-social {{ padding: 120px 24px; background: {background}; }}
    .social-container {{ max-width: 600px; margin: 0 auto; }}
    .social-header {{ text-align: center; margin-bottom: 48px; }}
    .social-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .social-links {{ display: flex; flex-direction: column; gap: 16px; }}
    .social-link {{ display: flex; align-items: center; gap: 20px; padding: 24px; background: {text}05; border-radius: 16px; text-decoration: none; transition: all 0.3s ease; }}
    .social-link:hover {{ background: {primary}10; transform: translateX(8px); }}
    .social-icon {{ font-size: 2rem; }}
    .social-info {{ flex: 1; }}
    .social-name {{ display: block; font-weight: 700; color: {text}; }}
    .social-handle {{ display: block; color: {secondary}; font-size: 0.9rem; }}
    .arrow {{ font-size: 1.3rem; color: {primary}; }}
    </style>
    '''
