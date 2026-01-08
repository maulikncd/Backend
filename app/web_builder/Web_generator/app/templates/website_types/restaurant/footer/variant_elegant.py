from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Restaurant Footer - Elegant footer with location, hours, and social links
    """
    name = props.get("name", props.get("businessName", "La Maison"))
    address = props.get("address", "123 Gourmet Street, New York, NY 10001")
    phone = props.get("phone", "+1 234 567 890")
    email = props.get("email", "reservations@lamaison.com")
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <footer class="restaurant-footer" id="footer">
        <div class="container">
            <div class="footer-main">
                <div class="footer-brand">
                    <h2 class="brand-name">{name}</h2>
                    <p class="brand-tagline">Fine Dining Experience</p>
                </div>
                
                <div class="footer-grid">
                    <div class="footer-column">
                        <h4>Location</h4>
                        <p>{address}</p>
                        <a href="#" class="map-link">View on Map →</a>
                    </div>
                    
                    <div class="footer-column">
                        <h4>Opening Hours</h4>
                        <p>Tuesday - Sunday</p>
                        <p>6:00 PM - 11:00 PM</p>
                        <p class="note">Closed on Mondays</p>
                    </div>
                    
                    <div class="footer-column">
                        <h4>Contact</h4>
                        <a href="tel:{phone}">{phone}</a>
                        <a href="mailto:{email}">{email}</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <div class="social-links">
                    <a href="#" aria-label="Instagram">📷</a>
                    <a href="#" aria-label="Facebook">📘</a>
                    <a href="#" aria-label="TripAdvisor">✈️</a>
                </div>
                
                <p class="copyright">© 2024 {name}. All rights reserved.</p>
                
                <div class="footer-links">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms</a>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .restaurant-footer {{
        background: {bg};
        padding: 80px 0 40px;
        border-top: 1px solid {text}10;
    }}
    .restaurant-footer .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .footer-main {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        padding-bottom: 60px;
        border-bottom: 1px solid {text}10;
        margin-bottom: 40px;
        flex-wrap: wrap;
        gap: 60px;
    }}
    .brand-name {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.5rem;
        color: {text};
        margin-bottom: 8px;
    }}
    .brand-tagline {{
        color: {primary};
        font-style: italic;
    }}
    .footer-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 60px;
    }}
    .footer-column h4 {{
        font-size: 0.85rem;
        color: {primary};
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }}
    .footer-column p,
    .footer-column a {{
        display: block;
        color: {text}70;
        font-size: 0.95rem;
        line-height: 1.8;
        text-decoration: none;
    }}
    .footer-column a:hover {{ color: {primary}; }}
    .map-link {{
        color: {primary} !important;
        margin-top: 16px;
    }}
    .note {{
        color: {text}40 !important;
        font-style: italic;
        margin-top: 10px;
    }}
    .footer-bottom {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 20px;
    }}
    .social-links {{
        display: flex;
        gap: 16px;
    }}
    .social-links a {{
        font-size: 1.2rem;
        opacity: 0.7;
        transition: opacity 0.3s;
    }}
    .social-links a:hover {{ opacity: 1; }}
    .copyright {{
        color: {text}40;
        font-size: 0.9rem;
    }}
    .footer-links {{
        display: flex;
        gap: 24px;
    }}
    .footer-links a {{
        color: {text}50;
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s;
    }}
    .footer-links a:hover {{ color: {primary}; }}
    @media (max-width: 900px) {{
        .footer-grid {{ grid-template-columns: 1fr; gap: 40px; }}
        .footer-main {{ flex-direction: column; align-items: center; text-align: center; }}
        .footer-bottom {{ flex-direction: column; text-align: center; }}
    }}
    </style>
    '''
