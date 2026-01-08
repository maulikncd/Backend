"""
Agency Website Templates
Complete template set for agency/corporate websites
"""

from .hero import AgencyHeroTemplates
from .services import AgencyServicesTemplates
from .team import AgencyTeamTemplates
from .stats import AgencyStatsTemplates
from .about import AgencyAboutTemplates
from .footer import AgencyFooterTemplates


class AgencyTemplates:
    """Complete template set for agency/business websites"""
    
    WEBSITE_TYPE = "agency"
    
    Home = AgencyHeroTemplates
    Hero = AgencyHeroTemplates
    Services = AgencyServicesTemplates
    Team = AgencyTeamTemplates
    Stats = AgencyStatsTemplates
    About = AgencyAboutTemplates
    Footer = AgencyFooterTemplates
    
    # Aliases
    Features = AgencyServicesTemplates
    
    COLOR_PALETTES = [
        {
            "name": "Professional Blue",
            "primary": "#2563EB",
            "secondary": "#3B82F6",
            "accent": "#60A5FA",
            "background": "#FFFFFF",
            "text": "#0F172A",
            "text_muted": "#64748B"
        },
        {
            "name": "Corporate Dark",
            "primary": "#6366F1",
            "secondary": "#8B5CF6",
            "accent": "#A78BFA",
            "background": "#0F172A",
            "text": "#F8FAFC",
            "text_muted": "#94A3B8"
        }
    ]
    
    SECTIONS = ["hero", "services", "about", "stats", "team", "portfolio", "testimonials", "contact", "footer"]
    
    @classmethod
    def get_section(cls, section_type: str):
        section_map = {
            "hero": cls.Hero,
            "home": cls.Home,
            "services": cls.Services,
            "features": cls.Features,
            "team": cls.Team,
            "stats": cls.Stats,
            "about": cls.About,
            "footer": cls.Footer,
        }
        return section_map.get(section_type.lower())


__all__ = [
    "AgencyTemplates",
    "AgencyHeroTemplates",
    "AgencyServicesTemplates",
    "AgencyTeamTemplates",
    "AgencyStatsTemplates",
    "AgencyAboutTemplates",
    "AgencyFooterTemplates"
]
