from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Screenshot Grid Gallery"""
    title = props.get("title", "Screenshots")
    primary = colors.get("primary", "#8B5CF6")
    
    images = [
        "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=600",
        "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600",
        "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600",
        "https://images.unsplash.com/photo-1493711662062-fa541f7f3d24?w=600"
    ]
    
    imgs_html = ""
    for img in images:
        imgs_html += f'<div class="gallery-item" style="background-image: url(\'{img}\')"><div class="overlay"><span>🔍</span></div></div>'
    
    return f'''
    <section class="gaming-gallery-grid" id="gallery"><div class="container"><h2>{title}</h2><div class="gallery-grid">{imgs_html}</div></div></section>
    <style>
    .gaming-gallery-grid {{ padding: 100px 40px; background: #0D0D15; }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    .gaming-gallery-grid h2 {{ font-size: 2.5rem; color: #fff; text-align: center; margin-bottom: 50px; }}
    .gallery-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }}
    .gallery-item {{ height: 300px; background-size: cover; background-position: center; border-radius: 16px; position: relative; overflow: hidden; cursor: pointer; }}
    .gallery-item .overlay {{ position: absolute; inset: 0; background: {primary}90; display: flex; align-items: center; justify-content: center; opacity: 0; transition: 0.3s; }}
    .gallery-item:hover .overlay {{ opacity: 1; }}
    .overlay span {{ font-size: 3rem; }}
    @media (max-width: 768px) {{ .gallery-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
