from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Cards Layout - Contact options in cards"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-contact-cards" id="contact">
        <div class="cards-container">
            <div class="cards-header"><h2>Get In Touch</h2></div>
            <div class="contact-cards">
                <div class="contact-card">
                    <span class="card-icon">📧</span>
                    <h3>Email</h3>
                    <p>hello@example.com</p>
                    <a href="mailto:hello@example.com" class="card-link">Send Email →</a>
                </div>
                <div class="contact-card">
                    <span class="card-icon">💬</span>
                    <h3>Social</h3>
                    <p>@username</p>
                    <a href="#" class="card-link">Connect →</a>
                </div>
                <div class="contact-card">
                    <span class="card-icon">📍</span>
                    <h3>Location</h3>
                    <p>San Francisco, CA</p>
                    <a href="#" class="card-link">View Map →</a>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-contact-cards {{ padding: 120px 24px; background: {background}; }}
    .cards-container {{ max-width: 1000px; margin: 0 auto; }}
    .cards-header {{ text-align: center; margin-bottom: 60px; }}
    .cards-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; }}
    .contact-cards {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }}
    .contact-card {{ background: {text}05; border: 1px solid {text}10; border-radius: 24px; padding: 40px; text-align: center; transition: all 0.4s ease; }}
    .contact-card:hover {{ transform: translateY(-8px); border-color: {primary}40; box-shadow: 0 30px 60px {primary}10; }}
    .card-icon {{ display: block; font-size: 3rem; margin-bottom: 20px; }}
    .contact-card h3 {{ font-size: 1.3rem; font-weight: 700; color: {text}; margin-bottom: 8px; }}
    .contact-card p {{ color: {secondary}; margin-bottom: 20px; }}
    .card-link {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    @media (max-width: 900px) {{ .contact-cards {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
