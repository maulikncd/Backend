from typing import Dict, Any
import random

from .variant_badges import render as render_badges
from .variant_aura_features import render as render_aura_features
from .variant_bento_grid import render as render_bento_grid


class EcommerceFeaturesTemplates:
    """E-commerce features/trust section"""
    
    VARIANTS = [
        "badges", 
        "aura-features", 
        "bento-grid"
    ]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "badges": render_badges,
            "aura-features": render_aura_features,
            "bento-grid": render_bento_grid
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_badges(props, colors)
