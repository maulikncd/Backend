"""
Website Types Templates Index
All website type-specific templates are imported and registered here
"""

from .cafe import CafeTemplates
from .gaming import GamingTemplates
from .ecommerce import EcommerceTemplates
from .movie import MovieTemplates
from .portfolio import PortfolioTemplates
from .restaurant import RestaurantTemplates
from .agency import AgencyTemplates


WEBSITE_TYPE_TEMPLATES = {
    # Food & Beverage
    "cafe": CafeTemplates,
    "coffee": CafeTemplates,
    "bakery": CafeTemplates,
    "restaurant": RestaurantTemplates,
    "dining": RestaurantTemplates,
    "bistro": RestaurantTemplates,
    
    # Entertainment
    "gaming": GamingTemplates,
    "esports": GamingTemplates,
    "movie": MovieTemplates,
    "cinema": MovieTemplates,
    "theater": MovieTemplates,
    "theatre": MovieTemplates,
    "film": MovieTemplates,
    
    # Professional
    "portfolio": PortfolioTemplates,
    "personal": PortfolioTemplates,
    "developer": PortfolioTemplates,
    "designer": PortfolioTemplates,
    "freelancer": PortfolioTemplates,
    
    # Business
    "agency": AgencyTemplates,
    "corporate": AgencyTemplates,
    "business": AgencyTemplates,
    "company": AgencyTemplates,
    "consulting": AgencyTemplates,
    "marketing": AgencyTemplates,
    
    # Commerce
    "ecommerce": EcommerceTemplates,
    "shop": EcommerceTemplates,
    "store": EcommerceTemplates,
}


def get_template_for_type(website_type: str):
    """Get the appropriate template class for a website type"""
    return WEBSITE_TYPE_TEMPLATES.get(website_type.lower(), AgencyTemplates)


__all__ = [
    "CafeTemplates",
    "GamingTemplates",
    "PortfolioTemplates",
    "RestaurantTemplates",
    "AgencyTemplates",
    "EcommerceTemplates",
    "MovieTemplates",
    "WEBSITE_TYPE_TEMPLATES",
    "get_template_for_type"
]
