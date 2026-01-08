from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Grid Showcase Games - Game cards grid layout"""
    title = props.get("title", "Our Games")
    primary = colors.get("primary", "#8B5CF6")
    
    games = props.get("games", [
        {"name": "Shadow Warriors", "genre": "Action RPG", "rating": "4.9", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=500"},
        {"name": "Cyber Chase", "genre": "Racing", "rating": "4.7", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500"},
        {"name": "Battle Arena", "genre": "FPS", "rating": "4.8", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500"},
        {"name": "Legend Quest", "genre": "MMORPG", "rating": "4.6", "img": "https://images.unsplash.com/photo-1493711662062-fa541f7f3d24?w=500"}
    ])
    
    cards_html = ""
    for g in games:
        cards_html += f'''<div class="game-card"><div class="card-img" style="background-image: url('{g.get("img", "")}')"><div class="card-overlay"><a href="#" class="play-btn">▶</a></div></div><div class="card-body"><div class="card-top"><span class="genre">{g.get("genre", "")}</span><span class="rating">★ {g.get("rating", "")}</span></div><h3>{g.get("name", "")}</h3><div class="card-actions"><a href="#" class="btn-primary">Play Now</a><a href="#" class="btn-ghost">Details</a></div></div></div>'''
    
    return f'''
    <section class="games-grid-showcase" id="games"><div class="container"><div class="section-header"><span class="tag">Game Library</span><h2>{title}</h2></div><div class="games-grid">{cards_html}</div></div></section>
    <style>
    .games-grid-showcase {{ padding: 120px 40px; background: #0D0D15; }}
    .container {{ max-width: 1300px; margin: 0 auto; }}
    .section-header {{ text-align: center; margin-bottom: 60px; color: #fff; }}
    .tag {{ color: {primary}; text-transform: uppercase; letter-spacing: 4px; font-size: 0.9rem; }}
    .section-header h2 {{ font-size: 3.5rem; font-weight: 800; margin-top: 15px; }}
    .games-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; }}
    .game-card {{ background: #1a1a2e; border-radius: 16px; overflow: hidden; transition: 0.4s; }}
    .game-card:hover {{ transform: translateY(-10px); box-shadow: 0 20px 50px rgba(0,0,0,0.5); }}
    .card-img {{ height: 200px; background-size: cover; background-position: center; position: relative; }}
    .card-overlay {{ position: absolute; inset: 0; background: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center; opacity: 0; transition: 0.3s; }}
    .game-card:hover .card-overlay {{ opacity: 1; }}
    .play-btn {{ width: 60px; height: 60px; background: {primary}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 1.5rem; text-decoration: none; }}
    .card-body {{ padding: 25px; color: #fff; }}
    .card-top {{ display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 0.85rem; }}
    .genre {{ color: {primary}; text-transform: uppercase; letter-spacing: 1px; }}
    .rating {{ color: #FFD700; }}
    .card-body h3 {{ font-size: 1.4rem; margin-bottom: 20px; }}
    .card-actions {{ display: flex; gap: 15px; }}
    .btn-primary {{ padding: 12px 25px; background: {primary}; color: #fff; text-decoration: none; font-weight: 600; font-size: 0.9rem; transition: 0.3s; }}
    .btn-ghost {{ padding: 12px 25px; border: 1px solid #555; color: #fff; text-decoration: none; font-weight: 600; font-size: 0.9rem; transition: 0.3s; }}
    .btn-ghost:hover {{ border-color: {primary}; color: {primary}; }}
    </style>
    '''
