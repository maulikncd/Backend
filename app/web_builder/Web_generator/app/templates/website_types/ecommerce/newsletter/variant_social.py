from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Social Connect - With social links"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-social" id="newsletter">
        <div class="nl-container">
            <div class="nl-left">
                <h2>Stay in Touch</h2>
                <p>Subscribe to our newsletter or follow us on social media</p>
                <form class="nl-form"><input type="email" placeholder="Email address"><button>Subscribe</button></form>
            </div>
            <div class="divider"><span>or</span></div>
            <div class="nl-right">
                <h3>Follow Us</h3>
                <div class="social-links">
                    <a href="#" class="social-link">Instagram</a>
                    <a href="#" class="social-link">Twitter</a>
                    <a href="#" class="social-link">Facebook</a>
                    <a href="#" class="social-link">TikTok</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-social {{ padding: 100px 24px; background: {text}05; }}
    .nl-container {{ max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: 1fr auto 1fr; gap: 60px; align-items: center; }}
    .nl-left h2 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .nl-left p {{ color: {secondary}; margin-bottom: 24px; }}
    .nl-form {{ display: flex; gap: 10px; }}
    .nl-form input {{ flex: 1; padding: 14px 18px; background: {background}; border: 1px solid {text}15; border-radius: 10px; color: {text}; }}
    .nl-form button {{ padding: 14px 24px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 10px; cursor: pointer; }}
    .divider {{ display: flex; align-items: center; }}
    .divider span {{ padding: 20px; background: {text}10; border-radius: 50%; color: {secondary}; font-size: 0.9rem; }}
    .nl-right {{ text-align: center; }}
    .nl-right h3 {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin-bottom: 20px; }}
    .social-links {{ display: flex; flex-direction: column; gap: 12px; }}
    .social-link {{ padding: 14px 28px; background: {text}08; color: {text}; text-decoration: none; border-radius: 100px; font-weight: 500; transition: all 0.3s ease; }}
    .social-link:hover {{ background: {primary}15; color: {primary}; }}
    @media (max-width: 900px) {{ .nl-container {{ grid-template-columns: 1fr; }} .divider {{ justify-content: center; padding: 20px 0; }} }}
    </style>
    '''
