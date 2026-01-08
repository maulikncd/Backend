from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """With Benefits - Show subscription benefits"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-benefits" id="newsletter">
        <div class="nl-container">
            <div class="nl-content">
                <h2>Join Our Newsletter</h2>
                <p>Be the first to know about new collections and exclusive offers</p>
                <ul class="benefits">
                    <li>✓ Exclusive discounts</li>
                    <li>✓ Early access to sales</li>
                    <li>✓ New arrival alerts</li>
                </ul>
            </div>
            <form class="nl-form">
                <input type="email" placeholder="Your email address">
                <button type="submit">Subscribe →</button>
                <span class="disclaimer">No spam. Unsubscribe anytime.</span>
            </form>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-benefits {{ padding: 100px 24px; background: linear-gradient(135deg, {primary}15, {background}); }}
    .nl-container {{ max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }}
    .nl-content h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; margin-bottom: 16px; }}
    .nl-content p {{ color: {secondary}; font-size: 1.1rem; margin-bottom: 24px; }}
    .benefits {{ list-style: none; padding: 0; }}
    .benefits li {{ color: {text}; padding: 8px 0; font-weight: 500; }}
    .nl-form {{ display: flex; flex-direction: column; gap: 16px; }}
    .nl-form input {{ padding: 20px; background: {text}05; border: 1px solid {text}15; border-radius: 14px; font-size: 1rem; color: {text}; }}
    .nl-form button {{ padding: 20px; background: {primary}; color: {background}; border: none; font-weight: 700; font-size: 1.1rem; border-radius: 14px; cursor: pointer; }}
    .disclaimer {{ color: {secondary}; font-size: 0.85rem; text-align: center; }}
    @media (max-width: 900px) {{ .nl-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
