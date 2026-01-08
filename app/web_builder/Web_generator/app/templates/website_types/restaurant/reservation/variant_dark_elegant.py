from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Dark Elegant - Dark luxury reservation"""
    title = props.get("sectionTitle", "Book Your Experience")
    subtitle = props.get("subtitle", "Reserve your table for an unforgettable evening")
    phone = props.get("phone", "(555) 123-4567")
    
    primary = colors.get("primary", "#D4AF37")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="reservation-dark" id="reservation">
        <div class="dark-container">
            <div class="reservation-header">
                <div class="decorative-line"></div>
                <span class="label">Reservations</span>
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            
            <div class="reservation-content">
                <div class="contact-info">
                    <div class="info-item">
                        <h4>By Phone</h4>
                        <p>Call us directly at</p>
                        <a href="tel:{phone}">{phone}</a>
                    </div>
                    <div class="info-item">
                        <h4>Hours</h4>
                        <p>Tuesday - Sunday</p>
                        <p>6:00 PM - 11:00 PM</p>
                    </div>
                </div>
                
                <form class="dark-form">
                    <input type="text" placeholder="Your Name" required>
                    <input type="email" placeholder="Email Address" required>
                    <div class="form-row">
                        <input type="date" required>
                        <input type="time" required>
                    </div>
                    <input type="number" placeholder="Number of Guests" min="1">
                    <textarea placeholder="Special requests or occasion"></textarea>
                    <button type="submit">Request Reservation</button>
                </form>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=Montserrat:wght@300;400&display=swap');
    
    .reservation-dark {{
        padding: 120px 60px;
        background: {bg};
    }}
    .dark-container {{
        max-width: 1000px;
        margin: 0 auto;
    }}
    .reservation-header {{
        text-align: center;
        margin-bottom: 70px;
    }}
    .decorative-line {{
        width: 100px;
        height: 1px;
        background: linear-gradient(90deg, transparent, {primary}, transparent);
        margin: 0 auto 25px;
    }}
    .reservation-header .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 20px;
    }}
    .reservation-header h2 {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        color: {text};
        margin-bottom: 15px;
    }}
    .reservation-header p {{
        color: {text}70;
        font-size: 1.1rem;
    }}
    .reservation-content {{
        display: grid;
        grid-template-columns: 1fr 1.5fr;
        gap: 80px;
    }}
    .contact-info {{
        display: flex;
        flex-direction: column;
        gap: 40px;
    }}
    .info-item h4 {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 15px;
    }}
    .info-item p {{
        color: {text}80;
        margin-bottom: 5px;
    }}
    .info-item a {{
        color: {text};
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.5rem;
        text-decoration: none;
    }}
    .dark-form {{
        display: flex;
        flex-direction: column;
        gap: 20px;
    }}
    .form-row {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }}
    .dark-form input, .dark-form textarea {{
        padding: 20px;
        background: transparent;
        border: 1px solid {text}20;
        color: {text};
        font-size: 1rem;
        transition: border-color 0.3s;
    }}
    .dark-form input:focus, .dark-form textarea:focus {{
        outline: none;
        border-color: {primary};
    }}
    .dark-form textarea {{
        min-height: 120px;
        resize: none;
    }}
    .dark-form button {{
        padding: 22px;
        background: transparent;
        border: 1px solid {primary};
        color: {primary};
        font-size: 0.9rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.4s;
    }}
    .dark-form button:hover {{
        background: {primary};
        color: #0A0A0A;
    }}
    @media (max-width: 868px) {{
        .reservation-dark {{ padding: 80px 30px; }}
        .reservation-content {{ grid-template-columns: 1fr; gap: 50px; }}
        .form-row {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
