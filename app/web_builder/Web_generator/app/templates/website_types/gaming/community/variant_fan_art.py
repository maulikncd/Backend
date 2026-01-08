from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Fan Art - Community art gallery"""
    title = props.get("title", "Fan Art Gallery")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    artworks = [
        {"artist": "ArtMaster", "title": "Shadow Warrior", "likes": "2.5K", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500"},
        {"artist": "PixelPro", "title": "Neon City", "likes": "1.8K", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=500"},
        {"artist": "DrawKing", "title": "Battle Scene", "likes": "3.2K", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500"},
        {"artist": "SketchLord", "title": "Hero Portrait", "likes": "1.4K", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f069d?w=500"},
    ]
    
    gallery_html = ""
    for a in artworks:
        gallery_html += f'''
        <div class="art-card">
            <img src="{a['img']}" alt="{a['title']}">
            <div class="art-overlay">
                <h4>{a['title']}</h4>
                <span class="artist">by {a['artist']}</span>
                <span class="likes">❤️ {a['likes']}</span>
            </div>
        </div>
        '''
    
    return f'''
    <section class="gaming-community-art" id="community">
        <div class="art-container">
            <div class="art-header">
                <h2>{title}</h2>
                <a href="#" class="submit-btn">Submit Artwork</a>
            </div>
            <div class="art-grid">{gallery_html}</div>
        </div>
    </section>
    
    <style>
    .gaming-community-art {{ padding: 120px 24px; background: {background}; }}
    .art-container {{ max-width: 1200px; margin: 0 auto; }}
    .art-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 48px; }}
    .art-header h2 {{ font-family: 'Rajdhani', sans-serif; font-size: 2.5rem; font-weight: 800; color: {text}; }}
    .submit-btn {{ padding: 12px 28px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 10px; }}
    .art-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .art-card {{ position: relative; border-radius: 16px; overflow: hidden; aspect-ratio: 1; cursor: pointer; }}
    .art-card img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }}
    .art-card:hover img {{ transform: scale(1.1); }}
    .art-overlay {{ position: absolute; inset: 0; background: linear-gradient(to top, {background}E6, transparent 50%); padding: 20px; display: flex; flex-direction: column; justify-content: flex-end; opacity: 0; transition: opacity 0.3s ease; }}
    .art-card:hover .art-overlay {{ opacity: 1; }}
    .art-overlay h4 {{ font-size: 1.1rem; font-weight: 700; color: {text}; margin-bottom: 4px; }}
    .artist {{ color: {secondary}; font-size: 0.9rem; }}
    .likes {{ color: {primary}; font-weight: 700; margin-top: auto; }}
    @media (max-width: 900px) {{ .art-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
