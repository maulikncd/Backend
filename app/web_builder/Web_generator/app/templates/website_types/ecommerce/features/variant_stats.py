from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Stats Focus - With numbers/stats"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    stats = [
        {"num": "50K+", "label": "Happy Customers"},
        {"num": "24h", "label": "Fast Delivery"},
        {"num": "100%", "label": "Secure Payments"},
        {"num": "30", "label": "Day Returns"},
    ]
    
    stats_html = ""
    for s in stats:
        stats_html += f'''<div class="stat-item"><span class="num">{s['num']}</span><span class="label">{s['label']}</span></div>'''
    
    return f'''
    <section class="ecom-features-stats" id="features">
        <div class="stats-container">{stats_html}</div>
    </section>
    
    <style>
    .ecom-features-stats {{ padding: 80px 24px; background: linear-gradient(135deg, {primary}15, {primary}05); }}
    .stats-container {{ max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; text-align: center; }}
    .stat-item {{ }}
    .num {{ display: block; font-size: 3rem; font-weight: 900; color: {primary}; margin-bottom: 8px; }}
    .label {{ color: {text}; font-weight: 600; }}
    @media (max-width: 768px) {{ .stats-container {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
