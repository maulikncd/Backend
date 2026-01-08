from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Bento Footer - Modern bento grid style"""
    name = props.get("name", "John Doe")
    
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    return f'''
    <footer class="portfolio-footer-bento" id="footer">
        <div class="footer-container">
            <div class="footer-bento">
                <div class="bento-item brand"><h3>{name}</h3><p>Developer & Designer</p></div>
                <div class="bento-item status"><div class="dot"></div><span>Available for work</span></div>
                <div class="bento-item email"><span class="label">Email</span><a href="mailto:hello@example.com">hello@example.com</a></div>
                <div class="bento-item social">
                    <a href="#">GH</a>
                    <a href="#">LI</a>
                    <a href="#">TW</a>
                </div>
            </div>
            <div class="footer-bottom"><p>© 2024 All rights reserved.</p></div>
        </div>
    </footer>
    
    <style>
    .portfolio-footer-bento {{ padding: 80px 24px 40px; background: {background}; }}
    .footer-container {{ max-width: 900px; margin: 0 auto; }}
    .footer-bento {{ display: grid; grid-template-columns: 2fr 1fr 1.5fr 1fr; gap: 16px; margin-bottom: 40px; }}
    .bento-item {{ background: {text}05; border-radius: 20px; padding: 24px; }}
    .brand h3 {{ font-size: 1.5rem; font-weight: 800; color: {text}; margin-bottom: 4px; }}
    .brand p {{ color: {secondary}; }}
    .status {{ display: flex; align-items: center; gap: 10px; }}
    .dot {{ width: 10px; height: 10px; background: #22c55e; border-radius: 50%; animation: pulse 2s infinite; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
    .status span {{ color: {text}; font-size: 0.9rem; font-weight: 500; }}
    .email .label {{ display: block; color: {secondary}; font-size: 0.8rem; margin-bottom: 4px; }}
    .email a {{ color: {primary}; text-decoration: none; font-weight: 600; }}
    .social {{ display: flex; align-items: center; gap: 8px; }}
    .social a {{ width: 40px; height: 40px; background: {text}08; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: {text}; text-decoration: none; font-weight: 700; font-size: 0.8rem; transition: all 0.3s ease; }}
    .social a:hover {{ background: {primary}; color: {background}; }}
    .footer-bottom {{ text-align: center; padding-top: 24px; border-top: 1px solid {text}10; }}
    .footer-bottom p {{ color: {secondary}; font-size: 0.85rem; }}
    @media (max-width: 768px) {{ .footer-bento {{ grid-template-columns: 1fr 1fr; }} }}
    </style>
    '''
