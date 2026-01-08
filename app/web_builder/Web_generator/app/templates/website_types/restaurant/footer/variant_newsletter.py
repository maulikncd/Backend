from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Newsletter Footer - With email signup"""
    business_name = props.get("businessName", "Restaurant")
    address = props.get("address", "123 Main Street, City")
    
    primary = colors.get("primary", "#8B7355")
    bg = colors.get("background", "#F5F1EB")
    text = colors.get("text", "#2D2013")
    
    return f'''
    <footer class="footer-newsletter" id="footer">
        <div class="footer-container">
            <div class="newsletter-section">
                <h3>Stay Updated</h3>
                <p>Subscribe for exclusive offers and seasonal menu updates</p>
                <form class="newsletter-form">
                    <input type="email" placeholder="Enter your email">
                    <button type="submit">Subscribe</button>
                </form>
            </div>
            
            <div class="footer-divider"></div>
            
            <div class="footer-bottom">
                <div class="footer-brand">
                    <h4>{business_name}</h4>
                    <p>{address}</p>
                </div>
                
                <div class="footer-nav">
                    <a href="#menu">Menu</a>
                    <a href="#about">About</a>
                    <a href="#reservation">Reserve</a>
                    <a href="#contact">Contact</a>
                </div>
                
                <div class="footer-social">
                    <span>Follow Us</span>
                    <div class="social-icons">
                        <a href="#">IG</a>
                        <a href="#">FB</a>
                        <a href="#">TW</a>
                    </div>
                </div>
            </div>
            
            <p class="copyright">© 2024 {business_name}. All rights reserved.</p>
        </div>
    </footer>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Lora:wght@400&display=swap');
    
    .footer-newsletter {{
        padding: 80px 60px 40px;
        background: {bg};
    }}
    .footer-container {{
        max-width: 1100px;
        margin: 0 auto;
    }}
    .newsletter-section {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .newsletter-section h3 {{
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: {text};
        margin-bottom: 15px;
    }}
    .newsletter-section p {{
        color: {text}80;
        margin-bottom: 30px;
    }}
    .newsletter-form {{
        display: flex;
        max-width: 500px;
        margin: 0 auto;
        gap: 15px;
    }}
    .newsletter-form input {{
        flex: 1;
        padding: 18px 25px;
        border: 1px solid {text}20;
        border-radius: 50px;
        font-size: 1rem;
        background: white;
    }}
    .newsletter-form button {{
        padding: 18px 35px;
        background: {primary};
        color: white;
        border: none;
        border-radius: 50px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .newsletter-form button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px {primary}40;
    }}
    .footer-divider {{
        height: 1px;
        background: {text}15;
        margin: 40px 0;
    }}
    .footer-bottom {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 40px;
        margin-bottom: 40px;
    }}
    .footer-brand h4 {{
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: {text};
        margin-bottom: 10px;
    }}
    .footer-brand p {{
        color: {text}70;
        font-size: 0.9rem;
    }}
    .footer-nav {{
        display: flex;
        justify-content: center;
        gap: 30px;
    }}
    .footer-nav a {{
        color: {text}80;
        text-decoration: none;
        transition: color 0.3s;
    }}
    .footer-nav a:hover {{ color: {primary}; }}
    .footer-social {{
        text-align: right;
    }}
    .footer-social span {{
        color: {text}60;
        font-size: 0.85rem;
        display: block;
        margin-bottom: 10px;
    }}
    .social-icons {{
        display: flex;
        justify-content: flex-end;
        gap: 15px;
    }}
    .social-icons a {{
        width: 40px;
        height: 40px;
        background: {primary};
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        font-size: 0.8rem;
        transition: all 0.3s;
    }}
    .social-icons a:hover {{
        transform: translateY(-3px);
    }}
    .copyright {{
        text-align: center;
        color: {text}50;
        font-size: 0.85rem;
    }}
    @media (max-width: 768px) {{
        .footer-newsletter {{ padding: 60px 30px 30px; }}
        .newsletter-form {{ flex-direction: column; }}
        .footer-bottom {{ grid-template-columns: 1fr; text-align: center; }}
        .footer-nav {{ flex-wrap: wrap; }}
        .footer-social {{ text-align: center; }}
        .social-icons {{ justify-content: center; }}
    }}
    </style>
    '''
