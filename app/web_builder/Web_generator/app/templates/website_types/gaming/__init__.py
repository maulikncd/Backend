from typing import Dict, Any, List
import random

from .hero import GamingHeroTemplates as GamingHomeTemplates
from .navbar import GamingNavbarTemplates
from .features import GamingFeaturesTemplates
from .gallery import GamingGalleryTemplates
from .footer import GamingFooterTemplates
from .about import GamingAboutTemplates
from .games import GamingGamesTemplates
from .news import GamingNewsTemplates
from .community import GamingCommunityTemplates
from .tournaments import GamingTournamentsTemplates
from .store import GamingStoreTemplates

class GamingTemplates:
    """Complete template set for gaming/esports websites - Premium Variants"""
    
    WEBSITE_TYPE = "gaming"
    
    # Component classes
    Navbar = GamingNavbarTemplates
    Home = GamingHomeTemplates
    Features = GamingFeaturesTemplates
    Gallery = GamingGalleryTemplates
    Footer = GamingFooterTemplates
    About = GamingAboutTemplates
    Games = GamingGamesTemplates
    News = GamingNewsTemplates
    Community = GamingCommunityTemplates
    Tournaments = GamingTournamentsTemplates
    Store = GamingStoreTemplates
    
    # Unique sections for gaming
    UNIQUE_SECTIONS = ["games", "news", "community", "tournaments", "store"]
    
    # Gaming color palettes
    COLOR_PALETTES = [
        {
            "name": "Neon Cyber",
            "primary": "#00FF88",
            "secondary": "#FF00FF",
            "accent": "#00FFFF",
            "background": "#0A0A0F",
            "text": "#FFFFFF",
            "text_muted": "#888888"
        },
        {
            "name": "Dark Pro",
            "primary": "#6366F1",
            "secondary": "#EC4899",
            "accent": "#F59E0B",
            "background": "#111111",
            "text": "#FFFFFF",
            "text_muted": "#9CA3AF"
        },
        {
            "name": "Esports Red",
            "primary": "#FF4444",
            "secondary": "#FFD700",
            "accent": "#FF6B6B",
            "background": "#0D0D15",
            "text": "#FFFFFF",
            "text_muted": "#888888"
        },
        {
            "name": "Retro Arcade",
            "primary": "#FF00FF",
            "secondary": "#00FFFF",
            "accent": "#FFFF00",
            "background": "#0a0a0a",
            "text": "#FFFFFF",
            "text_muted": "#888888"
        }
    ]
    
    @classmethod
    def get_section(cls, section_type: str):
        """Get the template class for a specific section"""
        section_map = {
            "navbar": cls.Navbar,
            "home": cls.Home,
            "features": cls.Features,
            "gallery": cls.Gallery,
            "footer": cls.Footer,
            "about": cls.About,
            "games": cls.Games,
            "news": cls.News,
            "community": cls.Community,
            "tournaments": cls.Tournaments,
            "store": cls.Store,
        }
        return section_map.get(section_type.lower())
    
    @classmethod
    def get_recommended_palette(cls, style: str = "neon"):
        """Get a recommended color palette based on style preference"""
        style_map = {
            "neon": cls.COLOR_PALETTES[0],
            "dark": cls.COLOR_PALETTES[1],
            "esports": cls.COLOR_PALETTES[2],
            "retro": cls.COLOR_PALETTES[3]
        }
        return style_map.get(style, cls.COLOR_PALETTES[0])

__all__ = ["GamingTemplates"]
