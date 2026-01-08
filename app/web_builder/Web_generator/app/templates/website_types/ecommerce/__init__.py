"""
E-Commerce Website Templates
Complete template set for online store websites
"""

from .hero import EcommerceHeroTemplates
from .products import EcommerceProductsTemplates
from .categories import EcommerceCategoriesTemplates
from .features import EcommerceFeaturesTemplates
from .footer import EcommerceFooterTemplates


class EcommerceTemplates:
    """Complete template set for e-commerce/shop websites"""
    
    WEBSITE_TYPE = "ecommerce"
    
    Home = EcommerceHeroTemplates
    Hero = EcommerceHeroTemplates
    Products = EcommerceProductsTemplates
    Categories = EcommerceCategoriesTemplates
    Features = EcommerceFeaturesTemplates
    Footer = EcommerceFooterTemplates
    
    UNIQUE_SECTIONS = ["products", "categories", "cart", "deals", "features"]
    
    COLOR_PALETTES = [
        {
            "name": "Modern Shop",
            "primary": "#000000",
            "secondary": "#FF4444",
            "accent": "#FFD700",
            "background": "#FFFFFF",
            "text": "#111111",
            "text_muted": "#666666"
        },
        {
            "name": "Luxury Brand",
            "primary": "#1A1A1A",
            "secondary": "#C9A962",
            "accent": "#D4AF37",
            "background": "#FAFAFA",
            "text": "#1A1A1A",
            "text_muted": "#888888"
        }
    ]
    
    SECTIONS = ["hero", "products", "categories", "features", "testimonials", "footer"]
    
    @classmethod
    def get_section(cls, section_type: str):
        section_map = {
            "hero": cls.Hero,
            "home": cls.Home,
            "products": cls.Products,
            "categories": cls.Categories,
            "features": cls.Features,
            "footer": cls.Footer,
        }
        return section_map.get(section_type.lower())


__all__ = ["EcommerceTemplates"]
