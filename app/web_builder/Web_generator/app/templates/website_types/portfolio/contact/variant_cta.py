from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Big CTA - Large call to action style"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-contact-cta" id="contact">
        <div class="cta-container">
            <div class="cta-content">
                <span class="tag">Available for Work</span>
                <h2>Let's build something amazing together</h2>
                <p>I'm currently open to new opportunities and exciting projects.</p>
                <div class="cta-buttons">
                    <a href="mailto:hello@example.com" class="btn-primary">Get in Touch</a>
                    <a href="#" class="btn-secondary">Download CV</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-contact-cta {{ padding: 160px 24px; background: linear-gradient(135deg, {primary}15, {primary}05); }}
    .cta-container {{ max-width: 800px; margin: 0 auto; text-align: center; }}
    .tag {{ display: inline-block; padding: 12px 28px; background: {primary}; color: {background}; font-weight: 700; border-radius: 100px; margin-bottom: 32px; }}
    .cta-content h2 {{ font-size: clamp(2.5rem, 6vw, 5rem); font-weight: 900; color: {text}; line-height: 1.1; margin-bottom: 24px; }}
    .cta-content p {{ font-size: 1.3rem; color: {secondary}; margin-bottom: 48px; }}
    .cta-buttons {{ display: flex; justify-content: center; gap: 20px; }}
    .btn-primary {{ padding: 20px 48px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; font-size: 1.1rem; border-radius: 14px; transition: all 0.3s ease; }}
    .btn-primary:hover {{ transform: translateY(-4px); box-shadow: 0 25px 50px {primary}40; }}
    .btn-secondary {{ padding: 20px 48px; background: transparent; border: 2px solid {text}20; color: {text}; text-decoration: none; font-weight: 700; font-size: 1.1rem; border-radius: 14px; transition: all 0.3s ease; }}
    .btn-secondary:hover {{ border-color: {primary}; color: {primary}; }}
    @media (max-width: 600px) {{ .cta-buttons {{ flex-direction: column; }} }}
    </style>
    '''
