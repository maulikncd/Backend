from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Layout - Two column layout"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-features-split" id="features">
        <div class="split-container">
            <div class="split-left">
                <span class="tag">Why Us</span>
                <h2>Shopping Made Better</h2>
                <p>We're committed to providing the best shopping experience with quality products and excellent service.</p>
            </div>
            <div class="split-right">
                <div class="feature-item"><span class="icon">🚚</span><div><h4>Free Shipping</h4><p>On orders over $50</p></div></div>
                <div class="feature-item"><span class="icon">🔄</span><div><h4>Easy Returns</h4><p>30-day return policy</p></div></div>
                <div class="feature-item"><span class="icon">🔒</span><div><h4>Secure Payment</h4><p>100% protected</p></div></div>
                <div class="feature-item"><span class="icon">💬</span><div><h4>24/7 Support</h4><p>Always here to help</p></div></div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-features-split {{ padding: 100px 24px; background: {background}; }}
    .split-container {{ max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }}
    .tag {{ display: inline-block; padding: 8px 18px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 16px; font-size: 0.9rem; }}
    .split-left h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; margin-bottom: 16px; }}
    .split-left p {{ color: {secondary}; font-size: 1.1rem; line-height: 1.7; }}
    .split-right {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }}
    .feature-item {{ display: flex; gap: 16px; }}
    .icon {{ font-size: 2rem; }}
    .feature-item h4 {{ font-size: 1.1rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .feature-item p {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .split-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
