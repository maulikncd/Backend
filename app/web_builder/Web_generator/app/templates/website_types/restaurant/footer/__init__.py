from typing import Dict, Any
import random

from .variant_elegant import render as render_elegant
from .variant_minimal import render as render_minimal
from .variant_dark_premium import render as render_dark_premium
from .variant_map_footer import render as render_map_footer
from .variant_newsletter import render as render_newsletter


class RestaurantFooterTemplates:
    """Restaurant footer section - 5 variants"""
    
    VARIANTS = [
        "elegant",
        "minimal",
        "dark-premium",
        "map-footer",
        "newsletter"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "elegant": render_elegant,
            "minimal": render_minimal,
            "dark-premium": render_dark_premium,
            "map-footer": render_map_footer,
            "newsletter": render_newsletter
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_elegant(props, colors)
