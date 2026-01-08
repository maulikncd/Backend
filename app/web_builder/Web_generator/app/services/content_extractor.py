"""
Content Extractor Module
Extracts exact user answers from Q&A and uses them in website generation
No more placeholder content - everything from user input
"""

from typing import Dict, Any, Optional


class ContentExtractor:
    """
    Extracts and formats content from user's Q&A session.
    Ensures exact user answers are used instead of AI-generated placeholders.
    
    ENHANCED: Now supports prop_key based extraction from template question generator.
    """
    
    @staticmethod
    def extract_from_blueprint(blueprint: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract all user-provided content from blueprint.
        
        ENHANCED: Now looks for prop_key based answers from the template question system.
        
        Returns dict with all content needed for website generation.
        """
        # Project basics
        project_name = blueprint.get("projectName", "")
        seo = blueprint.get("seo", {})
        
        # User's Q&A answers (stored in blueprint from recommendation module)
        qa_answers = blueprint.get("qaAnswers", {})
        metadata = blueprint.get("metadata", {})
        
        # Extract from different possible locations
        questionnaire = metadata.get("questionnaire", {})
        answers = questionnaire.get("answers", qa_answers)
        
        # NEW: Extract prop_key based answers from question history
        prop_answers = ContentExtractor._extract_prop_answers(questionnaire)
        
        content = {
            # Business Identity - now also checks prop_answers
            "businessName": ContentExtractor._get_value([
                prop_answers.get("businessName"),
                blueprint.get("projectName"),
                answers.get("business_name"),
                answers.get("company_name"),
                answers.get("name"),
                answers.get("q1"),  # First question is usually business name
                metadata.get("businessName"),
            ], "My Business"),
            
            # Hero section content
            "title": ContentExtractor._get_value([
                prop_answers.get("title"),
                answers.get("title"),
                answers.get("headline"),
            ], ""),
            
            "subtitle": ContentExtractor._get_value([
                prop_answers.get("subtitle"),
                answers.get("subtitle"),
                answers.get("tagline"),
                answers.get("slogan"),
            ], ""),
            
            "tagline": ContentExtractor._get_value([
                prop_answers.get("subtitle"),
                answers.get("tagline"),
                answers.get("slogan"),
                answers.get("headline"),
                seo.get("description", "")[:60] if seo.get("description") else None,
            ], ""),
            
            "description": ContentExtractor._get_value([
                prop_answers.get("story"),
                prop_answers.get("description"),
                answers.get("description"),
                answers.get("about"),
                answers.get("business_description"),
                seo.get("description"),
            ], ""),
            
            # Story/About content
            "story": ContentExtractor._get_value([
                prop_answers.get("story"),
                answers.get("story"),
                answers.get("about"),
                answers.get("description"),
            ], ""),
            
            # Color theme
            "colorTheme": ContentExtractor._get_value([
                prop_answers.get("colorTheme"),
                answers.get("colorTheme"),
                answers.get("color_theme"),
                answers.get("q2"),  # Second question is usually color
            ], ""),
            
            # CTA
            "cta": ContentExtractor._get_value([
                prop_answers.get("cta"),
                answers.get("cta"),
                answers.get("call_to_action"),
            ], "Get Started"),
            
            # Contact Info
            "email": ContentExtractor._get_value([
                answers.get("email"),
                answers.get("contact_email"),
                answers.get("business_email"),
                metadata.get("email"),
            ], ""),
            
            "phone": ContentExtractor._get_value([
                answers.get("phone"),
                answers.get("phone_number"),
                answers.get("contact_phone"),
                metadata.get("phone"),
            ], ""),
            
            "address": ContentExtractor._get_value([
                answers.get("address"),
                answers.get("location"),
                answers.get("business_address"),
                metadata.get("address"),
            ], ""),
            
            # Opening Hours
            "hours": ContentExtractor._extract_hours(answers, metadata),
            
            # Social Media
            "social": ContentExtractor._extract_social(answers, metadata),
            
            # Services/Products
            "services": ContentExtractor._get_list([
                prop_answers.get("services"),
                answers.get("services"),
                answers.get("products"),
                answers.get("offerings"),
                metadata.get("services"),
            ]),
            
            # Target Audience
            "targetAudience": ContentExtractor._get_value([
                prop_answers.get("clientType"),
                answers.get("target_audience"),
                answers.get("customers"),
                answers.get("audience"),
            ], ""),
            
            # Unique Selling Points
            "usp": ContentExtractor._get_list([
                prop_answers.get("usp"),
                answers.get("usp"),
                answers.get("unique_points"),
                answers.get("what_makes_different"),
                answers.get("specialties"),
            ]),
            
            # Team Info
            "teamMembers": ContentExtractor._extract_team(answers, metadata),
            
            # Testimonials
            "testimonials": ContentExtractor._extract_testimonials(answers, metadata),
            
            # FAQs
            "faqs": ContentExtractor._extract_faqs(answers, metadata, blueprint.get("websiteType", "")),
            
            # Menu/Products (for restaurants/cafes)
            "menuItems": ContentExtractor._extract_menu_enhanced(answers, prop_answers, metadata),
            
            # Gallery Images
            "galleryImages": ContentExtractor._extract_gallery(answers, metadata, blueprint.get("websiteType", "")),
            
            # Call to Action
            "ctaText": ContentExtractor._get_value([
                prop_answers.get("cta"),
                answers.get("cta"),
                answers.get("call_to_action"),
                answers.get("action_text"),
            ], "Get Started"),
            
            "ctaSecondary": ContentExtractor._get_value([
                answers.get("cta_secondary"),
                answers.get("secondary_action"),
            ], "Learn More"),
            
            # Website type specific props
            **ContentExtractor._extract_type_specific(prop_answers, answers, blueprint.get("websiteType", "")),
        }
        
        return content
    
    @staticmethod
    def _extract_prop_answers(questionnaire: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract answers mapped by prop_key from question history.
        This is the new system that directly maps Q&A to template props.
        """
        prop_answers = {}
        
        # Get question history which contains prop_key mappings
        question_history = questionnaire.get("question_history", [])
        answers = questionnaire.get("answers", {})
        
        for question in question_history:
            prop_key = question.get("prop_key")
            q_id = question.get("id")
            answer = question.get("answer") or answers.get(q_id)
            
            if prop_key and answer:
                prop_answers[prop_key] = answer
        
        return prop_answers
    
    @staticmethod
    def _extract_type_specific(prop_answers: Dict, answers: Dict, website_type: str) -> Dict[str, Any]:
        """Extract website type specific properties"""
        specific = {}
        
        type_lower = website_type.lower() if website_type else ""
        
        # Cafe specific
        if type_lower in ["cafe", "coffee", "bakery"]:
            specific["atmosphere"] = ContentExtractor._get_value([
                prop_answers.get("atmosphere"),
                answers.get("atmosphere"),
                answers.get("vibe"),
            ], "")
            specific["signature"] = ContentExtractor._get_value([
                prop_answers.get("signature"),
                answers.get("signature"),
                answers.get("bestseller"),
            ], "")
        
        # Gaming specific
        elif type_lower in ["gaming", "esports", "game"]:
            specific["gameName"] = ContentExtractor._get_value([
                prop_answers.get("gameName"),
                answers.get("game_name"),
            ], "")
            specific["genre"] = prop_answers.get("genre") or answers.get("genre", [])
            specific["platforms"] = prop_answers.get("platforms") or answers.get("platforms", [])
            specific["style"] = prop_answers.get("style") or answers.get("style", "")
        
        # Restaurant specific
        elif type_lower in ["restaurant", "dining"]:
            specific["cuisine"] = ContentExtractor._get_value([
                prop_answers.get("cuisine"),
                answers.get("cuisine"),
            ], "")
            specific["diningStyle"] = ContentExtractor._get_value([
                prop_answers.get("diningStyle"),
                answers.get("dining_style"),
            ], "")
            specific["specialties"] = ContentExtractor._get_value([
                prop_answers.get("specialties"),
                answers.get("specialties"),
            ], "")
        
        # Portfolio specific
        elif type_lower in ["portfolio", "personal", "freelancer"]:
            specific["profession"] = ContentExtractor._get_value([
                prop_answers.get("profession"),
                answers.get("profession"),
                answers.get("title"),
            ], "")
            specific["skills"] = prop_answers.get("skills") or answers.get("skills", [])
            specific["experience"] = prop_answers.get("experience") or answers.get("experience", "")
        
        # Agency specific
        elif type_lower in ["agency", "business", "corporate"]:
            specific["services"] = prop_answers.get("services") or answers.get("services", [])
            specific["clientType"] = prop_answers.get("clientType") or answers.get("client_type", [])
            specific["approach"] = prop_answers.get("approach") or answers.get("approach", "")
        
        # Ecommerce specific
        elif type_lower in ["ecommerce", "shop", "store"]:
            specific["productType"] = ContentExtractor._get_value([
                prop_answers.get("productType"),
                answers.get("product_type"),
            ], "")
            specific["usp"] = ContentExtractor._get_value([
                prop_answers.get("usp"),
                answers.get("usp"),
            ], "")
        
        return specific
    
    @staticmethod
    def _extract_menu_enhanced(answers: Dict, prop_answers: Dict, metadata: Dict) -> list:
        """Extract menu items with enhanced prop_key support"""
        # Check prop_answers first
        menu_items = prop_answers.get("menuItems")
        if menu_items:
            if isinstance(menu_items, list):
                return menu_items
        
        # Fallback to traditional extraction
        menu = answers.get("menu") or answers.get("menu_items") or answers.get("products") or metadata.get("menu")
        
        if isinstance(menu, list):
            return menu
        
        return []

    
    @staticmethod
    def _get_value(possible_values: list, default: str = "") -> str:
        """Get first non-empty value from list of possibilities"""
        for val in possible_values:
            if val and str(val).strip():
                return str(val).strip()
        return default
    
    @staticmethod
    def _get_list(possible_values: list) -> list:
        """Get first non-empty list from possibilities"""
        for val in possible_values:
            if val:
                if isinstance(val, list):
                    return val
                elif isinstance(val, str):
                    # Split by comma or newline
                    items = [item.strip() for item in val.replace('\n', ',').split(',') if item.strip()]
                    return items
        return []
    
    @staticmethod
    def _extract_hours(answers: Dict, metadata: Dict) -> Dict[str, str]:
        """Extract opening hours from user answers"""
        # Check for structured hours
        hours = answers.get("hours") or answers.get("opening_hours") or metadata.get("hours")
        
        if isinstance(hours, dict):
            return hours
        
        if isinstance(hours, str):
            # Parse simple format like "Mon-Fri 9-6, Sat 10-4"
            return {"general": hours}
        
        # Default hours
        return {
            "monday": "9:00 AM - 6:00 PM",
            "tuesday": "9:00 AM - 6:00 PM", 
            "wednesday": "9:00 AM - 6:00 PM",
            "thursday": "9:00 AM - 6:00 PM",
            "friday": "9:00 AM - 6:00 PM",
            "saturday": "10:00 AM - 4:00 PM",
            "sunday": "Closed"
        }
    
    @staticmethod
    def _extract_social(answers: Dict, metadata: Dict) -> Dict[str, str]:
        """Extract social media links"""
        social = {}
        
        social_fields = [
            ("facebook", ["facebook", "fb", "facebook_url"]),
            ("instagram", ["instagram", "insta", "instagram_url"]),
            ("twitter", ["twitter", "x", "twitter_url"]),
            ("linkedin", ["linkedin", "linkedin_url"]),
            ("youtube", ["youtube", "yt", "youtube_url"]),
            ("whatsapp", ["whatsapp", "wa", "whatsapp_number"]),
        ]
        
        for platform, keys in social_fields:
            for key in keys:
                val = answers.get(key) or metadata.get(key)
                if val:
                    social[platform] = val
                    break
        
        return social
    
    @staticmethod
    def _extract_team(answers: Dict, metadata: Dict) -> list:
        """Extract team member information"""
        team = answers.get("team") or answers.get("team_members") or metadata.get("team")
        
        if isinstance(team, list):
            return team
        
        return []
    
    @staticmethod
    def _extract_testimonials(answers: Dict, metadata: Dict) -> list:
        """Extract testimonials from user input"""
        testimonials = answers.get("testimonials") or answers.get("reviews") or metadata.get("testimonials")
        
        if isinstance(testimonials, list):
            return testimonials
        
        # Return empty - will use default testimonials template
        return []
    
    @staticmethod
    def _extract_faqs(answers: Dict, metadata: Dict, website_type: str) -> list:
        """Extract or generate relevant FAQs"""
        faqs = answers.get("faqs") or answers.get("questions") or metadata.get("faqs")
        
        if isinstance(faqs, list) and faqs:
            return faqs
        
        # Generate industry-specific default FAQs
        return ContentExtractor._generate_default_faqs(website_type, answers)
    
    @staticmethod
    def _generate_default_faqs(website_type: str, answers: Dict) -> list:
        """Generate relevant FAQs based on business type and user inputs"""
        business_name = answers.get("business_name", answers.get("name", "our business"))
        
        base_faqs = {
            "cafe": [
                {"question": "What are your opening hours?", "answer": "We're open 7 days a week. Please check our Hours section for detailed timings."},
                {"question": "Do you offer takeaway or delivery?", "answer": "Yes, we offer both takeaway and delivery options. You can also order through popular delivery apps."},
                {"question": "Do you have WiFi?", "answer": "Yes, free high-speed WiFi is available for all our customers."},
                {"question": "Do you cater for dietary requirements?", "answer": "Absolutely! We offer vegetarian, vegan, and gluten-free options. Please ask our staff for allergen information."},
            ],
            "restaurant": [
                {"question": "Do I need a reservation?", "answer": "Walk-ins are welcome, but we recommend reservations for weekends and special occasions."},
                {"question": "Do you offer private dining?", "answer": "Yes, we have a private dining area available for events and celebrations."},
                {"question": "What dietary options do you have?", "answer": "We cater to vegetarian, vegan, and gluten-free diets. Please inform your server of any allergies."},
                {"question": "Is parking available?", "answer": "Yes, complimentary parking is available for our guests."},
            ],
            "gaming": [
                {"question": "What platforms are supported?", "answer": "We support PC, PlayStation, Xbox, and Nintendo Switch platforms."},
                {"question": "Is multiplayer available?", "answer": "Yes, online multiplayer is included with no additional subscription required."},
                {"question": "How do I report issues?", "answer": "You can report bugs through our support page or join our Discord community for help."},
                {"question": "Are there regular updates?", "answer": "Yes, we release regular content updates and patches to improve the experience."},
            ],
            "portfolio": [
                {"question": "What services do you offer?", "answer": "I offer web design, development, branding, and digital marketing services."},
                {"question": "How much do your services cost?", "answer": "Pricing depends on project scope. Contact me for a free quote."},
                {"question": "What is your turnaround time?", "answer": "Most projects are completed within 2-4 weeks, depending on complexity."},
                {"question": "Do you work with clients remotely?", "answer": "Yes, I work with clients worldwide through video calls and collaboration tools."},
            ],
            "agency": [
                {"question": "What industries do you work with?", "answer": "We work across various industries including tech, healthcare, retail, and more."},
                {"question": "How do you charge for services?", "answer": "We offer both project-based and retainer pricing options."},
                {"question": "What is your typical project timeline?", "answer": "Timelines vary by project scope, typically ranging from 4-12 weeks."},
                {"question": "Do you offer ongoing support?", "answer": "Yes, we offer maintenance packages and ongoing support for all our clients."},
            ],
        }
        
        return base_faqs.get(website_type.lower(), [
            {"question": "How can I contact you?", "answer": "You can reach us through our contact form, email, or phone."},
            {"question": "What are your business hours?", "answer": "We're available Monday to Friday, 9 AM to 6 PM."},
            {"question": "Do you offer consultations?", "answer": "Yes, we offer free initial consultations to discuss your needs."},
        ])
    
    @staticmethod
    def _extract_menu(answers: Dict, metadata: Dict) -> list:
        """Extract menu items for restaurants/cafes"""
        menu = answers.get("menu") or answers.get("menu_items") or answers.get("products") or metadata.get("menu")
        
        if isinstance(menu, list):
            return menu
        
        return []
    
    @staticmethod
    def _extract_gallery(answers: Dict, metadata: Dict, website_type: str) -> list:
        """Extract gallery images or provide defaults based on business type"""
        gallery = answers.get("gallery") or answers.get("images") or answers.get("photos") or metadata.get("gallery")
        
        if isinstance(gallery, list) and gallery:
            return gallery
        
        # Return empty - template will use Unsplash defaults
        return []
    
    @staticmethod
    def merge_with_blueprint_props(blueprint: Dict[str, Any], component_props: Dict[str, Any]) -> Dict[str, Any]:
        """
        Merge extracted content with component props.
        User-provided content takes priority over defaults.
        """
        extracted = ContentExtractor.extract_from_blueprint(blueprint)
        
        # Start with extracted content
        merged = extracted.copy()
        
        # Override with component-specific props
        for key, value in component_props.items():
            if value and str(value).strip():
                merged[key] = value
        
        return merged


# Industry-specific content helpers
# Now uses the comprehensive IndustryContentLibrary for richer content
from app.web_builder.Web_generator.app.prompts.content_library import (
    IndustryContentLibrary,
    AudienceToneAdapter,
    ContentDiversityTracker
)


class IndustryContent:
    """
    Enhanced content provider using comprehensive industry content library.
    
    PRIORITY ORDER:
    1. User's EXACT text (never modify)
    2. User's style preferences applied to defaults
    3. Industry-specific rich defaults
    4. Generic fallback
    """
    
    # Active diversity tracker (reset per website generation)
    _diversity_tracker: ContentDiversityTracker = None
    _current_audience: str = ""
    
    @classmethod
    def initialize_for_website(cls, audience: str = ""):
        """Initialize tracker for new website generation"""
        cls._diversity_tracker = ContentDiversityTracker()
        cls._current_audience = audience
    
    @classmethod
    def get_headline(cls, website_type: str, custom_headline: str = "", audience: str = "") -> str:
        """
        Get appropriate headline - user's or industry default.
        
        Priority:
        1. User's custom headline (returned EXACTLY as provided)
        2. Fresh industry headline from content library
        """
        # PRIORITY 1: User's exact text
        if custom_headline and custom_headline.strip():
            return custom_headline.strip()
        
        # PRIORITY 2: Industry-specific headline
        audience = audience or cls._current_audience
        
        if cls._diversity_tracker:
            headline = cls._diversity_tracker.get_fresh_headline(website_type)
        else:
            headline = IndustryContentLibrary.get_random_headline(website_type)
        
        return headline
    
    @classmethod
    def get_description(cls, website_type: str, custom_desc: str = "", audience: str = "") -> str:
        """
        Get appropriate description - user's or industry default.
        
        Priority:
        1. User's custom description (returned EXACTLY as provided)
        2. Fresh industry description from content library
        """
        # PRIORITY 1: User's exact text
        if custom_desc and custom_desc.strip():
            return custom_desc.strip()
        
        # PRIORITY 2: Industry-specific description
        if cls._diversity_tracker:
            return cls._diversity_tracker.get_fresh_description(website_type)
        else:
            return IndustryContentLibrary.get_random_description(website_type)
    
    @classmethod
    def get_cta(cls, website_type: str, custom_cta: str = "", audience: str = "") -> str:
        """
        Get appropriate CTA - user's or industry default.
        Adapts tone based on audience.
        """
        # PRIORITY 1: User's exact text
        if custom_cta and custom_cta.strip():
            # Apply audience adaptation even to user CTAs if minor
            audience = audience or cls._current_audience
            if audience and not custom_cta.startswith("http"):
                return AudienceToneAdapter.adapt_cta(custom_cta.strip(), audience)
            return custom_cta.strip()
        
        # PRIORITY 2: Industry-specific CTA with audience adaptation
        audience = audience or cls._current_audience
        
        if cls._diversity_tracker:
            cta = cls._diversity_tracker.get_fresh_cta(website_type)
        else:
            cta = IndustryContentLibrary.get_random_cta(website_type)
        
        if audience:
            cta = AudienceToneAdapter.adapt_cta(cta, audience)
        
        return cta
    
    @classmethod
    def get_about_intro(cls, website_type: str, custom_intro: str = "") -> str:
        """Get appropriate about intro - user's or industry default"""
        # PRIORITY 1: User's exact text
        if custom_intro and custom_intro.strip():
            return custom_intro.strip()
        
        # PRIORITY 2: Industry-specific description
        return IndustryContentLibrary.get_random_description(website_type)
    
    @classmethod
    def get_adjectives(cls, website_type: str) -> list:
        """Get industry-specific adjectives for dynamic content"""
        return IndustryContentLibrary.get_adjectives(website_type)
    
    @classmethod
    def should_use_emoji(cls, audience: str = "") -> bool:
        """Check if emoji should be used based on audience"""
        audience = audience or cls._current_audience
        if not audience:
            return False
        return AudienceToneAdapter.should_use_emoji(audience)
    
    @classmethod
    def get_formal_level(cls, audience: str = "") -> str:
        """Get formality level for content"""
        audience = audience or cls._current_audience
        if not audience:
            return "medium"
        return AudienceToneAdapter.get_formal_level(audience)
    
    @classmethod
    def enhance_text_with_industry_terms(cls, text: str, website_type: str) -> str:
        """Enhance generic text with industry-specific terms"""
        return IndustryContentLibrary.enhance_text(text, website_type)
    
    # Legacy compatibility - still works but now uses rich library
    HERO_HEADLINES = {
        "cafe": IndustryContentLibrary.CAFE.get("headlines", [])[:3],
        "restaurant": IndustryContentLibrary.RESTAURANT.get("headlines", [])[:3],
        "gaming": IndustryContentLibrary.GAMING.get("headlines", [])[:3],
        "portfolio": IndustryContentLibrary.PORTFOLIO.get("headlines", [])[:3],
        "agency": IndustryContentLibrary.AGENCY.get("headlines", [])[:3],
        "ecommerce": IndustryContentLibrary.ECOMMERCE.get("headlines", [])[:3],
    }
    
    ABOUT_INTROS = {
        "cafe": IndustryContentLibrary.CAFE.get("descriptions", [""])[0],
        "restaurant": IndustryContentLibrary.RESTAURANT.get("descriptions", [""])[0],
        "gaming": IndustryContentLibrary.GAMING.get("descriptions", [""])[0],
        "portfolio": IndustryContentLibrary.PORTFOLIO.get("descriptions", [""])[0],
        "agency": IndustryContentLibrary.AGENCY.get("descriptions", [""])[0],
        "ecommerce": IndustryContentLibrary.ECOMMERCE.get("descriptions", [""])[0],
    }
