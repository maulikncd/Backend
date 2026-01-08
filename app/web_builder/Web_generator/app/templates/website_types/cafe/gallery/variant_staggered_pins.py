from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Staggered Grid Gallery - Pinterest-style varying heights"""
    title = props.get("title", "Visual Stories")
    images = props.get("images", [])[:9]
    primary = colors.get("primary", "#8B7355")
    
    if not images:
        images = [f"https://source.unsplash.com/400x{400 + (i%3)*100}/?cafe,coffee&sig={i}" for i in range(9)]
    
    items_html = ""
    heights = [350, 280, 400, 300, 380, 320, 360, 290, 340]
    for i, img in enumerate(images):
        if isinstance(img, dict): img = img.get("url", "")
        if "example.com" in img: img = f"https://source.unsplash.com/400x{heights[i%9]}/?cafe&sig={i}"
        items_html += f'<div class="stagger-item" style="height: {heights[i%9]}px"><img src="{img}" alt="Gallery"><div class="item-num">0{i+1}</div></div>'
    
    return f'''
    <section class="gallery-staggered" id="gallery">
        <div class="stagger-header"><span>Gallery</span><h2>{title}</h2></div>
        <div class="stagger-grid">{items_html}</div>
    </section>
    <style>
    .gallery-staggered {{ padding: 100px 24px; background: #fff; }}
    .stagger-header {{ text-align: center; margin-bottom: 60px; }}
    .stagger-header span {{ color: {primary}; text-transform: uppercase; letter-spacing: 4px; font-size: 0.85rem; }}
    .stagger-header h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; margin-top: 10px; }}
    .stagger-grid {{ columns: 3; column-gap: 20px; max-width: 1200px; margin: 0 auto; }}
    .stagger-item {{ margin-bottom: 20px; break-inside: avoid; position: relative; border-radius: 16px; overflow: hidden; }}
    .stagger-item img {{ width: 100%; height: 100%; object-fit: cover; transition: 0.5s; }}
    .stagger-item:hover img {{ transform: scale(1.05); }}
    .item-num {{ position: absolute; top: 20px; left: 20px; font-weight: 800; font-size: 1.5rem; color: #fff; text-shadow: 0 2px 10px rgba(0,0,0,0.3); }}
    @media (max-width: 900px) {{ .stagger-grid {{ columns: 2; }} }}
    @media (max-width: 600px) {{ .stagger-grid {{ columns: 1; }} }}
    </style>
    '''
