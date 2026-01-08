from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Style - Modern bento layout"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-newsletter-bento" id="newsletter">
        <div class="nl-container">
            <div class="bento-grid">
                <div class="bento-item main">
                    <h2>Join the Club</h2>
                    <p>Subscribe for exclusive access to new products, special offers, and insider content.</p>
                    <form class="nl-form"><input type="email" placeholder="Your email"><button>Subscribe</button></form>
                </div>
                <div class="bento-item stat"><span class="num">50K+</span><span class="label">Subscribers</span></div>
                <div class="bento-item stat"><span class="num">Weekly</span><span class="label">Updates</span></div>
                <div class="bento-item benefit"><span class="icon">🎁</span><span>Exclusive Deals</span></div>
                <div class="bento-item benefit"><span class="icon">🚀</span><span>Early Access</span></div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-newsletter-bento {{ padding: 100px 24px; background: {background}; }}
    .nl-container {{ max-width: 900px; margin: 0 auto; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }}
    .bento-item {{ background: {text}05; border-radius: 20px; padding: 28px; }}
    .bento-item.main {{ grid-column: span 2; grid-row: span 2; background: linear-gradient(135deg, {primary}15, {primary}05); }}
    .main h2 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .main p {{ color: {secondary}; margin-bottom: 28px; line-height: 1.6; }}
    .nl-form {{ display: flex; gap: 10px; }}
    .nl-form input {{ flex: 1; padding: 14px 18px; background: {background}; border: 1px solid {text}15; border-radius: 10px; color: {text}; }}
    .nl-form button {{ padding: 14px 24px; background: {primary}; color: {background}; border: none; font-weight: 700; border-radius: 10px; cursor: pointer; }}
    .stat {{ text-align: center; display: flex; flex-direction: column; justify-content: center; }}
    .stat .num {{ font-size: 1.8rem; font-weight: 900; color: {primary}; }}
    .stat .label {{ color: {secondary}; font-size: 0.85rem; }}
    .benefit {{ display: flex; align-items: center; gap: 12px; }}
    .benefit .icon {{ font-size: 1.5rem; }}
    .benefit span:last-child {{ color: {text}; font-weight: 600; }}
    @media (max-width: 768px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} .bento-item.main {{ grid-column: span 2; }} }}
    </style>
    '''
