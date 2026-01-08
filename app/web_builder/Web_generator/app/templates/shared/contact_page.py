"""
Contact Page Templates - Fully Functional
Includes Contact Form, Google Maps, Opening Hours, Social Links
"""

from typing import Dict, Any


class ContactPageTemplates:
    """Complete contact page templates with all functional elements"""
    
    VARIANTS = [
        "modern_split",
        "centered_elegant",
        "minimal_clean",
        "dark_professional"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        variant = variant or "modern_split"
        
        if variant == "modern_split":
            return cls._render_modern_split(props, colors)
        elif variant == "centered_elegant":
            return cls._render_centered_elegant(props, colors)
        elif variant == "minimal_clean":
            return cls._render_minimal_clean(props, colors)
        else:
            return cls._render_modern_split(props, colors)
    
    @classmethod
    def _render_modern_split(cls, props: Dict[str, Any], colors: Dict[str, str]) -> str:
        primary = colors.get("primary", "#6366f1")
        bg = colors.get("background", "#ffffff")
        text = colors.get("text", "#1f2937")
        
        # Extract props
        business_name = props.get("businessName", props.get("projectName", "Our Business"))
        address = props.get("address", "123 Main Street, City, Country")
        phone = props.get("phone", "+1 234 567 890")
        email = props.get("email", "hello@business.com")
        hours = props.get("hours", {
            "monday": "9:00 AM - 6:00 PM",
            "tuesday": "9:00 AM - 6:00 PM",
            "wednesday": "9:00 AM - 6:00 PM",
            "thursday": "9:00 AM - 6:00 PM",
            "friday": "9:00 AM - 6:00 PM",
            "saturday": "10:00 AM - 4:00 PM",
            "sunday": "Closed"
        })
        social = props.get("social", {})
        
        # Build hours HTML
        hours_html = ""
        for day, time in hours.items():
            is_closed = "closed" if time.lower() == "closed" else ""
            hours_html += f'<div class="hours-row {is_closed}"><span class="day">{day.capitalize()}</span><span class="time">{time}</span></div>'
        
        # Build social links
        social_html = ""
        social_icons = {
            "facebook": '<svg viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95c5.05-.5 9-4.76 9-9.95z"/></svg>',
            "instagram": '<svg viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M12 2c2.717 0 3.056.01 4.122.06 1.065.05 1.79.217 2.428.465.66.254 1.216.598 1.772 1.153.509.5.902 1.105 1.153 1.772.247.637.415 1.363.465 2.428.047 1.066.06 1.405.06 4.122 0 2.717-.01 3.056-.06 4.122-.05 1.065-.218 1.79-.465 2.428a4.883 4.883 0 01-1.153 1.772c-.5.508-1.105.902-1.772 1.153-.637.247-1.363.415-2.428.465-1.066.047-1.405.06-4.122.06-2.717 0-3.056-.01-4.122-.06-1.065-.05-1.79-.218-2.428-.465a4.89 4.89 0 01-1.772-1.153 4.904 4.904 0 01-1.153-1.772c-.248-.637-.415-1.363-.465-2.428C2.013 15.056 2 14.717 2 12c0-2.717.01-3.056.06-4.122.05-1.066.217-1.79.465-2.428a4.88 4.88 0 011.153-1.772A4.897 4.897 0 015.45 2.525c.638-.248 1.362-.415 2.428-.465C8.944 2.013 9.283 2 12 2zm0 1.802c-2.67 0-2.986.01-4.04.058-.976.045-1.505.207-1.858.344-.466.182-.8.398-1.15.748-.35.35-.566.684-.748 1.15-.137.353-.3.882-.344 1.857-.048 1.055-.058 1.37-.058 4.041 0 2.67.01 2.986.058 4.04.045.976.207 1.505.344 1.858.182.466.399.8.748 1.15.35.35.684.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058 2.67 0 2.987-.01 4.04-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.684.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041 0-2.67-.01-2.986-.058-4.04-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.055-.048-1.37-.058-4.041-.058zm0 3.063a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 8.468a3.333 3.333 0 100-6.666 3.333 3.333 0 000 6.666zm5.338-9.87a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z"/></svg>',
            "twitter": '<svg viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>',
            "linkedin": '<svg viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>',
            "youtube": '<svg viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>',
            "whatsapp": '<svg viewBox="0 0 24 24" width="20" height="20"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'
        }
        
        for platform, url in social.items():
            if platform.lower() in social_icons:
                social_html += f'<a href="{url}" target="_blank" rel="noopener" class="social-link">{social_icons[platform.lower()]}</a>'
        
        # Map embed
        encoded_address = address.replace(" ", "+").replace(",", "%2C")
        
        return f'''
        <section class="contact-page" id="contact">
            <div class="contact-grid">
                <!-- Left Side - Info -->
                <div class="contact-info">
                    <div class="info-content">
                        <h1 class="page-title">Get in Touch</h1>
                        <p class="page-subtitle">We'd love to hear from you. Send us a message and we'll respond as soon as possible.</p>
                        
                        <div class="info-cards">
                            <div class="info-card">
                                <div class="info-icon">
                                    <svg viewBox="0 0 24 24" width="24" height="24"><path fill="{primary}" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
                                </div>
                                <div class="info-text">
                                    <h4>Address</h4>
                                    <p>{address}</p>
                                </div>
                            </div>
                            
                            <div class="info-card">
                                <div class="info-icon">
                                    <svg viewBox="0 0 24 24" width="24" height="24"><path fill="{primary}" d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                                </div>
                                <div class="info-text">
                                    <h4>Phone</h4>
                                    <p><a href="tel:{phone.replace(' ', '')}">{phone}</a></p>
                                </div>
                            </div>
                            
                            <div class="info-card">
                                <div class="info-icon">
                                    <svg viewBox="0 0 24 24" width="24" height="24"><path fill="{primary}" d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                                </div>
                                <div class="info-text">
                                    <h4>Email</h4>
                                    <p><a href="mailto:{email}">{email}</a></p>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Opening Hours -->
                        <div class="hours-section">
                            <h3>Opening Hours</h3>
                            <div class="hours-list">{hours_html}</div>
                        </div>
                        
                        <!-- Social Links -->
                        <div class="social-section">
                            <h4>Follow Us</h4>
                            <div class="social-links">{social_html if social_html else '<p style="color:#6b7280;">Coming soon!</p>'}</div>
                        </div>
                    </div>
                </div>
                
                <!-- Right Side - Form & Map -->
                <div class="contact-form-section">
                    <div class="form-card">
                        <h2>Send us a Message</h2>
                        <form id="contactForm" onsubmit="return handleContactSubmit(event)">
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="firstName">First Name *</label>
                                    <input type="text" id="firstName" name="firstName" required placeholder="John" />
                                </div>
                                <div class="form-group">
                                    <label for="lastName">Last Name *</label>
                                    <input type="text" id="lastName" name="lastName" required placeholder="Doe" />
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="contactEmail">Email Address *</label>
                                <input type="email" id="contactEmail" name="email" required placeholder="john@example.com" />
                            </div>
                            <div class="form-group">
                                <label for="contactPhone">Phone Number</label>
                                <input type="tel" id="contactPhone" name="phone" placeholder="+1 234 567 890" />
                            </div>
                            <div class="form-group">
                                <label for="subject">Subject *</label>
                                <select id="subject" name="subject" required>
                                    <option value="">Select a topic</option>
                                    <option value="general">General Inquiry</option>
                                    <option value="support">Customer Support</option>
                                    <option value="feedback">Feedback</option>
                                    <option value="partnership">Partnership</option>
                                    <option value="other">Other</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label for="message">Message *</label>
                                <textarea id="message" name="message" rows="5" required placeholder="How can we help you?"></textarea>
                            </div>
                            <button type="submit" class="submit-button">
                                <span class="btn-text">Send Message</span>
                                <span class="btn-loading" style="display:none;">Sending...</span>
                            </button>
                        </form>
                        
                        <div class="form-success" id="formSuccess" style="display:none;">
                            <div class="success-icon">✓</div>
                            <h3>Message Sent!</h3>
                            <p>Thank you for reaching out. We'll get back to you within 24 hours.</p>
                        </div>
                    </div>
                    
                    <!-- Map -->
                    <div class="map-section">
                        <h3>Find Us</h3>
                        <div class="map-container">
                            <iframe 
                                src="https://maps.google.com/maps?q={encoded_address}&output=embed"
                                width="100%"
                                height="300"
                                style="border:0; border-radius: 16px;"
                                allowfullscreen=""
                                loading="lazy">
                            </iframe>
                        </div>
                        <a href="https://maps.google.com/?q={encoded_address}" target="_blank" class="directions-btn">
                            Get Directions →
                        </a>
                    </div>
                </div>
            </div>
        </section>
        
        <style>
        .contact-page {{
            min-height: 100vh;
            padding: 100px 0 60px;
            background: {bg};
        }}
        .contact-grid {{
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            max-width: 1400px;
            margin: 0 auto;
            gap: 60px;
            padding: 0 40px;
        }}
        .contact-info {{
            padding-right: 40px;
        }}
        .page-title {{
            font-size: 2.5rem;
            font-weight: 700;
            color: {text};
            margin-bottom: 16px;
        }}
        .page-subtitle {{
            color: #6b7280;
            font-size: 1.1rem;
            line-height: 1.7;
            margin-bottom: 40px;
        }}
        .info-cards {{ display: flex; flex-direction: column; gap: 24px; }}
        .info-card {{
            display: flex;
            align-items: flex-start;
            gap: 16px;
        }}
        .info-icon {{
            width: 50px;
            height: 50px;
            background: {primary}15;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }}
        .info-text h4 {{
            margin: 0 0 4px;
            color: {text};
            font-weight: 600;
        }}
        .info-text p {{ margin: 0; color: #6b7280; }}
        .info-text a {{ color: {primary}; text-decoration: none; }}
        .info-text a:hover {{ text-decoration: underline; }}
        
        .hours-section {{
            margin-top: 50px;
            padding: 30px;
            background: #f9fafb;
            border-radius: 16px;
        }}
        .hours-section h3 {{
            margin: 0 0 20px;
            color: {text};
        }}
        .hours-list {{ display: flex; flex-direction: column; gap: 12px; }}
        .hours-row {{
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px dashed #e5e7eb;
        }}
        .hours-row:last-child {{ border-bottom: none; }}
        .hours-row .day {{ font-weight: 500; color: {text}; text-transform: capitalize; }}
        .hours-row .time {{ color: #6b7280; }}
        .hours-row.closed .time {{ color: #ef4444; }}
        
        .social-section {{
            margin-top: 40px;
        }}
        .social-section h4 {{
            margin: 0 0 16px;
            color: {text};
        }}
        .social-links {{
            display: flex;
            gap: 12px;
        }}
        .social-link {{
            width: 44px;
            height: 44px;
            background: {primary};
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        .social-link:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 25px {primary}40;
        }}
        
        /* Form Section */
        .form-card {{
            background: white;
            padding: 40px;
            border-radius: 24px;
            box-shadow: 0 10px 50px rgba(0,0,0,0.08);
        }}
        .form-card h2 {{
            margin: 0 0 30px;
            color: {text};
        }}
        .form-row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }}
        .form-group {{
            margin-bottom: 20px;
        }}
        .form-group label {{
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: {text};
        }}
        .form-group input,
        .form-group select,
        .form-group textarea {{
            width: 100%;
            padding: 14px 16px;
            border: 2px solid #e5e7eb;
            border-radius: 10px;
            font-size: 1rem;
            transition: all 0.3s;
            background: white;
        }}
        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {{
            outline: none;
            border-color: {primary};
            box-shadow: 0 0 0 4px {primary}15;
        }}
        .submit-button {{
            width: 100%;
            padding: 16px;
            background: {primary};
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }}
        .submit-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 30px {primary}40;
        }}
        .submit-button:disabled {{ opacity: 0.7; cursor: not-allowed; }}
        
        .form-success {{
            text-align: center;
            padding: 40px;
        }}
        .success-icon {{
            width: 70px;
            height: 70px;
            background: #22c55e;
            color: white;
            font-size: 2rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px;
        }}
        .form-success h3 {{ color: #166534; margin-bottom: 8px; }}
        .form-success p {{ color: #15803d; }}
        
        /* Map */
        .map-section {{
            margin-top: 40px;
        }}
        .map-section h3 {{
            margin: 0 0 16px;
            color: {text};
        }}
        .map-container {{
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }}
        .directions-btn {{
            display: inline-block;
            margin-top: 16px;
            color: {primary};
            font-weight: 600;
            text-decoration: none;
        }}
        .directions-btn:hover {{ text-decoration: underline; }}
        
        @media (max-width: 1024px) {{
            .contact-grid {{
                grid-template-columns: 1fr;
                padding: 0 24px;
            }}
            .contact-info {{ padding-right: 0; }}
        }}
        @media (max-width: 600px) {{
            .form-row {{ grid-template-columns: 1fr; }}
            .form-card {{ padding: 24px; }}
        }}
        </style>
        
        <script>
        function handleContactSubmit(e) {{
            e.preventDefault();
            const form = document.getElementById('contactForm');
            const btn = form.querySelector('.submit-button');
            const btnText = btn.querySelector('.btn-text');
            const btnLoading = btn.querySelector('.btn-loading');
            
            // Show loading
            btnText.style.display = 'none';
            btnLoading.style.display = 'inline';
            btn.disabled = true;
            
            // Simulate form submission
            setTimeout(() => {{
                form.style.display = 'none';
                document.getElementById('formSuccess').style.display = 'block';
            }}, 1500);
            
            return false;
        }}
        </script>
        '''
    
    @classmethod
    def _render_centered_elegant(cls, props: Dict[str, Any], colors: Dict[str, str]) -> str:
        """Elegant centered contact layout"""
        primary = colors.get("primary", "#6366f1")
        text = colors.get("text", "#1f2937")
        
        address = props.get("address", "123 Main Street, City")
        phone = props.get("phone", "+1 234 567 890")
        email = props.get("email", "hello@business.com")
        
        return f'''
        <section class="contact-elegant" id="contact">
            <div class="container">
                <div class="contact-header">
                    <span class="contact-label">Contact Us</span>
                    <h1>Let's Start a Conversation</h1>
                    <p>Have a question or want to work together? We'd love to hear from you.</p>
                </div>
                
                <div class="contact-methods">
                    <a href="mailto:{email}" class="contact-method">
                        <div class="method-icon">✉️</div>
                        <span class="method-label">Email Us</span>
                        <span class="method-value">{email}</span>
                    </a>
                    <a href="tel:{phone.replace(' ', '')}" class="contact-method">
                        <div class="method-icon">📞</div>
                        <span class="method-label">Call Us</span>
                        <span class="method-value">{phone}</span>
                    </a>
                    <div class="contact-method">
                        <div class="method-icon">📍</div>
                        <span class="method-label">Visit Us</span>
                        <span class="method-value">{address}</span>
                    </div>
                </div>
            </div>
        </section>
        
        <style>
        .contact-elegant {{
            padding: 120px 24px;
            background: linear-gradient(135deg, #fafafa 0%, {primary}08 100%);
        }}
        .contact-elegant .container {{ max-width: 1000px; margin: 0 auto; }}
        .contact-header {{ text-align: center; margin-bottom: 60px; }}
        .contact-label {{
            display: inline-block;
            padding: 8px 20px;
            background: {primary}15;
            color: {primary};
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.9rem;
            margin-bottom: 20px;
        }}
        .contact-header h1 {{
            font-size: clamp(2rem, 5vw, 3rem);
            color: {text};
            margin-bottom: 16px;
        }}
        .contact-header p {{ color: #6b7280; font-size: 1.2rem; }}
        .contact-methods {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
        }}
        .contact-method {{
            background: white;
            padding: 40px 30px;
            border-radius: 20px;
            text-align: center;
            text-decoration: none;
            box-shadow: 0 10px 40px rgba(0,0,0,0.06);
            transition: all 0.3s;
        }}
        .contact-method:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 50px rgba(0,0,0,0.1);
        }}
        .method-icon {{ font-size: 2.5rem; margin-bottom: 16px; }}
        .method-label {{
            display: block;
            font-size: 0.9rem;
            color: #6b7280;
            margin-bottom: 8px;
        }}
        .method-value {{
            display: block;
            font-weight: 600;
            color: {text};
            font-size: 1rem;
        }}
        @media (max-width: 768px) {{
            .contact-methods {{ grid-template-columns: 1fr; }}
        }}
        </style>
        '''
    
    @classmethod
    def _render_minimal_clean(cls, props: Dict[str, Any], colors: Dict[str, str]) -> str:
        """Minimal clean contact section"""
        primary = colors.get("primary", "#6366f1")
        email = props.get("email", "hello@business.com")
        
        return f'''
        <section class="contact-minimal" id="contact">
            <div class="container">
                <h2>Got a project in mind?</h2>
                <a href="mailto:{email}" class="contact-cta">{email}</a>
            </div>
        </section>
        
        <style>
        .contact-minimal {{
            padding: 150px 24px;
            text-align: center;
        }}
        .contact-minimal h2 {{
            font-size: 1.5rem;
            color: #6b7280;
            font-weight: 400;
            margin-bottom: 20px;
        }}
        .contact-cta {{
            font-size: clamp(2rem, 6vw, 4rem);
            color: {primary};
            text-decoration: none;
            font-weight: 700;
            transition: opacity 0.3s;
        }}
        .contact-cta:hover {{ opacity: 0.7; }}
        </style>
        '''
