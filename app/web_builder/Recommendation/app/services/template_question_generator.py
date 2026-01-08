"""
Template-Based Question Generator

This module analyzes templates in website_types folder and dynamically generates
questions based on what data each template needs.

KEY FEATURES:
1. Auto-detects props needed by scanning template files
2. Generates variety of questions for same data points
3. Randomizes question selection for uniqueness
4. Maps answers directly to template props
"""

import random
import re
from typing import Dict, Any, List, Optional, Set, Tuple
from dataclasses import dataclass
from pathlib import Path


@dataclass
class QuestionSpec:
    """Specification for a question that maps to template props"""
    prop_key: str              # The key in props (e.g., "title", "subtitle")
    section: str               # Which section this belongs to (hero, menu, about)
    question_variants: List[str]  # Different ways to ask same question
    question_type: str = "text"   # text, textarea, radio, checkbox
    options: Optional[List[str]] = None  # For radio/checkbox
    priority: int = 5             # 1-10, higher = more important


class TemplatePropsAnalyzer:
    """
    Analyzes template files to extract what props they expect.
    Scans for props.get("key", ...) patterns.
    """
    
    # Patterns to find prop usage:
    # 1. props.get("key") or props.get('key')
    # 2. props["key"] or props['key']
    PROPS_PATTERN = re.compile(r'(?:props\.get\(|props\[)["\'](\w+)["\']')
    
    @classmethod
    def analyze_template_file(cls, file_path: Path) -> Set[str]:
        """Extract all prop keys from a template file"""
        props = set()
        try:
            content = file_path.read_text(encoding='utf-8')
            # Find all matches for props access
            matches = cls.PROPS_PATTERN.findall(content)
            props.update(matches)
            
            # Special check for 'items' if we see a loop over raw_items or props['items']
            if 'items' in content or 'raw_items' in content:
                props.add('items')
        except Exception as e:
            print(f"[TemplatePropsAnalyzer] Error reading {file_path}: {e}")
            pass
        return props
    
    @classmethod  
    def analyze_website_type(cls, website_type: str) -> Dict[str, Set[str]]:
        """
        Analyze all templates for a website type.
        Returns dict mapping section -> set of props
        """
        base_path = Path(__file__).parent.parent.parent.parent / "Web_generator" / "app" / "templates" / "website_types" / website_type
        
        section_props = {}
        
        if not base_path.exists():
            return section_props
        
        # Scan each section directory
        for section_dir in base_path.iterdir():
            if section_dir.is_dir() and not section_dir.name.startswith('_'):
                section_name = section_dir.name
                all_props = set()
                
                # Scan all variant files
                for variant_file in section_dir.glob("variant_*.py"):
                    props = cls.analyze_template_file(variant_file)
                    all_props.update(props)
                
                if all_props:
                    section_props[section_name] = all_props
        
        return section_props


class QuestionLibrary:
    """
    Library of question variants for common props.
    Each prop can be asked in multiple ways for variety.
    """
    
    # Common props across all website types
    COMMON_QUESTIONS: Dict[str, QuestionSpec] = {
        "title": QuestionSpec(
            prop_key="title",
            section="hero",
            priority=10,
            question_variants=[
                "What's the main headline for your website?",
                "What title should visitors see first?",
                "Write your website's main headline:",
                "What's your attention-grabbing headline?",
                "Complete: '[Your Brand] - ____'",
            ]
        ),
        "subtitle": QuestionSpec(
            prop_key="subtitle", 
            section="hero",
            priority=9,
            question_variants=[
                "What's your tagline or slogan?",
                "Describe your business in one line:",
                "What makes you special? (short phrase)",
                "Your brand's promise in one sentence:",
                "If you had 5 seconds to impress, what would you say?",
            ]
        ),
        "cta": QuestionSpec(
            prop_key="cta",
            section="hero",
            priority=8,
            question_type="radio",
            question_variants=[
                "What action should visitors take?",
                "What's the main button text?",
                "Primary call-to-action:",
            ],
            options=["View Menu", "Get Started", "Shop Now", "Learn More", "Book Now", "Contact Us", "Explore", "Join Now"]
        ),
        "story": QuestionSpec(
            prop_key="story",
            section="about",
            priority=7,
            question_type="textarea",
            question_variants=[
                "Tell us your story (2-3 sentences):",
                "What's the story behind your business?",
                "Share your journey with visitors:",
                "How did your business begin?",
                "What inspired you to start?",
            ]
        ),
        "image": QuestionSpec(
            prop_key="image",
            section="hero",
            priority=6,
            question_type="radio",
            question_variants=[
                "What type of hero image fits your brand?",
                "Choose your hero visual style:",
                "What should the background show?",
            ],
            options=["Professional photo", "Abstract/artistic", "Product showcase", "Team/people", "Location/space", "Auto-select for me"]
        ),
    }
    
    # Website type specific question libraries
    CAFE_QUESTIONS: Dict[str, QuestionSpec] = {
        "menuItems": QuestionSpec(
            prop_key="menuItems",
            section="menu",
            priority=9,
            question_type="checkbox",
            question_variants=[
                "What's on your menu?",
                "Select your main offerings:",
                "What do you serve?",
            ],
            options=["Coffee & Espresso", "Tea & Specialty Drinks", "Pastries & Baked Goods", "Sandwiches & Food", "Desserts", "Cold Drinks & Smoothies"]
        ),
        "atmosphere": QuestionSpec(
            prop_key="atmosphere",
            section="about",
            priority=8,
            question_type="radio",
            question_variants=[
                "What's the vibe of your cafe?",
                "Describe your atmosphere:",
                "How would you describe the feel?",
            ],
            options=["Cozy & Warm", "Modern & Minimal", "Rustic & Natural", "Industrial & Urban", "Elegant & Refined"]
        ),
        "signature": QuestionSpec(
            prop_key="signature",
            section="menu",
            priority=9,
            question_variants=[
                "What's your signature item?",
                "What's your bestseller?",
                "What are you famous for?",
                "What do customers love most?",
            ]
        ),
        "hours": QuestionSpec(
            prop_key="hours",
            section="footer",
            priority=7,
            question_variants=[
                "What are your opening hours?",
                "When can customers visit?",
                "Your business hours:",
            ]
        ),
        "location": QuestionSpec(
            prop_key="location",
            section="contact",
            priority=6,
            question_variants=[
                "Where is your cafe located?",
                "Your cafe's address or area:",
                "Where can customers find you?",
            ]
        ),
        "specialty": QuestionSpec(
            prop_key="specialty",
            section="about",
            priority=8,
            question_type="radio",
            question_variants=[
                "What type of cafe is it?",
                "Your specialty:",
                "What kind of cafe are you?",
            ],
            options=["Coffee Shop", "Bakery Cafe", "Tea House", "Brunch Spot", "Dessert Cafe", "Juice & Smoothie Bar"]
        ),
    }
    
    GAMING_QUESTIONS: Dict[str, QuestionSpec] = {
        "gameName": QuestionSpec(
            prop_key="gameName",
            section="hero",
            priority=10,
            question_variants=[
                "What's the name of your game/studio?",
                "Enter your game title:",
                "Your gaming brand name:",
            ]
        ),
        "genre": QuestionSpec(
            prop_key="genre",
            section="about",
            priority=9,
            question_type="checkbox",
            question_variants=[
                "What genre is your game?",
                "Select game categories:",
                "What type of gaming content?",
            ],
            options=["Action/FPS", "RPG/Adventure", "Strategy", "Sports/Racing", "Indie/Casual", "Esports/Competitive", "Streaming/Content"]
        ),
        "platforms": QuestionSpec(
            prop_key="platforms",
            section="about",
            priority=8,
            question_type="checkbox",
            question_variants=[
                "Which platforms do you support?",
                "Where can people play?",
                "Available on:",
            ],
            options=["PC/Steam", "PlayStation", "Xbox", "Nintendo Switch", "Mobile", "Browser/Web"]
        ),
        "style": QuestionSpec(
            prop_key="style",
            section="hero",
            priority=8,
            question_type="radio",
            question_variants=[
                "What visual style fits your brand?",
                "Choose your aesthetic:",
                "Pick your vibe:",
            ],
            options=["Neon Cyberpunk", "Dark & Epic", "Retro Arcade", "Clean Esports", "Colorful Fun"]
        ),
        "features": QuestionSpec(
            prop_key="features",
            section="features",
            priority=7,
            question_type="checkbox",
            question_variants=[
                "What features should we highlight?",
                "Key selling points:",
                "What makes your game special?",
            ],
            options=["Multiplayer", "Story Mode", "Open World", "Competitive Ranked", "Regular Updates", "Mod Support", "Cross-Platform"]
        ),
    }
    
    RESTAURANT_QUESTIONS: Dict[str, QuestionSpec] = {
        "cuisine": QuestionSpec(
            prop_key="cuisine",
            section="about",
            priority=10,
            question_type="radio",
            question_variants=[
                "What type of cuisine do you serve?",
                "Your restaurant's specialty:",
                "What food category fits best?",
            ],
            options=["Italian", "Indian", "Chinese/Asian", "American", "Mexican", "Mediterranean", "Multi-cuisine", "Fusion"]
        ),
        "diningStyle": QuestionSpec(
            prop_key="diningStyle",
            section="about",
            priority=9,
            question_type="radio",
            question_variants=[
                "What's your dining style?",
                "Describe your restaurant atmosphere:",
                "Type of dining experience:",
            ],
            options=["Fine Dining", "Casual Dining", "Fast Casual", "Family Style", "Cafe/Bistro", "Bar & Grill"]
        ),
        "specialties": QuestionSpec(
            prop_key="specialties",
            section="menu",
            priority=8,
            question_type="textarea",
            question_variants=[
                "What are your signature dishes?",
                "What's your chef's specialty?",
                "Dishes you're famous for:",
            ]
        ),
        "reservation": QuestionSpec(
            prop_key="reservation",
            section="contact",
            priority=7,
            question_type="radio",
            question_variants=[
                "Do you take reservations?",
                "Booking preference:",
            ],
            options=["Yes, reservations required", "Reservations recommended", "Walk-ins welcome", "Call ahead only"]
        ),
    }
    
    PORTFOLIO_QUESTIONS: Dict[str, QuestionSpec] = {
        "profession": QuestionSpec(
            prop_key="profession",
            section="hero",
            priority=10,
            question_variants=[
                "What's your profession/title?",
                "How should we introduce you?",
                "Your professional title:",
            ]
        ),
        "skills": QuestionSpec(
            prop_key="skills",
            section="about",
            priority=9,
            question_type="checkbox",
            question_variants=[
                "What are your main skills?",
                "Select your expertise areas:",
                "What do you specialize in?",
            ],
            options=["Web Development", "UI/UX Design", "Mobile Apps", "Graphic Design", "Photography", "Video/Motion", "3D/Animation", "Marketing"]
        ),
        "experience": QuestionSpec(
            prop_key="experience",
            section="about",
            priority=8,
            question_type="radio",
            question_variants=[
                "Years of experience?",
                "How long have you been working?",
            ],
            options=["1-2 years", "3-5 years", "5-10 years", "10+ years"]
        ),
        "workStyle": QuestionSpec(
            prop_key="workStyle",
            section="about",
            priority=7,
            question_type="radio",
            question_variants=[
                "How do you prefer to work?",
                "Your work arrangement:",
            ],
            options=["Freelance/Independent", "Available for hire", "Agency owner", "Open to collaboration"]
        ),
    }
    
    AGENCY_QUESTIONS: Dict[str, QuestionSpec] = {
        "services": QuestionSpec(
            prop_key="services",
            section="services",
            priority=10,
            question_type="checkbox",
            question_variants=[
                "What services do you offer?",
                "Select your core services:",
                "What does your agency do?",
            ],
            options=["Web Design/Development", "Branding & Identity", "Digital Marketing", "SEO/Content", "Social Media", "Video Production", "Consulting"]
        ),
        "clientType": QuestionSpec(
            prop_key="clientType",
            section="about",
            priority=9,
            question_type="checkbox",
            question_variants=[
                "Who are your ideal clients?",
                "Who do you work with?",
                "Your target clients:",
            ],
            options=["Startups", "Small Business", "Enterprise", "E-commerce", "Tech Companies", "Creatives", "Non-profits"]
        ),
        "approach": QuestionSpec(
            prop_key="approach",
            section="about",
            priority=8,
            question_type="radio",
            question_variants=[
                "What's your agency's approach?",
                "How do you describe your style?",
                "Your working philosophy:",
            ],
            options=["Data-driven & Strategic", "Creative & Bold", "Collaborative & Agile", "Results-focused", "Innovation-first"]
        ),
    }
    
    ECOMMERCE_QUESTIONS: Dict[str, QuestionSpec] = {
        "productType": QuestionSpec(
            prop_key="productType",
            section="hero",
            priority=10,
            question_type="radio",
            question_variants=[
                "What do you sell?",
                "Your product category:",
                "Type of products:",
            ],
            options=["Fashion & Apparel", "Electronics", "Home & Living", "Beauty & Wellness", "Food & Beverages", "Digital Products", "Handmade/Artisan"]
        ),
        "usp": QuestionSpec(
            prop_key="usp",
            section="hero",
            priority=9,
            question_variants=[
                "What makes your products special?",
                "Your unique selling point:",
                "Why should people buy from you?",
            ]
        ),
        "shipping": QuestionSpec(
            prop_key="shipping",
            section="features",
            priority=7,
            question_type="checkbox",
            question_variants=[
                "What shipping options do you offer?",
                "Delivery features:",
            ],
            options=["Free Shipping", "Same Day Delivery", "International Shipping", "Easy Returns", "Gift Wrapping"]
        ),
    }
    
    @classmethod
    def get_library_for_type(cls, website_type: str) -> Dict[str, QuestionSpec]:
        """Get combined question library for a website type"""
        type_lower = website_type.lower()
        
        # Map website types to their SPECIFIC question libraries
        # Don't mix Portfolio with Agency - they have different needs
        type_libraries = {
            # Cafe/Coffee types
            "cafe": cls.CAFE_QUESTIONS,
            "coffee": cls.CAFE_QUESTIONS,
            "bakery": cls.CAFE_QUESTIONS,
            
            # Gaming types
            "gaming": cls.GAMING_QUESTIONS,
            "esports": cls.GAMING_QUESTIONS,
            
            # Restaurant types
            "restaurant": cls.RESTAURANT_QUESTIONS,
            "dining": cls.RESTAURANT_QUESTIONS,
            
            # Portfolio types - ONLY portfolio questions, no agency overlap
            "portfolio": cls.PORTFOLIO_QUESTIONS,
            "personal": cls.PORTFOLIO_QUESTIONS,
            "freelancer": cls.PORTFOLIO_QUESTIONS,
            
            # Agency types - ONLY agency questions
            "agency": cls.AGENCY_QUESTIONS,
            "business": cls.AGENCY_QUESTIONS,
            "corporate": cls.AGENCY_QUESTIONS,
            
            # Ecommerce types
            "ecommerce": cls.ECOMMERCE_QUESTIONS,
            "shop": cls.ECOMMERCE_QUESTIONS,
            "store": cls.ECOMMERCE_QUESTIONS,
        }
        
        # Start with common questions
        combined = dict(cls.COMMON_QUESTIONS)
        
        # Add ONLY the type-specific questions (no mixing!)
        type_specific = type_libraries.get(type_lower, {})
        
        # For each type-specific question, ADD it only if not already in common
        # This prevents overwriting common questions
        for key, spec in type_specific.items():
            if key not in combined:
                combined[key] = spec
        
        return combined


class TemplateQuestionGenerator:
    """
    Main generator that creates dynamic questions based on templates.
    
    KEY FEATURE: Only asks questions for props that ACTUALLY exist in templates!
    
    USAGE:
        generator = TemplateQuestionGenerator("cafe")
        questions = generator.generate_questions(count=10)
    """
    
    def __init__(self, website_type: str, language: str = "English"):
        self.website_type = website_type.lower()
        self.language = language
        
        # STEP 1: Analyze templates to get ACTUAL props used
        self.template_props = TemplatePropsAnalyzer.analyze_website_type(self.website_type)
        self.all_template_props = self._get_all_template_props()
        
        print(f"[TemplateQuestionGenerator] 📂 Analyzed {self.website_type} templates")
        print(f"[TemplateQuestionGenerator] 📋 Template props: {self.all_template_props}")
        
        # STEP 2: Get full question library for this type
        full_library = QuestionLibrary.get_library_for_type(self.website_type)
        
        # STEP 3: FILTER library - only keep questions for props that templates ACTUALLY use
        self.question_library = self._filter_library_by_template_props(full_library)
        
        print(f"[TemplateQuestionGenerator] ✅ Filtered to {len(self.question_library)} relevant questions")
        
        # Track what we've asked to avoid duplicates
        self.asked_props: Set[str] = set()
        self.asked_sections: Dict[str, int] = {}  # section -> count asked
    
    def _get_all_template_props(self) -> Set[str]:
        """Get all props used across all template sections"""
        all_props = set()
        for section, props in self.template_props.items():
            all_props.update(props)
        return all_props
    
    def _filter_library_by_template_props(self, full_library: Dict[str, 'QuestionSpec']) -> Dict[str, 'QuestionSpec']:
        """
        Filter question library to ONLY include questions for props that templates use.
        Also automatically CREATES questions for props found in templates but missing from library.
        STRICT: Checks both if the prop is used AND if the section (feature) exists.
        """
        filtered = {}
        
        # Always include these fundamental props
        mandatory_props = {"businessName", "colorTheme"}
        
        # Get list of valid sections (folders) for this template type
        valid_sections = set(self.template_props.keys())
        # Add 'base' as a valid virtual section for common info
        valid_sections.add("base")
        
        print(f"[TemplateQuestionGenerator] 🏗️ Valid sections in {self.website_type} templates: {valid_sections}")
        
        # 1. Start with props that ARE in full_library
        for prop_key, spec in full_library.items():
            # Check if section exists in template
            section_exists = spec.section in valid_sections
            
            # Check if prop is used in ANY variant of that section (or mandatory)
            prop_used = (
                prop_key in self.all_template_props or 
                prop_key in mandatory_props or
                prop_key.lower() in [p.lower() for p in self.all_template_props]
            )
            
            # Also check if it's one of the common hero props which most templates assume
            # Even if they use specific names like 'heroTitle', we try to be smart
            hero_props = {"title", "subtitle", "cta", "image"}
            if spec.section == "hero" and prop_key in hero_props:
                # Keep hero props if hero section exists
                if "hero" in valid_sections:
                    prop_used = True
            
            if prop_used and section_exists:
                filtered[prop_key] = spec
            else:
                reason = "section missing" if not section_exists else "prop not in template"
                print(f"[TemplateQuestionGenerator] ⏭️ Skipping '{prop_key}' - {reason}")
        
        # 2. AUTO-GENERATE questions for props found in templates but MISSING from library
        for section, props_in_section in self.template_props.items():
            for template_prop in props_in_section:
                # Skip tech specs
                if template_prop in ["primary", "secondary", "accent", "background", "text", "surface"]:
                    continue
                    
                if template_prop not in filtered and template_prop not in mandatory_props:
                    print(f"[TemplateQuestionGenerator] ✨ Auto-generating question for template prop: '{template_prop}' in '{section}'")
                    
                    # Create a generic question spec
                    display_name = template_prop.replace("_", " ").title()
                    filtered[template_prop] = QuestionSpec(
                        prop_key=template_prop,
                        section=section,
                        priority=5,
                        question_variants=[
                            f"Tell us more about your {display_name} for the {section}:",
                            f"What would you like to say for '{display_name}'?",
                            f"Enter your information for '{display_name}':",
                        ]
                    )
        
        return filtered
        
    def generate_questions(self, count: int = 10, include_mandatory: bool = True) -> List[Dict[str, Any]]:
        """
        Generate a list of questions for this website type.
        
        Args:
            count: Number of questions to generate
            include_mandatory: Whether to include business name and color questions
            
        Returns:
            List of question dicts ready for the Q&A flow
        """
        questions = []
        question_index = 1
        
        # Mandatory questions first
        if include_mandatory:
            # Q1: Business/Project Name
            questions.append(self._create_business_name_question(question_index))
            question_index += 1
            
            # Q2: Color Theme
            questions.append(self._create_color_question(question_index))
            question_index += 1
        
        # Get remaining questions from library
        remaining = count - len(questions)
        dynamic_questions = self._generate_dynamic_questions(remaining, question_index)
        questions.extend(dynamic_questions)
        
        return questions
    
    def generate_single_question(self, question_index: int, previous_answers: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """
        Generate a single question based on context.
        Used for step-by-step Q&A flow.
        
        Args:
            question_index: 1-based index of question
            previous_answers: Answers given so far
            
        Returns:
            Question dict or None if no more questions
        """
        previous_answers = previous_answers or {}
        
        # Q1: Business name
        if question_index == 1:
            return self._create_business_name_question(question_index)
        
        # Q2: Color theme
        if question_index == 2:
            return self._create_color_question(question_index)
        
        # Q3+: Dynamic questions from library
        available_specs = self._get_available_questions()
        
        if not available_specs:
            return None
        
        # Weight by priority + some randomness
        weights = [spec.priority + random.randint(0, 3) for spec in available_specs]
        selected = random.choices(available_specs, weights=weights, k=1)[0]
        
        question = self._create_question_from_spec(selected, question_index)
        self.asked_props.add(selected.prop_key)
        
        return question
    
    def _get_available_questions(self) -> List[QuestionSpec]:
        """Get questions we haven't asked yet"""
        available = []
        for prop_key, spec in self.question_library.items():
            if prop_key not in self.asked_props:
                available.append(spec)
        return available
    
    def _create_business_name_question(self, index: int) -> Dict[str, Any]:
        """Create the business name question with variety"""
        variants = {
            "cafe": [
                "What's your cafe called?",
                "Enter your cafe name:",
                "What should we call your cafe?",
            ],
            "gaming": [
                "What's your game/studio name?",
                "Enter your gaming brand name:",
                "Your gaming identity:",
            ],
            "restaurant": [
                "What's your restaurant named?",
                "Enter your restaurant name:",
                "Your restaurant's name:",
            ],
            "portfolio": [
                "What's your name?",
                "Enter your full name:",
                "How should visitors address you?",
            ],
            "agency": [
                "What's your company name?",
                "Enter your agency name:",
                "Your business name:",
            ],
            "ecommerce": [
                "What's your store name?",
                "Enter your shop name:",
                "Your brand name:",
            ],
        }
        
        # Get type-specific variants or default
        type_variants = variants.get(self.website_type, [
            "What's your business name?",
            "Enter your brand name:",
            "What should we call your business?",
        ])
        
        question_text = random.choice(type_variants)
        
        return {
            "id": f"q{index}",
            "question": question_text,
            "type": "text",
            "prop_key": "businessName",
            "section": "base",
            "_mandatory": True,
        }
    
    def _create_color_question(self, index: int) -> Dict[str, Any]:
        """Create color preference question with variety"""
        color_palettes = {
            "cafe": [
                ("Warm Espresso", "Rich browns and cream - cozy and inviting"),
                ("Modern White", "Clean white with black accents - minimalist"),
                ("Forest Green", "Natural greens and wood tones - organic feel"),
                ("Dusty Rose", "Soft pinks and neutrals - elegant and feminine"),
            ],
            "gaming": [
                ("Neon Cyber", "Electric blues and purples - futuristic"),
                ("Dark Pro", "Black with red accents - competitive edge"),
                ("Retro Arcade", "Bright pinks and yellows - playful nostalgia"),
                ("Esports Green", "Black with neon green - pro gamer aesthetic"),
            ],
            "restaurant": [
                ("Elegant Gold", "Black and gold - fine dining sophistication"),
                ("Fresh Garden", "Greens and earth tones - farm to table vibe"),
                ("Warm Terracotta", "Warm oranges and browns - rustic comfort"),
                ("Ocean Blue", "Blues and whites - coastal fresh feel"),
            ],
            "portfolio": [
                ("Clean Minimal", "Black, white, and one accent color"),
                ("Bold Creative", "Vibrant colors that pop"),
                ("Professional", "Navy and gray - trustworthy"),
                ("Dark Mode", "Dark backgrounds with light text"),
            ],
            "agency": [
                ("Corporate Blue", "Professional blues and grays"),
                ("Creative Orange", "Energetic orange with dark accents"),
                ("Tech Purple", "Modern purple gradients"),
                ("Minimal B&W", "Black and white sophistication"),
            ],
            "ecommerce": [
                ("Trust Blue", "Blues that inspire confidence"),
                ("Luxury Black", "Black and gold - premium feel"),
                ("Fresh Green", "Eco-friendly, natural vibes"),
                ("Trendy Coral", "Coral and white - modern fashion"),
            ],
        }
        
        question_variants = [
            "Choose your color palette:",
            "What colors represent your brand?",
            "Pick your website's color scheme:",
            "Which vibe matches your brand?",
        ]
        
        palettes = color_palettes.get(self.website_type, [
            ("Professional", "Clean and modern colors"),
            ("Bold", "Vibrant and eye-catching"),
            ("Minimal", "Simple black and white"),
            ("Warm", "Welcoming earth tones"),
        ])
        
        return {
            "id": f"q{index}",
            "question": random.choice(question_variants),
            "type": "radio",
            "options": [f"{name} - {desc}" for name, desc in palettes],
            "prop_key": "colorTheme",
            "section": "base",
            "_mandatory": True,
        }
    
    def _generate_dynamic_questions(self, count: int, start_index: int) -> List[Dict[str, Any]]:
        """Generate dynamic questions from the library"""
        questions = []
        available = list(self.question_library.items())
        
        # Shuffle for variety
        random.shuffle(available)
        
        # Sort by priority (higher first) but with some randomness
        available.sort(key=lambda x: -(x[1].priority + random.randint(-2, 2)))
        
        for prop_key, spec in available[:count]:
            if prop_key in self.asked_props:
                continue
                
            question = self._create_question_from_spec(spec, start_index + len(questions))
            questions.append(question)
            self.asked_props.add(prop_key)
            
            if len(questions) >= count:
                break
        
        return questions
    
    def _create_question_from_spec(self, spec: QuestionSpec, index: int) -> Dict[str, Any]:
        """Create a question dict from a QuestionSpec"""
        # Pick a random variant of the question
        question_text = random.choice(spec.question_variants)
        
        question = {
            "id": f"q{index}",
            "question": question_text,
            "type": spec.question_type,
            "prop_key": spec.prop_key,
            "section": spec.section,
        }
        
        if spec.options:
            # Shuffle options for variety (except first/last which may be special)
            shuffled_options = list(spec.options)
            if len(shuffled_options) > 3:
                middle = shuffled_options[1:-1]
                random.shuffle(middle)
                shuffled_options = [shuffled_options[0]] + middle + [shuffled_options[-1]]
            question["options"] = shuffled_options
        
        return question


class AnswerToPropsMapper:
    """
    Maps Q&A answers directly to template props.
    Ensures user content goes exactly where templates need it.
    """
    
    @staticmethod
    def map_answers_to_props(questions: List[Dict[str, Any]], answers: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert Q&A answers to props dict for templates.
        
        Args:
            questions: The questions that were asked (with prop_key metadata)
            answers: User's answers keyed by question ID
            
        Returns:
            Props dict ready for template rendering
        """
        props = {}
        
        for question in questions:
            q_id = question.get("id")
            prop_key = question.get("prop_key")
            answer = answers.get(q_id)
            
            if prop_key and answer:
                # Handle special mappings
                if prop_key == "businessName":
                    props["businessName"] = answer
                    props["title"] = f"Welcome to {answer}"
                    props["name"] = answer
                elif prop_key == "colorTheme":
                    props["colorTheme"] = answer
                    # Extract just the palette name if it includes description
                    if " - " in str(answer):
                        props["colorThemeName"] = answer.split(" - ")[0]
                else:
                    props[prop_key] = answer
        
        return props


# Create singleton instance for easy import
def get_question_generator(website_type: str, language: str = "English") -> TemplateQuestionGenerator:
    """Factory function to create a question generator"""
    return TemplateQuestionGenerator(website_type, language)


__all__ = [
    "TemplateQuestionGenerator",
    "TemplatePropsAnalyzer", 
    "QuestionLibrary",
    "QuestionSpec",
    "AnswerToPropsMapper",
    "get_question_generator",
]
