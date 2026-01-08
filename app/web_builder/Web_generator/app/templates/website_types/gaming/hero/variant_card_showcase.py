from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Card Showcase Hero - Multiple game cards"""
    title = props.get("title", "Featured Games")
    
    # Use colors from user's selected palette - no hardcoded fallbacks
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    games = [
        {"name": "Shadow Quest", "genre": "RPG", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=400"},
        {"name": "Speed Racer", "genre": "Racing", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400"},
        {"name": "Battle Royal", "genre": "FPS", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400"}
    ]
    
    cards_html = ""
    for g in games:
        cards_html += f'<div class="game-card"><img src="{g["img"]}" alt="{g["name"]}"><div class="card-info"><span class="genre">{g["genre"]}</span><h3>{g["name"]}</h3><a href="#">Play Now</a></div></div>'
    
    return f'''
    <section class="gaming-hero-cards" id="hero">
        <div class="cards-content"><span class="section-tag">Featured</span><h1>{title}</h1><p>Discover our most popular titles</p></div>
        <div class="cards-row">{cards_html}</div>
    </section>
    <style>
    .gaming-hero-cards {{ min-height: 100vh; background: linear-gradient(135deg, {background}, {secondary}20); padding: 150px 40px 80px; display: flex; flex-direction: column; justify-content: center; }}
    .cards-content {{ text-align: center; color: {text}; margin-bottom: 60px; }}
    .section-tag {{ color: {primary}; text-transform: uppercase; letter-spacing: 5px; font-size: 0.9rem; }}
    .gaming-hero-cards h1 {{ font-size: clamp(3rem, 6vw, 5rem); font-weight: 900; margin: 20px 0; color: {text}; }}
    .gaming-hero-cards p {{ color: {secondary}; font-size: 1.2rem; }}
    .cards-row {{ display: flex; gap: 30px; justify-content: center; flex-wrap: wrap; }}
    .game-card {{ width: 350px; background: {background}; border-radius: 20px; overflow: hidden; transition: 0.4s; border: 1px solid {primary}20; }}
    .game-card:hover {{ transform: translateY(-20px) scale(1.02); box-shadow: 0 30px 60px {primary}30; }}
    .game-card img {{ width: 100%; height: 250px; object-fit: cover; }}
    .card-info {{ padding: 25px; color: {text}; }}
    .genre {{ color: {primary}; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px; }}
    .card-info h3 {{ font-size: 1.5rem; margin: 10px 0; color: {text}; }}
    .card-info a {{ display: inline-block; margin-top: 15px; padding: 12px 30px; background: {primary}; color: {background}; text-decoration: none; font-weight: 600; transition: 0.3s; }}
    .card-info a:hover {{ transform: scale(1.05); }}
    </style>
    '''
