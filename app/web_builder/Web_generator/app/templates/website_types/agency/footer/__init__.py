from typing import Dict, Any
import random

from .variant_professional import render as render_professional


class AgencyFooterTemplates:
    """Agency footer section"""
    
    VARIANTS = ["professional"]
    
    @classmethod
    def render(cls, props: Dict[str, Any], colors: Dict[str, str], variant: str = None) -> str:
        if variant is None:
            variant = random.choice(cls.VARIANTS)
        
        dispatch = {
            "professional": render_professional
        }
        
        render_func = dispatch.get(variant)
        if render_func:
            return render_func(props, colors)
        
        return render_professional(props, colors)
