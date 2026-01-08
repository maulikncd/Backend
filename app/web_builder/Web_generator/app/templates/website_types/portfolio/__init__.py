"""
Portfolio Website Templates
Complete template set for portfolio/personal websites
"""

from .hero import PortfolioHeroTemplates
from .projects import PortfolioProjectsTemplates
from .skills import PortfolioSkillsTemplates
from .about import PortfolioAboutTemplates
from .contact import PortfolioContactTemplates
from .footer import PortfolioFooterTemplates


class PortfolioTemplates:
    """
    Central class containing all portfolio-specific template classes.
    Each section has its own template class with multiple variants.
    """
    
    Home = PortfolioHeroTemplates
    Hero = PortfolioHeroTemplates
    Projects = PortfolioProjectsTemplates
    Work = PortfolioProjectsTemplates
    Skills = PortfolioSkillsTemplates
    About = PortfolioAboutTemplates
    Contact = PortfolioContactTemplates
    Footer = PortfolioFooterTemplates
    
    # Sections available for portfolio websites
    SECTIONS = [
        "hero", "about", "projects", "skills", "contact", "footer"
    ]


__all__ = [
    "PortfolioTemplates",
    "PortfolioHeroTemplates",
    "PortfolioProjectsTemplates",
    "PortfolioSkillsTemplates",
    "PortfolioAboutTemplates",
    "PortfolioContactTemplates",
    "PortfolioFooterTemplates"
]
