from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Marquee - Scrolling testimonials"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    reviews = [
        {"name": "Sarah J.", "text": "Amazing quality! Will buy again."},
        {"name": "Mike R.", "text": "Fast shipping, great service!"},
        {"name": "Emily L.", "text": "Love everything I ordered!"},
        {"name": "David K.", "text": "Best online store ever!"},
    ]
    
    marquee_html = ""
    for r in reviews:
        marquee_html += f'''<div class="marquee-card"><p>"{r['text']}"</p><span>— {r['name']} ⭐⭐⭐⭐⭐</span></div>'''
    
    return f'''
    <section class="ecom-testimonials-marquee" id="testimonials">
        <div class="marquee-header"><h2>Customer Love</h2></div>
        <div class="marquee-track"><div class="marquee-content">{marquee_html}{marquee_html}</div></div>
    </section>
    
    <style>
    .ecom-testimonials-marquee {{ padding: 120px 0; background: {background}; overflow: hidden; }}
    .marquee-header {{ text-align: center; margin-bottom: 60px; }}
    .marquee-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .marquee-track {{ overflow: hidden; }}
    .marquee-content {{ display: flex; gap: 32px; animation: marquee 30s linear infinite; width: max-content; }}
    @keyframes marquee {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-50%); }} }}
    .marquee-card {{ background: {text}05; border-radius: 20px; padding: 32px; min-width: 350px; }}
    .marquee-card p {{ color: {text}; font-size: 1.1rem; line-height: 1.6; margin-bottom: 16px; font-style: italic; }}
    .marquee-card span {{ color: {primary}; font-weight: 600; }}
    .marquee-track:hover .marquee-content {{ animation-play-state: paused; }}
    </style>
    '''
