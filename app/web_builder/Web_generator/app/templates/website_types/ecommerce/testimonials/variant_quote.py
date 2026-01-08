from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Featured Quote - Large single quote"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-testimonials-quote" id="testimonials">
        <div class="quote-container">
            <div class="quote-content">
                <span class="quote-mark">"</span>
                <blockquote>This store has completely changed how I shop online. The quality is unmatched, shipping is lightning fast, and the customer service is incredible. I've recommended it to everyone I know!</blockquote>
                <div class="author">
                    <div class="avatar">S</div>
                    <div class="info"><strong>Sarah Johnson</strong><span>Verified Customer • 15+ orders</span></div>
                    <div class="rating">⭐⭐⭐⭐⭐</div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-testimonials-quote {{ padding: 160px 24px; background: linear-gradient(135deg, {primary}10, {background}); }}
    .quote-container {{ max-width: 900px; margin: 0 auto; text-align: center; }}
    .quote-mark {{ font-size: 10rem; color: {primary}20; line-height: 0.3; display: block; margin-bottom: 20px; }}
    blockquote {{ font-size: clamp(1.5rem, 3vw, 2rem); color: {text}; line-height: 1.6; margin-bottom: 48px; font-weight: 500; }}
    .author {{ display: flex; justify-content: center; align-items: center; gap: 20px; }}
    .avatar {{ width: 64px; height: 64px; background: {primary}; color: {background}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 700; }}
    .info {{ text-align: left; }}
    .info strong {{ display: block; color: {text}; font-size: 1.2rem; }}
    .info span {{ color: {secondary}; }}
    .rating {{ font-size: 1.2rem; }}
    </style>
    '''
