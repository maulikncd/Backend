from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Centered Card - Card-style centered form"""
    title = props.get("sectionTitle", "Reserve a Table")
    subtitle = props.get("subtitle", "Join us for an unforgettable dining experience")
    
    primary = colors.get("primary", "#E63946")
    bg = colors.get("background", "#FFFFFF")
    text = colors.get("text", "#1A1A1A")
    
    return f'''
    <section class="reservation-centered" id="reservation">
        <div class="reservation-container">
            <div class="reservation-card">
                <span class="label">Reservations</span>
                <h2>{title}</h2>
                <p class="subtitle">{subtitle}</p>
                
                <form class="centered-form">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Name</label>
                            <input type="text" placeholder="John Doe" required>
                        </div>
                        <div class="form-group">
                            <label>Email</label>
                            <input type="email" placeholder="john@email.com" required>
                        </div>
                        <div class="form-group">
                            <label>Phone</label>
                            <input type="tel" placeholder="(555) 123-4567">
                        </div>
                        <div class="form-group">
                            <label>Party Size</label>
                            <select>
                                <option>2 Guests</option>
                                <option>3 Guests</option>
                                <option>4 Guests</option>
                                <option>5+ Guests</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>Date</label>
                            <input type="date" required>
                        </div>
                        <div class="form-group">
                            <label>Time</label>
                            <select>
                                <option>6:00 PM</option>
                                <option>7:00 PM</option>
                                <option>8:00 PM</option>
                                <option>9:00 PM</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="form-group full">
                        <label>Special Requests</label>
                        <textarea placeholder="Allergies, celebrations, seating preferences..."></textarea>
                    </div>
                    
                    <button type="submit">Book Table</button>
                </form>
            </div>
        </div>
    </section>
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Inter:wght@400;500&display=swap');
    
    .reservation-centered {{
        padding: 120px 60px;
        background: linear-gradient(135deg, {bg} 0%, #f5f5f5 100%);
    }}
    .reservation-container {{
        max-width: 700px;
        margin: 0 auto;
    }}
    .reservation-card {{
        background: white;
        padding: 60px;
        border-radius: 30px;
        box-shadow: 0 30px 80px rgba(0,0,0,0.08);
        text-align: center;
    }}
    .reservation-card .label {{
        color: {primary};
        font-size: 0.85rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 15px;
    }}
    .reservation-card h2 {{
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        color: {text};
        margin-bottom: 15px;
    }}
    .reservation-card .subtitle {{
        color: {text}70;
        margin-bottom: 40px;
    }}
    .centered-form {{
        text-align: left;
    }}
    .form-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 25px;
        margin-bottom: 25px;
    }}
    .form-group {{
        display: flex;
        flex-direction: column;
        gap: 8px;
    }}
    .form-group.full {{
        margin-bottom: 30px;
    }}
    .form-group label {{
        font-size: 0.85rem;
        color: {text}80;
        font-weight: 500;
    }}
    .form-group input, .form-group select, .form-group textarea {{
        padding: 15px 18px;
        border: 1px solid {text}20;
        border-radius: 10px;
        font-size: 1rem;
        transition: border-color 0.3s;
    }}
    .form-group input:focus, .form-group select:focus, .form-group textarea:focus {{
        outline: none;
        border-color: {primary};
    }}
    .form-group textarea {{
        min-height: 100px;
        resize: none;
    }}
    .centered-form button {{
        width: 100%;
        padding: 20px;
        background: {primary};
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .centered-form button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 40px {primary}40;
    }}
    @media (max-width: 768px) {{
        .reservation-centered {{ padding: 80px 30px; }}
        .reservation-card {{ padding: 40px 25px; }}
        .form-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    '''
