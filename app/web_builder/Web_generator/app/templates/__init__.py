"""
Templates Module for Website Generation
Now uses website-type-specific templates from website_types folder
"""

# Import from new website_types structure
from .website_types import (
    CafeTemplates,
    GamingTemplates,
    PortfolioTemplates,
    EcommerceTemplates,
    RestaurantTemplates,
    AgencyTemplates,
    WEBSITE_TYPE_TEMPLATES,
    get_template_for_type
)

# Import shared templates
from .shared import (
    SharedNavbarTemplates,
    SharedContactTemplates,
    SharedCTATemplates,
    SharedTestimonialsTemplates,
    SharedFAQTemplates,
    FAQPageTemplates
)

# Alias for backward compatibility - use AgencyTemplates as default/generic
HeroTemplates = AgencyTemplates.Home  # Backward compatible alias
HomeTemplates = AgencyTemplates.Home
HeaderTemplates = SharedNavbarTemplates
FooterTemplates = AgencyTemplates.Footer
AboutTemplates = AgencyTemplates.About
FeaturesTemplates = AgencyTemplates.Services
ContactTemplates = SharedContactTemplates
CTATemplates = SharedCTATemplates
TestimonialsTemplates = SharedTestimonialsTemplates
GalleryTemplates = PortfolioTemplates.Projects  # Fallback
NavbarTemplates = SharedNavbarTemplates
PricingTemplates = AgencyTemplates.Services  # Fallback
FAQTemplates = FAQPageTemplates


# For Menu - use CafeTemplates
MenuTemplates = CafeTemplates.Menu

# Placeholder for Cards - can use Features or similar
class CardsTemplates:
    VARIANTS = ["grid-3", "cards", "icons"]
    @classmethod
    def get_variant(cls, variant, props, colors):
        from .shared import FunctionalComponents
        return FunctionalComponents.render_cards(props, colors)
    @classmethod
    def render(cls, props, colors, variant=None):
        from .shared import FunctionalComponents
        return FunctionalComponents.render_cards(props, colors)


class BusinessTemplates:
    """Business-specific template configurations for different industries"""
    Home = AgencyTemplates.Home
    Services = AgencyTemplates.Services
    About = AgencyTemplates.About
    Footer = AgencyTemplates.Footer
    
    # Industry configurations
    INDUSTRY_CONFIGS = {
        "restaurant": {
            "display_name": "Restaurant",
            "style": "warm-elegant",
            "mood": "Warm & Inviting",
            "audience_tone": "welcoming and appetizing",
            "hero_variants": ["split-left-text", "fullscreen-overlay", "gradient-split"],
            "fonts": {
                "heading": {"family": "Playfair Display", "weights": [400, 600, 700]},
                "body": {"family": "Lato", "weights": [300, 400, 500]}
            },
            "animation_config": {
                "type": "fade-up",
                "duration": "0.8s",
                "delay": "0.1s",
                "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
            },
            "special_components": ["Menu", "Reservations", "Gallery", "Testimonials"]
        },
        "bakery": {
            "display_name": "Bakery",
            "style": "cozy-artisan",
            "mood": "Cozy & Artisanal",
            "audience_tone": "friendly and delightful",
            "hero_variants": ["split-left-text", "centered-overlay"],
            "fonts": {
                "heading": {"family": "Libre Baskerville", "weights": [400, 700]},
                "body": {"family": "Open Sans", "weights": [300, 400, 600]}
            },
            "animation_config": {
                "type": "fade-in",
                "duration": "0.7s",
                "delay": "0.15s",
                "easing": "ease-out"
            },
            "special_components": ["Menu", "Gallery", "Contact"]
        },
        "coffee_shop": {
            "display_name": "Coffee Shop",
            "style": "modern-cozy",
            "mood": "Modern & Cozy",
            "audience_tone": "casual and inviting",
            "hero_variants": ["gradient-split", "split-left-text"],
            "fonts": {
                "heading": {"family": "Poppins", "weights": [500, 600, 700]},
                "body": {"family": "Inter", "weights": [300, 400, 500]}
            },
            "animation_config": {
                "type": "slide-up",
                "duration": "0.6s",
                "delay": "0.1s",
                "easing": "cubic-bezier(0.4, 0, 0.2, 1)"
            },
            "special_components": ["Menu", "About", "Contact", "Instagram Feed"]
        },
        "cafe": {
            "display_name": "Cafe",
            "style": "modern-cozy",
            "mood": "Warm & Modern",
            "audience_tone": "friendly and sophisticated",
            "hero_variants": ["split-left-text", "fullscreen-overlay"],
            "fonts": {
                "heading": {"family": "Playfair Display", "weights": [400, 600, 700]},
                "body": {"family": "Source Sans Pro", "weights": [300, 400, 600]}
            },
            "animation_config": {
                "type": "fade-up",
                "duration": "0.7s",
                "delay": "0.12s",
                "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
            },
            "special_components": ["Menu", "Gallery", "About", "Reviews"]
        },
        "gaming": {
            "display_name": "Gaming",
            "style": "dark-neon",
            "mood": "Bold & Dynamic",
            "audience_tone": "energetic and immersive",
            "hero_variants": ["fullscreen-overlay", "gradient-split", "video-background"],
            "fonts": {
                "heading": {"family": "Orbitron", "weights": [400, 600, 700, 900]},
                "body": {"family": "Rajdhani", "weights": [300, 400, 500, 600]}
            },
            "animation_config": {
                "type": "glitch-reveal",
                "duration": "0.5s",
                "delay": "0.08s",
                "easing": "cubic-bezier(0.68, -0.55, 0.265, 1.55)"
            },
            "special_components": ["Games", "News", "Community", "Downloads", "Store"]
        },
        "portfolio": {
            "display_name": "Portfolio",
            "style": "minimal-elegant",
            "mood": "Clean & Creative",
            "audience_tone": "professional and creative",
            "hero_variants": ["split-left-text", "centered-minimal"],
            "fonts": {
                "heading": {"family": "Space Grotesk", "weights": [400, 500, 700]},
                "body": {"family": "Inter", "weights": [300, 400, 500]}
            },
            "animation_config": {
                "type": "fade-in",
                "duration": "0.8s",
                "delay": "0.15s",
                "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
            },
            "special_components": ["Projects", "About", "Skills", "Contact"]
        },
        "ecommerce": {
            "display_name": "E-Commerce",
            "style": "modern-commercial",
            "mood": "Professional & Trustworthy",
            "audience_tone": "persuasive and reliable",
            "hero_variants": ["split-left-text", "fullscreen-overlay", "carousel"],
            "fonts": {
                "heading": {"family": "Montserrat", "weights": [500, 600, 700]},
                "body": {"family": "Open Sans", "weights": [300, 400, 600]}
            },
            "animation_config": {
                "type": "slide-up",
                "duration": "0.5s",
                "delay": "0.1s",
                "easing": "cubic-bezier(0.4, 0, 0.2, 1)"
            },
            "special_components": ["Products", "Categories", "Cart", "Reviews", "FAQ"]
        },
        "agency": {
            "display_name": "Agency",
            "style": "bold-modern",
            "mood": "Bold & Professional",
            "audience_tone": "confident and innovative",
            "hero_variants": ["split-left-text", "fullscreen-overlay", "gradient-split"],
            "fonts": {
                "heading": {"family": "Sora", "weights": [400, 600, 700]},
                "body": {"family": "Inter", "weights": [300, 400, 500]}
            },
            "animation_config": {
                "type": "fade-up",
                "duration": "0.6s",
                "delay": "0.12s",
                "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
            },
            "special_components": ["Services", "Portfolio", "Team", "Testimonials", "Contact"]
        },
        "technology": {
            "display_name": "Technology",
            "style": "sleek-modern",
            "mood": "Innovative & Clean",
            "audience_tone": "forward-thinking and technical",
            "hero_variants": ["gradient-split", "fullscreen-overlay"],
            "fonts": {
                "heading": {"family": "Space Grotesk", "weights": [400, 500, 700]},
                "body": {"family": "Inter", "weights": [300, 400, 500]}
            },
            "animation_config": {
                "type": "slide-up",
                "duration": "0.5s",
                "delay": "0.1s",
                "easing": "cubic-bezier(0.4, 0, 0.2, 1)"
            },
            "special_components": ["Features", "Pricing", "Integrations", "Documentation"]
        },
        "healthcare": {
            "display_name": "Healthcare",
            "style": "clean-trustworthy",
            "mood": "Professional & Caring",
            "audience_tone": "compassionate and reliable",
            "hero_variants": ["split-left-text", "centered-overlay"],
            "fonts": {
                "heading": {"family": "Nunito", "weights": [400, 600, 700]},
                "body": {"family": "Open Sans", "weights": [300, 400, 600]}
            },
            "animation_config": {
                "type": "fade-in",
                "duration": "0.7s",
                "delay": "0.15s",
                "easing": "ease-out"
            },
            "special_components": ["Services", "Team", "Testimonials", "Appointments", "FAQ"]
        },
        "fitness": {
            "display_name": "Fitness",
            "style": "bold-energetic",
            "mood": "Energetic & Motivating",
            "audience_tone": "inspiring and active",
            "hero_variants": ["fullscreen-overlay", "split-left-text", "video-background"],
            "fonts": {
                "heading": {"family": "Bebas Neue", "weights": [400]},
                "body": {"family": "Roboto", "weights": [300, 400, 500]}
            },
            "animation_config": {
                "type": "slide-up",
                "duration": "0.4s",
                "delay": "0.08s",
                "easing": "cubic-bezier(0.68, -0.55, 0.265, 1.55)"
            },
            "special_components": ["Classes", "Trainers", "Membership", "Schedule", "Testimonials"]
        },
        "business": {
            "display_name": "Business",
            "style": "professional-modern",
            "mood": "Professional & Modern",
            "audience_tone": "professional and engaging",
            "hero_variants": ["split-left-text", "centered-overlay", "gradient-split"],
            "fonts": {
                "heading": {"family": "Inter", "weights": [400, 600, 700]},
                "body": {"family": "Inter", "weights": [300, 400, 500]}
            },
            "animation_config": {
                "type": "fade-up",
                "duration": "0.6s",
                "delay": "0.1s",
                "easing": "cubic-bezier(0.25, 1, 0.5, 1)"
            },
            "special_components": ["Services", "About", "Team", "Testimonials", "Contact"]
        }
    }
    
    @classmethod
    def get_full_config(cls, business_type: str, target_audience: str = "") -> dict:
        """
        Get complete configuration for a business type.
        
        Args:
            business_type: The type of business (restaurant, cafe, gaming, etc.)
            target_audience: Optional target audience for fine-tuning
            
        Returns:
            Complete configuration dict with fonts, animations, style, etc.
        """
        # Normalize business type
        business_type = business_type.lower().replace(" ", "_").replace("-", "_")
        
        # Get config or fallback to default business config
        config = cls.INDUSTRY_CONFIGS.get(business_type, cls.INDUSTRY_CONFIGS["business"]).copy()
        
        # Adjust tone based on target audience if provided
        if target_audience:
            audience_lower = target_audience.lower()
            if "young" in audience_lower or "teen" in audience_lower:
                config["audience_tone"] = f"youthful, {config['audience_tone']}"
            elif "professional" in audience_lower or "business" in audience_lower:
                config["audience_tone"] = f"corporate, {config['audience_tone']}"
            elif "family" in audience_lower or "parent" in audience_lower:
                config["audience_tone"] = f"family-friendly, {config['audience_tone']}"
        
        return config
    
    @classmethod
    def get_available_types(cls) -> list:
        """Get list of all available business types"""
        return list(cls.INDUSTRY_CONFIGS.keys())


__all__ = [
    # Website Type Templates
    "CafeTemplates",
    "GamingTemplates",
    "PortfolioTemplates",
    "EcommerceTemplates",
    "RestaurantTemplates",
    "AgencyTemplates",
    "WEBSITE_TYPE_TEMPLATES",
    "get_template_for_type",
    # Shared Templates
    "SharedNavbarTemplates",
    "SharedContactTemplates",
    "SharedCTATemplates",
    "SharedTestimonialsTemplates",
    # Backward compatibility aliases
    "HeroTemplates",
    "HomeTemplates",
    "HeaderTemplates",
    "FooterTemplates",
    "AboutTemplates",
    "FeaturesTemplates",
    "ContactTemplates",
    "CTATemplates",
    "TestimonialsTemplates",
    "GalleryTemplates",
    "NavbarTemplates",
    "PricingTemplates",
    "MenuTemplates",
    "FAQTemplates",
    "CardsTemplates",
    "BusinessTemplates",
]
