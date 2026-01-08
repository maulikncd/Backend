from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Video Reviews - Video testimonials"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="ecom-testimonials-video" id="testimonials">
        <div class="video-container">
            <div class="video-header"><span class="tag">Real Reviews</span><h2>Hear From Our Customers</h2></div>
            <div class="videos-grid">
                <div class="video-card main"><div class="play-btn">▶</div><div class="video-info"><span class="name">Sarah talks about her experience</span><span class="duration">2:34</span></div></div>
                <div class="video-card"><div class="play-btn">▶</div><span class="name">Mike's review</span></div>
                <div class="video-card"><div class="play-btn">▶</div><span class="name">Emily's unboxing</span></div>
                <div class="video-card"><div class="play-btn">▶</div><span class="name">David's feedback</span></div>
            </div>
        </div>
    </section>
    
    <style>
    .ecom-testimonials-video {{ padding: 120px 24px; background: {background}; }}
    .video-container {{ max-width: 1100px; margin: 0 auto; }}
    .video-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 16px; }}
    .video-header h2 {{ font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .videos-grid {{ display: grid; grid-template-columns: 2fr 1fr; grid-template-rows: repeat(3, 120px); gap: 20px; }}
    .video-card {{ background: linear-gradient(135deg, {primary}20, {primary}05); border-radius: 20px; position: relative; display: flex; align-items: center; justify-content: center; cursor: pointer; }}
    .video-card.main {{ grid-row: span 3; }}
    .play-btn {{ width: 60px; height: 60px; background: {primary}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: {background}; font-size: 1.2rem; }}
    .video-card.main .play-btn {{ width: 80px; height: 80px; font-size: 1.5rem; }}
    .video-info {{ position: absolute; bottom: 20px; left: 20px; }}
    .video-card .name {{ display: block; color: {text}; font-weight: 600; }}
    .video-info .name {{ font-size: 1.1rem; }}
    .duration {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .videos-grid {{ grid-template-columns: 1fr; }} .video-card.main {{ grid-row: span 1; min-height: 250px; }} }}
    </style>
    '''
