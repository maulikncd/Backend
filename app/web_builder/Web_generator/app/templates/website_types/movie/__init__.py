"""
Movie/Cinema Website Templates
Template set for movie theaters, cinemas, and film websites
"""

from .hero import MovieHeroTemplates


class MovieTemplates:
    """Template set for movie/cinema websites"""
    
    WEBSITE_TYPE = "movie"
    
    Home = MovieHeroTemplates
    Hero = MovieHeroTemplates
    
    COLOR_PALETTES = [
        {
            "name": "Cinema Dark",
            "primary": "#E50914",
            "secondary": "#FFD700",
            "accent": "#B81D24",
            "background": "#0A0A0A",
            "text": "#FFFFFF",
            "text_muted": "#888888"
        }
    ]
    
    SECTIONS = ["hero", "movies", "showtimes", "about", "contact", "footer"]
    
    @classmethod
    def get_section(cls, section_type: str):
        section_map = {
            "hero": cls.Hero,
            "home": cls.Home,
        }
        return section_map.get(section_type.lower())


__all__ = ["MovieTemplates"]
