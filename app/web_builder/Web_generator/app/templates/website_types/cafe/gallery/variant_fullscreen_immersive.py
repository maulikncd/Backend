from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Fullscreen Slider Gallery - Immersive full-viewport slides"""
    images = props.get("images", [])[:5]
    if not images:
        images = [f"https://source.unsplash.com/1920x1080/?cafe,coffee&sig={i}" for i in range(5)]
    
    main_img = images[0]
    if isinstance(main_img, dict): main_img = main_img.get("url", "")
    if "example.com" in main_img: main_img = "https://source.unsplash.com/1920x1080/?cafe"
    
    return f'''
    <section class="gallery-fullscreen" id="gallery" style="background-image: url('{main_img}')">
        <div class="fs-overlay"></div>
        <div class="fs-content"><span class="fs-count">01 / 0{len(images)}</span><h2>Visual Journey</h2><p>Swipe to explore our cafe atmosphere</p></div>
        <div class="fs-nav"><button class="fs-prev">←</button><button class="fs-next">→</button></div>
    </section>
    <style>
    .gallery-fullscreen {{ min-height: 100vh; background-size: cover; background-position: center; position: relative; display: flex; align-items: center; justify-content: center; text-align: center; color: #fff; }}
    .fs-overlay {{ position: absolute; inset: 0; background: rgba(0,0,0,0.5); }}
    .fs-content {{ position: relative; z-index: 2; }}
    .fs-count {{ display: block; font-size: 0.9rem; letter-spacing: 4px; margin-bottom: 20px; opacity: 0.7; }}
    .gallery-fullscreen h2 {{ font-family: 'Playfair Display', serif; font-size: 5rem; margin-bottom: 20px; }}
    .gallery-fullscreen p {{ font-size: 1.2rem; opacity: 0.8; }}
    .fs-nav {{ position: absolute; bottom: 60px; left: 50%; transform: translateX(-50%); display: flex; gap: 20px; z-index: 2; }}
    .fs-prev, .fs-next {{ width: 60px; height: 60px; border: 2px solid #fff; background: transparent; color: #fff; border-radius: 50%; font-size: 1.3rem; cursor: pointer; transition: 0.3s; }}
    .fs-prev:hover, .fs-next:hover {{ background: #fff; color: #000; }}
    </style>
    '''
