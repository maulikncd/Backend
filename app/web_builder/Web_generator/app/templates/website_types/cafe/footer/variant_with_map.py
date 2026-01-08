from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Map Footer - With embedded map placeholder"""
    logo = props.get("logo", "Cafe")
    tagline = props.get("tagline", "")
    primary = colors.get("primary", "#8B7355")
    
    return f'''
    <footer class="footer-with-map"><div class="map-section"><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.9663095919317!2d-74.00425878428698!3d40.71277537933185!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c25a1f0d6e7f5d%3A0x4b567d5e3b5d5b5e!2sNew%20York%2C%20NY!5e0!3m2!1sen!2sus!4v1" style="border:0;" allowfullscreen="" loading="lazy"></iframe></div><div class="footer-info"><div class="info-grid"><div class="info-col brand"><h3>{logo}</h3><p>{tagline if tagline else "Your neighborhood coffee spot"}</p></div><div class="info-col"><h4>Address</h4><p>123 Coffee Lane<br>New York, NY 10001</p></div><div class="info-col"><h4>Hours</h4><p>Mon-Fri: 7AM-9PM<br>Sat-Sun: 8AM-10PM</p></div><div class="info-col"><h4>Contact</h4><p>hello@cafe.com<br>+1 (555) 123-4567</p></div></div><div class="copyright-row"><span>© 2025 {logo}</span><div><a href="#">Privacy</a><a href="#">Terms</a></div></div></div></footer>
    <style>
    .footer-with-map {{ background: #111; }}
    .map-section {{ height: 300px; }}
    .map-section iframe {{ width: 100%; height: 100%; filter: grayscale(100%) invert(92%) contrast(83%); }}
    .footer-info {{ padding: 60px 40px; color: #fff; }}
    .info-grid {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 50px; margin-bottom: 50px; }}
    .brand h3 {{ font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 10px; }}
    .brand p {{ color: #888; }}
    .info-col h4 {{ color: {primary}; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 15px; }}
    .info-col p {{ color: #888; line-height: 1.8; }}
    .copyright-row {{ max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; padding-top: 30px; border-top: 1px solid #333; color: #666; font-size: 0.9rem; }}
    .copyright-row a {{ color: #666; text-decoration: none; margin-left: 20px; }}
    .copyright-row a:hover {{ color: #fff; }}
    @media (max-width: 900px) {{ .info-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    </style>
    '''
