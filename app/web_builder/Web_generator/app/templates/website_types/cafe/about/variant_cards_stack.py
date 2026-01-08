from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Cards Stack About - Layered info cards with depth"""
    title = props.get("title", "Why We're Different")
    stats = props.get("stats", [])
    milestones = props.get("milestones", [])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    bg = colors.get("background", "#FAF7F4")
    
    cards = []
    if milestones:
        for ms in milestones[:3]:
            cards.append({"title": ms.get("title", ""), "desc": ms.get("description", "")[:80], "year": ms.get("year", "")})
    else:
        cards = [
            {"title": "Founded", "desc": "Started with passion for exceptional coffee", "year": "2020"},
            {"title": "Expansion", "desc": "Opened our second location downtown", "year": "2022"},
            {"title": "Recognition", "desc": "Named best local cafe in the city", "year": "2024"}
        ]
    
    cards_html = ""
    for i, card in enumerate(cards):
        offset = i * 30
        cards_html += f'''
        <div class="stack-card" style="--offset: {offset}px; --index: {3-i}">
            <span class="card-year">{card["year"]}</span>
            <h4>{card["title"]}</h4>
            <p>{card["desc"]}</p>
        </div>
        '''
    
    return f'''
    <section class="about-stack" id="about">
        <div class="stack-container">
            <div class="stack-left">
                <h2>{title}</h2>
                <p>Our journey has been marked by dedication, innovation, and an unwavering commitment to quality.</p>
                <a href="#contact" class="stack-btn">Get in Touch</a>
            </div>
            <div class="stack-right">
                <div class="cards-wrapper">
                    {cards_html}
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .about-stack {{ padding: 120px 40px; background: {bg}; }}
    .stack-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }}
    .stack-left h2 {{ font-family: 'Playfair Display', serif; font-size: 3.5rem; color: {text}; margin-bottom: 24px; }}
    .stack-left p {{ font-size: 1.1rem; line-height: 1.8; color: #666; margin-bottom: 40px; }}
    .stack-btn {{ display: inline-block; padding: 16px 40px; background: {primary}; color: #fff; text-decoration: none; border-radius: 50px; font-weight: 600; transition: 0.3s; }}
    .stack-btn:hover {{ transform: translateY(-3px); box-shadow: 0 15px 30px {primary}40; }}
    .cards-wrapper {{ position: relative; height: 400px; }}
    .stack-card {{ position: absolute; top: var(--offset); left: var(--offset); width: calc(100% - 60px); background: #fff; padding: 40px; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.08); z-index: var(--index); transition: 0.4s; }}
    .stack-card:hover {{ transform: translateY(-10px) scale(1.02); z-index: 10; }}
    .card-year {{ display: inline-block; padding: 6px 16px; background: {primary}; color: #fff; border-radius: 50px; font-size: 0.85rem; font-weight: 600; margin-bottom: 20px; }}
    .stack-card h4 {{ font-family: 'Playfair Display', serif; font-size: 1.8rem; color: {text}; margin-bottom: 12px; }}
    .stack-card p {{ color: #888; line-height: 1.6; }}
    @media (max-width: 968px) {{ .stack-container {{ grid-template-columns: 1fr; }} .cards-wrapper {{ height: auto; position: static; }} .stack-card {{ position: static; width: 100%; margin-bottom: 20px; }} }}
    </style>
    '''
