from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Newsletter Footer"""
    logo = props.get("logoText", "STUDIO")
    primary = colors.get("primary", "#00F0FF")
    
    return f'''
    <footer class="gaming-footer-newsletter"><div class="container"><div class="newsletter-section"><h3>Stay in the Loop</h3><p>Get updates on new games, events, and exclusive content.</p><form class="newsletter-form"><input type="email" placeholder="Enter your email"><button type="submit">Subscribe</button></form></div><div class="footer-bottom"><span>© 2025 {logo}</span><nav><a href="#">Privacy</a><a href="#">Terms</a><a href="#">Contact</a></nav><div class="socials"><a href="#">Discord</a><a href="#">Twitter</a><a href="#">YouTube</a></div></div></div></footer>
    <style>
    .gaming-footer-newsletter {{ background: linear-gradient(135deg, #0D0D15, #1a1a2e); padding: 80px 40px 30px; }}
    .container {{ max-width: 900px; margin: 0 auto; text-align: center; color: #fff; }}
    .newsletter-section h3 {{ font-size: 2.5rem; margin-bottom: 15px; }}
    .newsletter-section p {{ color: #888; margin-bottom: 30px; }}
    .newsletter-form {{ display: flex; gap: 15px; justify-content: center; max-width: 500px; margin: 0 auto 60px; }}
    .newsletter-form input {{ flex: 1; padding: 18px 25px; background: #1a1a2e; border: 1px solid #333; color: #fff; font-size: 1rem; }}
    .newsletter-form input::placeholder {{ color: #666; }}
    .newsletter-form button {{ padding: 18px 35px; background: {primary}; color: #000; font-weight: 700; border: none; cursor: pointer; transition: 0.3s; }}
    .newsletter-form button:hover {{ transform: scale(1.05); }}
    .footer-bottom {{ display: flex; justify-content: space-between; align-items: center; padding-top: 30px; border-top: 1px solid #333; color: #666; font-size: 0.9rem; flex-wrap: wrap; gap: 20px; }}
    .footer-bottom nav a {{ color: #666; text-decoration: none; margin: 0 15px; }}
    .footer-bottom nav a:hover {{ color: #fff; }}
    .socials a {{ color: {primary}; text-decoration: none; margin-left: 15px; }}
    </style>
    '''
