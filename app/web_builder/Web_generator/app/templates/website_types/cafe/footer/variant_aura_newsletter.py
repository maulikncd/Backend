from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    Aura Premium Footer - Elegant dark footer with newsletter 
    and premium styling
    """
    logo = props.get("logo", "Cafe Name")
    tagline = props.get("tagline", "Where every moment is a fresh delight")
    sections = props.get("sections", [])
    copyright_text = props.get("copyright", f"© 2025 {logo}. All rights reserved.")
    
    primary = colors.get("primary", "#8B7355")
    
    # Build sections
    sections_html = ""
    if sections:
        for section in sections[:2]:
            links_html = ""
            for link in section.get("links", [])[:5]:
                links_html += f'<a href="{link.get("href", "#")}">{link.get("text", "Link")}</a>'
            sections_html += f'''
            <div class="footer-links">
                <h4>{section.get("title", "Links")}</h4>
                {links_html}
            </div>
            '''
    else:
        sections_html = '''
            <div class="footer-links">
                <h4>Quick Links</h4>
                <a href="#home">Home</a>
                <a href="#about">Our Story</a>
                <a href="#menu">Menu</a>
                <a href="#gallery">Gallery</a>
                <a href="#contact">Contact</a>
            </div>
            <div class="footer-links">
                <h4>Hours</h4>
                <a href="#">Mon-Fri: 7AM - 9PM</a>
                <a href="#">Sat-Sun: 8AM - 10PM</a>
                <a href="#">Holidays: 9AM - 6PM</a>
            </div>
        '''
    
    return f'''
    <footer class="aura-footer">
        <div class="footer-container">
            <div class="footer-top">
                <div class="footer-brand">
                    <h3 class="footer-logo">{logo}</h3>
                    <p class="footer-tagline">{tagline}</p>
                    <div class="social-links">
                        <a href="#" class="social-link">
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/></svg>
                        </a>
                        <a href="#" class="social-link">
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z"/></svg>
                        </a>
                        <a href="#" class="social-link">
                            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"/></svg>
                        </a>
                    </div>
                </div>
                
                {sections_html}
                
                <div class="footer-newsletter">
                    <h4>Stay Updated</h4>
                    <p>Subscribe to our newsletter for exclusive offers and updates.</p>
                    <form class="newsletter-form">
                        <input type="email" placeholder="Enter your email">
                        <button type="submit">Subscribe</button>
                    </form>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>{copyright_text}</p>
                <div class="footer-legal">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .aura-footer {{
        background: #0D0D0D;
        color: #fff;
        padding: 80px 40px 30px;
    }}
    .footer-container {{ max-width: 1300px; margin: 0 auto; }}
    .footer-top {{
        display: grid;
        grid-template-columns: 1.5fr 1fr 1fr 1.5fr;
        gap: 60px;
        padding-bottom: 60px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }}
    .footer-logo {{
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        margin-bottom: 16px;
    }}
    .footer-tagline {{
        color: rgba(255,255,255,0.6);
        font-size: 0.95rem;
        margin-bottom: 24px;
        line-height: 1.6;
    }}
    .social-links {{ display: flex; gap: 12px; }}
    .social-link {{
        width: 44px;
        height: 44px;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;
        transition: all 0.3s;
    }}
    .social-link:hover {{ background: {primary}; transform: translateY(-3px); }}
    .footer-links h4, .footer-newsletter h4 {{
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 24px;
        color: #fff;
    }}
    .footer-links a {{
        display: block;
        color: rgba(255,255,255,0.6);
        text-decoration: none;
        padding: 8px 0;
        transition: color 0.3s;
    }}
    .footer-links a:hover {{ color: {primary}; }}
    .footer-newsletter p {{
        color: rgba(255,255,255,0.6);
        font-size: 0.9rem;
        margin-bottom: 20px;
    }}
    .newsletter-form {{
        display: flex;
        gap: 10px;
    }}
    .newsletter-form input {{
        flex: 1;
        padding: 14px 20px;
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 50px;
        color: #fff;
        font-size: 0.95rem;
    }}
    .newsletter-form input::placeholder {{ color: rgba(255,255,255,0.5); }}
    .newsletter-form button {{
        padding: 14px 30px;
        background: {primary};
        color: #fff;
        border: none;
        border-radius: 50px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .newsletter-form button:hover {{ transform: translateY(-2px); box-shadow: 0 10px 20px {primary}40; }}
    .footer-bottom {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 30px;
        flex-wrap: wrap;
        gap: 20px;
    }}
    .footer-bottom p {{ color: rgba(255,255,255,0.5); font-size: 0.9rem; }}
    .footer-legal {{ display: flex; gap: 30px; }}
    .footer-legal a {{
        color: rgba(255,255,255,0.5);
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s;
    }}
    .footer-legal a:hover {{ color: #fff; }}
    @media (max-width: 1024px) {{
        .footer-top {{ grid-template-columns: repeat(2, 1fr); gap: 40px; }}
    }}
    @media (max-width: 600px) {{
        .footer-top {{ grid-template-columns: 1fr; }}
        .newsletter-form {{ flex-direction: column; }}
    }}
    </style>
    '''
