from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Text - Clean text-focused about"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-about-minimal" id="about">
        <div class="minimal-container">
            <div class="about-cols">
                <div class="col-left">
                    <span class="tag">About</span>
                    <h2>I build things for the web</h2>
                </div>
                <div class="col-right">
                    <p class="lead">A passionate developer focused on creating clean, user-friendly experiences that make a lasting impact.</p>
                    <p>With over 5 years of experience in web development, I've had the privilege of working with startups and enterprises alike. My approach combines technical expertise with creative problem-solving.</p>
                    <p>I believe great software is built through collaboration, attention to detail, and a deep understanding of user needs.</p>
                    <a href="#contact" class="link">Get in touch →</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-about-minimal {{ padding: 120px 24px; background: {background}; }}
    .minimal-container {{ max-width: 1100px; margin: 0 auto; }}
    .about-cols {{ display: grid; grid-template-columns: 1fr 1.5fr; gap: 80px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .col-left h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; line-height: 1.2; }}
    .lead {{ font-size: 1.4rem; color: {text}; font-weight: 500; line-height: 1.6; margin-bottom: 24px; }}
    .col-right p {{ color: {secondary}; font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px; }}
    .link {{ color: {primary}; text-decoration: none; font-weight: 700; font-size: 1.1rem; display: inline-block; margin-top: 16px; transition: transform 0.3s ease; }}
    .link:hover {{ transform: translateX(8px); }}
    @media (max-width: 900px) {{ .about-cols {{ grid-template-columns: 1fr; gap: 40px; }} }}
    </style>
    '''
