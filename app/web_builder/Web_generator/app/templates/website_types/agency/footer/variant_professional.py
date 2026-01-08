from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Agency Footer - Professional footer with links, contact, and newsletter
    """
    name = props.get("name", props.get("businessName", "Apex Digital"))
    email = props.get("email", "hello@apexdigital.com")
    phone = props.get("phone", "+1 234 567 890")
    address = props.get("address", "123 Business Ave, NYC")
    
    primary = colors.get("primary", "#2563EB")
    bg = colors.get("background", "#0F172A")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <footer class="agency-footer" id="footer">
        <div class="container">
            <div class="footer-top">
                <div class="footer-cta">
                    <h2>Have a project in mind?</h2>
                    <a href="#contact" class="cta-btn">Let's Talk</a>
                </div>
            </div>
            
            <div class="footer-main">
                <div class="footer-brand">
                    <h3 class="brand-name">{name}</h3>
                    <p class="brand-desc">We help brands grow through strategy, design, and technology.</p>
                </div>
                
                <div class="footer-links">
                    <div class="link-group">
                        <h4>Company</h4>
                        <a href="#about">About Us</a>
                        <a href="#services">Services</a>
                        <a href="#work">Our Work</a>
                        <a href="#contact">Contact</a>
                    </div>
                    <div class="link-group">
                        <h4>Services</h4>
                        <a href="#">Web Development</a>
                        <a href="#">UI/UX Design</a>
                        <a href="#">Digital Marketing</a>
                        <a href="#">Branding</a>
                    </div>
                </div>
                
                <div class="footer-contact">
                    <h4>Get in Touch</h4>
                    <a href="mailto:{email}">{email}</a>
                    <a href="tel:{phone}">{phone}</a>
                    <p>{address}</p>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>© 2024 {name}. All rights reserved.</p>
                <div class="social-links">
                    <a href="#">LinkedIn</a>
                    <a href="#">Twitter</a>
                    <a href="#">Instagram</a>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .agency-footer {{
        background: {bg};
        padding: 80px 0 40px;
    }}
    .agency-footer .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .footer-top {{
        text-align: center;
        padding-bottom: 60px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 60px;
    }}
    .footer-cta h2 {{
        font-size: 2.5rem;
        color: {text};
        margin-bottom: 30px;
    }}
    .cta-btn {{
        display: inline-block;
        padding: 18px 48px;
        background: {primary};
        color: white;
        text-decoration: none;
        font-weight: 600;
        border-radius: 12px;
        transition: all 0.3s;
    }}
    .cta-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px {primary}40;
    }}
    .footer-main {{
        display: grid;
        grid-template-columns: 1.5fr 2fr 1fr;
        gap: 60px;
        margin-bottom: 60px;
    }}
    .brand-name {{
        font-size: 1.5rem;
        color: {text};
        margin-bottom: 16px;
    }}
    .brand-desc {{
        color: rgba(255,255,255,0.6);
        line-height: 1.7;
    }}
    .footer-links {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 40px;
    }}
    .link-group h4 {{
        font-size: 0.9rem;
        color: {text};
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .link-group a {{
        display: block;
        color: rgba(255,255,255,0.6);
        text-decoration: none;
        padding: 8px 0;
        transition: color 0.3s;
    }}
    .link-group a:hover {{ color: {primary}; }}
    .footer-contact h4 {{
        font-size: 0.9rem;
        color: {text};
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .footer-contact a,
    .footer-contact p {{
        display: block;
        color: rgba(255,255,255,0.6);
        text-decoration: none;
        padding: 6px 0;
    }}
    .footer-contact a:hover {{ color: {primary}; }}
    .footer-bottom {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 30px;
        border-top: 1px solid rgba(255,255,255,0.1);
    }}
    .footer-bottom p {{
        color: rgba(255,255,255,0.4);
        font-size: 0.9rem;
    }}
    .social-links {{
        display: flex;
        gap: 24px;
    }}
    .social-links a {{
        color: rgba(255,255,255,0.6);
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s;
    }}
    .social-links a:hover {{ color: {primary}; }}
    @media (max-width: 900px) {{
        .footer-main {{ grid-template-columns: 1fr; gap: 40px; }}
        .footer-bottom {{ flex-direction: column; gap: 20px; text-align: center; }}
    }}
    </style>
    '''
