from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Fun Facts - Personal fun facts display"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    facts = [
        {"icon": "☕", "value": "1000+", "label": "Cups of Coffee"},
        {"icon": "💻", "value": "10K+", "label": "Lines of Code"},
        {"icon": "🎵", "value": "500+", "label": "Coding Playlists"},
        {"icon": "📚", "value": "50+", "label": "Books Read"},
    ]
    
    facts_html = ""
    for f in facts:
        facts_html += f'''
        <div class="fact-card">
            <span class="fact-icon">{f['icon']}</span>
            <span class="fact-value">{f['value']}</span>
            <span class="fact-label">{f['label']}</span>
        </div>
        '''
    
    return f'''
    <section class="portfolio-about-facts" id="about">
        <div class="facts-container">
            <div class="facts-text">
                <span class="tag">About</span>
                <h2>Beyond the code</h2>
                <p>A few fun facts about me and my journey</p>
            </div>
            <div class="facts-grid">{facts_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-about-facts {{ padding: 120px 24px; background: linear-gradient(135deg, {primary}08, {background}); }}
    .facts-container {{ max-width: 1100px; margin: 0 auto; }}
    .facts-text {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .facts-text h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .facts-text p {{ color: {secondary}; font-size: 1.2rem; }}
    .facts-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .fact-card {{ background: {background}; border-radius: 24px; padding: 40px 24px; text-align: center; box-shadow: 0 10px 40px {primary}08; transition: all 0.4s ease; }}
    .fact-card:hover {{ transform: translateY(-8px); box-shadow: 0 20px 60px {primary}15; }}
    .fact-icon {{ display: block; font-size: 3rem; margin-bottom: 16px; }}
    .fact-value {{ display: block; font-size: 2.5rem; font-weight: 900; color: {primary}; margin-bottom: 8px; }}
    .fact-label {{ display: block; color: {secondary}; }}
    @media (max-width: 900px) {{ .facts-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
