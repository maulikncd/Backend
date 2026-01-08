from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Video Trailer Gallery"""
    title = props.get("title", "Watch Trailers")
    primary = colors.get("primary", "#FF4444")
    
    return f'''
    <section class="gaming-gallery-trailers" id="gallery"><div class="container"><h2>{title}</h2><div class="trailer-grid">
        <div class="trailer-main"><div class="video-thumb" style="background: url('https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=1200') center/cover"><div class="play-btn">▶</div><span class="duration">2:45</span></div><h3>Official Launch Trailer</h3></div>
        <div class="trailer-list">
            <div class="trailer-item"><div class="thumb" style="background: url('https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400') center/cover"><span>▶</span></div><div class="info"><h4>Gameplay Preview</h4><span>1:30</span></div></div>
            <div class="trailer-item"><div class="thumb" style="background: url('https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400') center/cover"><span>▶</span></div><div class="info"><h4>Story Trailer</h4><span>3:00</span></div></div>
        </div>
    </div></div></section>
    <style>
    .gaming-gallery-trailers {{ padding: 100px 40px; background: #0D0D15; }}
    .container {{ max-width: 1100px; margin: 0 auto; }}
    .gaming-gallery-trailers h2 {{ font-size: 2.5rem; color: #fff; text-align: center; margin-bottom: 50px; }}
    .trailer-grid {{ display: grid; grid-template-columns: 2fr 1fr; gap: 30px; }}
    .trailer-main {{ }}
    .video-thumb {{ height: 400px; border-radius: 16px; display: flex; align-items: center; justify-content: center; position: relative; cursor: pointer; }}
    .play-btn {{ width: 80px; height: 80px; background: {primary}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; color: #fff; }}
    .duration {{ position: absolute; bottom: 20px; right: 20px; background: rgba(0,0,0,0.8); padding: 5px 12px; border-radius: 5px; color: #fff; font-size: 0.9rem; }}
    .trailer-main h3 {{ color: #fff; margin-top: 20px; font-size: 1.3rem; }}
    .trailer-list {{ display: flex; flex-direction: column; gap: 20px; }}
    .trailer-item {{ display: flex; gap: 15px; padding: 15px; background: #1a1a2e; border-radius: 12px; cursor: pointer; transition: 0.3s; }}
    .trailer-item:hover {{ background: #252540; }}
    .thumb {{ width: 120px; height: 80px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: #fff; }}
    .info h4 {{ color: #fff; font-size: 1rem; margin-bottom: 5px; }}
    .info span {{ color: #888; font-size: 0.85rem; }}
    @media (max-width: 900px) {{ .trailer-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
