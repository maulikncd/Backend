from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Image Form - Form with side image"""
    title = props.get("sectionTitle", "Make a Reservation")
    subtitle = props.get("subtitle", "Book your table today")
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="reservation-split" id="reservation">
        <div class="split-grid">
            <div class="split-image">
                <img src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200" alt="Restaurant">
                <div class="image-overlay">
                    <h3>An Experience Awaits</h3>
                </div>
            </div>
            
            <div class="split-form">
                <div class="form-content">
                    <span class="label">Reservations</span>
                    <h2>{title}</h2>
                    <p class="subtitle">{subtitle}</p>
                    
                    <form class="reserve-form">
                        <div class="form-row">
                            <input type="text" placeholder="Full Name" required>
                            <input type="email" placeholder="Email" required>
                        </div>
                        <div class="form-row">
                            <input type="tel" placeholder="Phone">
                            <input type="number" placeholder="Guests" min="1" max="20">
                        </div>
                        <div class="form-row">
                            <input type="date" required>
                            <input type="time" required>
                        </div>
                        <textarea placeholder="Special requests or dietary requirements"></textarea>
                        <button type="submit">Reserve Now</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Lato:wght@400&display=swap');
    
    .reservation-split {{
        background: {bg};
    }}
    .split-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        min-height: 100vh;
    }}
    .split-image {{
        position: relative;
    }}
    .split-image img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .image-overlay {{
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.4);
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .image-overlay h3 {{
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: white;
        text-align: center;
        padding: 30px;
        border: 2px solid white;
    }}
    .split-form {{
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 80px;
    }}
    .form-content {{
        max-width: 500px;
        width: 100%;
    }}
    .form-content .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .form-content h2 {{
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: {text};
        margin-bottom: 15px;
    }}
    .form-content .subtitle {{
        color: {text}70;
        margin-bottom: 40px;
    }}
    .reserve-form {{
        display: flex;
        flex-direction: column;
        gap: 20px;
    }}
    .form-row {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }}
    .reserve-form input, .reserve-form textarea {{
        padding: 18px 20px;
        background: transparent;
        border: 1px solid {text}30;
        border-radius: 8px;
        color: {text};
        font-size: 1rem;
        transition: border-color 0.3s;
    }}
    .reserve-form input:focus, .reserve-form textarea:focus {{
        outline: none;
        border-color: {primary};
    }}
    .reserve-form textarea {{
        min-height: 100px;
        resize: none;
    }}
    .reserve-form button {{
        padding: 20px;
        background: {primary};
        color: #0A0A0A;
        border: none;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .reserve-form button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    @media (max-width: 968px) {{
        .split-grid {{ grid-template-columns: 1fr; }}
        .split-image {{ height: 40vh; }}
        .split-form {{ padding: 60px 30px; }}
        .form-row {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
