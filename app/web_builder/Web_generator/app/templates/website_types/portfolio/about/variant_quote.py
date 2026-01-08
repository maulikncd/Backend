from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Quote Featured - Inspirational quote style"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-about-quote" id="about">
        <div class="quote-container">
            <div class="quote-box">
                <span class="quote-mark">"</span>
                <blockquote>Design is not just what it looks like. Design is how it works.</blockquote>
                <p class="quote-author">— My Philosophy</p>
            </div>
            <div class="about-text">
                <h2>About {name}</h2>
                <p>I'm a developer who believes in the power of simplicity. With years of experience building digital products, I focus on creating solutions that are both beautiful and functional.</p>
                <p>Every project is an opportunity to learn, grow, and create something meaningful.</p>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-about-quote {{ padding: 120px 24px; background: {background}; }}
    .quote-container {{ max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }}
    .quote-box {{ background: linear-gradient(135deg, {primary}15, {primary}05); border-radius: 32px; padding: 60px; position: relative; }}
    .quote-mark {{ font-size: 8rem; color: {primary}30; position: absolute; top: 20px; left: 30px; line-height: 1; font-family: Georgia, serif; }}
    .quote-box blockquote {{ font-size: 1.8rem; font-weight: 600; color: {text}; line-height: 1.5; position: relative; z-index: 2; }}
    .quote-author {{ color: {primary}; font-weight: 600; margin-top: 24px; }}
    .about-text h2 {{ font-size: 2rem; font-weight: 800; color: {text}; margin-bottom: 24px; }}
    .about-text p {{ color: {secondary}; font-size: 1.1rem; line-height: 1.8; margin-bottom: 16px; }}
    @media (max-width: 900px) {{ .quote-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
