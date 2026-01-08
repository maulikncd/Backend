from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Simple CTA - Basic newsletter signup"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-simple" id="newsletter">
        <div class="nl-container">
            <h2>Stay Updated</h2>
            <p>Subscribe for exclusive deals and new arrivals</p>
            <form class="nl-form"><input type="email" placeholder="Enter your email"><button type="submit">Subscribe</button></form>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-simple {{ padding: 100px 24px; background: {primary}; text-align: center; }}
    .nl-container {{ max-width: 600px; margin: 0 auto; }}
    .nl-container h2 {{ font-size: 2.5rem; font-weight: 800; color: {background}; margin-bottom: 12px; }}
    .nl-container p {{ color: {background}90; font-size: 1.1rem; margin-bottom: 32px; }}
    .nl-form {{ display: flex; gap: 12px; }}
    .nl-form input {{ flex: 1; padding: 18px 24px; background: {background}; border: none; border-radius: 12px; font-size: 1rem; color: {text}; }}
    .nl-form button {{ padding: 18px 36px; background: {text}; color: {background}; border: none; font-weight: 700; border-radius: 12px; cursor: pointer; transition: transform 0.3s ease; }}
    .nl-form button:hover {{ transform: scale(1.05); }}
    @media (max-width: 600px) {{ .nl-form {{ flex-direction: column; }} }}
    </style>
    '''
