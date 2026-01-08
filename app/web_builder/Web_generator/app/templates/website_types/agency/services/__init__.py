from typing import Dict, Any
import random

from .variant_grid import render as render_grid


class AgencyServicesTemplates:
    """Agency services section"""
    
    VARIANTS = ["grid"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "grid": render_grid
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_grid(props, colors)
