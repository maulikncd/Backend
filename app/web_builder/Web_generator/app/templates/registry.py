"""
Template Registry - Central system for website-type-specific templates
"""

from typing import Dict, Any, Optional, Type
import logging

# Import all website type templates
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
from .combination_tracker import CombinationTracker

logger = logging.getLogger(__name__)


class TemplateRegistry:
    """
    Central registry for getting appropriate templates based on website type.
    """
    
    @classmethod
    def get_templates_for_type(cls, website_type: str) -> Optional[Type]:
        """Get the template class for a specific website type"""
        return get_template_for_type(website_type)
    
    @classmethod
    def get_section_template(cls, website_type: str, section_type: str, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        """Get appropriate template for any section type"""
        template_class = cls.get_templates_for_type(website_type)
        
        if not template_class:
            # Default to agency
            template_class = AgencyTemplates
        
        # Map section types to template attributes
        section_map = {
            "navbar": "Navbar",
            "header": "Navbar",
            "nav": "Navbar",
            "hero": "Home",
            "home": "Home",
            "menu": "Menu",
            "products": "Products",
            "projects": "Projects",
            "services": "Services",
            "about": "About",
            "gallery": "Gallery",
            "features": "Features",
            "footer": "Footer",
            "specials": "Specials",
            "hours": "Hours",
            # Movie-specific sections
            "movies": "Movies",
            "films": "Movies",
            "showtimes": "Showtimes",
            "tickets": "Tickets",
            "booking": "Tickets",
            # Gaming-specific sections
            "games": "Games",
            "tournaments": "Tournaments",
            "community": "Community",
            # Common sections
            "faq": "FAQ",
            "cta": "CTA",
            "testimonials": "Testimonials",
            "reviews": "Testimonials",
            "contact": "Contact",
            "reservation": "Reservation",
            "reservations": "Reservation",
            "booking": "Reservation",
        }
        
        attr_name = section_map.get(section_type.lower())
        
        # Try type-specific template
        if attr_name and hasattr(template_class, attr_name):
            specific_template = getattr(template_class, attr_name)
            logger.info(f"[TemplateRegistry] Found {attr_name} for {website_type}: {specific_template}")
            
            # Use CombinationTracker if variant is not specified
            if variant is None and hasattr(specific_template, 'VARIANTS'):
                available_variants = getattr(specific_template, 'VARIANTS', [])
                if available_variants:
                    variant = CombinationTracker.select_fresh_variant(
                        website_type=website_type,
                        component_type=section_type.lower(),
                        available_variants=available_variants
                    )
                    logger.info(f"[TemplateRegistry] Selected variant: {variant}")
            
            if hasattr(specific_template, 'render'):
                try:
                    # Capture the selected variant if we picked one
                    html = specific_template.render(props, colors, variant)
                    if html:
                        logger.info(f"[TemplateRegistry] ✅ Rendered {section_type} with {variant}")
                        return html
                    else:
                        logger.warning(f"[TemplateRegistry] ⚠️ {section_type}.render() returned empty string")
                except Exception as e:
                    logger.error(f"[TemplateRegistry] ❌ Template render error for {section_type}: {e}")
                    import traceback
                    traceback.print_exc()
        elif attr_name:
            logger.warning(f"[TemplateRegistry] No attribute '{attr_name}' found on {template_class}")
        else:
            logger.warning(f"[TemplateRegistry] No mapping found for section type: '{section_type}'")
        
        # Fallback to SharedTemplates for common sections
        html = cls._try_shared_template(section_type.lower(), props, colors)
        if html:
            logger.info(f"[TemplateRegistry] 🔄 Using SharedTemplate for {section_type}")
            return html
        
        return ""
    
    @classmethod
    def _try_shared_template(cls, section_type: str, props: Dict[str, Any], colors: Dict[str, str]) -> str:
        """Try to render using SharedTemplates as fallback"""
        try:
            from .shared import (
                SharedContactTemplates,
                SharedTestimonialsTemplates,
                SharedCTATemplates,
                SharedFAQTemplates,
            )
            
            shared_map = {
                "contact": SharedContactTemplates,
                "testimonials": SharedTestimonialsTemplates,
                "reviews": SharedTestimonialsTemplates,
                "cta": SharedCTATemplates,
                "faq": SharedFAQTemplates,
            }
            
            template_class = shared_map.get(section_type)
            if template_class and hasattr(template_class, 'render'):
                return template_class.render(props, colors)
        except ImportError as e:
            logger.warning(f"[TemplateRegistry] SharedTemplates import error: {e}")
        except Exception as e:
            logger.error(f"[TemplateRegistry] SharedTemplate render error: {e}")
        
        return ""
    
    @classmethod
    def detect_website_type(cls, description: str) -> str:
        """Detect website type from description/prompt"""
        description_lower = description.lower()
        
        keywords = {
            "cafe": ["cafe", "coffee", "brew", "latte", "espresso", "bakery"],
            "gaming": ["gaming", "game", "esports", "streamer", "twitch", "xbox", "playstation"],
            "portfolio": ["portfolio", "personal", "developer", "designer", "freelance"],
            "ecommerce": ["shop", "store", "ecommerce", "buy", "sell", "product", "cart"],
            "restaurant": ["restaurant", "dining", "food", "chef", "menu", "reservation"],
            "agency": ["agency", "business", "corporate", "company", "marketing", "consulting"],
            "movie": ["movie", "cinema", "theater", "theatre", "film", "ticket", "showtime", "blockbuster", "premiere", "imax"],
        }
        
        for website_type, type_keywords in keywords.items():
            for keyword in type_keywords:
                if keyword in description_lower:
                    return website_type
        
        return "agency"  # Default


__all__ = ["TemplateRegistry"]
