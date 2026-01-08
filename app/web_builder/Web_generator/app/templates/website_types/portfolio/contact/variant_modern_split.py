from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Modern Split - Contact section with split layout,
    form and contact info
    """
    title = props.get("sectionTitle", props.get("title", "Let's Work Together"))
    subtitle = props.get("subtitle", "Have a project in mind? Let's create something amazing.")
    email = props.get("email", "hello@example.com")
    phone = props.get("phone", "+1 234 567 890")
    
    primary = colors.get("primary", "#6366F1")
    bg = colors.get("background", "#0F172A")
    text = colors.get("text", "#F8FAFC")
    
    return f'''
    <section class="contact-section" id="contact">
        <div class="container">
            <div class="contact-grid">
                <div class="contact-info">
                    <span class="section-label">Contact</span>
                    <h2 class="section-title">{title}</h2>
                    <p class="section-desc">{subtitle}</p>
                    
                    <div class="contact-details">
                        <div class="contact-item">
                            <span class="item-icon">📧</span>
                            <div class="item-content">
                                <span class="item-label">Email</span>
                                <a href="mailto:{email}" class="item-value">{email}</a>
                            </div>
                        </div>
                        <div class="contact-item">
                            <span class="item-icon">📱</span>
                            <div class="item-content">
                                <span class="item-label">Phone</span>
                                <a href="tel:{phone}" class="item-value">{phone}</a>
                            </div>
                        </div>
                    </div>
                    
                    <div class="social-links">
                        <a href="#" class="social-link">LinkedIn</a>
                        <a href="#" class="social-link">GitHub</a>
                        <a href="#" class="social-link">Twitter</a>
                        <a href="#" class="social-link">Dribbble</a>
                    </div>
                </div>
                
                <div class="contact-form-wrapper">
                    <form class="contact-form" id="contactForm" onsubmit="return handleSubmit(event)">
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" id="name" name="name" required placeholder="Your name">
                        </div>
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" required placeholder="your@email.com">
                        </div>
                        <div class="form-group">
                            <label for="project">Project Type</label>
                            <select id="project" name="project">
                                <option value="">Select project type</option>
                                <option value="website">Website Design</option>
                                <option value="app">Mobile App</option>
                                <option value="branding">Branding</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea id="message" name="message" rows="4" required placeholder="Tell me about your project..."></textarea>
                        </div>
                        <button type="submit" class="submit-btn">
                            <span class="btn-text">Send Message</span>
                            <span class="btn-loading" style="display:none;">Sending...</span>
                        </button>
                    </form>
                    <div class="form-success" id="formSuccess" style="display:none;">
                        <span class="success-icon">✓</span>
                        <h3>Message Sent!</h3>
                        <p>I'll get back to you within 24 hours.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <style>
    .contact-section {{
        padding: 120px 0;
        background: {bg};
    }}
    .contact-section .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .contact-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: start;
    }}
    .section-label {{
        display: inline-block;
        padding: 8px 20px;
        background: {primary}20;
        color: {primary};
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }}
    .section-title {{
        font-size: clamp(2.5rem, 5vw, 3.5rem);
        font-weight: 700;
        color: {text};
        margin-bottom: 20px;
    }}
    .section-desc {{
        font-size: 1.2rem;
        color: {text}70;
        margin-bottom: 50px;
        line-height: 1.7;
    }}
    .contact-details {{
        margin-bottom: 50px;
    }}
    .contact-item {{
        display: flex;
        align-items: center;
        gap: 20px;
        padding: 20px 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }}
    .item-icon {{
        font-size: 1.5rem;
    }}
    .item-label {{
        display: block;
        font-size: 0.8rem;
        color: {text}50;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 4px;
    }}
    .item-value {{
        color: {text};
        text-decoration: none;
        font-size: 1.1rem;
        font-weight: 500;
        transition: color 0.3s;
    }}
    .item-value:hover {{
        color: {primary};
    }}
    .social-links {{
        display: flex;
        gap: 30px;
    }}
    .social-link {{
        color: {text}60;
        text-decoration: none;
        font-size: 0.95rem;
        transition: color 0.3s;
    }}
    .social-link:hover {{
        color: {primary};
    }}
    .contact-form-wrapper {{
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 24px;
        padding: 50px;
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
    .form-group input::placeholder,
    .form-group textarea::placeholder {{
        color: {text}40;
    }}
    .submit-btn {{
        width: 100%;
        padding: 18px;
        background: {primary};
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .submit-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 15px 40px {primary}30;
    }}
    .form-success {{
        text-align: center;
        padding: 60px 40px;
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
        .contact-grid {{ grid-template-columns: 1fr; gap: 60px; }}
    }}
    @media (max-width: 640px) {{
        .contact-form-wrapper {{ padding: 30px 24px; }}
        .contact-section .container {{ padding: 0 24px; }}
    }}
    </style>
    
    <script>
    function handleSubmit(e) {{
        e.preventDefault();
        const form = document.getElementById('contactForm');
        const btn = form.querySelector('.submit-btn');
        btn.querySelector('.btn-text').style.display = 'none';
        btn.querySelector('.btn-loading').style.display = 'inline';
        btn.disabled = true;
        
        setTimeout(() => {{
            form.style.display = 'none';
            document.getElementById('formSuccess').style.display = 'block';
        }}, 1500);
        
        return false;
    }}
    </script>
    '''
