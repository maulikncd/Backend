from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento About - Modern bento grid style"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-about-bento" id="about">
        <div class="bento-container">
            <div class="bento-grid">
                <div class="bento-item bio">
                    <span class="label">About Me</span>
                    <h2>Crafting digital experiences with passion</h2>
                    <p>I'm a developer who loves turning ideas into reality through clean code and creative design.</p>
                </div>
                <div class="bento-item avatar">
                    <div class="avatar-circle">{name[0]}</div>
                </div>
                <div class="bento-item stat"><span class="num">5+</span><span class="lbl">Years</span></div>
                <div class="bento-item stat"><span class="num">50+</span><span class="lbl">Projects</span></div>
                <div class="bento-item tools">
                    <span class="label">Tools I Use</span>
                    <div class="tool-icons">
                        <span>⚛️ React</span>
                        <span>🟢 Node</span>
                        <span>🐍 Python</span>
                        <span>🎨 Figma</span>
                    </div>
                </div>
                <div class="bento-item values">
                    <span class="label">Values</span>
                    <ul>
                        <li>Clean Code</li>
                        <li>User First</li>
                        <li>Continuous Learning</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-about-bento {{ padding: 120px 24px; background: {background}; }}
    .bento-container {{ max-width: 1100px; margin: 0 auto; }}
    .bento-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(2, auto); gap: 20px; }}
    .bento-item {{ background: {text}05; border: 1px solid {text}10; border-radius: 24px; padding: 28px; }}
    .bento-item.bio {{ grid-column: span 2; }}
    .bento-item.avatar {{ display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, {primary}20, {primary}05); }}
    .bento-item.tools {{ grid-column: span 2; }}
    .bento-item.values {{ grid-column: span 2; }}
    .label {{ display: block; color: {primary}; font-weight: 600; font-size: 0.9rem; margin-bottom: 12px; }}
    .bio h2 {{ font-size: 1.8rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .bio p {{ color: {secondary}; line-height: 1.7; }}
    .avatar-circle {{ width: 100px; height: 100px; background: {primary}; color: {background}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 3rem; font-weight: 900; }}
    .stat {{ text-align: center; display: flex; flex-direction: column; justify-content: center; }}
    .num {{ font-size: 2.5rem; font-weight: 900; color: {primary}; }}
    .lbl {{ color: {secondary}; }}
    .tool-icons {{ display: flex; gap: 16px; flex-wrap: wrap; }}
    .tool-icons span {{ padding: 10px 16px; background: {text}08; border-radius: 100px; font-size: 0.9rem; color: {text}; }}
    .values ul {{ list-style: none; padding: 0; margin: 0; }}
    .values li {{ padding: 10px 0; border-bottom: 1px solid {text}08; color: {text}; }}
    @media (max-width: 900px) {{ .bento-grid {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
