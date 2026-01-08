from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """News Cards - Blog/news style cards"""
    title = props.get("title", "Latest News")
    primary = colors.get("primary", "#FF4444")
    
    news = [
        {"title": "New Update 2.5 Released", "date": "Dec 27, 2024", "tag": "Patch Notes", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500"},
        {"title": "Winter Event Starting Soon", "date": "Dec 25, 2024", "tag": "Event", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=500"},
        {"title": "Pro League Season 5", "date": "Dec 20, 2024", "tag": "Esports", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=500"}
    ]
    
    cards_html = ""
    for n in news:
        cards_html += f'''<article class="news-card"><div class="card-img" style="background-image: url('{n["img"]}')"><span class="card-tag">{n["tag"]}</span></div><div class="card-content"><span class="date">{n["date"]}</span><h3>{n["title"]}</h3><a href="#">Read More →</a></div></article>'''
    
    return f'''
    <section class="gaming-news" id="news"><div class="container"><div class="section-header"><h2>{title}</h2><a href="#" class="view-all">View All News →</a></div><div class="news-grid">{cards_html}</div></div></section>
    <style>
    .gaming-news {{ padding: 100px 40px; background: #0D0D15; }}
    .container {{ max-width: 1200px; margin: 0 auto; }}
    .section-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 50px; }}
    .section-header h2 {{ font-size: 2.5rem; color: #fff; font-weight: 800; }}
    .view-all {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    .news-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }}
    .news-card {{ background: #1a1a2e; border-radius: 16px; overflow: hidden; transition: 0.3s; }}
    .news-card:hover {{ transform: translateY(-10px); }}
    .card-img {{ height: 200px; background-size: cover; background-position: center; position: relative; }}
    .card-tag {{ position: absolute; top: 15px; left: 15px; padding: 6px 15px; background: {primary}; color: #fff; font-size: 0.75rem; font-weight: 700; }}
    .card-content {{ padding: 25px; color: #fff; }}
    .date {{ color: #888; font-size: 0.85rem; }}
    .card-content h3 {{ font-size: 1.3rem; margin: 10px 0 20px; }}
    .card-content a {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    @media (max-width: 900px) {{ .news-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
