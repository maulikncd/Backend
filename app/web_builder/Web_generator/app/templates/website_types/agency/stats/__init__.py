from typing import Dict, Any
import random

from .variant_counter import render as render_counter


class AgencyStatsTemplates:
    """Agency stats section"""
    
    VARIANTS = ["counter"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "counter": render_counter
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_counter(props, colors)
