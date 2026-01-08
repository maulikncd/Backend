from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Numbers Showcase About - Bold statistics-driven layout"""
    title = props.get("title", "By The Numbers")
    story = props.get("story", "")[:250]
    stats = props.get("stats", [])
    
    primary = colors.get("primary", "#8B7355")
    text = colors.get("text", "#2D2013")
    
    if not stats:
        stats = [
            {"value": "500K+", "label": "Cups Served"},
            {"value": "15+", "label": "Years Experience"},
            {"value": "30+", "label": "Coffee Varieties"},
            {"value": "98%", "label": "Happy Customers"}
        ]
    
    stats_html = ""
    for stat in stats[:4]:
        stats_html += f'''
        <div class="big-stat">
            <span class="stat-value">{stat.get("value", "0")}</span>
            <span class="stat-label">{stat.get("label", "")}</span>
        </div>
        '''
    
    return f'''
    <section class="about-numbers" id="about">
        <div class="numbers-container">
            <div class="numbers-top">
                <h2>{title}</h2>
                <p>{story if story else "Our story is written in the smiles of our customers and the quality of every cup we serve."}</p>
            </div>
            <div class="numbers-grid">
                {stats_html}
            </div>
        </div>
    </section>
    
    <style>
    .about-numbers {{ padding: 120px 40px; background: linear-gradient(135deg, {primary}, #5C4A3D); color: #fff; }}
    .numbers-container {{ max-width: 1200px; margin: 0 auto; }}
    .numbers-top {{ text-align: center; margin-bottom: 80px; }}
    .about-numbers h2 {{ font-family: 'Playfair Display', serif; font-size: 4rem; margin-bottom: 20px; }}
    .about-numbers .numbers-top p {{ font-size: 1.2rem; max-width: 600px; margin: 0 auto; opacity: 0.85; line-height: 1.8; }}
    .numbers-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; }}
    .big-stat {{ text-align: center; padding: 40px 20px; background: rgba(255,255,255,0.1); border-radius: 20px; backdrop-filter: blur(10px); transition: 0.3s; }}
    .big-stat:hover {{ background: rgba(255,255,255,0.2); transform: translateY(-10px); }}
    .stat-value {{ display: block; font-size: 4rem; font-weight: 800; margin-bottom: 10px; }}
    .stat-label {{ font-size: 1rem; text-transform: uppercase; letter-spacing: 2px; opacity: 0.8; }}
    @media (max-width: 968px) {{ .numbers-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 600px) {{ .numbers-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
