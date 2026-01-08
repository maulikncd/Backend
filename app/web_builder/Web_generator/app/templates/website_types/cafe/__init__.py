from .hero import CafeHeroTemplates as CafeHomeTemplates
from .menu import CafeMenuTemplates
from .about import CafeAboutTemplates
from .gallery import CafeGalleryTemplates
from .footer import CafeFooterTemplates
from .features import CafeFeaturesTemplates
from .navbar import CafeNavbarTemplates
from .specials import CafeSpecialsTemplates
from .hours import CafeHoursTemplates


class CafeTemplates:
    """Complete template set for cafe/coffee shop websites"""
    WEBSITE_TYPE = "cafe"
    
    Navbar = CafeNavbarTemplates
    Home = CafeHomeTemplates
    Menu = CafeMenuTemplates
    About = CafeAboutTemplates
    Gallery = CafeGalleryTemplates
    Footer = CafeFooterTemplates
    Features = CafeFeaturesTemplates
    Specials = CafeSpecialsTemplates
    Hours = CafeHoursTemplates
    
    COLOR_PALETTES = [
        {
            "name": "Warm Espresso",
            "primary": "#6F4E37",
            "secondary": "#C4A77D",
            "accent": "#D4A574",
            "background": "#FFF8F0",
            "text": "#2D2013",
            "text_muted": "#8B7355"
        }
    ]
    
    @classmethod
    def get_section(cls, section_type: str):
        section_map = {
            "navbar": cls.Navbar,
            "home": cls.Home,
            "menu": cls.Menu,
            "about": cls.About,
            "gallery": cls.Gallery,
            "footer": cls.Footer,
            "features": cls.Features,
            "specials": cls.Specials,
            "hours": cls.Hours,
        }
        return section_map.get(section_type.lower())

__all__ = ["CafeTemplates"]
