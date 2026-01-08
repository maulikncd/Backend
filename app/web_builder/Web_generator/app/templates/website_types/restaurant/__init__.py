"""
Restaurant Website Templates
Complete template set for restaurant/dining websites
"""

from .hero import RestaurantHeroTemplates
from .menu import RestaurantMenuTemplates
from .about import RestaurantAboutTemplates
from .reservation import RestaurantReservationTemplates
from .footer import RestaurantFooterTemplates
from .gallery import RestaurantGalleryTemplates


class RestaurantTemplates:
    """Complete template set for restaurant websites"""
    
    WEBSITE_TYPE = "restaurant"
    
    # Type-specific sections
    Home = RestaurantHeroTemplates
    Hero = RestaurantHeroTemplates
    Menu = RestaurantMenuTemplates
    About = RestaurantAboutTemplates
    Reservation = RestaurantReservationTemplates
    Reservations = RestaurantReservationTemplates  # Alias
    Contact = RestaurantReservationTemplates  # Alias
    Footer = RestaurantFooterTemplates
    Gallery = RestaurantGalleryTemplates  # Restaurant-specific gallery
    
    # Use shared for common components
    from ...shared import SharedTestimonialsTemplates, SharedCTATemplates
    
    Testimonials = SharedTestimonialsTemplates
    CTA = SharedCTATemplates

    
    COLOR_PALETTES = [
        {
            "name": "Elegant Dark",
            "primary": "#C9A962",
            "secondary": "#8B7355",
            "accent": "#D4AF37",
            "background": "#0A0A0A",
            "text": "#FFFFFF",
            "text_muted": "#888888"
        },
        {
            "name": "Warm Rustic",
            "primary": "#D97706",
            "secondary": "#DC2626",
            "accent": "#B45309",
            "background": "#FFFBEB",
            "text": "#1C1917",
            "text_muted": "#78716C"
        }
    ]
    
    SECTIONS = ["hero", "menu", "about", "reservation", "gallery", "testimonials", "footer"]
    
    @classmethod
    def get_section(cls, section_type: str):
        section_map = {
            "hero": cls.Hero,
            "home": cls.Home,
            "menu": cls.Menu,
            "about": cls.About,
            "reservation": cls.Reservation,
            "contact": cls.Contact,
            "footer": cls.Footer,
        }
        return section_map.get(section_type.lower())


__all__ = ["RestaurantTemplates"]
