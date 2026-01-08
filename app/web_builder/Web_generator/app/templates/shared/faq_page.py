"""
FAQ Page Templates - Fully Functional Accordion
"""

from typing import Dict, Any, List


class FAQPageTemplates:
    """FAQ page templates with working accordion"""
    
    VARIANTS = ["modern_accordion", "two_column", "categorized", "search_enabled"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        variant = variant or "modern_accordion"
        faqs = props.get("faqs", cls._get_default_faqs(props.get("businessType", "business")))
        
        if variant == "modern_accordion":
            return cls._render_modern_accordion(faqs, colors, props)
        elif variant == "two_column":
            return cls._render_two_column(faqs, colors, props)
        elif variant == "categorized":
            return cls._render_categorized(faqs, colors, props)
        elif variant == "search_enabled":
            return cls._render_search_enabled(faqs, colors, props)
        return cls._render_modern_accordion(faqs, colors, props)
    
    @staticmethod
    def _get_default_faqs(business_type: str) -> List[Dict]:
        """Generate relevant FAQs based on business type"""
        common = [
            {"q": "What are your business hours?", "a": "We're open Monday to Friday from 9 AM to 6 PM, and Saturday from 10 AM to 4 PM. We're closed on Sundays."},
            {"q": "How can I contact you?", "a": "You can reach us via email, phone, or by filling out our contact form. We typically respond within 24 hours."},
            {"q": "Do you offer refunds?", "a": "Yes, we offer a 30-day satisfaction guarantee. If you're not happy with our service, contact us for a full refund."}
        ]
        
        type_specific = {
            "cafe": [
                {"q": "Do you have vegan/vegetarian options?", "a": "Yes! We offer a variety of plant-based options including oat milk, almond milk, and vegan pastries."},
                {"q": "Do you offer WiFi?", "a": "Yes, complimentary high-speed WiFi is available for all our customers."},
                {"q": "Can I bring my laptop to work?", "a": "Absolutely! We have comfortable seating with power outlets perfect for working."}
            ],
            "restaurant": [
                {"q": "Do you take reservations?", "a": "Yes, we accept reservations online or by phone. For parties of 6 or more, advance booking is recommended."},
                {"q": "Do you cater for dietary restrictions?", "a": "We accommodate most dietary requirements including vegetarian, vegan, gluten-free, and allergies. Please inform your server."},
                {"q": "Is parking available?", "a": "Free parking is available in our lot behind the restaurant."}
            ],
            "gaming": [
                {"q": "What platforms do you support?", "a": "We support PC, PlayStation, Xbox, and Nintendo Switch platforms."},
                {"q": "Is online multiplayer included?", "a": "Yes, online multiplayer is included with your purchase. No subscription required."},
                {"q": "How do I report bugs?", "a": "You can report bugs through our support portal or Discord community."}
            ],
            "ecommerce": [
                {"q": "What payment methods do you accept?", "a": "We accept all major credit cards, PayPal, and bank transfers."},
                {"q": "How long does shipping take?", "a": "Standard shipping takes 5-7 business days. Express shipping (2-3 days) is also available."},
                {"q": "What is your return policy?", "a": "You can return unused items within 30 days for a full refund. See our returns page for details."}
            ]
        }
        
        return type_specific.get(business_type.lower(), common) + common
    
    @classmethod
    def _render_modern_accordion(cls, faqs: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        text = colors.get("text", "#1f2937")
        title = props.get("title", "Frequently Asked Questions")
        subtitle = props.get("subtitle", "Find answers to common questions")
        
        items = ""
        for i, faq in enumerate(faqs):
            items += f'''
            <div class="faq-item" data-faq="{i}">
                <button class="faq-question" onclick="toggleFAQ({i})" aria-expanded="false">
                    <span>{faq.get("q", faq.get("question", ""))}</span>
                    <svg class="faq-icon" viewBox="0 0 24 24" width="24" height="24">
                        <path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                </button>
                <div class="faq-answer" id="faq-answer-{i}">
                    <p>{faq.get("a", faq.get("answer", ""))}</p>
                </div>
            </div>
            '''
        
        return f'''
        <section class="faq-section" id="faq">
            <div class="container">
                <div class="faq-header">
                    <h2>{title}</h2>
                    <p>{subtitle}</p>
                </div>
                <div class="faq-list">{items}</div>
                <div class="faq-cta">
                    <p>Still have questions?</p>
                    <a href="#contact" class="cta-link">Contact our support team →</a>
                </div>
            </div>
        </section>
        
        <style>
        .faq-section {{
            padding: 100px 0;
            background: linear-gradient(180deg, white 0%, #f9fafb 100%);
        }}
        .faq-section .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 0 24px;
        }}
        .faq-header {{
            text-align: center;
            margin-bottom: 60px;
        }}
        .faq-header h2 {{
            font-size: 2.5rem;
            color: {text};
            margin-bottom: 12px;
        }}
        .faq-header p {{ color: #6b7280; font-size: 1.1rem; }}
        .faq-list {{ display: flex; flex-direction: column; gap: 16px; }}
        .faq-item {{
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 16px;
            overflow: hidden;
            transition: all 0.3s;
        }}
        .faq-item:hover {{ border-color: {primary}40; }}
        .faq-item.active {{
            border-color: {primary};
            box-shadow: 0 8px 30px {primary}15;
        }}
        .faq-question {{
            width: 100%;
            padding: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            background: none;
            border: none;
            cursor: pointer;
            text-align: left;
            font-size: 1.1rem;
            font-weight: 600;
            color: {text};
            transition: color 0.3s;
        }}
        .faq-question:hover {{ color: {primary}; }}
        .faq-icon {{
            flex-shrink: 0;
            color: {primary};
            transition: transform 0.3s;
        }}
        .faq-item.active .faq-icon {{ transform: rotate(45deg); }}
        .faq-answer {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease, padding 0.3s ease;
        }}
        .faq-answer p {{
            padding: 0 24px 24px;
            color: #6b7280;
            line-height: 1.8;
            margin: 0;
        }}
        .faq-item.active .faq-answer {{ max-height: 500px; }}
        .faq-cta {{
            text-align: center;
            margin-top: 60px;
            padding: 40px;
            background: {primary}08;
            border-radius: 20px;
        }}
        .faq-cta p {{ color: #6b7280; margin-bottom: 12px; }}
        .cta-link {{
            color: {primary};
            font-weight: 600;
            text-decoration: none;
            font-size: 1.1rem;
        }}
        .cta-link:hover {{ text-decoration: underline; }}
        </style>
        
        <script>
        function toggleFAQ(index) {{
            const item = document.querySelector(`[data-faq="${{index}}"]`);
            const wasActive = item.classList.contains('active');
            const btn = item.querySelector('.faq-question');
            
            // Close all
            document.querySelectorAll('.faq-item').forEach(el => {{
                el.classList.remove('active');
                el.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
            }});
            
            // Open clicked if wasn't active
            if (!wasActive) {{
                item.classList.add('active');
                btn.setAttribute('aria-expanded', 'true');
            }}
        }}
        
        // Keyboard navigation
        document.querySelectorAll('.faq-question').forEach((btn, i) => {{
            btn.addEventListener('keydown', (e) => {{
                if (e.key === 'Enter' || e.key === ' ') {{
                    e.preventDefault();
                    toggleFAQ(i);
                }}
            }});
        }});
        </script>
        '''
    
    @classmethod
    def _render_two_column(cls, faqs: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        text = colors.get("text", "#1f2937")
        
        mid = len(faqs) // 2
        left_faqs = faqs[:mid]
        right_faqs = faqs[mid:]
        
        def render_items(items, offset=0):
            html = ""
            for i, faq in enumerate(items):
                idx = i + offset
                html += f'''
                <div class="faq-card">
                    <h4>{faq.get("q", faq.get("question", ""))}</h4>
                    <p>{faq.get("a", faq.get("answer", ""))}</p>
                </div>
                '''
            return html
        
        return f'''
        <section class="faq-two-col" id="faq">
            <div class="container">
                <h2>FAQ</h2>
                <div class="faq-columns">
                    <div class="faq-column">{render_items(left_faqs)}</div>
                    <div class="faq-column">{render_items(right_faqs, mid)}</div>
                </div>
            </div>
        </section>
        
        <style>
        .faq-two-col {{ padding: 80px 24px; }}
        .faq-two-col .container {{ max-width: 1200px; margin: 0 auto; }}
        .faq-two-col h2 {{ text-align: center; font-size: 2.5rem; color: {text}; margin-bottom: 50px; }}
        .faq-columns {{ display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }}
        .faq-card {{
            background: #f9fafb;
            padding: 30px;
            border-radius: 16px;
            margin-bottom: 20px;
        }}
        .faq-card h4 {{ color: {text}; margin: 0 0 12px; font-size: 1.1rem; }}
        .faq-card p {{ color: #6b7280; margin: 0; line-height: 1.7; }}
        @media (max-width: 768px) {{ .faq-columns {{ grid-template-columns: 1fr; }} }}
        </style>
        '''
    
    @classmethod
    def _render_categorized(cls, faqs: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        text = colors.get("text", "#1f2937")
        categories = props.get("faqCategories", {
            "General": faqs[:3] if len(faqs) >= 3 else faqs,
            "Services": faqs[3:6] if len(faqs) >= 6 else [],
            "Support": faqs[6:] if len(faqs) > 6 else []
        })
        
        tabs = ""
        contents = ""
        for i, (cat, items) in enumerate(categories.items()):
            if not items:
                continue
            active = "active" if i == 0 else ""
            tabs += f'<button class="cat-tab {active}" onclick="switchFAQCategory({i})" data-cat="{i}">{cat}</button>'
            
            faq_html = ""
            for j, faq in enumerate(items):
                faq_html += f'''
                <div class="cat-faq-item">
                    <h4>{faq.get("q", faq.get("question", ""))}</h4>
                    <p>{faq.get("a", faq.get("answer", ""))}</p>
                </div>
                '''
            contents += f'<div class="cat-content {active}" id="cat-content-{i}">{faq_html}</div>'
        
        return f'''
        <section class="faq-categorized" id="faq">
            <div class="container">
                <h2>Help Center</h2>
                <div class="cat-tabs">{tabs}</div>
                <div class="cat-contents">{contents}</div>
            </div>
        </section>
        
        <style>
        .faq-categorized {{ padding: 80px 24px; }}
        .faq-categorized .container {{ max-width: 900px; margin: 0 auto; }}
        .faq-categorized h2 {{ text-align: center; color: {text}; margin-bottom: 40px; }}
        .cat-tabs {{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }}
        .cat-tab {{
            padding: 12px 28px;
            background: #f3f4f6;
            border: none;
            border-radius: 50px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
            color: {text};
        }}
        .cat-tab:hover {{ background: #e5e7eb; }}
        .cat-tab.active {{
            background: {primary};
            color: white;
        }}
        .cat-content {{ display: none; }}
        .cat-content.active {{ display: block; animation: fadeIn 0.3s; }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        .cat-faq-item {{
            padding: 24px;
            background: #f9fafb;
            border-radius: 12px;
            margin-bottom: 16px;
        }}
        .cat-faq-item h4 {{ color: {text}; margin: 0 0 8px; }}
        .cat-faq-item p {{ color: #6b7280; margin: 0; line-height: 1.7; }}
        </style>
        
        <script>
        function switchFAQCategory(index) {{
            document.querySelectorAll('.cat-tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.cat-content').forEach(c => c.classList.remove('active'));
            document.querySelector(`[data-cat="${{index}}"]`).classList.add('active');
            document.getElementById(`cat-content-${{index}}`).classList.add('active');
        }}
        </script>
        '''
    
    @classmethod
    def _render_search_enabled(cls, faqs: List[Dict], colors: Dict[str, str], props: Dict) -> str:
        primary = colors.get("primary", "#6366f1")
        text = colors.get("text", "#1f2937")
        
        items = ""
        for i, faq in enumerate(faqs):
            q = faq.get("q", faq.get("question", ""))
            a = faq.get("a", faq.get("answer", ""))
            items += f'''
            <div class="search-faq-item" data-search="{q.lower()} {a.lower()}">
                <h4>{q}</h4>
                <p>{a}</p>
            </div>
            '''
        
        return f'''
        <section class="faq-searchable" id="faq">
            <div class="container">
                <h2>How can we help?</h2>
                <div class="search-box">
                    <input type="text" id="faqSearch" placeholder="Search questions..." oninput="filterFAQs(this.value)" />
                    <svg viewBox="0 0 24 24" width="20" height="20"><circle cx="11" cy="11" r="8" stroke="currentColor" stroke-width="2" fill="none"/><path d="M21 21l-4.35-4.35" stroke="currentColor" stroke-width="2"/></svg>
                </div>
                <div class="search-faq-list" id="faqList">{items}</div>
                <p class="no-results" id="noResults" style="display:none;">No matching questions found.</p>
            </div>
        </section>
        
        <style>
        .faq-searchable {{ padding: 80px 24px; }}
        .faq-searchable .container {{ max-width: 800px; margin: 0 auto; }}
        .faq-searchable h2 {{ text-align: center; color: {text}; margin-bottom: 30px; }}
        .search-box {{
            position: relative;
            margin-bottom: 40px;
        }}
        .search-box input {{
            width: 100%;
            padding: 20px 20px 20px 50px;
            border: 2px solid #e5e7eb;
            border-radius: 16px;
            font-size: 1.1rem;
        }}
        .search-box input:focus {{
            outline: none;
            border-color: {primary};
        }}
        .search-box svg {{
            position: absolute;
            left: 18px;
            top: 50%;
            transform: translateY(-50%);
            color: #9ca3af;
        }}
        .search-faq-item {{
            padding: 24px;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            margin-bottom: 16px;
            transition: all 0.3s;
        }}
        .search-faq-item:hover {{
            border-color: {primary}40;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }}
        .search-faq-item.hidden {{ display: none; }}
        .search-faq-item h4 {{ color: {text}; margin: 0 0 8px; }}
        .search-faq-item p {{ color: #6b7280; margin: 0; line-height: 1.7; }}
        .no-results {{ text-align: center; color: #6b7280; padding: 40px; }}
        </style>
        
        <script>
        function filterFAQs(query) {{
            const q = query.toLowerCase().trim();
            const items = document.querySelectorAll('.search-faq-item');
            let hasResults = false;
            
            items.forEach(item => {{
                const searchText = item.dataset.search;
                if (q === '' || searchText.includes(q)) {{
                    item.classList.remove('hidden');
                    hasResults = true;
                }} else {{
                    item.classList.add('hidden');
                }}
            }});
            
            document.getElementById('noResults').style.display = hasResults ? 'none' : 'block';
        }}
        </script>
        '''
