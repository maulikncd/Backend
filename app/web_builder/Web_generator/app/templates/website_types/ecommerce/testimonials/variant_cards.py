from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Cards Grid - Testimonial cards grid"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    reviews = [
        {"name": "Sarah J.", "rating": 5, "text": "Amazing quality! The product exceeded my expectations. Will definitely buy again."},
        {"name": "Mike R.", "rating": 5, "text": "Fast shipping and great customer service. Highly recommend this store!"},
        {"name": "Emily L.", "rating": 5, "text": "Love everything I've ordered. The quality is outstanding for the price."},
    ]
    
    cards_html = ""
    for r in reviews:
        stars = "⭐" * r['rating']
        cards_html += f'''
        <div class="review-card">
            <div class="stars">{stars}</div>
            <p>"{r['text']}"</p>
            <div class="reviewer"><span class="avatar">{r['name'][0]}</span><span class="name">{r['name']}</span></div>
        </div>
        '''
    
    return f'''
    <section class="ecom-testimonials-grid" id="testimonials">
        <div class="test-container">
            <div class="test-header"><h2>What Our Customers Say</h2></div>
            <div class="reviews-grid">{cards_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-testimonials-grid {{ padding: 120px 24px; background: {background}; }}
    .test-container {{ max-width: 1100px; margin: 0 auto; }}
    .test-header {{ text-align: center; margin-bottom: 60px; }}
    .test-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .reviews-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }}
    .review-card {{ background: {text}05; border-radius: 24px; padding: 32px; }}
    .stars {{ font-size: 1.2rem; margin-bottom: 16px; }}
    .review-card p {{ color: {text}; font-size: 1.1rem; line-height: 1.7; margin-bottom: 24px; font-style: italic; }}
    .reviewer {{ display: flex; align-items: center; gap: 12px; }}
    .avatar {{ width: 48px; height: 48px; background: {primary}; color: {background}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; }}
    .name {{ font-weight: 600; color: {text}; }}
    @media (max-width: 900px) {{ .reviews-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
