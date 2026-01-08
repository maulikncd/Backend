from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Stacked Elegant Footer"""
    logo = props.get("logo", "Cafe")
    primary = colors.get("primary", "#8B7355")
    
    return f'''
    <footer class="footer-stacked"><div class="stacked-container"><div class="top-section"><h3>{logo}</h3><nav class="nav-links"><a href="#">Home</a><a href="#">Menu</a><a href="#">About</a><a href="#">Gallery</a><a href="#">Contact</a></nav></div><div class="middle-section"><div class="contact-item"><span class="label">Location</span><span class="value">123 Coffee Lane, NYC</span></div><div class="contact-item"><span class="label">Email</span><span class="value">hello@cafe.com</span></div><div class="contact-item"><span class="label">Phone</span><span class="value">+1 (555) 123-4567</span></div></div><div class="bottom-section"><div class="social"><a href="#">Facebook</a><a href="#">Instagram</a><a href="#">Twitter</a></div><span>© 2025 {logo}. All rights reserved.</span></div></div></footer>
    <style>
    .footer-stacked {{ background: #FAF7F4; padding: 80px 40px; }}
    .stacked-container {{ max-width: 1000px; margin: 0 auto; text-align: center; }}
    .top-section {{ padding-bottom: 40px; border-bottom: 1px solid #ddd; margin-bottom: 40px; }}
    .top-section h3 {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 30px; }}
    .nav-links {{ display: flex; justify-content: center; gap: 40px; }}
    .nav-links a {{ color: #666; text-decoration: none; font-weight: 500; transition: 0.3s; }}
    .nav-links a:hover {{ color: {primary}; }}
    .middle-section {{ display: flex; justify-content: center; gap: 80px; margin-bottom: 40px; }}
    .contact-item {{ text-align: center; }}
    .contact-item .label {{ display: block; color: {primary}; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; }}
    .contact-item .value {{ color: #333; }}
    .bottom-section {{ padding-top: 40px; border-top: 1px solid #ddd; display: flex; justify-content: space-between; align-items: center; }}
    .social a {{ color: {primary}; text-decoration: none; margin: 0 15px; font-weight: 500; }}
    .bottom-section span {{ color: #888; font-size: 0.9rem; }}
    @media (max-width: 768px) {{ .middle-section {{ flex-direction: column; gap: 30px; }} .bottom-section {{ flex-direction: column; gap: 20px; }} }}
    </style>
    '''
