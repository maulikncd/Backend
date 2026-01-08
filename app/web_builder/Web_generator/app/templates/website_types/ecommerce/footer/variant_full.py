from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """
    E-commerce Footer - Full shop footer with links,
    newsletter, payment icons and social links
    """
    name = props.get("name", props.get("businessName", "ShopHub"))
    email = props.get("email", "support@shophub.com")
    phone = props.get("phone", "+1 234 567 890")
    
    primary = colors.get("primary", "#000000")
    bg = colors.get("background", "#111111")
    text = colors.get("text", "#FFFFFF")
    
    return f'''
    <footer class="shop-footer" id="footer">
        <div class="container">
            <div class="footer-top">
                <div class="footer-newsletter">
                    <h3>Subscribe to Our Newsletter</h3>
                    <p>Get 10% off your first order and stay updated on new arrivals!</p>
                    <form class="newsletter-form" onsubmit="return handleNewsletterSubmit(event)">
                        <input type="email" placeholder="Enter your email" required>
                        <button type="submit">Subscribe</button>
                    </form>
                </div>
            </div>
            
            <div class="footer-main">
                <div class="footer-brand">
                    <h2 class="brand-name">{name}</h2>
                    <p class="brand-desc">Your one-stop shop for premium products at unbeatable prices.</p>
                    <div class="contact-info">
                        <a href="mailto:{email}">{email}</a>
                        <a href="tel:{phone}">{phone}</a>
                    </div>
                </div>
                
                <div class="footer-links">
                    <div class="link-group">
                        <h4>Shop</h4>
                        <a href="#">All Products</a>
                        <a href="#">New Arrivals</a>
                        <a href="#">Best Sellers</a>
                        <a href="#">Sale</a>
                    </div>
                    <div class="link-group">
                        <h4>Support</h4>
                        <a href="#">Contact Us</a>
                        <a href="#">FAQs</a>
                        <a href="#">Shipping Info</a>
                        <a href="#">Returns</a>
                    </div>
                    <div class="link-group">
                        <h4>Company</h4>
                        <a href="#">About Us</a>
                        <a href="#">Careers</a>
                        <a href="#">Press</a>
                        <a href="#">Blog</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <div class="payment-methods">
                    <span>We Accept:</span>
                    <div class="payment-icons">
                        <span class="payment-icon">💳 Visa</span>
                        <span class="payment-icon">💳 Mastercard</span>
                        <span class="payment-icon">💳 PayPal</span>
                        <span class="payment-icon">💳 Apple Pay</span>
                    </div>
                </div>
                
                <div class="social-links">
                    <a href="#" aria-label="Facebook">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
                    </a>
                    <a href="#" aria-label="Instagram">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
                    </a>
                    <a href="#" aria-label="Twitter">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                    </a>
                </div>
                
                <div class="copyright">
                    <p>© 2024 {name}. All rights reserved.</p>
                    <div class="legal-links">
                        <a href="#">Privacy Policy</a>
                        <a href="#">Terms of Service</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    
    <style>
    .shop-footer {{
        background: {bg};
        color: {text};
        padding: 80px 0 40px;
    }}
    .shop-footer .container {{
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 40px;
    }}
    .footer-top {{
        padding-bottom: 60px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 60px;
    }}
    .footer-newsletter {{
        max-width: 500px;
        margin: 0 auto;
        text-align: center;
    }}
    .footer-newsletter h3 {{
        font-size: 1.5rem;
        margin-bottom: 12px;
    }}
    .footer-newsletter p {{
        color: rgba(255,255,255,0.6);
        margin-bottom: 24px;
    }}
    .newsletter-form {{
        display: flex;
        gap: 12px;
    }}
    .newsletter-form input {{
        flex: 1;
        padding: 16px 24px;
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 50px;
        color: white;
        font-size: 1rem;
    }}
    .newsletter-form input::placeholder {{ color: rgba(255,255,255,0.5); }}
    .newsletter-form input:focus {{ outline: none; border-color: {primary}; }}
    .newsletter-form button {{
        padding: 16px 32px;
        background: {primary};
        color: white;
        border: none;
        border-radius: 50px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }}
    .newsletter-form button:hover {{ background: #333; }}
    .footer-main {{
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 60px;
        margin-bottom: 60px;
    }}
    .brand-name {{
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 16px;
    }}
    .brand-desc {{
        color: rgba(255,255,255,0.6);
        line-height: 1.7;
        margin-bottom: 24px;
    }}
    .contact-info a {{
        display: block;
        color: rgba(255,255,255,0.6);
        text-decoration: none;
        margin-bottom: 8px;
        transition: color 0.3s;
    }}
    .contact-info a:hover {{ color: white; }}
    .footer-links {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
    }}
    .link-group h4 {{
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 20px;
    }}
    .link-group a {{
        display: block;
        color: rgba(255,255,255,0.6);
        text-decoration: none;
        padding: 8px 0;
        transition: color 0.3s;
    }}
    .link-group a:hover {{ color: white; }}
    .footer-bottom {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 30px;
        padding-top: 40px;
        border-top: 1px solid rgba(255,255,255,0.1);
    }}
    .payment-methods {{
        display: flex;
        align-items: center;
        gap: 16px;
        color: rgba(255,255,255,0.6);
        font-size: 0.9rem;
    }}
    .payment-icons {{
        display: flex;
        gap: 12px;
    }}
    .payment-icon {{
        padding: 6px 12px;
        background: rgba(255,255,255,0.1);
        border-radius: 6px;
        font-size: 0.8rem;
    }}
    .social-links {{
        display: flex;
        gap: 12px;
    }}
    .social-links a {{
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        color: white;
        transition: all 0.3s;
    }}
    .social-links a:hover {{ background: {primary}; }}
    .copyright {{
        text-align: right;
    }}
    .copyright p {{
        color: rgba(255,255,255,0.4);
        font-size: 0.9rem;
        margin-bottom: 8px;
    }}
    .legal-links {{
        display: flex;
        gap: 20px;
    }}
    .legal-links a {{
        color: rgba(255,255,255,0.4);
        text-decoration: none;
        font-size: 0.85rem;
        transition: color 0.3s;
    }}
    .legal-links a:hover {{ color: white; }}
    @media (max-width: 900px) {{
        .footer-main {{ grid-template-columns: 1fr; }}
        .footer-links {{ grid-template-columns: repeat(3, 1fr); }}
        .footer-bottom {{ flex-direction: column; text-align: center; }}
        .copyright {{ text-align: center; }}
    }}
    @media (max-width: 600px) {{
        .footer-links {{ grid-template-columns: 1fr; text-align: center; }}
        .newsletter-form {{ flex-direction: column; }}
    }}
    </style>
    
    <script>
    function handleNewsletterSubmit(e) {{
        e.preventDefault();
        const form = e.target;
        const input = form.querySelector('input');
        const btn = form.querySelector('button');
        btn.textContent = 'Subscribed!';
        btn.disabled = true;
        input.value = '';
        setTimeout(() => {{
            btn.textContent = 'Subscribe';
            btn.disabled = false;
        }}, 3000);
        return false;
    }}
    </script>
    '''
