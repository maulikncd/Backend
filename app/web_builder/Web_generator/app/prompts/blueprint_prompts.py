"""
Blueprint Generation Prompts
Contains all AI prompts for generating rich blueprint content
"""

import json
from typing import Dict, Any, List


from app.web_builder.Web_generator.app.prompts.color_library import ColorPaletteLibrary


class BlueprintPrompts:
    """
    Collection of prompts for AI-based blueprint generation.
    Each method returns a structured prompt for specific content generation.
    """
    
    @staticmethod
    def get_system_prompt() -> str:
        """Base system prompt for blueprint generation"""
        return """You are an expert website content strategist and UX designer. 
Your task is to generate rich, engaging, and professional website content based on business metadata.

RULES:
1. Generate content that is specific to the business type and industry
2. Use compelling, action-oriented language
3. Keep the tone consistent with the brand personality
4. Generate realistic, professional content - no placeholders
5. All content should be SEO-friendly
6. Respond ONLY with valid JSON - no markdown, no explanations
7. Follow the exact JSON structure provided in each prompt"""

    @staticmethod
    def get_full_blueprint_prompt(metadata: Dict[str, Any]) -> str:
        """
        Main prompt to generate complete blueprint from metadata
        """
        business_data = metadata.get("business_extracted_data", {})
        questionnaire = metadata.get("questionnaire", {})
        design = metadata.get("design", {})
        features = metadata.get("features", [])
        user_prompt = metadata.get("user_prompt", "")
        
        # Extract questionnaire answers properly from preserved 'answers' dict
        qa_answers = {}
        answers_dict = questionnaire.get("answers", {})
        questions_list = questionnaire.get("questions", [])
        
        # If we have the answers dict (new format)
        if answers_dict:
            for q in questions_list:
                qid = q.get("id")
                if qid in answers_dict:
                    qa_answers[q.get("question", "")] = answers_dict[qid]
        else:
            # Fallback to legacy format or searching in questions list
            for q in questions_list:
                answer = q.get("answer") or q.get("user_answer") or ""
                if answer:
                    qa_answers[q.get("question", "")] = answer
        
        # Get color palette
        palette = design.get("selected_palette", {})
        colors = palette.get("colors", ["#4F46E5", "#10B981", "#F59E0B", "#FFFFFF"])
        
        # Get business name
        business_name = business_data.get("business_name", "")
        if not business_name:
            # Try to get from questionnaire answers
            q1_ans = answers_dict.get("q1", "")
            if isinstance(q1_ans, dict):
                business_name = q1_ans.get("answer", "")
            else:
                business_name = str(q1_ans) if q1_ans else ""
        
        # Fallback to prompt name
        if not business_name and user_prompt:
            business_name = user_prompt.split()[0].title()
            
        # Get industry-specific recommended palettes
        industry = business_data.get("industry", "General")
        recommended_palettes = ColorPaletteLibrary.get_palettes_for_industry(industry)
        
        # Properly map 5-color palette: [primary, secondary, accent, surface, background]
        # Most AI-generated palettes have: bright, secondary, accent, mid-tone, dark
        # For restaurant/luxury: use DARK color as background, light as text
        primary_color = colors[0] if colors else '#4F46E5'
        secondary_color = colors[1] if len(colors) > 1 else '#10B981'
        accent_color = colors[2] if len(colors) > 2 else '#F59E0B'
        
        # Smart background selection: prefer darker color (index 4) or use white fallback
        if len(colors) >= 5:
            # 5-color palette: [primary, secondary, accent, surface, background]
            surface_color = colors[3]
            bg_color = colors[4]  # Use 5th color (usually darkest) as background
        elif len(colors) >= 4:
            bg_color = colors[3]
            surface_color = '#1A1A1A' if bg_color.startswith('#0') or bg_color.startswith('#1') or bg_color.startswith('#2') else '#F5F5F5'
        else:
            bg_color = '#FFFFFF'
            surface_color = '#F9FAFB'
        
        # Derive contrasting text color based on background luminance
        # Simple check: if bg starts with low hex values (0-5), it's dark
        bg_hex = bg_color.lstrip('#').lower()
        try:
            r = int(bg_hex[0:2], 16)
            g = int(bg_hex[2:4], 16)
            b = int(bg_hex[4:6], 16)
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            text_color = '#FFFFFF' if luminance < 0.5 else '#1A1A1A'
        except:
            text_color = '#1A1A1A'
        
        prompt = f"""Generate a complete website blueprint JSON for the following business:

=== BUSINESS INFORMATION ===
Project Name: {business_name}
Business Type: {business_data.get("business_type", "Business")}
Industry: {industry}
Goals: {business_data.get("goals", "")}
Services: {json.dumps(business_data.get("services", []))}
Style Preferences: {json.dumps(business_data.get("style_preferences", []))}

=== USER QUESTIONNAIRE RESPONSES ===
{json.dumps(qa_answers, indent=2)}

=== 🎯 USER'S EXACT ANSWERS (MUST USE VERBATIM) ===
{json.dumps(metadata.get("prop_answers", {}), indent=2)}

=== ⚠️ USER-PROVIDED HERO CONTENT (USE EXACTLY AS WRITTEN) ===
Hero Title: "{metadata.get("user_hero", {}).get("title", "")}"
Hero Subtitle: "{metadata.get("user_hero", {}).get("subtitle", "")}"
Hero CTA Button: "{metadata.get("user_hero", {}).get("cta", "Get Started")}"

=== 🍕 CAFE/RESTAURANT SPECIFIC DATA (IF APPLICABLE) ===
Signature Item (MUST appear in menu): "{metadata.get("cafe_data", {}).get("signature", "")}"
Cuisine Type: "{metadata.get("cafe_data", {}).get("cuisine", "")}"
Atmosphere: "{metadata.get("cafe_data", {}).get("atmosphere", "")}"
Menu Categories: {json.dumps(metadata.get("cafe_data", {}).get("menu_items", []))}
Opening Hours: "{metadata.get("cafe_data", {}).get("hours", "")}"
Cafe Specialty: "{metadata.get("cafe_data", {}).get("specialty", "")}"
Location: "{metadata.get("cafe_data", {}).get("location", "")}"

=== 🎮 GAMING SPECIFIC DATA (IF APPLICABLE) ===
Game/Studio Name: "{metadata.get("gaming_data", {}).get("game_name", "")}"
Genre: {json.dumps(metadata.get("gaming_data", {}).get("genre", []))}
Platforms: {json.dumps(metadata.get("gaming_data", {}).get("platforms", []))}
Visual Style: "{metadata.get("gaming_data", {}).get("style", "")}"
Game Features: {json.dumps(metadata.get("gaming_data", {}).get("features", []))}

=== 👤 PORTFOLIO SPECIFIC DATA (IF APPLICABLE) ===
Profession: "{metadata.get("portfolio_data", {}).get("profession", "")}"
Skills: {json.dumps(metadata.get("portfolio_data", {}).get("skills", []))}
Work Style: "{metadata.get("portfolio_data", {}).get("work_style", "")}"
Experience: "{metadata.get("portfolio_data", {}).get("experience", "")}"

=== USER'S SERVICES (FROM QUESTIONNAIRE) ===
{json.dumps(metadata.get("user_services", []), indent=2)}

=== CRITICAL INSTRUCTIONS FOR USER CONTENT ===
1. If "Hero Title" is provided above, use it EXACTLY as the hero section title - DO NOT generate a new one
2. If "Hero Subtitle" is provided above, use it EXACTLY as the hero section subtitle - DO NOT generate a new one  
3. If "Hero CTA Button" is provided, use it EXACTLY as the button text
4. If "Signature Item" is provided for cafe/restaurant, it MUST appear as the FIRST item in the menu
5. If services are provided in USER'S EXACT ANSWERS, display those EXACT services
6. NEVER replace user-provided text with AI-generated alternatives
7. All user-provided data in prop_answers MUST be reflected in the generated content

=== DESIGN PREFERENCES ===
Current Colors: {json.dumps(colors)}
Color Theme Preference: {metadata.get("design", {}).get("color_theme_text", "")}

=== PREMIUM RECOMMENDED PALETTES FOR THIS INDUSTRY ===
{json.dumps(recommended_palettes, indent=2)}

=== INSTRUCTIONS FOR COLORS ===
1. CRITICAL: Use these EXACT color values in the colorPalette:
   - primary: "{primary_color}"
   - secondary: "{secondary_color}"
   - accent: "{accent_color}"
   - background: "{bg_color}"
   - surface: "{surface_color}"
   - text: "{text_color}"
2. DO NOT change or re-interpret these colors. Use them exactly as shown.
3. The text color is calculated to contrast with the background.

=== REQUIRED PAGES/SECTIONS ===
{json.dumps(features)}

=== IMPORTANT INSTRUCTIONS ===
1. USER PREFERENCES: The 'USER QUESTIONNAIRE RESPONSES' section contains specific user choices. You MUST prioritize these over generic industry defaults.
2. PROJECT NAME: Use "{business_name}" as the 'projectName'.
3. PERSONALIZED CONTENT: If a user answered a question about their menu, hero imagery, or style, use that EXACT information to craft the titles, subtitles, and descriptions in the 'props' of the relevant components.
4. NO PLACEHOLDERS: Generate real, high-quality content. For example, if it's a cafe, generate a real menu with names like 'Artisan Cappuccino' and prices, based on the user's answers.
5. EXACT FEATURES: Only generate sections listed in 'REQUIRED PAGES/SECTIONS'. Do not add extra pages.
6. COLOR ACCURACY: The colorPalette values MUST be EXACTLY as specified above. Do not change them.
7. JSON ACCURACY: Your response must be a single, valid JSON object following the structure below.

=== GENERATE BLUEPRINT WITH THIS EXACT STRUCTURE ===
{{
  "projectName": "{business_name}",
  "projectType": "{business_data.get('business_type', 'business').lower()}",
  "seo": {{
    "title": "<SEO optimized title max 60 chars>",
    "description": "<compelling meta description max 160 chars>",
    "keywords": ["<keyword1>", "<keyword2>", "...up to 10 keywords"]
  }},
  "theme": {{
    "themeName": "<creative theme name based on style>",
    "themeMood": "<mood: Premium/Warm/Modern/Elegant/Playful/Professional>",
    "primaryColor": "{primary_color}",
    "colorSchemeType": "Custom",
    "colorPalette": {{
      "primary": "{primary_color}",
      "secondary": "{secondary_color}",
      "accent": "{accent_color}",
      "background": "{bg_color}",
      "surface": "{surface_color}",
      "text": "{text_color}"
    }},
    "gradients": {{
      "hero": "<CSS linear-gradient using primary/secondary with opacity>",
      "accent": "<CSS linear-gradient for buttons>"
    }}
  }},
  "components": {{
    <FOR EACH SECTION IN FEATURES, generate component with this structure>
    "comp-<section_id>": {{

      "id": "<section_id>",
      "type": "<Hero|About|Features|Gallery|Testimonials|CTA|Contact|Menu|Services>",
      "name": "<Section Display Name>",
      "props": {{
        "layoutVariant": "<choose from: centered-hero, split-hero, minimal-statement, video-background, asymmetric-split, timeline, grid-cards, masonry, carousel, etc>",
        <section-specific props - CRAFTED USING USER ANSWERS>
      }},
      "animation": {{
        "type": "<fade-slide-up|reveal-mask|scale-in|parallax|stagger-fade>",
        "duration": 600,
        "delay": 0,
        "stagger": 100,
        "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
      }}
    }}
  }},
  "navigation": {{
    "header": {{
      "logo": {{ "text": "<business name>", "style": "modern" }},
      "links": [<nav links for each section>],
      "cta": {{ "text": "<action text>", "href": "#contact", "style": "primary" }},
      "style": "transparent-fixed",
      "scrollBehavior": {{ "changeOnScroll": true, "scrollThreshold": 100 }}
    }},
    "footer": {{
      "logo": "<business name>",
      "tagline": "<from questionnaire or generated>",
      "sections": [
        {{ "title": "Quick Links", "links": [...] }},
        {{ "title": "Connect", "links": [social links] }}
      ],
      "copyright": "© 2025 <business name>. All rights reserved."
    }}
  }},
  "globalStyles": {{
    "typography": {{
      "headingFont": {{ "family": "<Google Font name>", "weights": [400, 500, 700] }},
      "bodyFont": {{ "family": "<Google Font name>", "weights": [300, 400, 500] }},
      "style": "<warm|modern|elegant|playful>"
    }},
    "spacing": {{ "sectionGap": "100px", "containerMaxWidth": "1280px" }},
    "effects": {{
      "glassmorphism": true,
      "gradients": true,
      "shadows": "elevated",
      "animations": "smooth-reveal"
    }}
  }},
  "designVision": {{
    "design_theme": "<cinematic|minimal|bold|elegant|playful>",
    "hero_concept": "<describe the hero section vision using user answers>",
    "visual_personality": "<describe overall visual style using user answers>"
  }}
}}

=== COMPONENT-SPECIFIC PROPS REFERENCE ===

For Hero section:
- title: compelling headline based on user's specific answers
- subtitle: supporting text based on user's specific answers
- description: detailed description (2-3 sentences)
- cta: primary button text
- ctaSecondary: optional secondary button text
- backgroundStyle: gradient-mesh|solid|image|video (choose based on user answer)

For About section:
- title: section heading
- story: compelling business story (3-4 paragraphs)
- milestones: [{{ "year": "20XX", "title": "...", "description": "..." }}]
- stats: [{{ "value": "100+", "label": "Happy Customers" }}]

For Features/Services section:
- sectionTitle: section heading
- sectionSubtitle: supporting text
- featureList: [{{ "icon": "emoji", "title": "...", "description": "..." }}] (4-6 items)

For Gallery section:
- title, subtitle
- categories: ["Category1", "Category2"]
- images: [placeholder URLs or categories]

For Testimonials section:
- sectionTitle
- testimonials: [{{ "quote": "...", "author": "Name", "role": "Title" }}] (3 items)

For CTA section:
- title: action-oriented headline
- description: supporting text
- ctaText: button text

For Contact section:
- title, subtitle
- email, phone, address (if available)
- formFields: [{{ "type": "text|email|textarea", "name": "...", "placeholder": "...", "required": true }}]
- ctaText: submit button text

For Menu section (restaurants/cafes/etc):
- sectionTitle
- categories: ["Starters", "Mains", "Desserts"]
- items: [{{ "name": "...", "description": "...", "price": "$XX", "category": "..." }}] (base on user's menu preference)

IMPORTANT: 
- COMPLETENESS: You MUST generate a component for EVERY section listed in REQUIRED PAGES/SECTIONS.
- Do not skip any requested features.
- Generate ALL sections mentioned in features
- Always include Hero section first
- Always include Contact section
- Use emojis for feature icons
- Generate realistic, industry-specific content
- Response must be ONLY the JSON object, no other text"""

        return prompt

    @staticmethod
    def get_hero_content_prompt(business_info: Dict[str, Any]) -> str:
        """Prompt specifically for Hero section content"""
        return f"""Generate hero section content for:
Business: {business_info.get('business_type', 'Business')}
Industry: {business_info.get('industry', 'General')}
Style: {json.dumps(business_info.get('style_preferences', []))}

Return JSON:
{{
  "title": "<powerful headline max 10 words>",
  "subtitle": "<supporting tagline max 15 words>",
  "description": "<2-3 sentence description>",
  "cta": "<action button text>",
  "ctaSecondary": "<optional secondary button>"
}}"""

    @staticmethod
    def get_about_content_prompt(business_info: Dict[str, Any], qa_answers: Dict[str, str]) -> str:
        """Prompt for About section content"""
        return f"""Generate about section content for:
Business: {business_info.get('business_type', 'Business')}
Services: {json.dumps(business_info.get('services', []))}
Goals: {business_info.get('goals', '')}
Additional Info: {json.dumps(qa_answers)}

Return JSON:
{{
  "title": "<section heading>",
  "story": "<3-4 paragraph compelling business story>",
  "milestones": [
    {{ "year": "20XX", "title": "<milestone>", "description": "<detail>" }},
    {{ "year": "20XX", "title": "<milestone>", "description": "<detail>" }},
    {{ "year": "20XX", "title": "<milestone>", "description": "<detail>" }}
  ],
  "stats": [
    {{ "value": "<number+>", "label": "<stat label>" }},
    {{ "value": "<number+>", "label": "<stat label>" }},
    {{ "value": "<number+>", "label": "<stat label>" }}
  ]
}}"""

    @staticmethod
    def get_features_content_prompt(business_info: Dict[str, Any]) -> str:
        """Prompt for Features section content"""
        services = business_info.get('services', [])
        return f"""Generate features/services section for:
Business: {business_info.get('business_type', 'Business')}
Industry: {business_info.get('industry', 'General')}
Known Services: {json.dumps(services)}

Return JSON with 4-6 features:
{{
  "sectionTitle": "<compelling section title>",
  "sectionSubtitle": "<supporting subtitle>",
  "featureList": [
    {{
      "icon": "<relevant emoji>",
      "title": "<feature name>",
      "description": "<2-sentence description>"
    }}
  ]
}}"""

    @staticmethod
    def get_testimonials_prompt(business_info: Dict[str, Any]) -> str:
        """Prompt for Testimonials section"""
        return f"""Generate 3 realistic testimonials for:
Business Type: {business_info.get('business_type', 'Business')}
Industry: {business_info.get('industry', 'General')}

Return JSON:
{{
  "sectionTitle": "<section heading>",
  "testimonials": [
    {{
      "quote": "<detailed realistic testimonial 2-3 sentences>",
      "author": "<realistic name>",
      "role": "<realistic role/title>"
    }}
  ]
}}"""

    @staticmethod
    def get_seo_content_prompt(business_info: Dict[str, Any], business_name: str) -> str:
        """Prompt for SEO metadata"""
        return f"""Generate SEO optimized metadata for:
Business Name: {business_name}
Business Type: {business_info.get('business_type', 'Business')}
Industry: {business_info.get('industry', 'General')}
Services: {json.dumps(business_info.get('services', []))}

Return JSON:
{{
  "title": "<SEO title max 60 chars including business name>",
  "description": "<compelling meta description max 160 chars>",
  "keywords": ["<keyword1>", "<keyword2>", "...up to 10 relevant keywords"]
}}"""

    @staticmethod
    def get_menu_content_prompt(business_info: Dict[str, Any], services: List[str]) -> str:
        """Prompt for Menu section (restaurants, cafes, etc.)"""
        return f"""Generate menu section for:
Business Type: {business_info.get('business_type', 'Restaurant')}
Known Items: {json.dumps(services)}

Return JSON with 8-12 menu items across categories:
{{
  "sectionTitle": "<menu section title>",
  "categories": ["<category1>", "<category2>", "<category3>"],
  "items": [
    {{
      "name": "<item name>",
      "description": "<appetizing description>",
      "price": "$XX.XX",
      "category": "<category>"
    }}
  ]
}}"""

    @staticmethod
    def get_cta_content_prompt(business_info: Dict[str, Any], primary_goal: str) -> str:
        """Prompt for CTA section"""
        return f"""Generate call-to-action section for:
Business: {business_info.get('business_type', 'Business')}
Primary Goal: {primary_goal}

Return JSON:
{{
  "title": "<action-oriented headline>",
  "description": "<compelling 1-2 sentence description>",
  "ctaText": "<button text>"
}}"""

    @staticmethod
    def get_contact_content_prompt(business_name: str, business_type: str) -> str:
        """Prompt for Contact section"""
        return f"""Generate contact section for:
Business Name: {business_name}
Business Type: {business_type}

Return JSON:
{{
  "title": "<section heading>",
  "subtitle": "<welcoming subtitle>",
  "formFields": [
    {{ "type": "text", "name": "name", "placeholder": "<name placeholder>", "required": true }},
    {{ "type": "email", "name": "email", "placeholder": "<email placeholder>", "required": true }},
    {{ "type": "text", "name": "phone", "placeholder": "<phone placeholder>", "required": false }},
    {{ "type": "textarea", "name": "message", "placeholder": "<message placeholder>", "required": true, "rows": 4 }}
  ],
  "ctaText": "<submit button text>"
}}"""

    @staticmethod
    def get_layout_variants() -> Dict[str, List[str]]:
        """Returns available layout variants for each component type"""
        return {
            "Hero": [
                "centered-hero",
                "split-hero", 
                "minimal-statement",
                "video-background",
                "parallax-hero",
                "animated-gradient",
                "full-bleed-image"
            ],
            "Home": [  # Same as Hero
                "centered-hero",
                "split-hero", 
                "minimal-statement",
                "video-background",
                "parallax-hero",
                "animated-gradient",
                "full-bleed-image"
            ],
            "About": [
                "timeline",
                "milestone-cards",
                "split-content",
                "story-scroll",
                "team-focus",
                "stats-highlight"
            ],
            "Features": [
                "grid-cards",
                "orbit-layout",
                "alternating-rows",
                "icon-grid",
                "bento-grid",
                "carousel-features"
            ],
            "Gallery": [
                "masonry",
                "horizontal-filmstrip",
                "grid-lightbox",
                "carousel",
                "pinterest-style"
            ],
            "Testimonials": [
                "carousel",
                "grid-cards",
                "timeline-reviews",
                "quote-highlight",
                "video-testimonials"
            ],
            "CTA": [
                "full-bleed",
                "split-cta",
                "minimal-cta",
                "gradient-banner",
                "floating-card"
            ],
            "Contact": [
                "split-form",
                "asymmetric-split",
                "centered-form",
                "card-style",
                "map-integration"
            ],
            "Menu": [
                "tabbed-categories",
                "accordion-style",
                "grid-cards",
                "list-view",
                "image-cards"
            ]
        }

    @staticmethod
    def get_animation_types() -> List[Dict[str, Any]]:
        """Returns available animation configurations"""
        return [
            {
                "type": "fade-slide-up",
                "duration": 600,
                "stagger": 100,
                "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
            },
            {
                "type": "reveal-mask",
                "duration": 1000,
                "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
            },
            {
                "type": "scale-in",
                "duration": 500,
                "easing": "cubic-bezier(0.34, 1.56, 0.64, 1)"
            },
            {
                "type": "parallax",
                "duration": 800,
                "easing": "linear"
            },
            {
                "type": "stagger-fade",
                "duration": 400,
                "stagger": 50,
                "easing": "ease-out"
            }
        ]

    @staticmethod
    def get_font_pairings() -> List[Dict[str, Any]]:
        """Returns recommended font pairings based on mood"""
        return {
            "Premium": {
                "headingFont": {"family": "Playfair Display", "weights": [400, 500, 700]},
                "bodyFont": {"family": "Lato", "weights": [300, 400, 500]}
            },
            "Modern": {
                "headingFont": {"family": "Inter", "weights": [400, 600, 700]},
                "bodyFont": {"family": "Inter", "weights": [300, 400, 500]}
            },
            "Warm": {
                "headingFont": {"family": "Fraunces", "weights": [400, 500, 700]},
                "bodyFont": {"family": "Outfit", "weights": [300, 400, 500]}
            },
            "Elegant": {
                "headingFont": {"family": "Cormorant Garamond", "weights": [400, 500, 700]},
                "bodyFont": {"family": "Montserrat", "weights": [300, 400, 500]}
            },
            "Playful": {
                "headingFont": {"family": "Poppins", "weights": [400, 600, 700]},
                "bodyFont": {"family": "Nunito", "weights": [300, 400, 500]}
            },
            "Professional": {
                "headingFont": {"family": "Roboto Slab", "weights": [400, 500, 700]},
                "bodyFont": {"family": "Roboto", "weights": [300, 400, 500]}
            }
        }
