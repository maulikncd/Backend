from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Trust Badges - Brand trust section"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-features-trust" id="features">
        <div class="trust-container">
            <div class="trust-header"><h3>Trusted by Thousands</h3></div>
            <div class="badges-row">
                <div class="badge"><span class="icon">🔒</span><span>SSL Secure</span></div>
                <div class="badge"><span class="icon">💳</span><span>Visa/MC</span></div>
                <div class="badge"><span class="icon">📦</span><span>Tracked Shipping</span></div>
                <div class="badge"><span class="icon">✅</span><span>Verified Seller</span></div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-features-trust {{ padding: 60px 24px; background: {background}; border-top: 1px solid {text}10; }}
    .trust-container {{ max-width: 900px; margin: 0 auto; text-align: center; }}
    .trust-header h3 {{ font-size: 1.2rem; font-weight: 700; color: {text}; margin-bottom: 32px; }}
    .badges-row {{ display: flex; justify-content: center; gap: 48px; flex-wrap: wrap; }}
    .badge {{ display: flex; align-items: center; gap: 8px; }}
    .badge .icon {{ font-size: 1.5rem; }}
    .badge span:last-child {{ color: {secondary}; font-weight: 500; }}
    </style>
    '''
