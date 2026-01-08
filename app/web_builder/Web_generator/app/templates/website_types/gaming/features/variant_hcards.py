from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Horizontal Cards Features"""
    title = props.get("title", "What Makes Us Different")
    primary = colors.get("primary", "#00F0FF")
    
    features = [
        {"icon": "⚡", "title": "Fast-Paced Action", "desc": "Intense gameplay with quick reflexes"},
        {"icon": "🌍", "title": "Vast Open World", "desc": "Explore massive environments"},
        {"icon": "🎯", "title": "Precision Controls", "desc": "Responsive and smooth gameplay"},
        {"icon": "🤝", "title": "Co-op Mode", "desc": "Play with friends online"}
    ]
    
    cards_html = ""
    for f in features:
        cards_html += f'<div class="feature-card"><span class="icon">{f["icon"]}</span><h4>{f["title"]}</h4><p>{f["desc"]}</p></div>'
    
    return f'''
    <section class="gaming-features-hcards" id="features"><div class="container"><h2>{title}</h2><div class="cards-scroll">{cards_html}</div></div></section>
    <style>
    .gaming-features-hcards {{ padding: 100px 0; background: #0D0D15; overflow: hidden; }}
    .container {{ max-width: 1300px; margin: 0 auto; padding: 0 40px; }}
    .gaming-features-hcards h2 {{ font-size: 2.5rem; color: #fff; margin-bottom: 50px; }}
    .cards-scroll {{ display: flex; gap: 25px; overflow-x: auto; padding-bottom: 20px; scrollbar-width: none; }}
    .cards-scroll::-webkit-scrollbar {{ display: none; }}
    .feature-card {{ flex: 0 0 300px; background: linear-gradient(135deg, #1a1a2e, #252540); padding: 40px 30px; border-radius: 20px; color: #fff; transition: 0.3s; border: 1px solid transparent; }}
    .feature-card:hover {{ border-color: {primary}; transform: translateY(-10px); }}
    .icon {{ font-size: 3rem; display: block; margin-bottom: 20px; }}
    .feature-card h4 {{ font-size: 1.4rem; margin-bottom: 10px; }}
    .feature-card p {{ color: rgba(255,255,255,0.6); line-height: 1.6; }}
    </style>
    '''
