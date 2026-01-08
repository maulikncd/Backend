from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Style - Modern bento grid"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-testimonials-bento" id="testimonials">
        <div class="bento-container">
            <div class="bento-grid">
                <div class="bento-item header"><span class="tag">Reviews</span><h2>What People Say</h2></div>
                <div class="bento-item stat"><span class="num">4.9</span><span class="stars">⭐⭐⭐⭐⭐</span><span class="label">12K+ reviews</span></div>
                <div class="bento-item review main"><p>"Best shopping experience ever! The quality and service are unmatched."</p><span class="author">— Sarah J.</span></div>
                <div class="bento-item review"><p>"Fast shipping, great products!"</p><span class="author">— Mike R.</span></div>
                <div class="bento-item review"><p>"Highly recommend!"</p><span class="author">— Emily L.</span></div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-testimonials-bento {{ padding: 120px 24px; background: {background}; }}
    .bento-container {{ max-width: 1000px; margin: 0 auto; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, auto); gap: 20px; }}
    .bento-item {{ background: {text}05; border-radius: 24px; padding: 32px; }}
    .bento-item.header {{ grid-column: span 2; }}
    .tag {{ display: inline-block; padding: 8px 18px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 12px; font-size: 0.9rem; }}
    .header h2 {{ font-size: 2rem; font-weight: 800; color: {text}; }}
    .stat {{ text-align: center; display: flex; flex-direction: column; justify-content: center; align-items: center; background: linear-gradient(135deg, {primary}15, {primary}05); }}
    .stat .num {{ font-size: 3rem; font-weight: 900; color: {primary}; }}
    .stat .stars {{ margin: 8px 0; }}
    .stat .label {{ color: {secondary}; }}
    .review.main {{ grid-column: span 2; }}
    .review p {{ color: {text}; font-size: 1.2rem; line-height: 1.6; margin-bottom: 16px; font-style: italic; }}
    .author {{ color: {primary}; font-weight: 600; }}
    @media (max-width: 768px) {{ .bento-grid {{ grid-template-columns: 1fr; }} .bento-item.header, .review.main {{ grid-column: span 1; }} }}
    </style>
    '''
