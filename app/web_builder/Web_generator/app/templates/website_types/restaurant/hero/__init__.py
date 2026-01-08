from typing import Dict, Any
import random

from .variant_elegant_dining import render as render_elegant_dining
from .variant_rustic_bistro import render as render_rustic_bistro


class RestaurantHeroTemplates:
    """Restaurant-specific hero sections"""
    
    VARIANTS = ["elegant-dining", "rustic-bistro"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "elegant-dining": render_elegant_dining,
            "rustic-bistro": render_rustic_bistro
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_elegant_dining(props, colors)
