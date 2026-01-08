"""
Industry-Specific AI Prompts
Enhanced prompts for better, more targeted AI content generation
"""

from typing import Dict, Any, List, Optional
import json


class IndustryPrompts:
    """
    Industry-specific prompt enhancements for higher quality AI content.
    """
    
    # ============================================================
    # INDUSTRY-SPECIFIC CONTENT GUIDELINES
    # ============================================================
    
    INDUSTRY_GUIDELINES = {
        "restaurant": {
            "tone": "warm, inviting, and appetizing",
            "keywords": ["dining experience", "culinary", "flavors", "freshness", "cuisine"],
            "hero_tips": "Use food imagery metaphors. Emphasize ambiance and taste experience.",
            "about_tips": "Tell the chef's story, origin of recipes, passion for food.",
            "cta_examples": ["Reserve a Table", "View Our Menu", "Order Now", "Book Your Experience"],
            "content_focus": [
                "Highlight signature dishes",
                "Mention fresh/local ingredients",
                "Describe dining atmosphere",
                "Include opening hours subtly"
            ],
            "avoid": ["generic food descriptions", "overused phrases like 'delicious'"],
            "palette_mood": "Warm, earthy, and appetizing (Oranges, Deep Reds, Creams)"
        },
        
        "cafe": {
            "tone": "cozy, friendly, and relaxed",
            "keywords": ["artisanal", "fresh brewed", "handcrafted", "cozy corner", "perfect cup"],
            "hero_tips": "Create imagery of warm beverages, relaxed atmosphere, connection moments.",
            "about_tips": "Share the passion for coffee/tea, sourcing story, barista expertise.",
            "cta_examples": ["Order Your Favorite", "Find Your Blend", "Join Our Community", "Start Your Day Right"],
            "content_focus": [
                "Coffee/tea expertise and sourcing",
                "Cozy atmosphere description",
                "Community and connection",
                "Specialty drinks and pastries"
            ],
            "avoid": ["chain coffee language", "overly corporate tone"],
            "palette_mood": "Modern cozy (Rich Browns, Soft Creams, Muted Greens)"
        },
        
        "coffee_shop": {
            "tone": "artisanal, passionate, and community-focused",
            "keywords": ["craft coffee", "specialty beans", "pour-over", "espresso art", "third wave"],
            "hero_tips": "Emphasize the craft, the ritual, the experience of great coffee.",
            "about_tips": "Focus on bean sourcing, roasting process, barista training.",
            "cta_examples": ["Discover Our Blends", "Order Fresh", "Visit Us", "Try Our Signature"],
            "content_focus": [
                "Bean origin stories",
                "Brewing methods",
                "Sustainability practices",
                "Local community involvement"
            ],
            "avoid": ["mass-market coffee references", "generic descriptions"]
        },
        
        "bakery": {
            "tone": "warm, traditional yet fresh, artisanal",
            "keywords": ["fresh-baked", "handmade", "from scratch", "daily fresh", "generations"],
            "hero_tips": "Evoke the smell of fresh bread, warmth of the oven, tradition.",
            "about_tips": "Family recipes, baking tradition, passion for craft.",
            "cta_examples": ["Order Fresh Today", "View Our Treats", "Custom Orders", "Visit the Bakery"],
            "content_focus": [
                "Freshness and daily baking",
                "Traditional recipes",
                "Quality ingredients",
                "Custom cake/order services"
            ],
            "avoid": ["industrial baking terms", "processed food language"]
        },
        
        "salon": {
            "tone": "glamorous, confident, and transformative",
            "keywords": ["transform", "radiant", "expert stylists", "premium care", "beauty journey"],
            "hero_tips": "Focus on transformation, confidence boost, self-care luxury.",
            "about_tips": "Stylist expertise, continuous training, client transformations.",
            "cta_examples": ["Book Your Transformation", "Schedule Appointment", "Discover Services", "Treat Yourself"],
            "content_focus": [
                "Expert stylists credentials",
                "Premium products used",
                "Personalized consultations",
                "Before/after transformations"
            ],
            "avoid": ["cheap/discount language", "rushed service mentions"]
        },
        
        "spa": {
            "tone": "serene, healing, and luxurious",
            "keywords": ["rejuvenate", "tranquility", "wellness", "restore", "sanctuary"],
            "hero_tips": "Create imagery of peace, relaxation, escape from daily stress.",
            "about_tips": "Wellness philosophy, healing traditions, expert therapists.",
            "cta_examples": ["Begin Your Journey", "Book Wellness Session", "Find Your Calm", "Escape Today"],
            "content_focus": [
                "Healing and wellness benefits",
                "Unique treatments offered",
                "Serene environment",
                "Expert therapist profiles"
            ],
            "avoid": ["clinical language", "rushed service mentions"]
        },
        
        "fitness": {
            "tone": "motivating, energetic, and empowering",
            "keywords": ["transform", "achieve", "strength", "push limits", "results"],
            "hero_tips": "Focus on transformation, community support, achieving goals.",
            "about_tips": "Trainer expertise, success stories, training philosophy.",
            "cta_examples": ["Start Your Journey", "Join Today", "Get Your Free Trial", "Transform Now"],
            "content_focus": [
                "Results and transformations",
                "Expert trainer backgrounds",
                "State-of-the-art equipment",
                "Supportive community"
            ],
            "avoid": ["intimidating language", "unrealistic promises"]
        },
        
        "gaming": {
            "tone": "bold, energetic, and immersive",
            "keywords": ["level up", "epic", "legendary", "competitive", "immersive world"],
            "hero_tips": "Use high-energy words. Focus on victory, achievement, and world-building.",
            "about_tips": "Mission to innovate gaming, community passion, technical excellence.",
            "cta_examples": ["Play Now", "Join the Battle", "Start Your Journey", "Enter the Arena"],
            "content_focus": [
                "Unique gameplay features",
                "Community and leaderboards",
                "Immersive story elements",
                "Technical performance"
            ],
            "avoid": ["slow-paced language", "generic 'fun' descriptions"],
            "palette_mood": "Dark with Neon accents (Cyber Blue, Toxic Green, Purple)"
        },

        "movie": {
            "tone": "cinematic, dramatic, and storytelling",
            "keywords": ["premiere", "blockbuster", "cinematic", "now showing", "red carpet"],
            "hero_tips": "Focus on the magic of cinema, large-scale drama, and excitement.",
            "about_tips": "Passion for storytelling, history of the theater, cinematic quality.",
            "cta_examples": ["Get Tickets", "Watch Trailer", "View Showtimes", "Book Premiere"],
            "content_focus": [
                "Upcoming blockbusters",
                "Premium viewing experience",
                "Showtime schedules",
                "Concessions and amenities"
            ],
            "avoid": ["boring schedules", "low-quality imagery mentions"],
            "palette_mood": "Cinema Dark (Netflix Red, Obsidian, Gold)"
        },
        
        "agency": {
            "tone": "innovative, results-driven, and creative",
            "keywords": ["innovate", "transform", "strategic", "creative solutions", "growth"],
            "hero_tips": "Showcase innovation, bold thinking, measurable results.",
            "about_tips": "Team expertise, notable projects, creative process.",
            "cta_examples": ["Start a Project", "Get a Quote", "Let's Create", "Work With Us"],
            "content_focus": [
                "Case studies and results",
                "Creative process explanation",
                "Team expertise highlights",
                "Client success stories"
            ],
            "avoid": ["jargon overload", "vague promises"]
        },
        
        "technology": {
            "tone": "innovative, clear, and forward-thinking",
            "keywords": ["innovation", "seamless", "intelligent", "next-generation", "streamline"],
            "hero_tips": "Focus on problem-solving, efficiency gains, innovation.",
            "about_tips": "Mission, team expertise, technology philosophy.",
            "cta_examples": ["Get Started", "Try Free", "See Demo", "Start Building"],
            "content_focus": [
                "Clear value proposition",
                "Key features and benefits",
                "Integration capabilities",
                "Customer success metrics"
            ],
            "avoid": ["too much technical jargon", "vague buzzwords"]
        },
        
        "healthcare": {
            "tone": "caring, professional, and trustworthy",
            "keywords": ["compassionate care", "expert team", "your health", "trusted", "personalized"],
            "hero_tips": "Emphasize trust, expertise, patient-centered care.",
            "about_tips": "Medical team credentials, facility quality, patient focus.",
            "cta_examples": ["Book Appointment", "Contact Us", "Schedule Consultation", "Learn More"],
            "content_focus": [
                "Medical team credentials",
                "Patient-centered approach",
                "Modern facilities",
                "Range of services"
            ],
            "avoid": ["alarming medical language", "guaranteed cures"]
        },
        
        "education": {
            "tone": "inspiring, supportive, and aspirational",
            "keywords": ["unlock potential", "learn", "grow", "future leaders", "excellence"],
            "hero_tips": "Focus on student success, future opportunities, supportive environment.",
            "about_tips": "Educational philosophy, faculty expertise, success stories.",
            "cta_examples": ["Apply Now", "Explore Programs", "Schedule Visit", "Start Learning"],
            "content_focus": [
                "Academic excellence",
                "Student support services",
                "Career outcomes",
                "Faculty credentials"
            ],
            "avoid": ["pressure tactics", "unrealistic success promises"]
        },
        
        "real_estate": {
            "tone": "professional, trustworthy, and aspirational",
            "keywords": ["dream home", "premier properties", "expert guidance", "investment", "lifestyle"],
            "hero_tips": "Focus on lifestyle, dream fulfillment, expert guidance.",
            "about_tips": "Market expertise, track record, client testimonials.",
            "cta_examples": ["Find Your Home", "Get Valuation", "Schedule Viewing", "Contact Agent"],
            "content_focus": [
                "Local market expertise",
                "Property portfolio highlights",
                "Client success stories",
                "Full-service support"
            ],
            "avoid": ["pushy sales language", "unrealistic promises"]
        },
        
        "photography": {
            "tone": "artistic, emotive, and authentic",
            "keywords": ["capture moments", "timeless", "authentic", "artistic vision", "memories"],
            "hero_tips": "Let the work speak, focus on emotional connection, unique style.",
            "about_tips": "Artistic journey, photography philosophy, notable work.",
            "cta_examples": ["View Portfolio", "Book Session", "Tell Your Story", "Let's Create"],
            "content_focus": [
                "Unique artistic style",
                "Types of sessions offered",
                "Client experience",
                "Portfolio highlights"
            ],
            "avoid": ["generic stock photo language", "price-focused messaging"]
        },
        
        "retail": {
            "tone": "trendy, accessible, and customer-focused",
            "keywords": ["discover", "trending", "curated", "quality", "style"],
            "hero_tips": "Highlight products, trends, shopping experience.",
            "about_tips": "Brand story, quality commitment, customer focus.",
            "cta_examples": ["Shop Now", "Explore Collection", "Find Your Style", "Discover More"],
            "content_focus": [
                "Product quality",
                "Unique offerings",
                "Customer satisfaction",
                "Easy shopping experience"
            ],
            "avoid": ["discount-heavy messaging", "pushy sales tactics"]
        },
        
        "business": {
            "tone": "professional, reliable, and solution-oriented",
            "keywords": ["solutions", "expertise", "trust", "results", "partnership"],
            "hero_tips": "Clear value proposition, problem-solving focus.",
            "about_tips": "Company history, team expertise, mission and values.",
            "cta_examples": ["Get Started", "Contact Us", "Learn More", "Request Quote"],
            "content_focus": [
                "Clear service offerings",
                "Company values",
                "Client testimonials",
                "Industry expertise"
            ],
            "avoid": ["vague corporate speak", "overused buzzwords"]
        }
    }
    
    @classmethod
    def get_industry_context(cls, business_type: str) -> Dict[str, Any]:
        """Get industry-specific context for AI prompts"""
        business_type = business_type.lower().replace(" ", "_").replace("-", "_")
        return cls.INDUSTRY_GUIDELINES.get(business_type, cls.INDUSTRY_GUIDELINES["business"])
    
    @classmethod
    def get_enhanced_system_prompt(cls, business_type: str) -> str:
        """Get enhanced system prompt with industry context"""
        context = cls.get_industry_context(business_type)
        
        return f"""You are an expert website content strategist specializing in {business_type} industry websites.

Your content must be:
- Tone: {context.get('tone', 'professional and engaging')}
- Keywords to incorporate naturally: {', '.join(context.get('keywords', []))}
- Hero section: {context.get('hero_tips', 'Create compelling headline')}
- About section: {context.get('about_tips', 'Tell authentic story')}
- Color Palette/Mood: {context.get('palette_mood', 'Professional and balanced')}

CONTENT FOCUS AREAS:
{chr(10).join('- ' + focus for focus in context.get('content_focus', []))}

AVOID:
{chr(10).join('- ' + avoid for avoid in context.get('avoid', []))}

CTA INSPIRATION:
{', '.join(context.get('cta_examples', ['Get Started', 'Learn More']))}

CRITICAL RULES:
1. Generate content specific to this {business_type} - NO generic business content
2. Use compelling, action-oriented language matching the tone
3. Keep the tone consistent throughout
4. Generate realistic, professional content - NO placeholders
5. All content should be SEO-friendly for {business_type} industry
6. Respond ONLY with valid JSON - no markdown, no explanations
7. Follow the exact JSON structure provided"""
    
    @classmethod
    def get_hero_enhancement(cls, business_type: str, target_audience: str = None) -> str:
        """Get hero-specific prompt enhancement"""
        context = cls.get_industry_context(business_type)
        
        audience_note = ""
        if target_audience:
            audience_note = f"\nTarget Audience: {target_audience} - tailor the messaging to appeal specifically to this audience."
        
        return f"""HERO SECTION GUIDELINES:
{context.get('hero_tips', '')}
{audience_note}

HEADLINE TIPS:
- Max 8-10 words, powerful and memorable
- Evoke emotion or paint a picture
- Avoid generic phrases like "Welcome to" or "Best in Town"

SUGGESTED CTA STYLES: {', '.join(context.get('cta_examples', ['Get Started']))}"""
    
    @classmethod
    def get_about_enhancement(cls, business_type: str) -> str:
        """Get about section prompt enhancement"""
        context = cls.get_industry_context(business_type)
        
        return f"""ABOUT SECTION GUIDELINES:
{context.get('about_tips', '')}

STORY REQUIREMENTS:
- 3-4 well-structured paragraphs
- Include founding story or inspiration
- Highlight unique value proposition
- End with forward-looking vision
- Make it authentic, not corporate"""
    
    @classmethod
    def get_menu_enhancement(cls, business_type: str) -> str:
        """Get menu section prompt enhancement (for food businesses)"""
        if business_type.lower() in ["restaurant", "cafe", "coffee_shop", "bakery"]:
            return """MENU SECTION GUIDELINES:
- Create appetizing, evocative descriptions (not just ingredient lists)
- Each item description: 15-25 words
- Include sensory language (textures, aromas, flavors)
- Price range should be realistic for the business type
- Organize into clear categories
- Highlight specialty/signature items

DESCRIPTION FORMAT:
Bad: "Coffee with milk and foam"
Good: "Velvety smooth espresso crowned with silken microfoam, perfect for those who appreciate the classics"
"""
        return ""
    
    @classmethod
    def get_testimonial_enhancement(cls, business_type: str) -> str:
        """Get testimonial prompt enhancement"""
        context = cls.get_industry_context(business_type)
        
        return f"""TESTIMONIAL GUIDELINES:
- Create 3 realistic, varied testimonials
- Each testimonial: 2-3 sentences, specific to {business_type}
- Include specific details about the experience
- Vary the customer types (different names, roles)
- Sound authentic, not scripted

AVOID:
- Over-the-top superlatives
- Generic "great service" comments
- Unrealistic praise"""
    
    @classmethod
    def get_audience_context(cls, target_audience: str) -> Dict[str, Any]:
        """
        Get audience-specific context for tone adaptation.
        
        Returns context including:
        - formal_level: low/medium/high
        - slang_allowed: bool
        - emoji_use: bool
        - cta_style: description
        """
        audience_lower = target_audience.lower() if target_audience else ""
        
        # Young adults / Gen Z
        if any(k in audience_lower for k in ["young", "gen z", "millennial", "student", "teen"]):
            return {
                "formal_level": "low",
                "slang_allowed": True,
                "emoji_use": True,
                "cta_style": "casual, action-oriented",
                "description": "Use modern, relatable language. Short sentences. Trendy phrases OK."
            }
        
        # Professionals / B2B
        elif any(k in audience_lower for k in ["professional", "corporate", "business", "b2b", "executive"]):
            return {
                "formal_level": "high",
                "slang_allowed": False,
                "emoji_use": False,
                "cta_style": "professional, clear",
                "description": "Use polished, professional language. Focus on value and ROI."
            }
        
        # Families
        elif any(k in audience_lower for k in ["family", "parent", "mom", "dad", "kids"]):
            return {
                "formal_level": "medium",
                "slang_allowed": False,
                "emoji_use": True,
                "cta_style": "warm, welcoming",
                "description": "Use warm, friendly language. Focus on family benefits and safety."
            }
        
        # Seniors
        elif any(k in audience_lower for k in ["senior", "elderly", "retired", "50+", "60+"]):
            return {
                "formal_level": "medium-high",
                "slang_allowed": False,
                "emoji_use": False,
                "cta_style": "clear, trustworthy",
                "description": "Use respectful, clear language. Avoid jargon. Emphasize trust."
            }
        
        # Tech-savvy
        elif any(k in audience_lower for k in ["tech", "developer", "engineer", "startup", "gamer"]):
            return {
                "formal_level": "low-medium",
                "slang_allowed": True,
                "emoji_use": True,
                "cta_style": "action-oriented, techy",
                "description": "Can use technical terms. Modern language. Reference tech culture."
            }
        
        # Luxury / Premium
        elif any(k in audience_lower for k in ["luxury", "premium", "high-end", "exclusive", "affluent"]):
            return {
                "formal_level": "high",
                "slang_allowed": False,
                "emoji_use": False,
                "cta_style": "elegant, exclusive",
                "description": "Use refined, sophisticated language. Emphasize exclusivity and quality."
            }
        
        # Default
        else:
            return {
                "formal_level": "medium",
                "slang_allowed": False,
                "emoji_use": False,
                "cta_style": "clear, friendly",
                "description": "Use clear, approachable language. Balance professional and friendly."
            }
    
    @classmethod
    def get_audience_enhanced_prompt(cls, business_type: str, target_audience: str) -> str:
        """
        Get combined industry and audience-aware prompt enhancement.
        """
        industry_context = cls.get_industry_context(business_type)
        audience_context = cls.get_audience_context(target_audience)
        
        return f"""
=== INDUSTRY CONTEXT ({business_type}) ===
Tone: {industry_context.get('tone', 'professional')}
Keywords to use: {', '.join(industry_context.get('keywords', []))}
Content Focus: {', '.join(industry_context.get('content_focus', []))}
Avoid: {', '.join(industry_context.get('avoid', []))}

=== AUDIENCE CONTEXT ({target_audience or 'General'}) ===
Formality Level: {audience_context.get('formal_level', 'medium')}
Slang/Casual Language: {'OK' if audience_context.get('slang_allowed') else 'Avoid'}
Emoji Use: {'OK for CTAs' if audience_context.get('emoji_use') else 'Do not use'}
CTA Style: {audience_context.get('cta_style', 'action-oriented')}
Writing Note: {audience_context.get('description', '')}

=== IMPORTANT CONTENT RULES ===
1. USER INPUT PRIORITY: If user provided specific text, use it EXACTLY - do not rephrase
2. INDUSTRY FIT: All content must feel authentic to {business_type} industry
3. AUDIENCE FIT: Language and tone must match {target_audience or 'general'} audience
4. NO GENERIC CONTENT: Every phrase should feel specific and crafted
5. NO PLACEHOLDERS: Generate real, usable content - no [brackets] or TODO markers
"""


class QualityValidator:
    """
    Validates blueprint quality and completeness.
    """
    
    REQUIRED_FIELDS = [
        "projectName",
        "projectType", 
        "seo",
        "theme",
        "components",
        "navigation"
    ]
    
    REQUIRED_SEO_FIELDS = ["title", "description", "keywords"]
    
    REQUIRED_THEME_FIELDS = ["primaryColor", "colorPalette"]
    
    MIN_COMPONENT_COUNT = 1
    MAX_COMPONENT_COUNT = 15
    
    @classmethod
    def validate(cls, blueprint: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate blueprint and return validation result.
        
        Returns:
            {
                "valid": bool,
                "score": int (0-100),
                "issues": [list of issues],
                "suggestions": [list of suggestions]
            }
        """
        issues = []
        suggestions = []
        score = 100
        
        # Check required fields
        for field in cls.REQUIRED_FIELDS:
            if field not in blueprint:
                issues.append(f"Missing required field: {field}")
                score -= 15
        
        if "error" in blueprint:
            return {
                "valid": False,
                "score": 0,
                "issues": [f"Blueprint has error: {blueprint['error']}"],
                "suggestions": ["Regenerate blueprint"]
            }
        
        # Validate SEO
        seo = blueprint.get("seo", {})
        for field in cls.REQUIRED_SEO_FIELDS:
            if field not in seo or not seo[field]:
                issues.append(f"Missing SEO field: {field}")
                score -= 5
        
        if seo.get("title") and len(seo["title"]) > 65:
            suggestions.append("SEO title exceeds 65 characters - may be truncated in search results")
            score -= 2
        
        if seo.get("description") and len(seo["description"]) > 160:
            suggestions.append("SEO description exceeds 160 characters - may be truncated")
            score -= 2
        
        # Validate Theme
        theme = blueprint.get("theme", {})
        for field in cls.REQUIRED_THEME_FIELDS:
            if field not in theme:
                issues.append(f"Missing theme field: {field}")
                score -= 5
        
        # Validate color format
        primary_color = theme.get("primaryColor", "")
        if primary_color and not cls._is_valid_color(primary_color):
            issues.append(f"Invalid primary color format: {primary_color}")
            score -= 5
        
        # Validate Components
        components = blueprint.get("components", {})
        component_count = len(components)
        
        if component_count < cls.MIN_COMPONENT_COUNT:
            issues.append(f"Too few components: {component_count}. Minimum: {cls.MIN_COMPONENT_COUNT}")
            score -= 10
        elif component_count > cls.MAX_COMPONENT_COUNT:
            suggestions.append(f"Many components ({component_count}). Consider simplifying.")
            score -= 3
        
        # Check Hero component
        has_hero = any(
            comp.get("type") == "Hero" 
            for comp in components.values() 
            if isinstance(comp, dict)
        )
        if not has_hero:
            issues.append("Missing Hero component - every website needs a hero section")
            score -= 10
        
        # Check Contact component
        has_contact = any(
            comp.get("type") == "Contact" 
            for comp in components.values() 
            if isinstance(comp, dict)
        )
        if not has_contact:
            suggestions.append("Consider adding a Contact section for better user engagement")
            score -= 5
        
        # Validate component structure
        for comp_key, comp in components.items():
            if not isinstance(comp, dict):
                continue
            
            if "type" not in comp:
                issues.append(f"Component {comp_key} missing 'type' field")
                score -= 5
            
            if "props" not in comp:
                issues.append(f"Component {comp_key} missing 'props' field")
                score -= 5
            else:
                props = comp["props"]
                # Check for placeholder content
                for key, value in props.items():
                    if isinstance(value, str):
                        if "[" in value and "]" in value:
                            suggestions.append(f"Possible placeholder in {comp_key}.{key}")
                            score -= 2
                        if "lorem ipsum" in value.lower():
                            issues.append(f"Lorem ipsum found in {comp_key}.{key}")
                            score -= 5
        
        # Validate Navigation
        navigation = blueprint.get("navigation", {})
        header = navigation.get("header", {})
        if not header.get("links"):
            suggestions.append("Navigation header has no links")
            score -= 3
        
        footer = navigation.get("footer", {})
        if not footer:
            suggestions.append("Consider adding footer section")
            score -= 2
        
        # Calculate final score
        score = max(0, min(100, score))
        
        return {
            "valid": len(issues) == 0 and score >= 50,
            "score": score,
            "issues": issues,
            "suggestions": suggestions
        }
    
    @classmethod
    def _is_valid_color(cls, color: str) -> bool:
        """Check if color is valid hex format"""
        if not color:
            return False
        color = color.strip()
        if color.startswith("#"):
            color = color[1:]
        if len(color) not in [3, 6]:
            return False
        try:
            int(color, 16)
            return True
        except ValueError:
            return False
    
    @classmethod
    def get_quality_grade(cls, score: int) -> str:
        """Get letter grade from score"""
        if score >= 95:
            return "A+"
        elif score >= 90:
            return "A"
        elif score >= 85:
            return "A-"
        elif score >= 80:
            return "B+"
        elif score >= 75:
            return "B"
        elif score >= 70:
            return "B-"
        elif score >= 65:
            return "C+"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"
    
    @classmethod
    def auto_fix(cls, blueprint: Dict[str, Any]) -> Dict[str, Any]:
        """
        Attempt to auto-fix common issues.
        Returns fixed blueprint.
        """
        fixed = blueprint.copy()
        
        # Ensure SEO exists
        if "seo" not in fixed:
            project_name = fixed.get("projectName", "Website")
            fixed["seo"] = {
                "title": f"{project_name} - Official Website",
                "description": f"Welcome to {project_name}. Discover our services.",
                "keywords": [project_name.lower(), "services", "contact"]
            }
        
        # Ensure theme colorPalette exists
        if "theme" in fixed:
            theme = fixed["theme"]
            if "colorPalette" not in theme and "primaryColor" in theme:
                primary = theme["primaryColor"]
                theme["colorPalette"] = {
                    "primary": primary,
                    "secondary": "#10B981",
                    "accent": "#F59E0B",
                    "background": "#FFFFFF",
                    "surface": "#F5F5F5",
                    "text": "#1A1A1A"
                }
        
        # Ensure globalStyles exists  
        if "globalStyles" not in fixed:
            fixed["globalStyles"] = {
                "typography": {
                    "headingFont": {"family": "Inter", "weights": [400, 600, 700]},
                    "bodyFont": {"family": "Inter", "weights": [300, 400, 500]},
                    "style": "modern"
                },
                "spacing": {
                    "sectionGap": "100px",
                    "containerMaxWidth": "1280px"
                },
                "effects": {
                    "glassmorphism": True,
                    "gradients": True,
                    "shadows": "elevated",
                    "animations": "smooth-reveal"
                }
            }
        
        # Ensure componentOrder exists
        if "componentOrder" not in fixed and "components" in fixed:
            fixed["componentOrder"] = list(fixed["components"].keys())
        
        return fixed
