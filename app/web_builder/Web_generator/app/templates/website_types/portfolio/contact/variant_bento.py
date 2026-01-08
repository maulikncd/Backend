from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Contact - Modern bento grid layout"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-contact-bento" id="contact">
        <div class="bento-container">
            <div class="bento-grid">
                <div class="bento-item intro">
                    <span class="tag">Contact</span>
                    <h2>Let's Work Together</h2>
                    <p>Ready to start your next project?</p>
                </div>
                <div class="bento-item email">
                    <span class="icon">📧</span>
                    <h3>Email</h3>
                    <a href="mailto:hello@example.com">hello@example.com</a>
                </div>
                <div class="bento-item social">
                    <span class="icon">🔗</span>
                    <h3>Social</h3>
                    <div class="social-links">
                        <a href="#">GitHub</a>
                        <a href="#">LinkedIn</a>
                        <a href="#">Twitter</a>
                    </div>
                </div>
                <div class="bento-item availability">
                    <div class="status"></div>
                    <span>Available for freelance</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-contact-bento {{ padding: 120px 24px; background: {background}; }}
    .bento-container {{ max-width: 900px; margin: 0 auto; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }}
    .bento-item {{ background: {text}05; border: 1px solid {text}10; border-radius: 24px; padding: 32px; }}
    .bento-item.intro {{ grid-column: span 2; }}
    .tag {{ display: inline-block; padding: 8px 20px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 16px; font-size: 0.9rem; }}
    .intro h2 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 8px; }}
    .intro p {{ color: {secondary}; }}
    .icon {{ display: block; font-size: 2rem; margin-bottom: 12px; }}
    .bento-item h3 {{ font-size: 1rem; font-weight: 600; color: {secondary}; margin-bottom: 8px; }}
    .bento-item a {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    .social-links {{ display: flex; gap: 16px; }}
    .social-links a {{ color: {text}; }}
    .bento-item.availability {{ display: flex; align-items: center; gap: 12px; background: linear-gradient(135deg, {primary}15, {primary}05); }}
    .status {{ width: 12px; height: 12px; background: #22c55e; border-radius: 50%; animation: pulse 2s infinite; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
    .availability span {{ color: {text}; font-weight: 600; }}
    @media (max-width: 768px) {{ .bento-grid {{ grid-template-columns: 1fr; }} .bento-item.intro {{ grid-column: span 1; }} }}
    </style>
    '''
