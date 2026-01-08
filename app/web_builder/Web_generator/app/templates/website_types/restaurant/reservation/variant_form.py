from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Reservation Form - Restaurant booking form with date/time picker
    and party size selection
    """
    title = props.get("sectionTitle", props.get("title", "Reserve a Table"))
    subtitle = props.get("subtitle", "We look forward to serving you")
    phone = props.get("phone", "+1 234 567 890")
    
    primary = colors.get("primary", "#C9A962")
    bg = colors.get("background", "#0A0A0A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <section class="reservation-section" id="reservation">
        <div class="container">
            <div class="reservation-grid">
                <div class="reservation-info">
                    <span class="section-label">Reservations</span>
                    <h2 class="section-title">{title}</h2>
                    <p class="section-desc">{subtitle}</p>
                    
                    <div class="contact-option">
                        <span class="option-icon">📞</span>
                        <div>
                            <span class="option-label">Call us directly</span>
                            <a href="tel:{phone}" class="option-value">{phone}</a>
                        </div>
                    </div>
                    
                    <div class="opening-hours">
                        <h4>Opening Hours</h4>
                        <div class="hours-list">
                            <div class="hours-item">
                                <span>Monday - Friday</span>
                                <span>12:00 PM - 10:00 PM</span>
                            </div>
                            <div class="hours-item">
                                <span>Saturday - Sunday</span>
                                <span>11:00 AM - 11:00 PM</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="reservation-form-wrapper">
                    <form class="reservation-form" id="reservationForm" onsubmit="return handleReservation(event)">
                        <div class="form-row">
                            <div class="form-group">
                                <label for="res-name">Full Name</label>
                                <input type="text" id="res-name" name="name" required placeholder="John Doe">
                            </div>
                            <div class="form-group">
                                <label for="res-phone">Phone Number</label>
                                <input type="tel" id="res-phone" name="phone" required placeholder="+1 234 567 890">
                            </div>
                        </div>
                        
                        <div class="form-row">
                            <div class="form-group">
                                <label for="res-date">Date</label>
                                <input type="date" id="res-date" name="date" required>
                            </div>
                            <div class="form-group">
                                <label for="res-time">Time</label>
                                <select id="res-time" name="time" required>
                                    <option value="">Select time</option>
                                    <option value="12:00">12:00 PM</option>
                                    <option value="13:00">1:00 PM</option>
                                    <option value="14:00">2:00 PM</option>
                                    <option value="18:00">6:00 PM</option>
                                    <option value="19:00">7:00 PM</option>
                                    <option value="20:00">8:00 PM</option>
                                    <option value="21:00">9:00 PM</option>
                                </select>
                            </div>
                        </div>
                        
                        <div class="form-group">
                            <label for="res-guests">Number of Guests</label>
                            <select id="res-guests" name="guests" required>
                                <option value="">Select guests</option>
                                <option value="1">1 Guest</option>
                                <option value="2">2 Guests</option>
                                <option value="3">3 Guests</option>
                                <option value="4">4 Guests</option>
                                <option value="5">5 Guests</option>
                                <option value="6">6 Guests</option>
                                <option value="7+">7+ Guests</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="res-notes">Special Requests (Optional)</label>
                            <textarea id="res-notes" name="notes" rows="3" placeholder="Any dietary requirements or special occasions?"></textarea>
                        </div>
                        
                        <button type="submit" class="submit-btn">Book Table</button>
                    </form>
                    
                    <div class="form-success" id="reservationSuccess" style="display:none;">
                        <span class="success-icon">✓</span>
                        <h3>Reservation Confirmed!</h3>
                        <p>We'll send a confirmation to your phone shortly.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .reservation-section {{
        padding: 120px 0;
        background: linear-gradient(135deg, {bg} 50%, #1a1a1a 50%);
    }}
    .reservation-section .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .reservation-grid {{
        display: grid;
        grid-template-columns: 1fr 1.2fr;
        gap: 80px;
        align-items: start;
    }}
    .section-label {{
        display: inline-block;
        font-size: 0.85rem;
        color: {primary};
        text-transform: uppercase;
        letter-spacing: 4px;
        margin-bottom: 20px;
    }}
    .section-title {{
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(2.5rem, 4vw, 3.5rem);
        color: {text};
        margin-bottom: 20px;
    }}
    .section-desc {{
        font-size: 1.1rem;
        color: {text}70;
        margin-bottom: 40px;
    }}
    .contact-option {{
        display: flex;
        align-items: center;
        gap: 20px;
        padding: 24px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 16px;
        margin-bottom: 40px;
    }}
    .option-icon {{ font-size: 2rem; }}
    .option-label {{
        font-size: 0.85rem;
        color: {text}60;
        display: block;
        margin-bottom: 4px;
    }}
    .option-value {{
        font-size: 1.2rem;
        color: {primary};
        text-decoration: none;
        font-weight: 600;
    }}
    .opening-hours h4 {{
        font-size: 1rem;
        color: {text};
        margin-bottom: 16px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    .hours-item {{
        display: flex;
        justify-content: space-between;
        padding: 12px 0;
        border-bottom: 1px solid {text}10;
        color: {text}70;
        font-size: 0.95rem;
    }}
    .reservation-form-wrapper {{
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 24px;
        padding: 50px;
    }}
    .form-row {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }}
    .form-group {{
        margin-bottom: 24px;
    }}
    .form-group label {{
        display: block;
        font-size: 0.9rem;
        color: {text}80;
        margin-bottom: 10px;
    }}
    .form-group input,
    .form-group select,
    .form-group textarea {{
        width: 100%;
        padding: 16px 20px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        color: {text};
        font-size: 1rem;
        transition: all 0.3s;
    }}
    .form-group input:focus,
    .form-group select:focus,
    .form-group textarea:focus {{
        outline: none;
        border-color: {primary};
        background: rgba(255,255,255,0.08);
    }}
    .submit-btn {{
        width: 100%;
        padding: 18px;
        background: {primary};
        color: #0A0A0A;
        border: none;
        border-radius: 12px;
        font-size: 1rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .submit-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px {primary}40;
    }}
    .form-success {{
        text-align: center;
        padding: 60px;
    }}
    .success-icon {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 80px;
        height: 80px;
        background: #22C55E;
        color: white;
        font-size: 2rem;
        border-radius: 50%;
        margin-bottom: 24px;
    }}
    .form-success h3 {{
        color: {text};
        font-size: 1.5rem;
        margin-bottom: 10px;
    }}
    .form-success p {{
        color: {text}60;
    }}
    @media (max-width: 1024px) {{
        .reservation-grid {{ grid-template-columns: 1fr; gap: 60px; }}
        .reservation-section {{ background: {bg}; }}
    }}
    @media (max-width: 640px) {{
        .form-row {{ grid-template-columns: 1fr; }}
        .reservation-form-wrapper {{ padding: 30px 24px; }}
    }}
    </style>
    
    <script>
    function handleReservation(e) {{
        e.preventDefault();
        const form = document.getElementById('reservationForm');
        const success = document.getElementById('reservationSuccess');
        form.style.display = 'none';
        success.style.display = 'block';
        return false;
    }}
    </script>
    '''
