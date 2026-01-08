from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Discount Offer - With discount code"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-discount" id="newsletter">
        <div class="nl-container">
            <div class="discount-badge">15% OFF</div>
            <h2>Get 15% Off Your First Order</h2>
            <p>Subscribe and receive your discount code instantly</p>
            <form class="nl-form"><input type="email" placeholder="Enter your email"><button type="submit">Get My Code</button></form>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-discount {{ padding: 100px 24px; background: {text}; text-align: center; }}
    .nl-container {{ max-width: 600px; margin: 0 auto; }}
    .discount-badge {{ display: inline-block; padding: 16px 32px; background: {primary}; color: {background}; font-size: 2rem; font-weight: 900; border-radius: 16px; margin-bottom: 32px; animation: pulse 2s infinite; }}
    @keyframes pulse {{ 0%, 100% {{ transform: scale(1); }} 50% {{ transform: scale(1.05); }} }}
    .nl-container h2 {{ font-size: 2.5rem; font-weight: 800; color: {background}; margin-bottom: 12px; }}
    .nl-container p {{ color: {background}80; font-size: 1.1rem; margin-bottom: 32px; }}
    .nl-form {{ display: flex; gap: 12px; }}
    .nl-form input {{ flex: 1; padding: 20px; background: {background}; border: none; border-radius: 14px; font-size: 1rem; color: {text}; }}
    .nl-form button {{ padding: 20px 40px; background: {primary}; color: {background}; border: none; font-weight: 700; font-size: 1rem; border-radius: 14px; cursor: pointer; }}
    @media (max-width: 600px) {{ .nl-form {{ flex-direction: column; }} }}
    </style>
    '''
