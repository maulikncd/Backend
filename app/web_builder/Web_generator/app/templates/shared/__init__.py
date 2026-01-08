"""
Shared Templates - Used across all website types
Navbar, Contact, CTA, Testimonials - these are common components
"""

from typing import Dict, Any
import random


class SharedNavbarTemplates:
    """Universal Premium Navbar Templates"""
    
    VARIANTS = ["glassmorphic-premium", "floating-dark", "luxury-minimal", "sticky-minimal", "transparent-overlay"]
    PREMIUM_VARIANTS = ["glassmorphic-premium", "floating-dark", "luxury-minimal"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            # 80% chance for premium variant
            if random.random() < 0.8:
                variant = random.choice(cls.PREMIUM_VARIANTS)
            else:
                variant = random.choice(cls.VARIANTS)
        
        method_name = f"_variant_{variant.replace('-', '_')}"
        if hasattr(cls, method_name):
            return getattr(cls, method_name)(props, colors)
        return cls._variant_glassmorphic_premium(props, colors)
    
    @classmethod
    def _variant_glassmorphic_premium(cls, props: Dict[str, Any], colors: Dict[str, str]) -> str:
        """Ultra Modern Glassmorphic Navbar"""
        business_name = props.get("businessName", props.get("logo_text", "Brand"))
        nav_items = props.get("navItems", props.get("links", [
            {"text": "Home", "url": "#home"},
            {"text": "About", "url": "#about"},
            {"text": "Services", "url": "#services"},
            {"text": "Contact", "url": "#contact"}
        ]))
        cta_text = props.get("cta_text", "Get Started")
        primary = colors.get("primary", "#6366F1")
        secondary = colors.get("secondary", "#EC4899")
        
        nav_html = ""
        for item in nav_items:
            if isinstance(item, str):
                nav_html += f'<a href="#{item.lower()}" class="glass-nav-link">{item}</a>'
            else:
                nav_html += f'<a href="{item.get("url", "#")}" class="glass-nav-link">{item.get("text", "Link")}</a>'
        
        return f'''
        <nav id="glass-navbar" class="glass-navbar">
            <div class="glass-nav-inner">
                <a href="#" class="glass-logo">
                    <span class="logo-dot" style="background: linear-gradient(135deg, {primary}, {secondary})"></span>
                    <span class="logo-text">{business_name}</span>
                </a>
                
                <div class="glass-nav-links">{nav_html}</div>
                
                <a href="#contact" class="glass-cta">
                    <span>{cta_text}</span>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
                
                <button class="glass-mobile-btn" onclick="document.getElementById('glass-mobile-menu').classList.toggle('active')">
                    <span></span><span></span><span></span>
                </button>
            </div>
            
            <div class="glass-mobile-menu" id="glass-mobile-menu">
                {nav_html}
                <a href="#contact" class="glass-mobile-cta">{cta_text}</a>
            </div>
        </nav>
        
        <style>
        .glass-navbar {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
            padding: 16px 24px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .glass-navbar.scrolled {{
            padding: 8px 24px;
            background: rgba(255,255,255,0.9);
            backdrop-filter: blur(20px);
            box-shadow: 0 4px 30px rgba(0,0,0,0.08);
        }}
        .glass-nav-inner {{
            max-width: 1280px; margin: 0 auto;
            display: flex; align-items: center; justify-content: space-between;
            padding: 12px 24px;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(16px);
            border-radius: 100px;
            border: 1px solid rgba(255,255,255,0.15);
        }}
        .glass-navbar.scrolled .glass-nav-inner {{
            background: transparent; backdrop-filter: none; border: none;
        }}
        .glass-logo {{
            display: flex; align-items: center; gap: 10px;
            text-decoration: none; color: #fff;
        }}
        .glass-navbar.scrolled .glass-logo {{ color: #1a1a1a; }}
        .logo-dot {{
            width: 10px; height: 10px; border-radius: 50%;
            animation: pulse 2s ease-in-out infinite;
        }}
        @keyframes pulse {{ 0%,100% {{ transform: scale(1); }} 50% {{ transform: scale(1.2); }} }}
        .logo-text {{ font-weight: 700; font-size: 1.1rem; letter-spacing: -0.02em; }}
        .glass-nav-links {{
            display: flex; align-items: center; gap: 8px;
            padding: 4px; background: rgba(255,255,255,0.05); border-radius: 50px;
        }}
        .glass-nav-link {{
            padding: 10px 18px; color: rgba(255,255,255,0.85);
            text-decoration: none; font-size: 0.9rem; font-weight: 500;
            border-radius: 50px; transition: all 0.3s;
        }}
        .glass-navbar.scrolled .glass-nav-link {{ color: #4a4a4a; }}
        .glass-nav-link:hover {{ background: rgba(255,255,255,0.15); color: #fff; }}
        .glass-navbar.scrolled .glass-nav-link:hover {{ background: rgba(0,0,0,0.05); color: {primary}; }}
        .glass-cta {{
            display: flex; align-items: center; gap: 8px;
            padding: 12px 24px;
            background: linear-gradient(135deg, {primary}, {secondary});
            color: #fff; text-decoration: none;
            font-size: 0.9rem; font-weight: 600;
            border-radius: 50px;
            transition: all 0.3s;
            box-shadow: 0 4px 15px {primary}50;
        }}
        .glass-cta:hover {{ transform: translateY(-2px); box-shadow: 0 8px 25px {primary}60; }}
        .glass-cta svg {{ transition: transform 0.3s; }}
        .glass-cta:hover svg {{ transform: translateX(4px); }}
        .glass-mobile-btn {{
            display: none; flex-direction: column; gap: 5px;
            padding: 10px; background: transparent; border: none; cursor: pointer;
        }}
        .glass-mobile-btn span {{
            width: 22px; height: 2px; background: #fff; border-radius: 2px; transition: 0.3s;
        }}
        .glass-navbar.scrolled .glass-mobile-btn span {{ background: #1a1a1a; }}
        .glass-mobile-menu {{
            display: none; flex-direction: column; gap: 8px;
            margin-top: 12px; padding: 24px;
            background: rgba(255,255,255,0.95); backdrop-filter: blur(20px);
            border-radius: 24px; box-shadow: 0 20px 50px rgba(0,0,0,0.15);
        }}
        .glass-mobile-menu.active {{ display: flex; }}
        .glass-mobile-menu .glass-nav-link {{ color: #1a1a1a; padding: 16px 20px; border-radius: 12px; }}
        .glass-mobile-cta {{
            margin-top: 16px; padding: 16px;
            background: linear-gradient(135deg, {primary}, {secondary});
            color: #fff; text-align: center; text-decoration: none;
            font-weight: 600; border-radius: 12px;
        }}
        @media (max-width: 768px) {{
            .glass-nav-links, .glass-cta {{ display: none; }}
            .glass-mobile-btn {{ display: flex; }}
        }}
        </style>
        
        <script>
        window.addEventListener('scroll', () => {{
            const nav = document.getElementById('glass-navbar');
            if (window.scrollY > 50) nav.classList.add('scrolled');
            else nav.classList.remove('scrolled');
        }});
        </script>
        '''
    
    @classmethod
    def _variant_floating_dark(cls, props: Dict[str, Any], colors: Dict[str, str]) -> str:
        """Modern Floating Dark Navbar"""
        business_name = props.get("businessName", props.get("logo_text", "Brand"))
        nav_items = props.get("navItems", props.get("links", [
            {"text": "Home", "url": "#home"},
            {"text": "About", "url": "#about"},
            {"text": "Services", "url": "#services"},
            {"text": "Contact", "url": "#contact"}
        ]))
        primary = colors.get("primary", "#6366F1")
        
        nav_html = ""
        for item in nav_items:
            if isinstance(item, str):
                nav_html += f'<a href="#{item.lower()}" class="dark-nav-link">{item}</a>'
            else:
                nav_html += f'<a href="{item.get("url", "#")}" class="dark-nav-link">{item.get("text", "Link")}</a>'
        
        return f'''
        <nav id="dark-navbar" class="dark-navbar">
            <div class="dark-nav-container">
                <a href="#" class="dark-logo">
                    <div class="logo-ring" style="border-color: {primary}"><span>{business_name[0] if business_name else "B"}</span></div>
                    <span class="logo-name">{business_name}</span>
                </a>
                <div class="dark-nav-links">{nav_html}</div>
                <a href="#contact" class="dark-cta">Book Now</a>
            </div>
        </nav>
        
        <style>
        .dark-navbar {{
            position: fixed; top: 20px; left: 50%; transform: translateX(-50%);
            z-index: 9999; width: calc(100% - 48px); max-width: 1200px;
        }}
        .dark-nav-container {{
            display: flex; justify-content: space-between; align-items: center;
            padding: 12px 12px 12px 20px;
            background: rgba(10,10,10,0.9); backdrop-filter: blur(24px);
            border-radius: 100px; border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
        }}
        .dark-logo {{
            display: flex; align-items: center; gap: 12px;
            text-decoration: none; color: #fff;
        }}
        .logo-ring {{
            width: 40px; height: 40px; border: 2px solid {primary};
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
            font-weight: 700; color: #fff;
        }}
        .logo-name {{ font-weight: 600; font-size: 1.1rem; }}
        .dark-nav-links {{
            display: flex; gap: 4px; padding: 4px;
            background: rgba(255,255,255,0.05); border-radius: 50px;
        }}
        .dark-nav-link {{
            padding: 10px 20px; color: rgba(255,255,255,0.7);
            text-decoration: none; font-size: 0.9rem; font-weight: 500;
            border-radius: 50px; transition: all 0.3s;
        }}
        .dark-nav-link:hover {{ color: #fff; background: rgba(255,255,255,0.1); }}
        .dark-cta {{
            padding: 12px 24px; background: #fff; color: #0a0a0a;
            text-decoration: none; font-weight: 600; border-radius: 50px;
            transition: all 0.3s;
        }}
        .dark-cta:hover {{ background: {primary}; color: #fff; transform: scale(1.02); }}
        @media (max-width: 768px) {{
            .dark-nav-links {{ display: none; }}
            .dark-navbar {{ width: calc(100% - 32px); top: 12px; }}
        }}
        </style>
        '''
    
    @classmethod
    def _variant_luxury_minimal(cls, props: Dict[str, Any], colors: Dict[str, str]) -> str:
        """Luxury Minimal Navbar with serif fonts"""
        business_name = props.get("businessName", props.get("logo_text", "Brand"))
        nav_items = props.get("navItems", props.get("links", [
            {"text": "Home", "url": "#home"},
            {"text": "About", "url": "#about"},
            {"text": "Services", "url": "#services"},
            {"text": "Contact", "url": "#contact"}
        ]))
        primary = colors.get("primary", "#B8860B")
        
        nav_html = ""
        for i, item in enumerate(nav_items):
            text = item if isinstance(item, str) else item.get("text", "Link")
            url = f"#{item.lower()}" if isinstance(item, str) else item.get("url", "#")
            nav_html += f'<a href="{url}" class="lux-link"><span class="link-num">0{i+1}</span>{text}</a>'
        
        return f'''
        <nav id="lux-navbar" class="lux-navbar">
            <div class="lux-nav-inner">
                <a href="#" class="lux-logo">
                    <span class="logo-deco">✦</span>
                    <span class="logo-main">{business_name.upper()}</span>
                    <span class="logo-deco">✦</span>
                </a>
                <div class="lux-links">{nav_html}</div>
                <a href="#contact" class="lux-cta">
                    <span class="cta-line"></span>
                    <span>Reserve</span>
                    <span class="cta-line"></span>
                </a>
            </div>
        </nav>
        
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&display=swap');
        .lux-navbar {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 9999;
            padding: 24px 48px; transition: all 0.5s;
        }}
        .lux-navbar.scrolled {{
            padding: 16px 48px; background: rgba(255,252,247,0.98);
            backdrop-filter: blur(16px); box-shadow: 0 1px 0 rgba(0,0,0,0.05);
        }}
        .lux-nav-inner {{
            max-width: 1400px; margin: 0 auto;
            display: flex; justify-content: space-between; align-items: center;
        }}
        .lux-logo {{
            display: flex; align-items: center; gap: 16px;
            text-decoration: none; color: #fff;
        }}
        .lux-navbar.scrolled .lux-logo {{ color: #1a1a1a; }}
        .logo-deco {{ color: {primary}; font-size: 0.75rem; opacity: 0.8; }}
        .logo-main {{
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.8rem; font-weight: 600; letter-spacing: 0.15em;
        }}
        .lux-links {{ display: flex; gap: 48px; }}
        .lux-link {{
            display: flex; flex-direction: column; align-items: center; gap: 4px;
            text-decoration: none; color: rgba(255,255,255,0.85);
            font-family: 'Cormorant Garamond', serif;
            font-size: 1rem; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase;
            transition: color 0.3s; position: relative;
        }}
        .lux-navbar.scrolled .lux-link {{ color: #4a4a4a; }}
        .lux-link:hover {{ color: {primary}; }}
        .link-num {{ font-size: 0.65rem; opacity: 0.5; }}
        .lux-link::after {{
            content: ''; position: absolute; bottom: -8px; left: 50%;
            transform: translateX(-50%); width: 0; height: 1px;
            background: {primary}; transition: width 0.4s;
        }}
        .lux-link:hover::after {{ width: 100%; }}
        .lux-cta {{
            display: flex; align-items: center; gap: 16px;
            text-decoration: none; color: #fff;
            font-family: 'Cormorant Garamond', serif;
            font-size: 0.9rem; letter-spacing: 0.15em; text-transform: uppercase;
            transition: color 0.3s;
        }}
        .lux-navbar.scrolled .lux-cta {{ color: #1a1a1a; }}
        .cta-line {{ width: 40px; height: 1px; background: {primary}; transition: width 0.3s; }}
        .lux-cta:hover .cta-line {{ width: 24px; }}
        .lux-cta:hover {{ color: {primary}; }}
        @media (max-width: 1024px) {{
            .lux-links {{ display: none; }}
            .lux-navbar {{ padding: 16px 24px; }}
        }}
        </style>
        
        <script>
        window.addEventListener('scroll', () => {{
            const nav = document.getElementById('lux-navbar');
            if (window.scrollY > 80) nav.classList.add('scrolled');
            else nav.classList.remove('scrolled');
        }});
        </script>
        '''
    
    @classmethod
    def _variant_sticky_minimal(cls, props: Dict[str, Any], colors: Dict[str, str]) -> str:
        business_name = props.get("businessName", "Brand")
        nav_items = props.get("navItems", ["Home", "About", "Services", "Contact"])
        
        nav_html = ""
        for item in nav_items:
            if isinstance(item, str):
                nav_html += f'<a href="#{item.lower()}">{item}</a>'
            else:
                nav_html += f'<a href="{item.get("url", "#")}">{item.get("text", "Link")}</a>'
        
        return f'''
        <header class="shared-navbar shared-navbar-minimal">
            <div class="nav-container">
                <a href="#" class="nav-logo">{business_name}</a>
                <nav class="nav-menu">{nav_html}</nav>
                <a href="#contact" class="nav-cta">Get Started</a>
            </div>
        </header>
        
        <style>
        .shared-navbar-minimal {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
            background: {colors.get("background", "#fff")};
            box-shadow: 0 2px 20px rgba(0,0,0,0.08); padding: 0 24px;
        }}
        .nav-container {{
            max-width: 1200px; margin: 0 auto;
            display: flex; align-items: center; justify-content: space-between; height: 70px;
        }}
        .nav-logo {{ font-size: 1.5rem; font-weight: 700; color: {colors.get("text", "#1a1a1a")}; text-decoration: none; }}
        .nav-menu {{ display: flex; gap: 32px; }}
        .nav-menu a {{ color: {colors.get("text_muted", "#666")}; text-decoration: none; font-size: 0.95rem; font-weight: 500; transition: color 0.3s; }}
        .nav-menu a:hover {{ color: {colors.get("primary", "#2563EB")}; }}
        .nav-cta {{
            padding: 10px 24px; background: {colors.get("primary", "#2563EB")}; color: #fff;
            text-decoration: none; font-size: 0.9rem; font-weight: 600; border-radius: 6px; transition: all 0.3s;
        }}
        .nav-cta:hover {{ transform: translateY(-2px); box-shadow: 0 5px 15px {colors.get("primary", "#2563EB")}40; }}
        @media (max-width: 768px) {{ .nav-menu {{ display: none; }} }}
        </style>
        '''
    
    @classmethod
    def _variant_transparent_overlay(cls, props: Dict[str, Any], colors: Dict[str, str]) -> str:
        business_name = props.get("businessName", "Brand")
        
        return f'''
        <header class="shared-navbar shared-navbar-transparent">
            <div class="nav-container">
                <a href="#" class="nav-logo">{business_name}</a>
                <nav class="nav-menu">
                    <a href="#about">About</a>
                    <a href="#services">Services</a>
                    <a href="#contact">Contact</a>
                </nav>
            </div>
        </header>
        
        <style>
        .shared-navbar-transparent {{
            position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
            padding: 20px 24px; transition: background 0.3s;
        }}
        .nav-container {{
            max-width: 1200px; margin: 0 auto;
            display: flex; align-items: center; justify-content: space-between;
        }}
        .nav-logo {{ font-size: 1.5rem; font-weight: 700; color: #fff; text-decoration: none; }}
        .nav-menu {{ display: flex; gap: 32px; }}
        .nav-menu a {{ color: rgba(255,255,255,0.9); text-decoration: none; font-size: 0.95rem; transition: color 0.3s; }}
        .nav-menu a:hover {{ color: #fff; }}
        </style>
        '''


class SharedContactTemplates:
    """Universal contact form templates"""
    
    VARIANTS = ["split-form"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        title = props.get("title", "Get in Touch")
        email = props.get("email", "hello@example.com")
        phone = props.get("phone", "(555) 123-4567")
        
        return f'''
        <section class="shared-contact" id="contact">
            <div class="container">
                <div class="contact-grid">
                    <div class="contact-info">
                        <h2>{title}</h2>
                        <p>We'd love to hear from you. Send us a message and we'll respond as soon as possible.</p>
                        <div class="info-item">
                            <span class="icon">✉️</span>
                            <span>{email}</span>
                        </div>
                        <div class="info-item">
                            <span class="icon">📞</span>
                            <span>{phone}</span>
                        </div>
                    </div>
                    <form class="contact-form">
                        <input type="text" placeholder="Your Name" required>
                        <input type="email" placeholder="Your Email" required>
                        <textarea placeholder="Your Message" rows="5" required></textarea>
                        <button type="submit">Send Message</button>
                    </form>
                </div>
            </div>
        </section>
        
        <style>
        .shared-contact {{ padding: 100px 24px; background: {colors.get("background", "#f9f9f9")}; }}
        .shared-contact .container {{ max-width: 1000px; margin: 0 auto; }}
        .contact-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 60px; }}
        .contact-info h2 {{ font-size: 2rem; color: {colors.get("text", "#1a1a1a")}; margin-bottom: 16px; }}
        .contact-info p {{ color: {colors.get("text_muted", "#666")}; margin-bottom: 32px; line-height: 1.7; }}
        .info-item {{ display: flex; align-items: center; gap: 12px; margin-bottom: 16px; color: {colors.get("text", "#1a1a1a")}; }}
        .contact-form {{ display: flex; flex-direction: column; gap: 16px; }}
        .contact-form input, .contact-form textarea {{
            padding: 16px;
            border: 1px solid #ddd;
            font-size: 1rem;
            background: #fff;
        }}
        .contact-form button {{
            padding: 16px;
            background: {colors.get("primary", "#2563EB")};
            color: #fff;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s;
        }}
        .contact-form button:hover {{
            background: {colors.get("text", "#1a1a1a")};
        }}
        @media (max-width: 768px) {{
            .contact-grid {{ grid-template-columns: 1fr; }}
        }}
        </style>
        '''


class SharedCTATemplates:
    """Universal Call-to-Action templates"""
    
    VARIANTS = ["centered-cta"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        title = props.get("title", "Ready to Get Started?")
        subtitle = props.get("subtitle", "Join thousands of satisfied customers today")
        cta = props.get("cta", "Get Started Now")
        
        return f'''
        <section class="shared-cta">
            <div class="container">
                <h2>{title}</h2>
                <p>{subtitle}</p>
                <a href="#contact" class="btn-cta">{cta}</a>
            </div>
        </section>
        
        <style>
        .shared-cta {{ padding: 100px 24px; background: {colors.get("primary", "#2563EB")}; text-align: center; }}
        .shared-cta .container {{ max-width: 700px; margin: 0 auto; }}
        .shared-cta h2 {{ font-size: 2.5rem; color: #fff; margin-bottom: 16px; }}
        .shared-cta p {{ color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 32px; }}
        .shared-cta .btn-cta {{
            display: inline-block;
            padding: 18px 48px;
            background: #fff;
            color: {colors.get("primary", "#2563EB")};
            text-decoration: none;
            font-weight: 600;
            border-radius: 8px;
            transition: all 0.3s;
        }}
        .shared-cta .btn-cta:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        </style>
        '''


class SharedTestimonialsTemplates:
    """Universal testimonial templates"""
    
    VARIANTS = ["cards-grid"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        title = props.get("title", "What Our Clients Say")
        
        return f'''
        <section class="shared-testimonials" id="testimonials">
            <div class="container">
                <h2>{title}</h2>
                <div class="testimonials-grid">
                    <div class="testimonial-card">
                        <p class="quote">"Exceptional service and amazing results. Highly recommended!"</p>
                        <div class="author">
                            <span class="name">John Smith</span>
                            <span class="role">CEO, TechCorp</span>
                        </div>
                    </div>
                    <div class="testimonial-card">
                        <p class="quote">"They exceeded our expectations in every way possible."</p>
                        <div class="author">
                            <span class="name">Sarah Johnson</span>
                            <span class="role">Marketing Director</span>
                        </div>
                    </div>
                    <div class="testimonial-card">
                        <p class="quote">"Professional, creative, and incredibly easy to work with."</p>
                        <div class="author">
                            <span class="name">Mike Williams</span>
                            <span class="role">Founder, StartupXYZ</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <style>
        .shared-testimonials {{ padding: 100px 24px; background: {colors.get("background", "#fff")}; }}
        .shared-testimonials .container {{ max-width: 1200px; margin: 0 auto; }}
        .shared-testimonials h2 {{ font-size: 2rem; color: {colors.get("text", "#1a1a1a")}; text-align: center; margin-bottom: 60px; }}
        .testimonials-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }}
        .testimonial-card {{ background: {colors.get("background", "#f9f9f9")}; padding: 32px; border-radius: 12px; }}
        .quote {{ font-size: 1.1rem; color: {colors.get("text", "#1a1a1a")}; line-height: 1.7; margin-bottom: 24px; font-style: italic; }}
        .author {{ display: flex; flex-direction: column; }}
        .author .name {{ font-weight: 600; color: {colors.get("text", "#1a1a1a")}; }}
        .author .role {{ font-size: 0.9rem; color: {colors.get("text_muted", "#666")}; }}
        @media (max-width: 768px) {{ .testimonials-grid {{ grid-template-columns: 1fr; }} }}
        </style>
        '''


class SharedFAQTemplates:
    """Universal FAQ templates"""
    
    VARIANTS = ["accordion"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        title = props.get("sectionTitle", props.get("title", "Frequently Asked Questions"))
        faqs = props.get("faqs", [
            {"question": "How do I get started?", "answer": "Simply sign up and explore our services."},
            {"question": "What payment methods do you accept?", "answer": "We accept all major credit cards and PayPal."},
            {"question": "How can I contact support?", "answer": "Reach out via our contact form or email us directly."}
        ])
        
        faq_items = ""
        for i, faq in enumerate(faqs):
            faq_items += f'''
            <div class="faq-item">
                <button class="faq-question" onclick="this.parentElement.classList.toggle('active')">
                    <span>{faq.get("question", "Question?")}</span>
                    <span class="faq-icon">+</span>
                </button>
                <div class="faq-answer">
                    <p>{faq.get("answer", "Answer coming soon.")}</p>
                </div>
            </div>
            '''
        
        return f'''
        <section class="shared-faq" id="faq">
            <div class="container">
                <h2>{title}</h2>
                <div class="faq-list">
                    {faq_items}
                </div>
            </div>
        </section>
        
        <style>
        .shared-faq {{ padding: 100px 24px; background: {colors.get("background", "#fff")}; }}
        .shared-faq .container {{ max-width: 800px; margin: 0 auto; }}
        .shared-faq h2 {{ font-size: 2rem; color: {colors.get("text", "#1a1a1a")}; text-align: center; margin-bottom: 50px; }}
        .faq-list {{ display: flex; flex-direction: column; gap: 16px; }}
        .faq-item {{ 
            border: 1px solid {colors.get("text_muted", "#ddd")}20;
            border-radius: 12px;
            overflow: hidden;
            background: {colors.get("surface", "#f9f9f9")};
        }}
        .faq-question {{
            width: 100%;
            padding: 20px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: transparent;
            border: none;
            cursor: pointer;
            font-size: 1.1rem;
            font-weight: 500;
            color: {colors.get("text", "#1a1a1a")};
            text-align: left;
        }}
        .faq-icon {{
            font-size: 1.5rem;
            color: {colors.get("primary", "#2563EB")};
            transition: transform 0.3s;
        }}
        .faq-item.active .faq-icon {{ transform: rotate(45deg); }}
        .faq-answer {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
        }}
        .faq-item.active .faq-answer {{ max-height: 200px; }}
        .faq-answer p {{
            padding: 0 24px 20px;
            color: {colors.get("text_muted", "#666")};
            line-height: 1.7;
        }}
        </style>
        '''



# Import new modules
from .functional_components import FunctionalComponents
from .testimonials import TestimonialsTemplates as NewTestimonialsTemplates
from .contact_page import ContactPageTemplates
from .faq_page import FAQPageTemplates
from .gallery_page import GalleryPageTemplates


__all__ = [
    "SharedNavbarTemplates",
    "SharedContactTemplates", 
    "SharedCTATemplates",
    "SharedTestimonialsTemplates",
    "SharedFAQTemplates",
    # New Functional Components
    "FunctionalComponents",
    "NewTestimonialsTemplates",
    "ContactPageTemplates",
    "FAQPageTemplates",
    "GalleryPageTemplates"
]

