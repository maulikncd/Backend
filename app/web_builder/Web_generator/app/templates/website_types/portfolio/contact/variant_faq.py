from typing import Dict, Any

def render(props: Dict[str, Any], colors: Dict[str, str]) -> str:
    """FAQ Contact - Contact with FAQs"""
    primary = colors.get("primary")
    secondary = colors.get("secondary")
    background = colors.get("background")
    text = colors.get("text")
    
    faqs = [
        {"q": "What's your typical project timeline?", "a": "Most projects take 4-8 weeks depending on complexity."},
        {"q": "Do you work with international clients?", "a": "Yes! I work with clients worldwide and am flexible with time zones."},
        {"q": "What's your pricing model?", "a": "I offer both fixed-price projects and hourly consulting."},
    ]
    
    faqs_html = ""
    for f in faqs:
        faqs_html += f'''
        <div class="faq-item"><h4>{f['q']}</h4><p>{f['a']}</p></div>
        '''
    
    return f'''
    <section class="portfolio-contact-faq" id="contact">
        <div class="faq-container">
            <div class="faq-left">
                <span class="tag">FAQ</span>
                <h2>Common Questions</h2>
                <div class="faqs">{faqs_html}</div>
            </div>
            <div class="faq-right">
                <h3>Still have questions?</h3>
                <p>Drop me a message and I'll get back to you within 24 hours.</p>
                <a href="mailto:hello@example.com" class="contact-btn">Contact Me →</a>
            </div>
        </div>
    </section>
    
    <style>
    .portfolio-contact-faq {{ padding: 120px 24px; background: {background}; }}
    .faq-container {{ max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1.5fr 1fr; gap: 80px; align-items: start; }}
    .tag {{ display: inline-block; padding: 10px 24px; background: {primary}15; color: {primary}; font-weight: 600; border-radius: 100px; margin-bottom: 20px; }}
    .faq-left h2 {{ font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; color: {text}; margin-bottom: 40px; }}
    .faq-item {{ padding: 24px 0; border-bottom: 1px solid {text}10; }}
    .faq-item h4 {{ font-size: 1.1rem; font-weight: 700; color: {text}; margin-bottom: 8px; }}
    .faq-item p {{ color: {secondary}; line-height: 1.6; }}
    .faq-right {{ background: linear-gradient(135deg, {primary}15, {primary}05); border-radius: 24px; padding: 40px; }}
    .faq-right h3 {{ font-size: 1.5rem; font-weight: 800; color: {text}; margin-bottom: 12px; }}
    .faq-right p {{ color: {secondary}; margin-bottom: 28px; }}
    .contact-btn {{ display: inline-block; padding: 16px 36px; background: {primary}; color: {background}; text-decoration: none; font-weight: 700; border-radius: 12px; transition: all 0.3s ease; }}
    .contact-btn:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px {primary}40; }}
    @media (max-width: 900px) {{ .faq-container {{ grid-template-columns: 1fr; }} }}
    </style>
    '''
