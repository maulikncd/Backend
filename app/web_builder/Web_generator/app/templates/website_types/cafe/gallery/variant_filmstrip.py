from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Filmstrip Gallery - Continuous horizontal film-style"""
    title = props.get("title", "Behind The Scenes")
    images = props.get("images", [])[:8]
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    if not images:
        images = [f"https://source.unsplash.com/400x300/?cafe,coffee&sig={i}" for i in range(8)]
    
    frames_html = ""
    for i, img in enumerate(images):
        if isinstance(img, dict): img = img.get("url", "")
        if "example.com" in img: img = f"https://source.unsplash.com/400x300/?cafe&sig={i}"
        frames_html += f'<div class="film-frame"><div class="frame-holes top"></div><img src="{img}" alt="Scene {i+1}"><div class="frame-holes bottom"></div></div>'
    
    return f'''
    <section class="gallery-filmstrip" id="gallery">
        <div class="filmstrip-header"><h2>{title}</h2></div>
        <div class="filmstrip-track">{frames_html}</div>
    </section>
    <style>
    .gallery-filmstrip {{ padding: 80px 0; background: {text}; overflow: hidden; }}
    .filmstrip-header {{ text-align: center; margin-bottom: 50px; }}
    .filmstrip-header h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; color: #fff; }}
    .filmstrip-track {{ display: flex; gap: 0; animation: scroll 30s linear infinite; }}
    @keyframes scroll {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}
    .film-frame {{ flex: 0 0 300px; background: #1a1a1a; padding: 10px; }}
    .frame-holes {{ height: 15px; display: flex; justify-content: space-between; padding: 0 10px; }}
    .frame-holes::before, .frame-holes::after {{ content: ''; width: 10px; height: 10px; background: #333; border-radius: 2px; }}
    .film-frame img {{ width: 100%; height: 220px; object-fit: cover; }}
    </style>
    '''
