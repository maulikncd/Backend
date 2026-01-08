from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Photo Reviews - Reviews with product photos"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-testimonials-photos" id="testimonials">
        <div class="photos-container">
            <div class="photos-header"><h2>Customer Photos</h2><span class="subtitle">See our products in action</span></div>
            <div class="photos-grid">
                <div class="photo-card"><div class="photo-placeholder"></div><div class="review-overlay"><span class="stars">⭐⭐⭐⭐⭐</span><p>"Love it!"</p><span>@sarah_j</span></div></div>
                <div class="photo-card"><div class="photo-placeholder"></div><div class="review-overlay"><span class="stars">⭐⭐⭐⭐⭐</span><p>"Perfect!"</p><span>@mike_r</span></div></div>
                <div class="photo-card"><div class="photo-placeholder"></div><div class="review-overlay"><span class="stars">⭐⭐⭐⭐⭐</span><p>"Amazing!"</p><span>@emily_l</span></div></div>
                <div class="photo-card"><div class="photo-placeholder"></div><div class="review-overlay"><span class="stars">⭐⭐⭐⭐⭐</span><p>"Beautiful!"</p><span>@david_k</span></div></div>
                <div class="photo-card"><div class="photo-placeholder"></div><div class="review-overlay"><span class="stars">⭐⭐⭐⭐⭐</span><p>"Best ever!"</p><span>@anna_m</span></div></div>
                <div class="photo-card"><div class="photo-placeholder"></div><div class="review-overlay"><span class="stars">⭐⭐⭐⭐⭐</span><p>"5/5!"</p><span>@chris_p</span></div></div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-testimonials-photos {{ padding: 120px 24px; background: {text}03; }}
    .photos-container {{ max-width: 1200px; margin: 0 auto; }}
    .photos-header {{ text-align: center; margin-bottom: 60px; }}
    .photos-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; margin-bottom: 8px; }}
    .subtitle {{ color: {secondary}; }}
    .photos-grid {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 16px; }}
    .photo-card {{ position: relative; aspect-ratio: 1; border-radius: 16px; overflow: hidden; cursor: pointer; }}
    .photo-placeholder {{ width: 100%; height: 100%; background: linear-gradient(135deg, {primary}20, {primary}05); }}
    .review-overlay {{ position: absolute; inset: 0; background: {primary}E6; display: flex; flex-direction: column; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s ease; padding: 16px; text-align: center; }}
    .photo-card:hover .review-overlay {{ opacity: 1; }}
    .review-overlay .stars {{ font-size: 0.8rem; margin-bottom: 8px; }}
    .review-overlay p {{ color: {background}; font-weight: 700; margin-bottom: 8px; }}
    .review-overlay span {{ color: {background}80; font-size: 0.85rem; }}
    @media (max-width: 900px) {{ .photos-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
    </style>
    '''
