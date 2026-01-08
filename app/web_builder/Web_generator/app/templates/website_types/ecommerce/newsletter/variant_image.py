from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """With Image - Newsletter with visual"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-image" id="newsletter">
        <div class="nl-container">
            <div class="nl-visual"><span class="icon">📬</span></div>
            <div class="nl-content">
                <h2>Join Our Mailing List</h2>
                <p>Be the first to hear about new launches, exclusive offers, and more!</p>
                <form class="nl-form"><input type="email" placeholder="Enter your email"><button>Join Now</button></form>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-image {{ padding: 100px 24px; background: {background}; }}
    .nl-container {{ max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1.5fr; gap: 60px; align-items: center; }}
    .nl-visual {{ aspect-ratio: 1; background: linear-gradient(135deg, {primary}20, {primary}05); border-radius: 32px; display: flex; align-items: center; justify-content: center; }}
    .icon {{ font-size: 6rem; }}
    .nl-content h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; margin-bottom: 16px; }}
    .nl-content p {{ color: {secondary}; font-size: 1.1rem; margin-bottom: 32px; }}
    .nl-form {{ display: flex; gap: 12px; }}
    .nl-form input {{ flex: 1; padding: 18px 24px; background: {text}05; border: 1px solid {text}15; border-radius: 14px; font-size: 1rem; color: {text}; }}
    .nl-form button {{ padding: 18px 36px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 14px; cursor: pointer; }}
    @media (max-width: 900px) {{ .nl-container {{ grid-template-columns: 1fr; }} .nl-visual {{ display: none; }} }}
    </style>
    '''
