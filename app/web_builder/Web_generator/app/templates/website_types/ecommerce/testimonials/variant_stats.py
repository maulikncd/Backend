from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Stats Focus - With rating stats"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-testimonials-stats" id="testimonials">
        <div class="stats-container">
            <div class="stats-left">
                <h2>Loved by<br/>Thousands</h2>
                <div class="overall-rating">
                    <span class="rating-num">4.9</span>
                    <div class="rating-info"><span class="stars">⭐⭐⭐⭐⭐</span><span class="count">Based on 12,543 reviews</span></div>
                </div>
                <div class="rating-bars">
                    <div class="bar-row"><span>5 ⭐</span><div class="bar"><div class="fill" style="width: 85%"></div></div><span>85%</span></div>
                    <div class="bar-row"><span>4 ⭐</span><div class="bar"><div class="fill" style="width: 10%"></div></div><span>10%</span></div>
                    <div class="bar-row"><span>3 ⭐</span><div class="bar"><div class="fill" style="width: 3%"></div></div><span>3%</span></div>
                </div>
            </div>
            <div class="stats-right">
                <div class="review-card">
                    <div class="stars">⭐⭐⭐⭐⭐</div>
                    <p>"Absolutely love this store! Fast shipping, great products, and amazing customer service."</p>
                    <span class="name">— Jessica M.</span>
                </div>
                <div class="review-card">
                    <div class="stars">⭐⭐⭐⭐⭐</div>
                    <p>"Best quality for the price. I've been a customer for 2 years now!"</p>
                    <span class="name">— David K.</span>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-testimonials-stats {{ padding: 120px 24px; background: {background}; }}
    .stats-container {{ max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 80px; }}
    .stats-left h2 {{ font-size: 3rem; font-weight: 900; color: {text}; margin-bottom: 40px; }}
    .overall-rating {{ display: flex; align-items: center; gap: 20px; margin-bottom: 40px; }}
    .rating-num {{ font-size: 4rem; font-weight: 900; color: {primary}; }}
    .stars {{ display: block; font-size: 1.2rem; }}
    .count {{ display: block; color: {secondary}; font-size: 0.9rem; margin-top: 4px; }}
    .rating-bars {{ display: flex; flex-direction: column; gap: 12px; }}
    .bar-row {{ display: flex; align-items: center; gap: 12px; }}
    .bar {{ flex: 1; height: 8px; background: {text}10; border-radius: 100px; overflow: hidden; }}
    .fill {{ height: 100%; background: {primary}; border-radius: 100px; }}
    .bar-row span {{ color: {secondary}; font-size: 0.9rem; min-width: 40px; }}
    .stats-right {{ display: flex; flex-direction: column; gap: 24px; }}
    .review-card {{ background: {text}05; border-radius: 20px; padding: 28px; }}
    .review-card .stars {{ margin-bottom: 12px; }}
    .review-card p {{ color: {text}; line-height: 1.6; margin-bottom: 16px; }}
    .name {{ color: {primary}; font-weight: 600; }}
    @media (max-width: 900px) {{ .stats-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
