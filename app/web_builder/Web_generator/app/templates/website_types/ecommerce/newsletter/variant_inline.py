from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Inline Bar - Compact inline style"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-inline" id="newsletter">
        <div class="nl-container">
            <div class="nl-text"><h3>Subscribe for Updates</h3><p>New arrivals and exclusive deals</p></div>
            <form class="nl-form"><input type="email" placeholder="Email address"><button type="submit">Subscribe</button></form>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-inline {{ padding: 40px 24px; background: {text}05; border-top: 1px solid {text}10; border-bottom: 1px solid {text}10; }}
    .nl-container {{ max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; gap: 40px; }}
    .nl-text h3 {{ font-size: 1.3rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .nl-text p {{ color: {secondary}; font-size: 0.9rem; }}
    .nl-form {{ display: flex; gap: 12px; }}
    .nl-form input {{ padding: 14px 20px; background: {background}; border: 1px solid {text}15; border-radius: 10px; width: 280px; color: {text}; }}
    .nl-form button {{ padding: 14px 28px; background: {primary}; color: {background}; border: none; font-weight: 600; border-radius: 10px; cursor: pointer; }}
    @media (max-width: 768px) {{ .nl-container {{ flex-direction: column; text-align: center; }} .nl-form {{ flex-direction: column; width: 100%; }} .nl-form input {{ width: 100%; }} }}
    </style>
    '''
