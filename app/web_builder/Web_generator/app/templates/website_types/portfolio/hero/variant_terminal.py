from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Terminal Style - Developer terminal look"""
    name = props.get("name", "John Doe")
    title = props.get("title", "Full Stack Developer")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-hero-terminal" id="hero">
        <div class="terminal-container">
            <div class="terminal-window">
                <div class="terminal-header">
                    <div class="terminal-dots">
                        <span class="dot red"></span>
                        <span class="dot yellow"></span>
                        <span class="dot green"></span>
                    </div>
                    <span class="terminal-title">portfolio.dev</span>
                </div>
                <div class="terminal-body">
                    <div class="line"><span class="prompt">$</span> whoami</div>
                    <div class="output name">{name}</div>
                    <div class="line"><span class="prompt">$</span> cat role.txt</div>
                    <div class="output role">{title}</div>
                    <div class="line"><span class="prompt">$</span> cat skills.json</div>
                    <div class="output skills">{{"languages": ["JavaScript", "Python", "TypeScript"]}}</div>
                    <div class="line typing"><span class="prompt">$</span> <span class="cursor">_</span></div>
                </div>
            </div>
            <div class="hero-info">
                <h1>Building the future,<br/>one commit at a time.</h1>
                <div class="hero-links">
                    <a href="#projects" class="link">→ View Projects</a>
                    <a href="#contact" class="link">→ Contact Me</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-hero-terminal {{ min-height: 100vh; background: {background}; display: flex; align-items: center; padding: 80px 24px; }}
    .terminal-container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1.2fr 1fr; gap: 60px; align-items: center; }}
    .terminal-window {{ background: #0d1117; border-radius: 16px; overflow: hidden; box-shadow: 0 30px 80px rgba(0,0,0,0.4); }}
    .terminal-header {{ background: #161b22; padding: 16px 20px; display: flex; align-items: center; gap: 16px; }}
    .terminal-dots {{ display: flex; gap: 8px; }}
    .dot {{ width: 12px; height: 12px; border-radius: 50%; }}
    .dot.red {{ background: #ff5f56; }}
    .dot.yellow {{ background: #ffbd2e; }}
    .dot.green {{ background: #27c93f; }}
    .terminal-title {{ color: #8b949e; font-size: 0.85rem; }}
    .terminal-body {{ padding: 24px; font-family: 'JetBrains Mono', monospace; font-size: 0.95rem; }}
    .line {{ color: #c9d1d9; margin-bottom: 8px; }}
    .prompt {{ color: {primary}; margin-right: 12px; }}
    .output {{ color: {primary}; margin-bottom: 16px; padding-left: 24px; }}
    .output.name {{ font-size: 1.5rem; font-weight: 700; }}
    .output.role {{ color: #58a6ff; }}
    .output.skills {{ color: #7ee787; font-size: 0.85rem; }}
    .cursor {{ animation: blink 1s infinite; }}
    @keyframes blink {{ 0%, 50% {{ opacity: 1; }} 51%, 100% {{ opacity: 0; }} }}
    .hero-info h1 {{ font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; color: {text}; line-height: 1.3; margin-bottom: 32px; }}
    .hero-links {{ display: flex; flex-direction: column; gap: 16px; }}
    .link {{ color: {primary}; text-decoration: none; font-weight: 600; font-size: 1.1rem; transition: transform 0.3s ease; }}
    .link:hover {{ transform: translateX(8px); }}
    @media (max-width: 900px) {{ .terminal-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
