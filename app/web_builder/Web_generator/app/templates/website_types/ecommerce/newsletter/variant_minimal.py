from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Center - Clean centered minimal"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-minimal" id="newsletter">
        <div class="nl-container">
            <h2>Stay in the loop</h2>
            <form class="nl-form"><input type="email" placeholder="your@email.com"><button>→</button></form>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-minimal {{ padding: 120px 24px; background: {background}; text-align: center; }}
    .nl-container {{ max-width: 500px; margin: 0 auto; }}
    .nl-container h2 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 32px; }}
    .nl-form {{ display: flex; border: 2px solid {text}15; border-radius: 100px; overflow: hidden; }}
    .nl-form input {{ flex: 1; padding: 16px 24px; border: none; background: transparent; font-size: 1rem; color: {text}; }}
    .nl-form button {{ width: 56px; background: {primary}; color: {background}; border: none; font-size: 1.2rem; cursor: pointer; }}
    </style>
    '''
