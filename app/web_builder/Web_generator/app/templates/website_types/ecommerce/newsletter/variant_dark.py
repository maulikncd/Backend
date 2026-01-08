from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Dark Mode - Dark themed"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-dark" id="newsletter">
        <div class="nl-container">
            <h2>Stay Connected</h2>
            <p>Subscribe to get exclusive deals, style tips, and new arrivals.</p>
            <form class="nl-form"><input type="email" placeholder="Your email address"><button>Subscribe →</button></form>
            <span class="note">Join 50,000+ subscribers</span>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-dark {{ padding: 120px 24px; background: {text}; text-align: center; }}
    .nl-container {{ max-width: 600px; margin: 0 auto; }}
    .nl-container h2 {{ font-size: 3rem; font-weight: 900; color: {background}; margin-bottom: 16px; }}
    .nl-container p {{ color: {background}70; font-size: 1.1rem; margin-bottom: 40px; }}
    .nl-form {{ display: flex; gap: 12px; margin-bottom: 20px; }}
    .nl-form input {{ flex: 1; padding: 20px; background: {background}15; border: 1px solid {background}20; border-radius: 14px; font-size: 1rem; color: {background}; }}
    .nl-form input::placeholder {{ color: {background}50; }}
    .nl-form button {{ padding: 20px 40px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 14px; cursor: pointer; }}
    .note {{ color: {background}50; font-size: 0.9rem; }}
    @media (max-width: 600px) {{ .nl-form {{ flex-direction: column; }} }}
    </style>
    '''
