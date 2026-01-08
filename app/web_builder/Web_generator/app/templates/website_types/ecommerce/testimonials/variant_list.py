from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal List - Clean list style"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    reviews = [
        {"name": "Sarah J.", "product": "Premium Headphones", "text": "Best purchase I've made this year!"},
        {"name": "Mike R.", "product": "Smart Watch", "text": "Exceeded all my expectations."},
        {"name": "Emily L.", "product": "Wireless Speaker", "text": "Amazing sound quality."},
    ]
    
    list_html = ""
    for r in reviews:
        list_html += f'''
        <div class="review-row">
            <div class="review-text"><p>"{r['text']}"</p><span class="product">on {r['product']}</span></div>
            <div class="review-author"><span class="name">{r['name']}</span><span class="rating">⭐⭐⭐⭐⭐</span></div>
        </div>
        '''
    
    return f'''
    <section class="ecom-testimonials-list" id="testimonials">
        <div class="list-container">
            <div class="list-header"><h2>Recent Reviews</h2></div>
            <div class="reviews-list">{list_html}</div>
        </div>
    </section>
    
    <style>
    .ecom-testimonials-list {{ padding: 120px 24px; background: {background}; }}
    .list-container {{ max-width: 900px; margin: 0 auto; }}
    .list-header {{ margin-bottom: 48px; }}
    .list-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .reviews-list {{ display: flex; flex-direction: column; }}
    .review-row {{ display: flex; justify-content: space-between; align-items: center; padding: 32px 0; border-bottom: 1px solid {text}10; }}
    .review-text p {{ color: {text}; font-size: 1.2rem; margin-bottom: 6px; }}
    .product {{ color: {secondary}; font-size: 0.9rem; }}
    .review-author {{ text-align: right; }}
    .name {{ display: block; color: {text}; font-weight: 600; margin-bottom: 4px; }}
    .rating {{ color: {primary}; }}
    @media (max-width: 768px) {{ .review-row {{ flex-direction: column; align-items: flex-start; gap: 16px; }} .review-author {{ text-align: left; }} }}
    </style>
    '''
