from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Studio Timeline About"""
    title = props.get("title", "Our Journey")
    primary = colors.get("primary", "#00F0FF")
    
    milestones = [
        {"year": "2018", "title": "Founded", "desc": "Started with a dream"},
        {"year": "2020", "title": "First Game", "desc": "Launched our debut title"},
        {"year": "2022", "title": "10M Players", "desc": "Hit major milestone"},
        {"year": "2024", "title": "Global", "desc": "Offices worldwide"}
    ]
    
    timeline_html = ""
    for m in milestones:
        timeline_html += f'<div class="timeline-item"><span class="year">{m["year"]}</span><div class="content"><h4>{m["title"]}</h4><p>{m["desc"]}</p></div></div>'
    
    return f'''
    <section class="gaming-about-timeline" id="about"><div class="container"><h2>{title}</h2><div class="timeline">{timeline_html}</div></div></section>
    <style>
    .gaming-about-timeline {{ padding: 100px 40px; background: linear-gradient(135deg, #0D0D15, #1a1a2e); }}
    .container {{ max-width: 900px; margin: 0 auto; text-align: center; color: #fff; }}
    .gaming-about-timeline h2 {{ font-size: 3rem; font-weight: 800; margin-bottom: 60px; }}
    .timeline {{ position: relative; padding-left: 50px; text-align: left; }}
    .timeline::before {{ content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: {primary}30; }}
    .timeline-item {{ position: relative; margin-bottom: 50px; }}
    .timeline-item::before {{ content: ''; position: absolute; left: -56px; top: 5px; width: 14px; height: 14px; background: {primary}; border-radius: 50%; }}
    .year {{ color: {primary}; font-weight: 700; font-size: 0.9rem; letter-spacing: 2px; }}
    .content h4 {{ font-size: 1.5rem; margin: 10px 0; }}
    .content p {{ color: rgba(255,255,255,0.6); }}
    </style>
    '''
