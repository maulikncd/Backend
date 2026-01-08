from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Mega Footer - Large comprehensive footer"""
    logo = props.get("logo", "Cafe")
    sections = props.get("sections", [])
    primary = colors.get("primary", "#8B7355")
    
    sections_html = ""
    if sections:
        for sec in sections[:3]:
            links = "".join([f'<a href="{l.get("href", "#")}">{l.get("text", "")}</a>' for l in sec.get("links", [])[:5]])
            sections_html += f'<div class="mega-col"><h4>{sec.get("title", "Links")}</h4>{links}</div>'
    else:
        sections_html = '''<div class="mega-col"><h4>Menu</h4><a href="#">Coffee</a><a href="#">Pastries</a><a href="#">Brunch</a><a href="#">Specials</a></div>
        <div class="mega-col"><h4>Company</h4><a href="#">About Us</a><a href="#">Careers</a><a href="#">Press</a><a href="#">Blog</a></div>
        <div class="mega-col"><h4>Support</h4><a href="#">FAQ</a><a href="#">Contact</a><a href="#">Locations</a><a href="#">Feedback</a></div>'''
    
    return f'''
    <footer class="footer-mega"><div class="mega-container"><div class="mega-top"><div class="mega-brand"><h3>{logo}</h3><p>Crafting exceptional coffee experiences since 2020.</p><div class="social-links"><a href="#">FB</a><a href="#">IG</a><a href="#">TW</a><a href="#">YT</a></div></div>{sections_html}<div class="mega-col newsletter"><h4>Stay Updated</h4><p>Get exclusive offers and updates.</p><form><input type="email" placeholder="Your email"><button>→</button></form></div></div><div class="mega-bottom"><span>© 2025 {logo}. All rights reserved.</span><div class="legal-links"><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Cookies</a></div></div></div></footer>
    <style>
    .footer-mega {{ background: #111; color: #fff; padding: 80px 40px 30px; }}
    .mega-container {{ max-width: 1300px; margin: 0 auto; }}
    .mega-top {{ display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr 1.5fr; gap: 50px; padding-bottom: 60px; border-bottom: 1px solid #333; }}
    .mega-brand h3 {{ font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 15px; }}
    .mega-brand p {{ color: #888; margin-bottom: 25px; line-height: 1.6; }}
    .social-links {{ display: flex; gap: 10px; }}
    .social-links a {{ width: 40px; height: 40px; background: #222; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #fff; text-decoration: none; font-size: 0.8rem; transition: 0.3s; }}
    .social-links a:hover {{ background: {primary}; }}
    .mega-col h4 {{ font-size: 1rem; margin-bottom: 20px; color: #fff; }}
    .mega-col a {{ display: block; color: #888; text-decoration: none; padding: 8px 0; transition: 0.3s; font-size: 0.95rem; }}
    .mega-col a:hover {{ color: {primary}; }}
    .newsletter p {{ color: #888; margin-bottom: 15px; font-size: 0.9rem; }}
    .newsletter form {{ display: flex; }}
    .newsletter input {{ flex: 1; padding: 12px 15px; background: #222; border: none; border-radius: 8px 0 0 8px; color: #fff; }}
    .newsletter button {{ padding: 12px 20px; background: {primary}; border: none; border-radius: 0 8px 8px 0; color: #fff; cursor: pointer; }}
    .mega-bottom {{ display: flex; justify-content: space-between; padding-top: 30px; color: #666; font-size: 0.9rem; }}
    .legal-links a {{ color: #666; text-decoration: none; margin-left: 25px; transition: 0.3s; }}
    .legal-links a:hover {{ color: #fff; }}
    @media (max-width: 1024px) {{ .mega-top {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 600px) {{ .mega-top {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
