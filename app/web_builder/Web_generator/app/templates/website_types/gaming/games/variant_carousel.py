from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Carousel Games - Horizontal scrolling"""
    title = props.get("title", "Popular Games")
    primary = colors.get("primary", "#00F0FF")
    
    return f'''
    <section class="games-carousel" id="games"><div class="carousel-header"><h2>{title}</h2><div class="nav-arrows"><button>←</button><button>→</button></div></div><div class="carousel-track"><div class="game-slide featured"><img src="https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=800"><div class="slide-info"><span class="badge">Featured</span><h3>Shadow Warriors</h3><p>Epic action RPG adventure</p><a href="#">Play Free</a></div></div><div class="game-slide"><img src="https://images.unsplash.com/photo-1511512578047-dfb367046420?w=600"><div class="slide-info"><h3>Cyber Racer</h3><a href="#">Details →</a></div></div><div class="game-slide"><img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600"><div class="slide-info"><h3>Battle Zone</h3><a href="#">Details →</a></div></div></div></section>
    <style>
    .games-carousel {{ padding: 100px 0; background: #0a0a0f; overflow: hidden; }}
    .carousel-header {{ max-width: 1300px; margin: 0 auto 40px; padding: 0 40px; display: flex; justify-content: space-between; align-items: center; color: #fff; }}
    .carousel-header h2 {{ font-size: 2.5rem; font-weight: 800; }}
    .nav-arrows button {{ width: 50px; height: 50px; border: 2px solid {primary}; background: transparent; color: {primary}; font-size: 1.2rem; cursor: pointer; margin-left: 10px; transition: 0.3s; }}
    .nav-arrows button:hover {{ background: {primary}; color: #000; }}
    .carousel-track {{ display: flex; gap: 30px; padding: 0 40px; overflow-x: auto; scroll-behavior: smooth; scrollbar-width: none; }}
    .carousel-track::-webkit-scrollbar {{ display: none; }}
    .game-slide {{ flex: 0 0 350px; position: relative; border-radius: 16px; overflow: hidden; height: 450px; }}
    .game-slide.featured {{ flex: 0 0 600px; }}
    .game-slide img {{ width: 100%; height: 100%; object-fit: cover; }}
    .slide-info {{ position: absolute; bottom: 0; left: 0; right: 0; padding: 30px; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); color: #fff; }}
    .badge {{ display: inline-block; padding: 6px 15px; background: {primary}; font-size: 0.75rem; font-weight: 700; margin-bottom: 10px; }}
    .slide-info h3 {{ font-size: 1.8rem; margin-bottom: 8px; }}
    .slide-info p {{ color: rgba(255,255,255,0.7); margin-bottom: 15px; }}
    .slide-info a {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    </style>
    '''
