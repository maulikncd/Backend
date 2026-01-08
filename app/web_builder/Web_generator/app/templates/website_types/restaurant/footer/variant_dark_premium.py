from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Dark Premium - Luxurious dark footer"""
    business_name = props.get("businessName", "Restaurant")
    address = props.get("address", "123 Main Street, City")
    phone = props.get("phone", "(555) 123-4567")
    
    primary = colors.get("primary", "#D4AF37")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <footer class="footer-dark" id="footer">
        <div class="footer-bg"></div>
        <div class="footer-container">
            <div class="footer-main">
                <div class="brand-section">
                    <div class="brand-mark">✦</div>
                    <h3>{business_name}</h3>
                    <p>Where moments become memories</p>
                </div>
                
                <div class="info-grid">
                    <div class="info-box">
                        <h4>Hours</h4>
                        <p>Tuesday - Sunday</p>
                        <p>6:00 PM - 11:00 PM</p>
                    </div>
                    <div class="info-box">
                        <h4>Location</h4>
                        <p>{address}</p>
                    </div>
                    <div class="info-box">
                        <h4>Contact</h4>
                        <p>{phone}</p>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>© 2024 {business_name}</p>
            </div>
        </div>
    </footer>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&display=swap');
    
    .footer-dark {{
        position: relative;
        padding: 100px 60px 40px;
        background: {bg};
    }}
    .footer-bg {{
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, {primary}, transparent);
    }}
    .footer-container {{
        max-width: 1100px;
        margin: 0 auto;
    }}
    .footer-main {{
        text-align: center;
        margin-bottom: 60px;
    }}
    .brand-section {{
        margin-bottom: 60px;
    }}
    .brand-mark {{
        font-size: 2rem;
        color: {primary};
        margin-bottom: 20px;
    }}
    .brand-section h3 {{
        font-family: 'Cormorant Garamond', serif;
        font-size: 3rem;
        color: {text};
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }}
    .brand-section p {{
        color: {text}60;
        font-size: 1rem;
        letter-spacing: 2px;
    }}
    .info-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
    }}
    .info-box h4 {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }}
    .info-box p {{
        color: {text}80;
        font-size: 0.95rem;
        margin-bottom: 5px;
    }}
    .footer-bottom {{
        text-align: center;
        padding-top: 40px;
        border-top: 1px solid {text}10;
    }}
    .footer-bottom p {{
        color: {text}40;
        font-size: 0.85rem;
        letter-spacing: 2px;
    }}
    @media (max-width: 768px) {{
        .footer-dark {{ padding: 80px 30px 30px; }}
        .info-grid {{ grid-template-columns: 1fr; gap: 30px; }}
    }}
    </style>
    '''
