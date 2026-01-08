from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Marquee Skills - Scrolling skills ticker"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    skills = ["React", "Next.js", "Vue", "TypeScript", "Node.js", "Python", "PostgreSQL", "MongoDB", "Docker", "AWS", "Figma", "Git"]
    
    marquee_html = ""
    for s in skills:
        marquee_html += f'<span class="marquee-item">{s}</span><span class="dot">•</span>'
    
    return f'''
    <section class="portfolio-skills-marquee" id="skills">
        <div class="marquee-container">
            <div class="marquee-header"><h2>Technologies</h2></div>
            <div class="marquee-track">
                <div class="marquee-content">{marquee_html}{marquee_html}</div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-skills-marquee {{ padding: 120px 24px; background: {background}; overflow: hidden; }}
    .marquee-container {{ max-width: 1200px; margin: 0 auto; }}
    .marquee-header {{ text-align: center; margin-bottom: 60px; }}
    .marquee-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .marquee-track {{ overflow: hidden; padding: 40px 0; background: {text}05; border-radius: 20px; }}
    .marquee-content {{ display: flex; align-items: center; gap: 40px; animation: marquee 30s linear infinite; width: max-content; }}
    @keyframes marquee {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-50%); }} }}
    .marquee-item {{ font-size: 2rem; font-weight: 700; color: {text}; white-space: nowrap; }}
    .dot {{ font-size: 2rem; color: {primary}; }}
    .marquee-track:hover .marquee-content {{ animation-play-state: paused; }}
    </style>
    '''
