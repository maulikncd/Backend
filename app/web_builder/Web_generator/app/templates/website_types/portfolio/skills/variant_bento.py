from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Skills - Modern bento grid layout"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-skills-bento" id="skills">
        <div class="bento-container">
            <div class="bento-grid">
                <div class="bento-item intro">
                    <span class="tag">Skills</span>
                    <h2>My Tech Stack</h2>
                    <p>Technologies I use to bring ideas to life</p>
                </div>
                <div class="bento-item frontend">
                    <h3>Frontend</h3>
                    <div class="chips"><span>React</span><span>Vue</span><span>Next.js</span></div>
                </div>
                <div class="bento-item backend">
                    <h3>Backend</h3>
                    <div class="chips"><span>Node.js</span><span>Python</span><span>Go</span></div>
                </div>
                <div class="bento-item database">
                    <h3>Database</h3>
                    <div class="chips"><span>PostgreSQL</span><span>MongoDB</span></div>
                </div>
                <div class="bento-item tools">
                    <h3>Tools</h3>
                    <div class="chips"><span>Git</span><span>Docker</span><span>AWS</span><span>Figma</span></div>
                </div>
                <div class="bento-item stat"><span class="num">50+</span><span class="lbl">Technologies Mastered</span></div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-skills-bento {{ padding: 120px 24px; background: {background}; }}
    .bento-container {{ max-width: 1100px; margin: 0 auto; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(2, auto); gap: 20px; }}
    .bento-item {{ background: {text}05; border: 1px solid {text}10; border-radius: 24px; padding: 28px; }}
    .bento-item.intro {{ grid-column: span 2; }}
    .bento-item.tools {{ grid-column: span 2; }}
    .tag {{ display: inline-block; padding: 8px 20px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 12px; font-size: 0.9rem; }}
    .intro h2 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 8px; }}
    .intro p {{ color: {secondary}; }}
    .bento-item h3 {{ font-size: 1rem; font-weight: 600; color: {secondary}; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 1px; }}
    .chips {{ display: flex; flex-wrap: wrap; gap: 10px; }}
    .chips span {{ padding: 10px 18px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; font-size: 0.9rem; }}
    .stat {{ text-align: center; display: flex; flex-direction: column; justify-content: center; background: linear-gradient(135deg, {primary}15, {primary}05); }}
    .num {{ font-size: 3rem; font-weight: 900; color: {primary}; }}
    .lbl {{ color: {secondary}; font-size: 0.9rem; }}
    @media (max-width: 900px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
