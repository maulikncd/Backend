from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Glass Card - Glassmorphism style"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-glass" id="newsletter">
        <div class="nl-container">
            <div class="glass-card">
                <h2>Newsletter</h2>
                <p>Get notified about new products & sales</p>
                <form class="nl-form"><input type="email" placeholder="Email address"><button>Subscribe</button></form>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-glass {{ padding: 100px 24px; background: linear-gradient(135deg, {primary}20, {primary}05); }}
    .nl-container {{ max-width: 500px; margin: 0 auto; }}
    .glass-card {{ background: {background}80; backdrop-filter: blur(20px); border: 1px solid {text}10; border-radius: 32px; padding: 48px; text-align: center; }}
    .glass-card h2 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .glass-card p {{ color: {secondary}; margin-bottom: 32px; }}
    .nl-form {{ display: flex; flex-direction: column; gap: 16px; }}
    .nl-form input {{ padding: 18px; background: {text}05; border: 1px solid {text}15; border-radius: 14px; font-size: 1rem; color: {text}; text-align: center; }}
    .nl-form button {{ padding: 18px; background: {primary}; color: {background}; border: none; font-weight: 700; font-size: 1rem; border-radius: 14px; cursor: pointer; transition: all 0.3s ease; }}
    .nl-form button:hover {{ transform: scale(1.02); }}
    </style>
    '''
