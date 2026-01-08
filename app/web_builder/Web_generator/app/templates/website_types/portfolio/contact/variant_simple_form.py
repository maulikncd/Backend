from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Simple Form - Clean minimal contact form"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <section class="portfolio-contact-simple" id="contact">
        <div class="contact-container">
            <div class="contact-header">
                <span class="tag">Contact</span>
                <h2>Let's Talk</h2>
                <p>Have a project in mind? Let's create something amazing together.</p>
            </div>
            <form class="contact-form">
                <div class="form-row">
                    <div class="form-group"><label>Name</label><input type="text" placeholder="Your name"></div>
                    <div class="form-group"><label>Email</label><input type="email" placeholder="your@email.com"></div>
                </div>
                <div class="form-group"><label>Subject</label><input type="text" placeholder="Project inquiry"></div>
                <div class="form-group"><label>Message</label><textarea rows="5" placeholder="Tell me about your project..."></textarea></div>
                <button type="submit" class="submit-btn">Send Message →</button>
            </form>
        </div>
    </section>
    
    <style>
    .portfolio-contact-simple {{ padding: 120px 24px; background: {background}; }}
    .contact-container {{ max-width: 700px; margin: 0 auto; }}
    .contact-header {{ text-align: center; margin-bottom: 48px; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .contact-header h2 {{ font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .contact-header p {{ color: {secondary}; font-size: 1.1rem; }}
    .form-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
    .form-group {{ margin-bottom: 20px; }}
    .form-group label {{ display: block; color: {text}; font-weight: 600; margin-bottom: 8px; }}
    .form-group input, .form-group textarea {{ width: 100%; padding: 16px; background: {text}05; border: 1px solid {text}15; border-radius: 12px; color: {text}; font-size: 1rem; transition: border-color 0.3s ease; }}
    .form-group input:focus, .form-group textarea:focus {{ border-color: {primary}; outline: none; }}
    .submit-btn {{ width: 100%; padding: 18px; background: {primary}; color: {background}; border: none; font-weight: 700; font-size: 1.1rem; border-radius: 12px; cursor: pointer; transition: all 0.3s ease; }}
    .submit-btn:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px {primary}40; }}
    @media (max-width: 600px) {{ .form-row {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
