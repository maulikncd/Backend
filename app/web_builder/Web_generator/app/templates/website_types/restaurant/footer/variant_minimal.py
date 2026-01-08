from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Minimal Elegant - Clean minimal footer"""
    business_name = props.get("businessName", "Restaurant")
    address = props.get("address", "123 Main Street, City")
    phone = props.get("phone", "(555) 123-4567")
    email = props.get("email", "info@restaurant.com")
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <footer class="footer-minimal" id="footer">
        <div class="footer-container">
            <div class="footer-top">
                <div class="footer-brand">
                    <h3>{business_name}</h3>
                    <p>Fine Dining Experience</p>
                </div>
                
                <div class="footer-links">
                    <a href="#about">About</a>
                    <a href="#menu">Menu</a>
                    <a href="#gallery">Gallery</a>
                    <a href="#reservation">Reserve</a>
                </div>
                
                <div class="footer-contact">
                    <p>{address}</p>
                    <p>{phone}</p>
                    <p>{email}</p>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>© 2024 {business_name}. All rights reserved.</p>
                <div class="social-links">
                    <a href="#">Instagram</a>
                    <a href="#">Facebook</a>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .footer-minimal {{
        padding: 80px 60px 40px;
        background: {bg};
    }}
    .footer-container {{
        max-width: 1200px;
        margin: 0 auto;
    }}
    .footer-top {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 60px;
        padding-bottom: 60px;
        border-bottom: 1px solid {text}15;
    }}
    .footer-brand h3 {{
        font-size: 1.8rem;
        color: {text};
        margin-bottom: 10px;
    }}
    .footer-brand p {{
        color: {primary};
        font-size: 0.9rem;
    }}
    .footer-links {{
        display: flex;
        flex-direction: column;
        gap: 15px;
    }}
    .footer-links a {{
        color: {text}80;
        text-decoration: none;
        transition: color 0.3s;
    }}
    .footer-links a:hover {{ color: {primary}; }}
    .footer-contact p {{
        color: {text}80;
        margin-bottom: 10px;
        font-size: 0.95rem;
    }}
    .footer-bottom {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 40px;
    }}
    .footer-bottom p {{
        color: {text}50;
        font-size: 0.85rem;
    }}
    .social-links {{
        display: flex;
        gap: 25px;
    }}
    .social-links a {{
        color: {text}60;
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s;
    }}
    .social-links a:hover {{ color: {primary}; }}
    @media (max-width: 768px) {{
        .footer-minimal {{ padding: 60px 30px 30px; }}
        .footer-top {{ grid-template-columns: 1fr; gap: 40px; }}
        .footer-bottom {{ flex-direction: column; gap: 20px; text-align: center; }}
    }}
    </style>
    '''
