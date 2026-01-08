from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Gradient CTA Footer"""
    logo = props.get("logo", "Cafe")
    primary = colors.get("primary", "#8B7355")
    
    return f'''
    <footer class="footer-gradient-cta"><div class="cta-section"><h2>Ready to Experience the Best Coffee?</h2><p>Visit us today or order online</p><div class="cta-buttons"><a href="#" class="btn-primary">Order Now</a><a href="#" class="btn-outline">Find Location</a></div></div><div class="footer-bottom"><div class="bottom-content"><h3>{logo}</h3><div class="bottom-links"><a href="#">About</a><a href="#">Menu</a><a href="#">Contact</a><a href="#">Careers</a></div><span>© 2025 {logo}</span></div></div></footer>
    <style>
    .footer-gradient-cta {{ }}
    .cta-section {{ background: linear-gradient(135deg, {primary}, #5C4A3D); padding: 100px 24px; text-align: center; color: #fff; }}
    .cta-section h2 {{ font-family: 'Playfair Display', serif; font-size: 3rem; margin-bottom: 15px; }}
    .cta-section p {{ font-size: 1.2rem; margin-bottom: 40px; opacity: 0.9; }}
    .cta-buttons {{ display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }}
    .btn-primary {{ padding: 16px 40px; background: #fff; color: {primary}; text-decoration: none; border-radius: 50px; font-weight: 600; transition: 0.3s; }}
    .btn-primary:hover {{ transform: translateY(-3px); box-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
    .btn-outline {{ padding: 16px 40px; background: transparent; border: 2px solid #fff; color: #fff; text-decoration: none; border-radius: 50px; font-weight: 600; transition: 0.3s; }}
    .btn-outline:hover {{ background: #fff; color: {primary}; }}
    .footer-bottom {{ background: #0D0D0D; padding: 40px 24px; }}
    .bottom-content {{ max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; }}
    .bottom-content h3 {{ font-family: 'Playfair Display', serif; color: #fff; }}
    .bottom-links {{ display: flex; gap: 30px; }}
    .bottom-links a {{ color: #888; text-decoration: none; transition: 0.3s; }}
    .bottom-links a:hover {{ color: #fff; }}
    .bottom-content span {{ color: #666; font-size: 0.9rem; }}
    </style>
    '''
