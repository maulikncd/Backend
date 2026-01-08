from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Map Footer - Footer with embedded map"""
    business_name = props.get("businessName", "Restaurant")
    address = props.get("address", "123 Main Street, City")
    phone = props.get("phone", "(555) 123-4567")
    
    primary = colors.get("primary", "#E63946")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <footer class="footer-map" id="footer">
        <div class="footer-grid">
            <div class="map-section">
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.15830869428!2d-74.119763973046!3d40.69766374874431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2s!4v1635959481000!5m2!1sen!2s"
                    width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy">
                </iframe>
            </div>
            
            <div class="info-section">
                <h3>{business_name}</h3>
                
                <div class="info-item">
                    <h4>Address</h4>
                    <p>{address}</p>
                </div>
                
                <div class="info-item">
                    <h4>Hours</h4>
                    <p>Mon-Thu: 5PM - 10PM</p>
                    <p>Fri-Sat: 5PM - 11PM</p>
                    <p>Sun: 4PM - 9PM</p>
                </div>
                
                <div class="info-item">
                    <h4>Contact</h4>
                    <p>{phone}</p>
                </div>
                
                <a href="#reservation" class="btn-reserve">Make Reservation</a>
                
                <div class="copyright">
                    <p>© 2024 {business_name}</p>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Inter:wght@400;500&display=swap');
    
    .footer-map {{
        background: {bg};
    }}
    .footer-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
    }}
    .map-section {{
        min-height: 500px;
    }}
    .map-section iframe {{
        filter: grayscale(100%);
    }}
    .info-section {{
        padding: 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .info-section h3 {{
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: {text};
        margin-bottom: 40px;
    }}
    .info-item {{
        margin-bottom: 30px;
    }}
    .info-item h4 {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }}
    .info-item p {{
        color: {text}80;
        font-size: 1rem;
        margin-bottom: 5px;
    }}
    .btn-reserve {{
        display: inline-block;
        padding: 18px 40px;
        background: {primary};
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 500;
        margin: 30px 0;
        text-align: center;
        transition: all 0.3s;
    }}
    .btn-reserve:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    .copyright {{
        margin-top: auto;
    }}
    .copyright p {{
        color: {text}50;
        font-size: 0.85rem;
    }}
    @media (max-width: 968px) {{
        .footer-grid {{ grid-template-columns: 1fr; }}
        .map-section {{ min-height: 300px; }}
        .info-section {{ padding: 40px 30px; }}
    }}
    </style>
    '''
