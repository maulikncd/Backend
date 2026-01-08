from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Carousel - Sliding testimonials"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-testimonials-carousel" id="testimonials">
        <div class="carousel-container">
            <div class="carousel-header">
                <h2>Customer Reviews</h2>
                <div class="nav-dots"><span class="dot active"></span><span class="dot"></span><span class="dot"></span></div>
            </div>
            <div class="carousel-track">
                <div class="review-slide active">
                    <div class="quote-mark">"</div>
                    <p>This is hands down the best online shopping experience I've ever had. The quality of products is exceptional!</p>
                    <div class="reviewer">
                        <div class="avatar">S</div>
                        <div class="info"><strong>Sarah Johnson</strong><span>Verified Buyer</span></div>
                        <div class="rating">⭐⭐⭐⭐⭐</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-testimonials-carousel {{ padding: 120px 24px; background: linear-gradient(135deg, {primary}08, {background}); }}
    .carousel-container {{ max-width: 800px; margin: 0 auto; text-align: center; }}
    .carousel-header {{ margin-bottom: 60px; }}
    .carousel-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; margin-bottom: 24px; }}
    .nav-dots {{ display: flex; justify-content: center; gap: 10px; }}
    .dot {{ width: 10px; height: 10px; background: {text}20; border-radius: 50%; cursor: pointer; transition: all 0.3s ease; }}
    .dot.active {{ background: {primary}; width: 30px; border-radius: 10px; }}
    .quote-mark {{ font-size: 8rem; color: {primary}20; line-height: 0.5; margin-bottom: 20px; }}
    .review-slide p {{ font-size: 1.4rem; color: {text}; line-height: 1.7; margin-bottom: 40px; }}
    .reviewer {{ display: flex; justify-content: center; align-items: center; gap: 16px; }}
    .avatar {{ width: 56px; height: 56px; background: {primary}; color: {background}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; font-weight: 700; }}
    .info {{ text-align: left; }}
    .info strong {{ display: block; color: {text}; font-size: 1.1rem; }}
    .info span {{ color: {secondary}; font-size: 0.9rem; }}
    .rating {{ margin-left: 16px; }}
    </style>
    '''
