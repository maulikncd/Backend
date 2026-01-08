from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Process Flow - Work process steps"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    steps = [
        {"num": "01", "title": "Discovery", "desc": "Understanding your goals and requirements"},
        {"num": "02", "title": "Design", "desc": "Creating intuitive and beautiful interfaces"},
        {"num": "03", "title": "Develop", "desc": "Building with clean, scalable code"},
        {"num": "04", "title": "Deliver", "desc": "Testing and launching your product"},
    ]
    
    steps_html = ""
    for s in steps:
        steps_html += f'''
        <div class="step-card">
            <span class="step-num">{s['num']}</span>
            <h3>{s['title']}</h3>
            <p>{s['desc']}</p>
        </div>
        '''
    
    return f'''
    <section class="portfolio-about-process" id="about">
        <div class="process-container">
            <div class="process-header">
                <span class="tag">How I Work</span>
                <h2>My Process</h2>
            </div>
            <div class="steps-grid">{steps_html}</div>
        </div>
    </section>
    
    <style>
    .portfolio-about-process {{ padding: 120px 24px; background: {background}; }}
    .process-container {{ max-width: 1100px; margin: 0 auto; }}
    .process-header {{ text-align: center; margin-bottom: 60px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .process-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .steps-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }}
    .step-card {{ background: {text}05; border-radius: 24px; padding: 40px 28px; position: relative; overflow: hidden; transition: all 0.4s ease; }}
    .step-card:hover {{ background: {primary}10; }}
    .step-num {{ display: block; font-size: 4rem; font-weight: 900; color: {primary}20; margin-bottom: 16px; }}
    .step-card h3 {{ font-size: 1.4rem; font-weight: 700; color: {text}; margin-bottom: 12px; }}
    .step-card p {{ color: {secondary}; line-height: 1.6; }}
    @media (max-width: 900px) {{ .steps-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 600px) {{ .steps-grid {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
