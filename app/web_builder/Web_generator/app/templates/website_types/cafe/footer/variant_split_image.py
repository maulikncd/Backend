from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """Split Image Footer - Half image half content"""
    logo = props.get("logo", "Cafe")
    tagline = props.get("tagline", "")
    primary = colors.get("primary", "#8B7355")
    
    return f'''
    <footer class="footer-split-image"><div class="split-grid"><div class="footer-image" style="background-image: url('https://images.unsplash.com/photo-1445116572660-236099ec97a0?w=800')"></div><div class="footer-info"><h3>{logo}</h3><p>{tagline if tagline else "Your neighborhood coffee destination"}</p><div class="info-items"><div class="info-item"><strong>Visit Us</strong><span>123 Coffee Lane, NYC</span></div><div class="info-item"><strong>Hours</strong><span>7AM - 10PM Daily</span></div><div class="info-item"><strong>Contact</strong><span>hello@cafe.com</span></div></div><span class="copyright">© 2025 {logo}</span></div></div></footer>
    <style>
    .footer-split-image {{ background: #0D0D0D; }}
    .split-grid {{ display: grid; grid-template-columns: 1fr 1fr; min-height: 400px; }}
    .footer-image {{ background-size: cover; background-position: center; }}
    .footer-info {{ padding: 60px; color: #fff; display: flex; flex-direction: column; justify-content: center; }}
    .footer-info h3 {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 15px; }}
    .footer-info > p {{ color: rgba(255,255,255,0.7); margin-bottom: 40px; }}
    .info-items {{ display: flex; gap: 40px; margin-bottom: 40px; }}
    .info-item strong {{ display: block; color: {primary}; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 8px; }}
    .info-item span {{ color: rgba(255,255,255,0.8); }}
    .copyright {{ color: rgba(255,255,255,0.4); font-size: 0.85rem; }}
    @media (max-width: 768px) {{ .split-grid {{ grid-template-columns: 1fr; }} .footer-image {{ height: 250px; }} .info-items {{ flex-direction: column; gap: 20px; }} }}
    </style>
    '''
