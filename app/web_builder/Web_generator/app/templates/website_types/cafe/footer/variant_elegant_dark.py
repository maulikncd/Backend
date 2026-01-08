from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    logo = props.get("logo_text", "CAFE")
    address = props.get("address", "123 Coffee Lane, Brewville")
    phone = props.get("phone", "(555) 123-4567")
    
    return f'''
    <footer class="cafe-footer-elegant" id="footer">
        <div class="footer-container">
            <div class="footer-brand">
                <h2 class="footer-logo">{logo}</h2>
                <p class="brand-desc">Serving premium coffee and joy since 2024.</p>
            </div>
            <div class="footer-links">
                <h4>Quick Links</h4>
                <a href="#about">About Us</a>
                <a href="#menu">Our Menu</a>
                <a href="#gallery">Gallery</a>
                <a href="#contact">Contact</a>
            </div>
            <div class="footer-contact">
                <h4>Visit Us</h4>
                <p>{address}</p>
                <p>{phone}</p>
                <div class="social-icons">
                    <span>IG</span> <span>FB</span> <span>TW</span>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 {logo}. All rights reserved.</p>
        </div>
    </footer>
    
    <style>
    .cafe-footer-elegant {{
        background: {colors.get("primary", "#2C1810")};
        color: rgba(255,255,255,0.8);
        padding: 80px 24px 40px;
    }}
    .footer-container {{
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 2fr 1fr 1.5fr;
        gap: 60px;
        margin-bottom: 60px;
    }}
    .footer-logo {{ font-family: 'Playfair Display', serif; color: #fff; margin-bottom: 20px; }}
    .footer-links h4, .footer-contact h4 {{ color: #fff; margin-bottom: 24px; font-size: 1.1rem; }}
    .footer-links {{ display: flex; flex-direction: column; gap: 12px; }}
    .footer-links a {{ color: inherit; text-decoration: none; transition: color 0.3s; }}
    .footer-links a:hover {{ color: {colors.get("secondary", "#C4A77D")}; }}
    .social-icons {{ display: flex; gap: 20px; margin-top: 24px; }}
    .footer-bottom {{ text-align: center; padding-top: 40px; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.9rem; }}
    @media (max-width: 768px) {{ .footer-container {{ grid-template-columns: 1fr; gap: 40px; }} }}
    </style>
    '''
